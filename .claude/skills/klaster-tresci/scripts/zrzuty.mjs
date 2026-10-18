#!/usr/bin/env node
/* Zrzuty całych stron (full page) do przeglądu wizualnego, bez zależności (Node 22+, Chrome/Edge/Brave).
   Łączy się z headless Chrome przez DevTools Protocol, przewija stronę (lazy loading, animacje wejścia),
   czeka na fonty i robi zrzut całej wysokości. Bardzo długie strony tnie na części po 8000 px.

   node zrzuty.mjs --base http://127.0.0.1:4321 --out przeglad --szer 1280,375 / /poradniki/ /poradniki/hub/ /poradniki/tekst/
   node zrzuty.mjs ... --kontrast        # dodatkowo raport kontrastu tekstu (kontrast.js) w <out>/kontrast.json
   node zrzuty.mjs ... --ciemny          # emuluje prefers-color-scheme: dark
   node zrzuty.mjs ... --wys 1600        # tylko górne 1600 px (podgląd do arkusza stylów)

   Pliki: <out>/<ścieżka>-<szerokość>.png (np. poradniki_hub-375.png). Każde uruchomienie ma własny profil Chrome. */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const args = process.argv.slice(2);
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : def; };
const flag = (name) => { const i = args.indexOf(name); if (i >= 0) args.splice(i, 1); return i >= 0; };
const base = opt('--base', 'http://127.0.0.1:4321');
const out = opt('--out', 'przeglad');
const widths = opt('--szer', '1280,375').split(',').map(Number);
const wait = Number(opt('--czekaj', '600'));
const maxH = Number(opt('--wys', '0')); // >0: tylko górne N px (np. do arkusza stylów)
const kontrast = flag('--kontrast');
const dark = flag('--ciemny');
const paths = args.length ? args : ['/'];

const CHROMES = [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/microsoft-edge',
];
const chrome = CHROMES.find(existsSync);
if (!chrome) { console.error('Brak Chrome/Edge/Brave/Chromium.'); process.exit(1); }
mkdirSync(out, { recursive: true });

const profile = mkdtempSync(join(tmpdir(), 'zrzuty-'));
const proc = spawn(chrome, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`, '--hide-scrollbars',
  '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: ['ignore', 'ignore', 'pipe'] });
const wsUrl = await new Promise((res, rej) => {
  let buf = '';
  proc.stderr.on('data', (d) => { buf += d; const m = buf.match(/DevTools listening on (ws:\/\/\S+)/); if (m) res(m[1]); });
  setTimeout(() => rej(new Error('Chrome nie wystartował')), 20000);
});

const ws = new WebSocket(wsUrl);
await new Promise((r) => ws.addEventListener('open', r, { once: true }));
let id = 0; const pending = new Map(); const listeners = [];
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data);
  if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result); }
  else listeners.forEach((fn) => fn(m));
});
const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
  const msg = { id: ++id, method, params }; if (sessionId) msg.sessionId = sessionId;
  pending.set(msg.id, { res, rej }); ws.send(JSON.stringify(msg));
});
const once = (method, sessionId) => new Promise((res) => {
  const fn = (m) => { if (m.method === method && m.sessionId === sessionId) { listeners.splice(listeners.indexOf(fn), 1); res(m.params); } };
  listeners.push(fn);
});
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const here = dirname(fileURLToPath(import.meta.url));
const kontrastJs = kontrast ? readFileSync(join(here, 'kontrast.js'), 'utf8') : '';
const raport = {};

try {
  for (const w of widths) {
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const { sessionId: s } = await send('Target.attachToTarget', { targetId, flatten: true });
    await send('Page.enable', {}, s);
    await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 768 }, s);
    if (dark) await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'dark' }] }, s);
    for (const p of paths) {
      const loaded = once('Page.loadEventFired', s);
      await send('Page.navigate', { url: new URL(p, base).href }, s);
      await Promise.race([loaded, sleep(15000)]);
      // przewiń całą stronę (lazy loading, animacje wejścia), wróć na górę, poczekaj na fonty
      await send('Runtime.evaluate', { awaitPromise: true, expression: `(async()=>{const h=()=>document.documentElement.scrollHeight;
        for(let y=0;y<h();y+=innerHeight*.8){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}
        scrollTo(0,0);await document.fonts.ready;})()` }, s);
      await sleep(wait);
      const { cssContentSize } = await send('Page.getLayoutMetrics', {}, s);
      const H = maxH > 0 ? Math.min(maxH, Math.ceil(cssContentSize.height)) : Math.ceil(cssContentSize.height);
      const name = (p.replace(/^\/|\/$/g, '').replace(/\//g, '_') || 'index') + `-${w}`;
      const STEP = 8000;
      for (let y = 0, i = 0; y < H; y += STEP, i++) {
        const h = Math.min(STEP, H - y);
        const { data } = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y, width: w, height: h, scale: 1 } }, s);
        const file = join(out, H > STEP ? `${name}-${i + 1}.png` : `${name}.png`);
        writeFileSync(file, Buffer.from(data, 'base64'));
        console.log(`${file}  (${w}×${h}${H > STEP ? `, część ${i + 1}` : ''})`);
      }
      if (kontrast) {
        const { result } = await send('Runtime.evaluate', { expression: kontrastJs, returnByValue: true }, s);
        raport[name] = result.value;
        if (result.value?.n) console.log(`  kontrast: ${result.value.n} elementów poniżej progu WCAG AA`);
      }
    }
    await send('Target.closeTarget', { targetId });
  }
  if (kontrast) writeFileSync(join(out, 'kontrast.json'), JSON.stringify(raport, null, 2));
} finally {
  ws.close(); proc.kill();
  await sleep(300);
  rmSync(profile, { recursive: true, force: true });
}

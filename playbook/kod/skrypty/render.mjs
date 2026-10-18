// Render wypełnionych HTML okładek (okladka.py --keep-html) w dokładnym rozmiarze.
import { createRequire } from 'module'; import fs from 'fs'; import path from 'path';
const require = createRequire(import.meta.url); const { chromium } = require(process.env.PW);
const [dir, out] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
for (const f of fs.readdirSync(dir).filter(f => f.startsWith('.okladka-') && f.endsWith('.html'))) {
  const fmt = f.includes('-hero-') ? [1600, 900] : [1200, 630];
  const name = f.replace(/^\.okladka-szablon-/, '').replace(/-\d+\.html$/, '.png');
  const p = await b.newPage({ viewport: { width: fmt[0], height: fmt[1] } });
  await p.goto('file://' + path.join(dir, f)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(out, name) }); await p.close(); console.log(name);
}
await b.close();

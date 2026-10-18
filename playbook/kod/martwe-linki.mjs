/* Po buildzie: w gotowych plikach HTML zamienia na zwykły tekst linki wewnętrzne, które nie mogą działać:
   1) prowadzą do strony, której nie ma w dist (np. poradnik zaplanowany na później),
   2) w trybie „blog” (src/data/etap.json) prowadzą do stron oferty i formularza.
   Działa na gotowym HTML, więc nie zależy od pamięci podręcznej Astro. Po kolejnym buildzie linki wracają same. */
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const OFERTA = ['/audyt-strony/', '/wizytowka-google/', '/strona-dla-fachowca/', '/strony-dla/', '/dziekuje/'];
const pliki = (dir) => readdirSync(dir).flatMap((n) => { const p = join(dir, n); return statSync(p).isDirectory() ? pliki(p) : p.endsWith('.html') ? [p] : []; });

export default function martweLinki() {
  return {
    name: 'martwe-linki',
    hooks: {
      'astro:build:done': ({ dir, logger }) => {
        const root = fileURLToPath(dir);
        const { etap } = JSON.parse(readFileSync(new URL('../data/etap.json', import.meta.url), 'utf8'));
        const istnieje = (href) => {
          const sciezka = href.split(/[?#]/)[0];
          if (sciezka === '/') return true;
          return existsSync(join(root, sciezka, 'index.html')) || existsSync(join(root, sciezka));
        };
        const blokuj = (href) => (etap === 'blog' && OFERTA.some((p) => href.startsWith(p))) || !istnieje(href);
        let licznik = 0;
        for (const plik of pliki(root)) {
          const html = readFileSync(plik, 'utf8');
          const nowy = html.replace(/<a\b([^>]*?)\shref="(\/[^"]*)"([^>]*)>([\s\S]*?)<\/a>/g, (cale, a, href, b, tresc) => {
            // przyciski i karty z klasą zostawiamy w spokoju tylko wtedy, gdy cel istnieje
            if (!blokuj(href)) return cale;
            licznik++;
            return `<span class="link-wkrotce">${tresc}</span>`;
          });
          if (nowy !== html) writeFileSync(plik, nowy);
        }
        logger.info(`Zamieniono na tekst ${licznik} linków bez celu.`);
      },
    },
  };
}

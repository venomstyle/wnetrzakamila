// IndexNow po publikacji: zgłasza Bingowi, Yandexowi i innym wyszukiwarkom z IndexNow adresy poradników
// zmienionych w ostatnich 2 dniach (z <lastmod> w mapie strony) oraz stron głównych.
// Google nie korzysta z IndexNow; dla niego jest mapa strony. Klucz to publiczny plik public/<klucz>.txt
// (tak działa IndexNow: wyszukiwarka sprawdza, że plik leży na naszej domenie).
import { readFileSync, readdirSync } from 'node:fs';

const HOST = 'niechcieznajda.pl';
const DNI = 2;
const klucz = readdirSync('public').map((f) => f.match(/^([0-9a-f]{32})\.txt$/)?.[1]).find(Boolean);
if (!klucz) { console.log('Brak pliku klucza IndexNow w public/: pomijam.'); process.exit(0); }

const xml = readFileSync('dist/sitemap-0.xml', 'utf8');
const od = Date.now() - DNI * 864e5;
const nowe = [...xml.matchAll(/<loc>([^<]+)<\/loc><lastmod>([^<]+)<\/lastmod>/g)].filter(([, , d]) => Date.parse(d) >= od).map(([, u]) => u);
if (!nowe.length) { console.log(`IndexNow: brak poradników zmienionych w ostatnich ${DNI} dniach.`); process.exit(0); }
const urlList = [...new Set([...nowe, `https://${HOST}/`, `https://${HOST}/poradniki/`])];

const r = await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'content-type': 'application/json; charset=utf-8' },
  body: JSON.stringify({ host: HOST, key: klucz, keyLocation: `https://${HOST}/${klucz}.txt`, urlList }),
});
console.log(`IndexNow: ${r.status} ${r.statusText} dla ${urlList.length} adresów`);
urlList.forEach((u) => console.log(`  ${u}`));
// 200 i 202 to sukces; inne kody nie zatrzymują publikacji (krok ma continue-on-error).
if (![200, 202].includes(r.status)) { console.log(await r.text()); process.exit(1); }

// Search Console po publikacji: zgłasza mapę strony i sprawdza, czy nowe poradniki są w indeksie Google.
// Uruchamia go GitHub Actions po wysyłce na Zenbox. Bez sekretu GSC_KLUCZ nic nie robi.
// Sekrety: GSC_KLUCZ (cały plik JSON klucza konta usługi), opcjonalnie GSC_WLASCIWOSC
// (domyślnie sc-domain:niechcieznajda.pl; dla właściwości z prefiksem URL: https://niechcieznajda.pl/).
// Prośby o zindeksowanie nie da się wysłać przez API (Indexing API Google dopuszcza tylko oferty pracy
// i transmisje na żywo), więc skrypt tylko zgłasza mapę i pokazuje, które adresy kliknąć ręcznie.
import { createSign } from 'node:crypto';
import { readFileSync, appendFileSync } from 'node:fs';

const KLUCZ = process.env.GSC_KLUCZ;
const WLASCIWOSC = process.env.GSC_WLASCIWOSC || 'sc-domain:niechcieznajda.pl';
const STRONA = 'https://niechcieznajda.pl';
const MAPA = `${STRONA}/sitemap-index.xml`;
const DNI = 14; // sprawdzamy poradniki zmienione w ostatnich 14 dniach
const raport = (t) => { console.log(t); if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, t + '\n'); };

if (!KLUCZ) { console.log('Brak sekretu GSC_KLUCZ: pomijam Search Console.'); process.exit(0); }
const konto = JSON.parse(KLUCZ);

async function token() {
  const b64 = (o) => Buffer.from(JSON.stringify(o)).toString('base64url');
  const teraz = Math.floor(Date.now() / 1000);
  const tresc = `${b64({ alg: 'RS256', typ: 'JWT' })}.${b64({ iss: konto.client_email, scope: 'https://www.googleapis.com/auth/webmasters', aud: 'https://oauth2.googleapis.com/token', iat: teraz, exp: teraz + 3600 })}`;
  const podpis = createSign('RSA-SHA256').update(tresc).sign(konto.private_key, 'base64url');
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${tresc}.${podpis}` }) });
  if (!r.ok) throw new Error(`Token: ${r.status} ${await r.text()}`);
  return (await r.json()).access_token;
}

const t = await token();
const naglowki = { authorization: `Bearer ${t}`, 'content-type': 'application/json' };

// 1. Zgłoszenie mapy strony
const zgl = await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(WLASCIWOSC)}/sitemaps/${encodeURIComponent(MAPA)}`, { method: 'PUT', headers: naglowki });
raport(`## Search Console\n\nMapa strony ${MAPA}: ${zgl.ok ? 'zgłoszona' : `błąd ${zgl.status} ${await zgl.text()}`}\n`);

// 2. Stan indeksu nowych i zmienionych poradników (z mapy strony w dist/)
const xml = readFileSync('dist/sitemap-0.xml', 'utf8');
const od = Date.now() - DNI * 864e5;
const adresy = [...xml.matchAll(/<loc>([^<]+)<\/loc><lastmod>([^<]+)<\/lastmod>/g)].filter(([, , d]) => Date.parse(d) >= od).map(([, u]) => u);
if (!adresy.length) { raport(`Brak poradników zmienionych w ostatnich ${DNI} dniach.`); process.exit(0); }
raport(`| Adres | Stan w Google | Ostatnia wizyta Google |\n|---|---|---|`);
const doKlikniecia = [];
for (const u of adresy) {
  const r = await fetch('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect', { method: 'POST', headers: naglowki, body: JSON.stringify({ inspectionUrl: u, siteUrl: WLASCIWOSC, languageCode: 'pl' }) });
  if (!r.ok) { raport(`| ${u} | błąd ${r.status} | |`); continue; }
  const s = (await r.json()).inspectionResult?.indexStatusResult ?? {};
  const wIndeksie = s.verdict === 'PASS';
  if (!wIndeksie) doKlikniecia.push(u);
  raport(`| ${u.replace(STRONA, '')} | ${wIndeksie ? 'w indeksie' : (s.coverageState ?? s.verdict ?? 'brak danych')} | ${s.lastCrawlTime?.slice(0, 10) ?? 'jeszcze nie' } |`);
}
raport(doKlikniecia.length
  ? `\n**Poza indeksem: ${doKlikniecia.length}.** Jeśli adres wisi tak dłużej niż tydzień, wklej go w Search Console w pole „Sprawdź dowolny URL” i kliknij „Poproś o zindeksowanie”.`
  : '\nWszystkie nowe poradniki są w indeksie.');

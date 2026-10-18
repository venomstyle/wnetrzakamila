/* Kanał RSS z poradnikami (blueprint skilla: pętla świeżości). Tylko opublikowane teksty, najnowsze 50. */
import type { APIRoute } from 'astro';
import { brand } from '../data/site';
import { getPoradniki, urlOf, ogOf } from '../lib/poradniki';

const x = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export const GET: APIRoute = async () => {
  const lista = (await getPoradniki()).slice(0, 50);
  const ostatnia = lista.reduce((m, p) => Math.max(m, p.data.updatedAt.getTime(), p.data.publishedAt.getTime()), 0);
  const items = lista.map((p) => {
    const url = new URL(urlOf(p), brand.url).href;
    return `<item><title>${x(p.data.title)}</title><link>${url}</link><guid isPermaLink="true">${url}</guid>`
      + `<pubDate>${p.data.publishedAt.toUTCString()}</pubDate><category>${x(p.data.kicker)}</category>`
      + `<description>${x(p.data.description)}</description>`
      + `<enclosure url="${new URL(ogOf(p), brand.url).href}" type="image/png" length="0" /></item>`;
  }).join('');
  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>`
    + `<title>${x(brand.name)}: poradniki dla fachowców</title><link>${brand.url}/poradniki/</link>`
    + `<atom:link href="${brand.url}/rss.xml" rel="self" type="application/rss+xml" />`
    + `<description>Wizytówka Google, opinie, strona firmy i zlecenia. Każdy tekst ma źródła i datę sprawdzenia.</description>`
    + `<language>pl</language>${ostatnia ? `<lastBuildDate>${new Date(ostatnia).toUTCString()}</lastBuildDate>` : ''}${items}</channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
};

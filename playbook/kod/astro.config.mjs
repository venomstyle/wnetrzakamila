import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkRamki from './src/lib/remark-ramki.mjs';
import martweLinki from './src/integrations/martwe-linki.mjs';
import { readFileSync, readdirSync } from 'node:fs';
const { etap } = JSON.parse(readFileSync(new URL('./src/data/etap.json', import.meta.url), 'utf8'));
// W trybie „blog” strony oferty są tylko „Wkrótce” (noindex), więc nie trafiają do mapy strony.
const OFERTA = ['/audyt-strony/', '/wizytowka-google/', '/strona-dla-fachowca/', '/strony-dla/'];
// Data ostatniej zmiany poradnika (updatedAt, a bez niej publishedAt) trafia do mapy strony jako <lastmod>.
// Google bierze ją pod uwagę, gdy jest prawdziwa, więc zmieniaj updatedAt tylko przy realnej zmianie treści.
const DIR = new URL('./src/content/poradniki/', import.meta.url);
const ZMIANY = new Map(readdirSync(DIR).filter((f) => f.endsWith('.md')).map((f) => {
  const t = readFileSync(new URL(f, DIR), 'utf8');
  const pole = (k) => t.match(new RegExp(`^${k}: *"?([^"\\n]+)"?`, 'm'))?.[1].trim();
  return [`/poradniki/${pole('slug') ?? f.slice(0, -3)}/`, pole('updatedAt') ?? pole('publishedAt')];
}));

export default defineConfig({
  // Keep in sync with brand.url in src/data/site.ts and public/robots.txt.
  site: 'https://niechcieznajda.pl',
  trailingSlash: 'always',
  markdown: { remarkPlugins: [remarkRamki] },
  // /dziekuje is the Google Ads conversion page — keep it out of search.
  integrations: [martweLinki(), sitemap({
    filter: (page) => !page.includes('/dziekuje') && !(etap === 'blog' && OFERTA.some((p) => page.includes(p))),
    serialize: (item) => {
      const data = ZMIANY.get(new URL(item.url).pathname);
      return data ? { ...item, lastmod: new Date(`${data}T00:00:00Z`).toISOString() } : item;
    },
  })],
});

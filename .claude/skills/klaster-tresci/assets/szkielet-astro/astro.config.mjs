import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkRamki from './src/lib/remark-ramki.mjs';

export default defineConfig({
  // Trzymaj zgodnie z marka.url w src/data/marka.ts.
  site: 'https://example.pl',
  trailingSlash: 'always',
  markdown: { remarkPlugins: [remarkRamki] },
  integrations: [sitemap()],
});

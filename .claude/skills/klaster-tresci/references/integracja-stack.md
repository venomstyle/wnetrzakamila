# Integracja ze stackiem

Najpierw sprawdź, co projekt już ma (`package.json`, `astro.config.*`, `src/content/`, `src/layouts/`). Dopasuj się do istniejących konwencji; poniższe to punkt wyjścia, gdy czegoś brakuje.

**Astro: gotowy szkielet** w `assets/szkielet-astro/` (kolekcja, lista z harmonogramem, huby, ramki, layout artykułu z JSON-LD, hub, lista, karta, stopka z kolumnami poradników; bez własnego wyglądu). Co jest w nim stałe, a co pochodzi z wyborów marki: `szkielet.md`. Fragmenty niżej opisują to samo dla innych stacków i do ręcznej integracji.

## Astro (preferowane)

**Kolekcja** - `src/content.config.ts` (Astro 5+; w starszych `src/content/config.ts`):

```ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const poradniki = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/poradniki' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string().max(60),
    description: z.string().min(110).max(165),
    slug: z.string().optional(),
    type: z.enum(['poradnik', 'hub', 'porownanie', 'encja', 'narzedzie', 'news']).default('poradnik'),
    category: z.string(),
    kicker: z.string(),
    cluster: z.string(),
    hub: z.string(),
    primaryKeyword: z.string(),
    secondaryKeywords: z.array(z.string()).default([]),
    intent: z.string().optional(),
    publishedAt: z.coerce.date(),
    verifiedAt: z.coerce.date(),
    updatedAt: z.coerce.date(),
    author: z.string(),
    readingTime: z.number(),
    lead: z.string(),
    tldr: z.array(z.string()).min(3).max(5),
    cover: z.object({ src: z.string(), og: z.string().optional(), alt: z.string(),
      big: z.string().optional(), sub: z.string().optional(), label: z.string().optional() }),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    sources: z.array(z.object({ title: z.string(), url: z.string().url(), checkedAt: z.coerce.date() })).min(1),
    related: z.array(z.string()).default([]),
    cta: z.object({ title: z.string(), text: z.string(), href: z.string() }).optional(),
    affiliate: z.boolean().default(false),
    ymyl: z.boolean().default(false),
    draft: z.boolean().default(true),
  }),
});
export const collections = { poradniki };
```

Encje: osobna kolekcja z loaderem `file()` na `src/data/<encje>.json` i stroną `src/pages/<katalog>/[slug].astro`.

**Strona** - `src/pages/[slug].astro`: `getStaticPaths` z `getCollection('poradniki', e => !e.data.draft || import.meta.env.DEV)`, render przez `ArticleLayout`.

**ArticleLayout** renderuje w kolejności z `szablon-artykulu.md` i generuje JSON-LD z frontmattera:

```astro
---
const { entry, site } = Astro.props; const d = entry.data;
const ld = [
  { '@context':'https://schema.org', '@type':'Article', headline:d.title, description:d.description,
    datePublished:d.publishedAt.toISOString(), dateModified:d.updatedAt.toISOString(),
    author:{ '@type':'Person', name:d.author }, image:new URL(d.cover.og ?? d.cover.src, site).href },
  { '@context':'https://schema.org', '@type':'BreadcrumbList', itemListElement:[/* strona główna, hub, tekst */] },
  ...(d.faq.length ? [{ '@context':'https://schema.org', '@type':'FAQPage',
    mainEntity:d.faq.map(f => ({ '@type':'Question', name:f.q, acceptedAnswer:{ '@type':'Answer', text:f.a } })) }] : []),
];
---
<script type="application/ld+json" set:html={JSON.stringify(ld)} />
```

**Ramki z `> [!uwaga]`** - mała wtyczka remark albo gotowa (`remark-github-blockquote-alert` / `rehype-callouts`) skonfigurowana na typy `uwaga | praktyka | wzor | liczba`. W MDX prościej użyć komponentów.

**Okładki** - szablon HTML projektu (np. `src/okladki/szablon.html`) renderowany przez `scripts/okladka.py` do `public/okladki/*.png` (proces w `okladki.md`). WebP i warianty rozmiarów zrobi `astro:assets` / `<Image>` przy buildzie. Alternatywa bez Chrome: generowanie OG przy buildzie (`satori` + `@resvg/resvg-js`) z tych samych pól `cover.*`.

**Sitemap/RSS** - `@astrojs/sitemap` (z `lastmod` = `updatedAt`), `@astrojs/rss`. Wyszukiwarka: endpoint `src/pages/szukaj.json.ts` zwracający indeks.

Po dużych zmianach w komponentach/stylach zrestartuj serwer deweloperski Astro, jeśli podgląd pokazuje stary CSS (znany problem z cache transformacji). Podgląd lokalny na `127.0.0.1`.

## Next.js / inne z MDX

Ten sam frontmatter, `contentlayer`/`velite`/własny loader, komponenty ramek w MDX, `generateMetadata` dla title/description/OG, JSON-LD w layoucie.

## WordPress

Artykuły jako Markdown → import (np. WP CLI + konwersja do bloków) albo przez REST API (`/wp-json/wp/v2/posts`, status `draft`). Pola frontmattera mapuj na: tytuł, excerpt (description), pola SEO wtyczki (Rank Math/Yoast: seoTitle, description), kategorie (category), własne pola/ACF (tldr, faq, sources, verifiedAt). FAQ przez blok FAQ wtyczki SEO, żeby schema była spójna. Nigdy nie ustawiaj dat wstecz.

## Statyczny HTML bez frameworka

Prosty generator: skrypt buildu (Python/Node) czyta `content/*.md` + `data/*.json`, renderuje szablony, zapisuje `dist/<slug>/index.html`, `sitemap.xml`, `rss.xml`, `assets/dane/szukaj.json`.

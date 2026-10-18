/* Poradniki: Markdown w src/content/poradniki. Pola opisuje skill klaster-tresci
   (references/szablon-artykulu.md). Huby to wpisy z type: 'hub'; tekst należy do huba przez pole hub: '/poradniki/<slug-huba>/'. */
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const poradniki = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/poradniki' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string().max(60),
    description: z.string().min(100).max(170),
    slug: z.string().optional(),
    type: z.enum(['poradnik', 'hub', 'porownanie', 'encja', 'narzedzie', 'zestawienie', 'news']).default('poradnik'),
    category: z.string().optional(),
    kicker: z.string(),
    cluster: z.string().optional(),
    hub: z.string().optional(),
    primaryKeyword: z.string(),
    secondaryKeywords: z.array(z.string()).default([]),
    intent: z.string().optional(),
    publishedAt: z.coerce.date(),
    verifiedAt: z.coerce.date(),
    updatedAt: z.coerce.date(),
    author: z.string(),
    readingTime: z.number().optional(),
    lead: z.string(),
    tldr: z.array(z.string()).default([]),
    cover: z.object({
      src: z.string().optional(),
      og: z.string().optional(),
      alt: z.string().optional(),
      big: z.string().optional(),
      sub: z.string().optional(),
      label: z.string().optional(),
    }).default({}),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    sources: z.array(z.object({ title: z.string(), url: z.string().url(), checkedAt: z.coerce.date() })).default([]),
    related: z.array(z.string()).default([]),
    cta: z.object({ title: z.string(), text: z.string(), href: z.string() }).optional(),
    affiliate: z.boolean().default(false),
    ymyl: z.boolean().default(false),
    draft: z.boolean().default(true),
  }),
});

export const collections = { poradniki };

/* Wspólne funkcje dla poradników: lista, huby, okładki, daty. */
import { getCollection, type CollectionEntry } from 'astro:content';
import { marka } from '../data/marka';

export type Poradnik = CollectionEntry<'poradniki'>;

/* Szkice i wpisy zaplanowane widać tylko w podglądzie lokalnym (astro dev).
   Build pomija draft: true oraz wpisy z publishedAt w przyszłości (harmonogram.py).
   Zaplanowany tekst pojawia się po pierwszym buildzie od jego daty, więc hosting robi codzienny rebuild. */
export const isScheduled = (p: Poradnik) => p.data.publishedAt.getTime() > Date.now();
export async function getPoradniki(): Promise<Poradnik[]> {
  const all = await getCollection('poradniki', (e) => import.meta.env.DEV || (!e.data.draft && e.data.publishedAt.getTime() <= Date.now()));
  return all.sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());
}

export const slugOf = (p: Poradnik) => p.data.slug ?? p.id;
export const urlOf = (p: Poradnik) => `${marka.blog.base}${slugOf(p)}/`;
/* Klucz kategorii do CSS (data-kat): slug huba albo cluster. Kolor kategorii ustawia tokeny.css. */
export const katOf = (p: Poradnik) => (p.data.type === 'hub' ? slugOf(p) : (p.data.hub ?? '').split('/').filter(Boolean).pop() ?? p.data.cluster ?? '');

/* Okładki generuje scripts/okladka.py do public/okladki/<slug>-hero.png i -og.png */
const dirOkladek = 'okladki';
export const coverOf = (p: Poradnik) => p.data.cover.src ?? `/${dirOkladek}/${slugOf(p)}-hero.png`;
export const ogOf = (p: Poradnik) => p.data.cover.og ?? `/${dirOkladek}/${slugOf(p)}-og.png`;

export const hubs = (all: Poradnik[]) => all.filter((p) => p.data.type === 'hub');
export const inHub = (all: Poradnik[], hub: Poradnik) =>
  all.filter((p) => p.data.type !== 'hub' && p.data.hub === urlOf(hub));

/* Polska odmiana: 1 poradnik, 2-4 poradniki, 5+ poradników (12-14 też „poradników”). */
export const plural = (n: number, [one, few, many] = ['poradnik', 'poradniki', 'poradników']) =>
  n === 1 ? one : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 12 || n % 100 > 14) ? few : many;

const fmt = new Intl.DateTimeFormat('pl-PL', { day: 'numeric', month: 'long', year: 'numeric' });
export const dateLong = (d: Date) => fmt.format(d);
export const dateShort = (d: Date) => d.toLocaleDateString('pl-PL', { day: '2-digit', month: '2-digit', year: 'numeric' });
export const isoDate = (d: Date) => d.toISOString().slice(0, 10);

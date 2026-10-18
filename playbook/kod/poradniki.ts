/* Wspólne funkcje dla poradników: lista, huby, okładki, daty. */
import { getCollection, type CollectionEntry } from 'astro:content';
import { dzialy, pozostale, kolorHuba, KOLOR_DOMYSLNY, type Dzial } from '../data/dzialy';

export type Poradnik = CollectionEntry<'poradniki'>;

/* Szkice i wpisy zaplanowane widać tylko w podglądzie lokalnym (npm run dev).
   Build pomija draft: true oraz wpisy z publishedAt w przyszłości (harmonogram).
   Zaplanowane teksty pojawiają się po najbliższym buildzie od ich daty. */
/* PUBLIKUJ_NA=2026-10-17 npm run build: zbuduj stronę „na dzień” (np. paczka przygotowana wieczorem dzień wcześniej). */
const teraz = () => (process.env.PUBLIKUJ_NA ? new Date(`${process.env.PUBLIKUJ_NA}T23:59:59+02:00`).getTime() : Date.now());
export const isScheduled = (p: Poradnik) => p.data.publishedAt.getTime() > teraz();
export async function getPoradniki(): Promise<Poradnik[]> {
  const all = await getCollection('poradniki', (e) => import.meta.env.DEV || (!e.data.draft && e.data.publishedAt.getTime() <= teraz()));
  return all.sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());
}

export const slugOf = (p: Poradnik) => p.data.slug ?? p.id;
export const urlOf = (p: Poradnik) => `/poradniki/${slugOf(p)}/`;

/* Okładki generuje skrypt skilla do public/okladki/<slug>-hero.png i -og.png */
const dirOkladek = 'okladki';
export const coverOf = (p: Poradnik) => p.data.cover.src ?? `/${dirOkladek}/${slugOf(p)}-hero.png`;
export const ogOf = (p: Poradnik) => p.data.cover.og ?? `/${dirOkladek}/${slugOf(p)}-og.png`;

export const hubs = (all: Poradnik[]) => all.filter((p) => p.data.type === 'hub');
export const inHub = (all: Poradnik[], hub: Poradnik) =>
  all.filter((p) => p.data.type !== 'hub' && p.data.hub === urlOf(hub));

const fmt = new Intl.DateTimeFormat('pl-PL', { day: 'numeric', month: 'long', year: 'numeric' });
export const dateLong = (d: Date) => fmt.format(d);
export const dateShort = (d: Date) => d.toLocaleDateString('pl-PL', { day: '2-digit', month: '2-digit', year: 'numeric' });
export const isoDate = (d: Date) => d.toISOString().slice(0, 10);

/* Działy z opublikowanymi hubami i ich tekstami (puste działy pomijamy). */
export interface HubWDziale { hub: Poradnik; items: Poradnik[]; kolor: string }
export interface DzialZHubami { dzial: Dzial; huby: HubWDziale[] }
export const kolorOf = (hub: Poradnik) => kolorHuba[slugOf(hub)] ?? KOLOR_DOMYSLNY;
export function dzialyOf(all: Poradnik[]): DzialZHubami[] {
  const wszystkie = hubs(all).map((h) => ({ hub: h, items: inHub(all, h), kolor: kolorOf(h) })).filter((g) => g.items.length > 0);
  const przypisane = new Set(dzialy.flatMap((d) => d.huby));
  const wynik = dzialy.map((d) => ({ dzial: d, huby: d.huby.map((s) => wszystkie.find((g) => slugOf(g.hub) === s)).filter((g): g is HubWDziale => !!g) }));
  const reszta = wszystkie.filter((g) => !przypisane.has(slugOf(g.hub)));
  if (reszta.length) wynik.push({ dzial: pozostale, huby: reszta });
  return wynik.filter((d) => d.huby.length > 0);
}
export const dzialHuba = (hub: Poradnik) => dzialy.find((d) => d.huby.includes(slugOf(hub))) ?? pozostale;

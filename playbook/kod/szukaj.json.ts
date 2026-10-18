/* Indeks wyszukiwarki poradników (blueprint skilla: wyszukiwarka z indeksu JSON, bez serwera).
   t: tytuł, u: adres, o: opis, k: temat, s: frazy i nagłówki do dopasowania. */
import type { APIRoute } from 'astro';
import { getPoradniki, urlOf } from '../../lib/poradniki';

export const GET: APIRoute = async () => {
  const lista = await getPoradniki();
  const indeks = lista.map((p) => {
    const naglowki = (p.body ?? '').match(/^#{2,3} .+$/gm)?.map((h) => h.replace(/^#+ /, '')) ?? [];
    return { t: p.data.title, u: urlOf(p), o: p.data.description, k: p.data.kicker, h: p.data.type === 'hub' ? 1 : 0,
      s: [p.data.primaryKeyword, ...(p.data.secondaryKeywords ?? []), ...naglowki].filter(Boolean).join(' · ') };
  });
  return new Response(JSON.stringify(indeks), { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
};

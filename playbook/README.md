# Playbook z niechcieznajda.pl

Wszystko, co zbudowaliśmy i przetestowaliśmy w niechcieznajda.pl (październik 2026): serwis z poradnikami dla fachowców, Astro 5 jako strona statyczna, hosting Zenbox przez FTP z GitHub Actions. Bierz mechanizmy, a nie wygląd. Taśma miernicza, kolory i teksty należą do tamtej marki.

## Metoda w skrócie

1. **Badanie:** frazy z 12-miesięcznym trendem (nie średnia), SERP-y, dane własne (np. Mapy Google zbiorczo).
2. **Plan klastrów:** hub i 3–5 tekstów na temat. Publikujemy cały klaster jednego dnia (poniedziałek), a potem dogrywkę: 2–3 dni po 1 węższym tekście.
3. **Pisanie agentami** według briefu (`prompty/brief-*`) i skilla `klaster-tresci`, potem **przegląd niezależny** przez agenta bez kontekstu.
4. **Okładki** z szablonu HTML (`okladka.py` w skillu, render przez Playwright), arkusz opcji dla właściciela.
5. **QA i buildy** na daty publikacji (`PUBLIKUJ_NA=RRRR-MM-DD npm run build`), potem PR, który właściciel scala z telefonu.
6. **Publikacja z harmonogramu:** build pomija teksty z datą w przyszłości, a codzienny build o 6:00 publikuje kolejne.
7. **Świeżość:** kwartalny przegląd cen (zaplanowane zadanie), `updatedAt` zmieniany tylko przy realnej zmianie treści, data w `<lastmod>` mapy strony.

## Kod do przeniesienia (`kod/`)

| Plik | Co robi |
|---|---|
| `workflow/publikuj.yml` | GitHub Actions: build Astro, wysyłka FTP na hosting codziennie o 6:00, po pushu do main i ręcznie; potem IndexNow i Search Console. Sekrety: `FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`. |
| `astro.config.mjs` | Mapa strony z `<lastmod>` z `updatedAt` poradników i filtrem stron noindex. |
| `martwe-linki.mjs` | Integracja Astro: po buildzie zamienia linki do stron, których jeszcze nie ma (np. zaplanowanych tekstów), na zwykły tekst. |
| `poradniki.ts` | Lista poradników z bramką daty (`PUBLIKUJ_NA`), huby, działy, okładki, daty. |
| `dzialy.ts` | Drugi poziom nawigacji: działy → huby, kolory taśm. |
| `indexnow.mjs` | Zgłasza Bingowi i innym nowe adresy z ostatnich 2 dni (klucz w `public/<hex>.txt`). |
| `gsc.mjs` + `GSC.md` | Zgłoszenie mapy strony do Search Console i raport indeksu (konto usługi, opcjonalnie). |
| `Plausible.astro`, `ConsentBanner.astro`, `zgoda.ts` | Statystyki Plausible dopiero po zgodzie, cele przez `data-cel="Nazwa"`, wyłącznik właściciela `#nie-licz-mnie`. |
| `Szukaj.astro`, `szukaj.json.ts` | Wyszukiwarka z indeksu JSON, bez serwera. |
| `Swieze.astro`, `rss.xml.ts` | „Ostatnio dodane i zaktualizowane” oraz RSS. |
| `Newsletter.astro` | Test popytu (fake door): liczy kliknięcia, nie zbiera adresów, mówi uczciwie „wkrótce”. |
| `cennik.astro` | Tabela cen z poradników (dane w JSON ze źródłem i datą), filtry, pokazuje tylko ceny z opublikowanych tekstów. |
| `kreacje/` | Generator grafik reklamowych (HTML → PNG) i filmy pionowe w Remotion. |
| `skrypty/pr-klaster.sh`, `skrypty/render.mjs` | Gałąź klastra: daty, okładki, QA, buildy na dni publikacji; render okładek Playwrightem. |

Szkielet Astro do nowej strony jest w skillu: `.claude/skills/klaster-tresci/assets/szkielet-astro`.

## Lekcje (co zadziałało, czego unikać)

- **Fachowcy nie szukają „strony”**, szukają zleceń. Zawsze sprawdź, czego odbiorca naprawdę szuka, zanim zaplanujesz treści albo reklamy.
- **Przegląd niezależny łapie realne błędy:** netto i brutto, ceny po rabacie, błędne rachunki, twierdzenia bez źródła. Rób go po każdej serii tekstów.
- **Ceny w obrazkach albo ładowane skryptem:** nie zgaduj. Wpisz „sprawdź w cenniku” z linkiem. Instant pages z JS w DataForSEO często je odczyta.
- **Zaplanowane zadania potrzebują konektorów** (DataForSEO, GitHub), dodanych w claude.ai. Bez nich zadanie nie odczyta stron ani nie otworzy PR.
- **Nie dawaj wzorów dokumentów** (protokoły, umowy, oferty do podpisu). Ryzyko, że ktoś ich użyje i będzie miał pretensje.
- **Licencje źródeł:** dane „tylko do użytku niekomercyjnego” odpadają.
- **Stopka ma stały rozmiar:** nowe działy idą do menu „Tematy”, nie do stopki.
- **Reklamy:**
  - W badaniu wyszły dwie obiekcje: oszuści „z Google” i niechęć do portali z punktami. Pasek zaufania „Nie dzwonię · Nie jestem z Google · Bez haseł · Bez zobowiązań” odpowiada na pierwszą.
  - Formularz: telefon opcjonalny, najwyżej 3 pola.
  - Pionowe wideo z twarzą właściciela.
- **Telefon właściciela:** krótkie odpowiedzi, linki do PR, każda adresy do skopiowania w osobnym bloku kodu.

## Prompty (`prompty/`)

- `analiza-strony.md`: pierwsza analiza istniejącej strony (to samo co `START.md`).
- `badanie-reklam.md`: trzy równoległe badania przed kampanią (konkurencja w Ads Transparency, odbiorca, benchmarki konwersji).
- `brief-klastra-przyklad-niechcieznajda.md` i `brief-dopisek-przyklad.md`: przykład briefu dla agentów piszących klaster. Podmień markę, odbiorcę, listę linków.
- `przeglad-cen-kwartalny.md`: treść zaplanowanego zadania co kwartał.
- `cennik-dane.md`: wyciągnięcie tabeli cen z poradników.
- Przegląd niezależny: `.claude/skills/klaster-tresci/references/przeglad-niezalezny.md`.

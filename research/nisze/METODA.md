# Metoda oceny nisz (18.10.2026)

Cel: znaleźć niszę na polskim rynku dla nowego serwisu zbudowanego na naszym setupie:
- statyczna strona Astro, klastry poradników (skill `klaster-tresci`);
- narzędzia (kalkulatory, sprawdzarki, kalendarze);
- strony encji z danych (jak paliwownia.pl: baza programów → strony z szablonu → huby);
- publikacja z harmonogramu, przegląd niezależny, uczciwe źródła.

Lekcja z portfela: ruch bez produktu jest kruchy. Liczy się intencja, na której da się zarobić (afiliacja, leady, własny produkt, freemium), a nie same odsłony.

## Dane (DataForSEO, location_code 2616, language_code "pl")

Dla każdej niszy:
1. **Popyt:** 40–80 fraz rdzeniowych (główne tematy, narzędzia, encje, pytania „ile/jak/jaki”). Endpoint: `/v3/keywords_data/google_ads/search_volume/live` (12 miesięcy, CPC). Rozszerzanie: `/v3/dataforseo_labs/google/keyword_ideas/live` lub `related_keywords`. Podaj sumę wolumenu rdzenia, trend rok do roku (ostatnie 3 mies. vs te same 3 mies. rok wcześniej) i sezonowość (min/max miesiąc).
2. **Słabość SERP:** 5 reprezentatywnych fraz (w tym 1–2 pod narzędzie i 1–2 pod stronę encji), `/v3/serp/google/organic/live/advanced` depth 10. Dla domen z top 10: `/v3/backlinks/bulk_referring_domains/live` (do 1000 celów naraz) lub `/v3/dataforseo_labs/google/bulk_traffic_estimation/live`. Policz: mediana domen linkujących w top 10, ile wyników ma <50 domen linkujących, ile to fora/PDF/stare wpisy (sprzed 2023), czy dominują sklepy/portale.
3. **AI Overview:** w ilu z 5 SERP-ów jest AI Overview; czy cytuje małe serwisy.
4. **Zarobek:** CPC (USD), polskie programy partnerskie lub sieci (sprawdź istnienie, bez rejestrowania się), sprzedaż leadów, możliwy własny produkt (płatne narzędzie, PDF, subskrypcja). Krótko: kto dziś płaci za reklamy (`/v3/serp/google/ads_advertisers/live/advanced` dla 1–2 fraz, opcjonalnie).
5. **Fosa danych:** otwarte źródło danych do stron encji (dane.gov.pl, GUS, NBP, URE, ARiMR, GDOŚ, rejestry). Podaj URL i licencję. Dane „tylko niekomercyjne” odpadają.
6. **Ryzyko:** YMYL (zdrowie, finanse, prawo), treści prawne (właściciel jeszcze nie zdecydował, czy dozwolone), wzory dokumentów (zakazane), sezonowość, zależność od jednego programu.

## Ocena (1–5, 5 = najlepiej)

| Kryterium | Waga |
|---|---|
| Popyt i trend | 20% |
| Słabość SERP | 25% |
| Zarobek | 25% |
| Fosa danych / narzędzia | 15% |
| Niskie ryzyko (YMYL, AIO, prawo) | 15% |

Wynik ważony 1–5. Każda liczba ze źródłem (endpoint) i datą. Nie zgaduj; czego nie sprawdzono, napisz wprost. Bez kontaktu z firmami. Dane z Map tylko zbiorczo.

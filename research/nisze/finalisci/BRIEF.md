# Brief: badanie „tak/nie” dla finalisty (18.10.2026)

Kontekst: wybieramy niszę na nowy polski serwis na naszym setupie:
- Astro, strona statyczna;
- klastry poradników (skill `klaster-tresci`);
- narzędzia (kalkulatory);
- strony encji z danych (model paliwownia.pl);
- przegląd niezależny.

Wcześniejsza ocena jest w `research/nisze/RANKING.md` i plikach grup A–E. Zacznij od przeczytania pliku swojej grupy, żeby nie powtarzać pracy.

## Twarde zasady właściciela

- **Bez treści prawnych.** Nie planujemy stron o przepisach, pozwoleniach, rejestracjach, karach, ubezpieczeniach obowiązkowych, dopłatach i warunkach programów, CITES itp. Wypisz takie tematy w sekcji „Omijamy”, żeby autorzy ich nie ruszali.
- **Bez wzorów dokumentów.**
- **Każda cena i liczba ma źródło i datę.** Ceny, których nie da się potwierdzić, zastępujemy „sprawdź u źródła” z linkiem.
- **Licencje:** źródła „tylko niekomercyjne” odpadają.
- **Kontakt i prywatność:** bez kontaktu z firmami, bez rejestrowania się w programach, bez poczty i Teams.
- **Model zarobku dobierasz sam** na podstawie danych. Uzasadnij go.

## Co zrobić

1. **Mapa fraz (300–500 fraz):**
   - rozszerz rdzeń z pliku grupy: `/v3/dataforseo_labs/google/keyword_ideas/live`, `keyword_suggestions`, `related_keywords` (location_code 2616, language_code "pl");
   - pobierz wolumeny z 12 mies. i CPC: `/v3/keywords_data/google_ads/search_volume/live`;
   - usuń frazy wieloznaczne i prawne;
   - przypisz każdą frazę do typu strony: hub, encja, narzędzie, poradnik, porównanie/ranking;
   - zapisz CSV do `research/nisze/finalisci/dane/<slug>-mapa.csv`.
2. **20 SERP-ów** dla fraz z największym potencjałem (`/v3/serp/google/organic/live/advanced`, depth 10):
   - liczba domen linkujących **dla konkretnych URL-i**, nie domen (`/v3/backlinks/bulk_referring_domains/live` z URL-ami);
   - wiek treści;
   - AI Overview i czy cytuje małe serwisy;
   - typ strony, która wygrywa.
   Policz, na ile fraz realnie wejdzie nowa domena w 6–12 mies. (kryterium: w top 10 są ≥2 URL-e z <10 domenami linkującymi albo fora/PDF/stare treści).
3. **Zarobek, potwierdzony u źródła:**
   - **programy partnerskie** dostępne w PL: oficjalna strona programu albo sieci (Awin, CJ, Webepartners, Convertiser, TradeTracker, Allegro/Ceneo), prowizja, cookie, czy działa dla PL. WebSearch/WebFetch przez ToolSearch; gdy proxy blokuje, czytaj przez `/v3/on_page/content_parsing/live`;
   - **reklamy:** RPM display dla PL z wiarygodnego źródła z datą, inaczej oznacz jako założenie;
   - **leady i własny produkt:** płatne narzędzie, PDF, pakiet, subskrypcja, ogłoszenia płatne przez firmy z branży. Oceń realność;
   - **wybór modelu:** główny i dodatkowy, z uzasadnieniem.
4. **Rachunek przychodu po 12 mies.** w wariantach ostrożnym i realnym:
   - ruch = suma wolumenów fraz „do wzięcia” × CTR pozycji (podaj źródło krzywej CTR albo oznacz jako założenie);
   - przychód = ruch × konwersja × prowizja lub RPM.
   Każde założenie wypisz jawnie.
5. **Dane do stron encji:**
   - konkretne źródło, URL, licencja potwierdzona na stronie źródła (zacytuj);
   - liczba encji;
   - częstotliwość aktualizacji.
   Jeśli bazę trzeba zbudować ręcznie, oszacuj, ile to pracy.
6. **Szkic serwisu:**
   - działy, liczba stron każdego typu na start i po 6 mies.;
   - lista narzędzi;
   - pierwszy klaster na start z datą wg sezonu;
   - propozycje nazwy i domeny (tylko pomysły; nie sprawdzaj dostępności u rejestratorów).
7. **Ryzyka:** AIO, sezonowość, zależność od jednego programu, „Omijamy” (tematy prawne).
8. **Werdykt:** TAK / NIE / WARUNKOWO z 3 powodami i wynikiem 1–5 wg `research/nisze/METODA.md`.

Każda liczba: endpoint lub URL i data 18.10.2026. Nie zgaduj; czego nie sprawdzono, napisz wprost. Prosty polski, bez kalek. Nie commituj.

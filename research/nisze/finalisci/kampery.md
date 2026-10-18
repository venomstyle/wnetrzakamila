# Kampery, kamping i vanlife w Polsce: badanie „tak/nie” (18.10.2026)

Brief: [BRIEF.md](BRIEF.md). Wcześniejsza ocena grupy: [B-natura-outdoor.md](../B-natura-outdoor.md) (wynik 3,7). Dane surowe: `dane/kampery-*.csv`.

**Werdykt: WARUNKOWO. Wynik 3,0 / 5** (niżej niż 3,7 w ocenie grupy, bo polskiego płatnika nie udało się potwierdzić).

Skróty źródeł (wszystkie odczyty 18.10.2026):

- **[SV]** `/v3/keywords_data/google_ads/search_volume/live`, PL, język pl; średnia z 12 mies. (10.2025–09.2026), CPC w USD.
- **[LABS]** `/v3/dataforseo_labs/google/keyword_suggestions/live`, `related_keywords/live`, `keyword_ideas/live` (rozszerzanie fraz).
- **[SERP]** `/v3/serp/google/organic/live/advanced`, depth 10, desktop, z asynchronicznym AI Overview.
- **[BL]** `/v3/backlinks/bulk_referring_domains/live`: domeny linkujące do konkretnego URL-a oraz do hosta.
- **[BIZ]** `/v3/business_data/business_listings/search/live` (Mapy Google, tylko liczby zbiorcze).
- **[OSM]** API taginfo Geofabrik dla Polski, stan danych 17.10.2026 20:20 UTC (odczyt przez `/v3/on_page/instant_pages` + `raw_html`).
- **[CP]** `/v3/on_page/content_parsing/live` (odczyt oficjalnych stron).
- **[WS]** WebSearch.
- **[NBP]** kursy średnie NBP, tabela 202/A/NBP/2026 z 16.10.2026: 1 GBP = 5,1746 zł, 1 EUR = 4,3661 zł.

---

## 1. Mapa fraz

Plik: `dane/kampery-mapa.csv` (1 048 wierszy z wykluczonymi i wariantami).

**Jak powstała.** Rdzeń z pliku grupy B rozszerzyłem przez [LABS] (13 zapytań: kamper, kampera, kamperem, kamperów, camper, kemping, kempingi, pole namiotowe, przyczepa kempingowa, glamping, biwak oraz related dla „wynajem kampera” i „wyposażenie kampera”). Dało to 6 169 fraz. Po odrzuceniu zabawek (Barbie, LEGO), butów marki Camper, krzyżówek, wyjazdów zagranicznych, ogłoszeń OLX/Otomoto i nazw pojedynczych obiektów wysłałem 991 fraz do [SV] (981 wróciło z danymi).

**Wynik [SV]:**

| | Frazy | Wolumen / mies. |
|---|---|---|
| Unikalne frazy z wolumenem > 0 | 853 | 594 910 |
| Warianty tej samej frazy (scalone, ten sam przebieg miesięczny) | 80 | nie liczę |
| Wykluczone: wieloznaczne, nawigacyjne, obce, „Zanocuj w lesie” | 34 | nie liczę |
| Wykluczone: prawne (wolumen z [LABS]) | 67 | 7 820 |

Mapa ma więcej niż 300–500 fraz, bo długi ogon to strony regionów („pole namiotowe łeba”). Najmocniejsze 500 fraz daje 569 180 wyszukań, czyli 95,7% sumy (500. fraza ma 140/mies.) [SV].

**Typy stron** (unikalne frazy, z 14 frazami o zerowym wolumenie): encja 424 (noclegi wg regionu 300, wynajem wg miasta 120, marki 4), porównanie/ranking 239 (wyposażenie 139, typy kamperów 39, wynajem 24, zakup 21, platformy 12, rankingi kempingów 4), poradnik 97, narzędzie 67, hub 40.

**Największe klastry [SV]:**

| Klaster | Typ | Frazy | Wolumen / mies. | Przykłady |
|---|---|---|---|---|
| Huby (pole namiotowe, kemping, kamper, glamping) | hub | 22 | 312 040 | pole namiotowe 110 000; kemping 49 500; kamper 33 100; przyczepa kempingowa 33 100; glamping 22 200 |
| Wyposażenie kampera i kempingu | ranking | 139 | 128 380 | lodówka turystyczna 33 100; toaleta turystyczna 9 900; namiot dachowy 9 900; klimatyzator do kampera 1 600; lodówka do kampera 1 000 |
| Noclegi wg regionu | encja | 300 | 67 590 | pole namiotowe nad morzem 2 900; pole namiotowe mazury 2 400; pole namiotowe nad jeziorem 1 900 |
| Wynajem wg miasta | encja | 120 | 17 230 | wynajem kampera warszawa 1 000; poznań 720; wrocław 720; kraków 590 |
| Typy kamperów | porównanie | 39 | 16 950 | kamper van 1 900; mini kamper 1 600; kamper integra 1 000; kamper półintegra 720 |
| Zabudowa i vanlife | poradnik | 30 | 8 930 | bus kamper 1 000; bus przerobiony na kamper 720; vanlife 720 |
| Koszt wynajmu | narzędzie | 30 | 6 250 | wynajem kampera cena 1 600; ile kosztuje wynajem kampera 880 |
| Trasy | poradnik | 38 | 2 180 | kamperem po polsce 320; gdzie kamperem w polsce 170 |

**Sezon [SV]:** cała mapa lipiec 2026: 1 392 600, grudzień 2025: 216 690 (×6,4). Noclegi ×10,2, wynajem ×4,7 (styczeń 31 200 wobec grudnia 17 860), wyposażenie ×3,8. Trend r/r z oceny grupy B: −1,9% (lip–wrz), „wynajem kampera” −26% r/r.

**CPC [SV]:** ważony 0,22 USD. Wyżej tylko frazy lokalne i marki platform: pole namiotowe sielpia 3,85; camper park mazury 3,24; pitchup 1,46; pole namiotowe krynica morska 1,20. Najdroższe frazy z grupy B („zanocuj w lesie” 2,32, „park4night” 1,90, „ubezpieczenie kampera” 3,08) wypadły jako prawne lub nawigacyjne.

---

## 2. SERP: 20 fraz

Pliki: `dane/kampery-serp-top10.csv` (171 URL-i z domenami linkującymi do URL-a i do hosta), `dane/kampery-serp-podsumowanie.csv`.

| Fraza (wolumen [SV]) | Typ | Mediana dom. do URL | Mediana dom. do hosta | URL <10 dom. | w tym na hostach <300 dom. | AIO | Local Pack |
|---|---|---|---|---|---|---|---|
| wynajem kampera (8 100) | hub | 73 | 105,5 | 4 | 1 | tak | tak |
| wypożyczalnia kamperów (4 400) | hub | 27 | 70 | 3 | 3 | nie | tak |
| wynajem kampera warszawa (1 000) | encja | 24,5 | 83 | 5 | 3 | nie | tak |
| ile kosztuje wynajem kampera (880) | narzędzie | 1 | 93 | 9 | 6 | tak | nie |
| zanocuj w lesie mapa (4 400) | Omijamy | 1,5 | 249,5 | 6 | 5 | tak | nie |
| parking dla kamperów (1 900) | narzędzie | 0 | 298 | 7 | 3 | nie | tak |
| pole namiotowe mazury (2 400) | encja | 1 | 210,5 | 7 | 4 | nie | tak |
| kempingi w polsce (880) | hub | 1 | 808,5 | 7 | 1 | nie | tak |
| pole namiotowe nad morzem (2 900) | poradnik/encja | 0 | 1 027,5 | 7 | 3 | nie | tak |
| lodówka do kampera (1 000) | ranking | 0 | 670 | 7 | 3 | nie | nie |
| kamper integra (1 000) | porównanie | 0 | 4 793 | 8 | 0 | tak | nie |
| klimatyzator do kampera (1 600) | ranking | 0 | 57 | 7 | 5 | nie | nie |
| toaleta turystyczna (9 900) | ranking | 0 | 3 164 | 7 | 2 | nie | nie |
| namiot dachowy (9 900) | ranking | 0 | 316 | 9 | 4 | nie | tak |
| glamping co to (1 600) | poradnik | 0 | 65 | 5 | 3 | tak | nie |
| bus przerobiony na kampera (720) | poradnik | 0 | 9 141 | 7 | 2 | tak | nie |
| kamperem po polsce (320) | poradnik | 0 | 193 | 8 | 5 | tak | nie |
| mini kamper (1 600) | porównanie | 0 | 1 789 | 7 | 2 | tak | nie |
| co zabrać na kemping (140) | narzędzie | 0 | 872,5 | 8 | 1 | tak | nie |
| wynajem przyczepy kempingowej (1 300) | hub | 0 | 73,5 | 9 | 6 | nie | tak |

Źródła tabeli: [SERP], [BL].

**Ile fraz realnie wejdzie nowa domena w 6–12 mies.**

- Kryterium z briefu (≥2 URL-e z <10 domenami linkującymi albo fora/PDF/stare treści): **20 z 20**. To kryterium jest za miękkie: podstrony kategorii Allegro, OLX czy Leroy Merlin też mają 0 linków do URL-a, a wygrywają siłą domeny.
- Kryterium ścisłe (≥2 URL-e z <10 domenami do URL-a **na hostach z <300 domenami**): **16 z 20**. Odpadają: „wynajem kampera”, „kempingi w polsce”, „kamper integra” (OLX, sprzedajemy.pl, truck1) i „co zabrać na kemping” (AIO z pełną listą, euro.com.pl, Decathlon).
- Wszystkie 171 URL-i: mediana domen linkujących do URL-a 0; 137 ma <10; mediana dla hosta 274; 90 stoi na hostach <300 [BL].
- 12 URL-i to treści sprzed 2023 albo wideo/fora: reddit z 2018, sportroom.pl z 2018, domowa.tv z 2016, polskicaravaning.pl z 2018, campingtramp.com z 2019 [SERP].

**Kto wygrywa** [SERP]: wypożyczalnie (25 URL-i), sklepy (19), ogłoszenia OLX/Otomoto/sprzedajemy (17), obiekty noclegowe (14), blogi sklepów i wypożyczalni (10), katalogi kempingów (camprest.com, eurocampings.pl, jetcamp.com). Przy „wynajem kampera” w top 10 są wyłącznie małe wypożyczalnie (strony główne z 43–493 domenami do hosta), OLX, BookingCamper.pl, CamperDays i grupa FB. Nikt nie ma porównywarki cenników.

**AI Overview** [SERP]: 9 z 20. W 7 z 9 cytuje małe serwisy: slaskiekampery.pl i wisla66.pl (koszt wynajmu), busmaniak.pl z 5 domenami linkującymi (mini kamper, zabudowa busa), bookamp.pl i mskamp.pl (trasy), globtroterek.com i domowa.tv (lista rzeczy). AIO przy „ile kosztuje wynajem kampera” podaje widełki 300–1 100 zł/doba, kaucję 4 000–10 000 zł i opłatę serwisową 200–350 zł. Strona z tabelą konkretnych cenników daje więcej niż te widełki (to wniosek, nie pomiar).

**Local Pack** [SERP]: 9 z 20, przy wszystkich frazach o wynajmie i noclegach w regionie.

---

## 3. Zarobek (sprawdzony u źródła)

Plik: `dane/kampery-programy.csv`. Nie rejestrowałem się w żadnym programie i z nikim się nie kontaktowałem.

### Programy partnerskie

| Program | Gdzie | Warunki | Działa dla PL? | Źródło |
|---|---|---|---|---|
| CamperDays | Awin 52885 | 3% od rezerwacji (śr. 90 GBP = 465,71 zł), 8 GBP = 41,40 zł za zapytanie; cookie 30 dni | **Nie.** Profil: „The registration is valid for UK!”. Programu dla camperdays.pl nie znalazłem | [CP] ui.awin.com/merchant-profile/52885, [NBP] |
| Yescapa | TradeTracker UK/ES | brak stawki | Nie. Kampanie UK i ES oznaczone jako zamknięte | [WS] affi.io/m/yescapa |
| Goboony | Tradedoubler NL/UK | NL 5–10%, UK 8–14% zależnie od liczby rezerwacji | Nie (NL, UK, BE, DE, IT, FR) | [WS] katalog Tradedoubler |
| PaulCamper | Partnerize, Travelpayouts | ok. 20% prowizji PaulCamper + 50–100 EUR za nowego właściciela | Nie (DE, AT, NL, UK) | [WS] travelpayouts.com |
| Indie Campers | TradeTracker | brak stawki, cookie 30 dni | Nie potwierdzono; status zamknięty | [WS] affi.io |
| Campiri.pl, BookingCamper.pl, CampRest, Alohacamp, Pitchup | brak | brak | Programu nie znalazłem | [WS] |
| park4night | brak | brak | Programu nie znalazłem; aplikacja ma płatny abonament | [WS] |
| Booking.com | CJ Affiliate (Europa) | ok. 4% od zrealizowanego pobytu | Prawdopodobnie, ale niepotwierdzone u źródła (strona programu wymaga JavaScript) | [WS] makeinfluence.com, track360.io |
| ACSI Eurocampings | TradeTracker | 3% od rezerwacji + 0,25 EUR (1,09 zł) za opinię; cookie 100 dni | Strona programu dotyczy eurocampings.co.uk. Dla PL niepotwierdzone, choć eurocampings.pl rankuje w PL | [CP] eurocampings.co.uk/extra-information/affiliate-partners/ |
| Decathlon Polska | TradeTracker PL | stawki nie podano | Tak (kampania PL istnieje; data artykułu nieznana) | [CP] tradetracker.com/pl/start-kampanii-decathlon/ |
| Allegro Share | Allegro | 1,67% ceny (jedno źródło wtórne) | Tak, ale stawka niepotwierdzona | [WS] tabletowo.pl |
| Sklepy kempingowe (yolco, mpcamp, allcamp, campingshop, thecampers) | brak | brak | Nie sprawdzono, wyszukiwanie nic nie dało | [WS] |

**Wniosek:** żaden program wynajmu kamperów nie jest dziś potwierdzony dla polskiego wydawcy. Noclegi (Booking, Eurocampings) i sprzęt (Decathlon, Allegro) mają programy, ale stawek dla PL nie potwierdziłem u źródła.

### Reklamy

RPM display dla PL: wiarygodnego źródła z datą nie znalazłem [WS]. W rachunku to założenie: 5 zł (ostrożny) i 10 zł (realny) za 1 000 odsłon. Ważony CPC 0,22 USD [SV] sugeruje niski RPM.

### Leady i własny produkt

- **Leady dla wypożyczalni.** W Mapach Google jest 656 wizytówek w kategorii „wypożyczalnia kamperów” [BIZ, liczba zbiorcza]. Rynek jest rozdrobniony: w top 10 dominują firmy z 1–12 pojazdami i 50–130 domenami linkującymi. Punkt odniesienia: CamperDays płaci 8 GBP (41,40 zł) za jedno zapytanie [CP, NBP]. Ile zapłaciłaby polska wypożyczalnia, nie wiadomo; zasada „bez kontaktu z firmami” oznacza, że firmy muszą zgłosić się same (formularz „dodaj wypożyczalnię”). Realne po ruchu, nie od startu.
- **Płatne wyróżnienie wypożyczalni na stronach miast.** Cennika konkurencji (BookingCamper, CampRest) nie znalazłem [WS].
- **Własny produkt.** Płatny PDF z trasami lub checklistą przegrywa z AIO, które podaje pełną listę rzeczy [SERP]. Płatne narzędzie: brak sygnału, że ktoś płaci. Oceniam jako mało realne.

### Wybór modelu

- **Główny: porównywarka cenników wypożyczalni + zapytania (leady) do wypożyczalni, które same się zgłoszą.** Uzasadnienie: najsłabszy SERP z pieniędzmi to wynajem (małe firmy, brak porównywarki), transakcja to 3 100–4 900 zł za tydzień [SERP, snippet vipcamper.pl], a zapytanie ma rynkową cenę ok. 41 zł (CamperDays UK).
- **Dodatkowy: afiliacja sprzętu (rankingi wyposażenia) i noclegów** po potwierdzeniu programów w panelach sieci, plus reklamy display na poradnikach.

---

## 4. Rachunek po 12 miesiącach

Plik: `dane/kampery-rachunek.csv`. Model: `ruch = wolumen [SV] × CTR pozycji × korekta SERP × pokrycie`, `przychód = ruch × konwersja × prowizja lub RPM`.

**Krzywa CTR:** SISTRIX (badanie mobile, ponad 80 mln fraz) cytowane przez SEO Inc. (przegląd 28.07.2026, seoinc.com/seo-blog/much-traffic-comes-organic-search/): poz. 1: 28,5%, 2: 15,7%, 3: 11%, 10: 2,5%. Pozycje 4–9 (8%; 6,5%; 5%; 4%; 3,3%; 2,8%) to moja interpolacja, czyli założenie.

**Założenia (wszystkie poza wolumenem i CTR):**

| Parametr | Ostrożny | Realny |
|---|---|---|
| Frazy „do wzięcia” | 717 fraz, 169 520/mies. | 840 fraz, 322 360/mies. |
| Pozycja: encja / narzędzie / ranking / poradnik | 8 / 6 / 7–8 / 5–6 | 5 / 4 / 4–5 / 3–4 |
| Frazy ≥5 000 i huby | poza top 10 | huby <10 000 na 9; frazy ≥5 000 o 2 pozycje niżej |
| Korekta SERP (Local Pack, AIO, Shopping, OLX) | ×0,5–0,8 wg klastra | to samo |
| Pokrycie fraz stronami po 12 mies. | 60% | 85% |
| Odsłony na sesję; RPM | 1,3; 5 zł | 1,6; 10 zł |
| Wyposażenie: klik do sklepu / konwersja / koszyk / prowizja | 12% / 2% / 300 zł / 3% | 12% / 3% / 600 zł / 5% |
| Noclegi: klik / rezerwacja / wartość / prowizja | 8% / 2% / 500 zł / 0% (brak potwierdzonego programu) | 12% / 4% / 800 zł / 3% (stawka ACSI) |
| Wynajem: zapytania / sprzedane / cena | 3% / 0% / 0 zł | 3% / 50% / 40 zł |

Koszyki: ceny w Google Shopping 18.10.2026 [SERP] to klimatyzatory do kampera 1 428,99–7 400 zł i toalety turystyczne 45,19–499 zł; reszta to założenia.

**Wynik (średnia miesięczna po 12 mies.):**

| | Ostrożny | Realny |
|---|---|---|
| Sesje / mies. | 2 646 | 10 653 |
| w tym wynajem / noclegi / wyposażenie / poradniki | 444 / 1 142 / 812 / 247 | 1 465 / 3 672 / 4 418 / 1 098 |
| Reklamy | 17 zł | 170 zł |
| Afiliacja wyposażenia | 18 zł | 477 zł |
| Afiliacja noclegów | 0 zł | 423 zł |
| Zapytania do wypożyczalni | 13 szt. | 44 szt. |
| Leady | 0 zł | 879 zł |
| **Razem** | **35 zł / mies.** | **1 950 zł / mies.** |

W lipcu przychód będzie ok. 2× średniej, w grudniu ok. 0,3× (sezon z [SV]).

Wrażliwość: gdyby polska platforma wynajmu dała warunki jak CamperDays UK (3% od rezerwacji, śr. 465,71 zł prowizji), realny wariant zyskałby ok. 680 zł/mies. (1 465 sesji × 5% kliknięć × 2% rezerwacji × 465,71 zł; konwersje to założenie).

---

## 5. Dane do stron encji

Plik: `dane/kampery-encje-zrodla.csv`.

### OpenStreetMap: kempingi, camper parki, zrzut nieczystości

| Obiekt | Liczba w PL [OSM] |
|---|---|
| `tourism=camp_site` (kempingi, pola namiotowe) | 1 813 (853 punkty, 938 obrysów, 22 relacje) |
| `tourism=caravan_site` (camper parki) | 273 |
| `amenity=sanitary_dump_station` (zrzut) | 111 |

Dla skali: Mapy Google mają w PL 2 317 wizytówek „campground” i 541 „RV park” [BIZ, tylko liczby]. Camping.info pokazuje 349 kempingów (z oceny grupy B). Nie sprawdziłem, ile obiektów OSM ma nazwę, stronę WWW czy atrybuty (prąd, psy); to pierwszy krok po pobraniu ekstraktu.

**Licencja potwierdzona u źródła** (openstreetmap.org/copyright [CP]):

> „You are free to copy, distribute, transmit and adapt our data, as long as you credit OpenStreetMap and its contributors. If you alter or build upon our data, you may distribute the result only under the same license.”

> „Where you use OpenStreetMap data, you are required to do the following two things: Provide credit to OpenStreetMap by displaying our attribution notice. Make clear that the data is available under the Open Database License.”

> „Although OpenStreetMap is open data, we cannot provide a free-of-charge map API or map tiles for third-parties.”

Wytyczna OSMF o bazach zbiorczych (Collective Database Guideline, zatwierdzona 17.06.2016 [CP]):

> „an OSM dataset used in combination with a non-OSM dataset will be considered a Collective Database, and will not trigger share-alike when: the non-OSM and OSM datasets do not reference each other; or (…) a non-OSM database replaces or adds a property of a primary feature, and uses either all OSM data or no OSM data for that property of that primary feature within the same regional cut”

> „You have a proprietary list of restaurants for a country. You would like to complement your list with the corresponding data from OpenStreetMap removing any duplicate objects in the process. The resulting, combined database would not be covered by this guideline and you would, if the dataset is publicly used, have to consider that your proprietary data may be subject to the ODbL share-alike terms.”

**Co to znaczy dla naszej bazy:**

1. **Strony i mapy z danymi OSM** to „produced work”: wystarczy podpis „© OpenStreetMap contributors” z linkiem do openstreetmap.org/copyright i informacja o licencji ODbL. Tekstów stron nie musimy udostępniać.
2. **Poprawki danych OSM** (np. dopisany prąd, poprawione współrzędne kempingu) w naszej bazie tworzą bazę pochodną. Jeśli ją publikujemy, musimy ją udostępnić na ODbL. Najprościej poprawki wnosić do samego OSM.
3. **Własne dane trzymamy osobno:** cenniki wypożyczalni nie dotyczą obiektów OSM, więc nie podlegają share-alike. Własny atrybut kempingów (np. „cena za noc”) jest bezpieczny tylko wtedy, gdy dla danego atrybutu w całym regionie bierzemy wszystko z jednego źródła, nie mieszając z OSM.
4. **Nie łączymy z listami prywatnymi** (camping.info, CampRest, Mapy Google) w jedną bazę z usuwaniem duplikatów. To przypadek z wytycznej, który uruchamia share-alike, a dane z Map Google są zakazane zasadami projektu.
5. **Kafelki map:** OSMF nie daje darmowych kafelków dla serwisów. Potrzebne są własne kafelki, statyczne mapki generowane przy budowie strony albo płatny dostawca (kosztów nie sprawdzałem).

Aktualizacja: OSM zmienia się na bieżąco; ekstrakt można odświeżać przy każdej budowie strony (np. raz w tygodniu).

### Cenniki wypożyczalni (własna baza)

Próbka: `dane/kampery-ceny-wynajmu-probka.csv`. W samych SERP-ach 18.10.2026 12 firm pokazuje w snippetach ceny lub opłaty (10 z nich cenę za dobę lub tydzień), zwykle w trzech sezonach: np. kamperykrakow.pl 499 / 599 / 699 zł, camperdiem.wroclaw.pl 390 / 480 / 650 zł, kokokamper.pl 590–950 zł (cennik 2027), kamperomania.pl 330 zł netto w niskim sezonie [SERP].

**Czy uczciwa porównywarka jest możliwa? Tak, przy kilku warunkach:**

- każda cena z linkiem do cennika i datą sprawdzenia; gdy cennika nie ma lub nie da się go dziś potwierdzić, „sprawdź u źródła”;
- normalizacja: netto/brutto (kamperomania i kamperypoznan podają netto), różne granice sezonów, opłata serwisowa (np. 230 zł w przyczepyszczecinek.pl), kaucja, limit kilometrów, minimalna liczba dni;
- porównanie na jednym koszyku, np. „7 dni w lipcu, brutto, z opłatą serwisową”, liczone tylko gdy wszystkie składniki są w cenniku;
- kopiujemy wyłącznie liczby (fakty), bez opisów i zdjęć firm.

**Praca:** 656 wizytówek to górna granica; z publicznym cennikiem będzie zapewne 100–150 firm (szacunek, nie liczyłem). Przy ok. 15 min na firmę start to 25–40 godzin, aktualizacja dwa razy w roku (styczeń przed sezonem i maj) 15–20 godzin. Część pracy może zrobić agent, ale wynik musi przejść przegląd niezależny.

---

## 6. Szkic serwisu

**Działy i liczba stron:**

| Dział | Start | Po 6 mies. |
|---|---|---|
| Wynajem kampera (hub, cenniki, wynajem wg województw i miast, typy kamperów do wynajęcia) | 1 hub + 16 województw + 20 miast + 6 porównań = 43 | + 40 miast + strony firm z cennikiem (cel 100) = ok. 180 |
| Noclegi: kempingi, pola namiotowe, camper parki (hub, regiony, miejscowości) | 1 hub + 16 województw + 30 regionów i miejscowości = 47 | + 120 miejscowości + strony kempingów z OSM z nazwą i min. 3 atrybutami (do 600, liczba do sprawdzenia) = ok. 770 |
| Wyposażenie kampera i kempingu (rankingi) | 15 | 45 |
| Zabudowa busa i vanlife (poradniki techniczne, bez przepisów) | 8 | 20 |
| Trasy po Polsce | 6 | 20 |
| Narzędzia | 3 | 6 |
| **Razem** | **ok. 120** | **ok. 1 040** |

**Narzędzia:**

1. Kalkulator kosztu wynajmu kampera (doby × sezon, opłata serwisowa, kaucja zwrotna, limit km, paliwo, kempingi) na danych z naszej bazy cenników.
2. Porównywarka cenników wypożyczalni (tabela z ceną za dobę w trzech sezonach, netto/brutto, opłatą serwisową, kaucją, linkiem i datą sprawdzenia).
3. Mapa kempingów, camper parków i punktów zrzutu z OSM z filtrami (prąd, woda, psy, całoroczny).
4. Kalkulator kosztu paliwa na trasę kamperem (spalanie i cena paliwa wpisuje użytkownik).
5. Kalkulator prądu w kamperze: akumulator, panel solarny, lodówka, klimatyzator (wspiera rankingi wyposażenia).
6. Interaktywna lista rzeczy do kampera i na kemping (checklista do odhaczania, bez wzorów dokumentów).

Nie robimy kalkulatora „czy kamper zmieści się w kat. B / DMC”: to treść prawna.

**Pierwszy klaster: „Wynajem kampera 2027: ceny i porównanie wypożyczalni”.** Zbieranie cenników 2027 od połowy grudnia 2026 (KoKo Kamper ma już cennik 2027 [SERP]), publikacja do 31.01.2027. Uzasadnienie [SV]: wyszukiwania wynajmu rosną ze 17 860 w grudniu do 31 200 w styczniu i 46 810 w marcu, szczyt w lipcu (83 460). Drugi klaster (noclegi nad morzem i na Mazurach) do końca marca 2027, bo noclegi ruszają w maju (98 090) i szczytują w lipcu (246 710).

**Nazwa i domena (tylko pomysły, dostępności nie sprawdzałem):** Kamperownia (kamperownia.pl, nawiązuje do paliwowni), Ile za kampera (ilezakampera.pl), Gdzie Kamperem (gdziekamperem.pl), Kempingownik (kempingownik.pl), Na Postój (napostoj.pl).

---

## 7. Ryzyka

- **AI Overview:** 9 z 20 SERP-ów [SERP]. Najmocniej przy definicjach („glamping co to”), listach („co zabrać na kemping”) i widełkach cen. Słabiej przy stronach z konkretną tabelą cenników i przy encjach lokalnych (tam jest Local Pack zamiast AIO).
- **Local Pack i OLX:** 9 z 20 SERP-ów ma Local Pack; OLX jest w 8 z 20 [SERP]. Frazy „kamper integra”, „mini kamper”, „bus przerobiony na kampera” to głównie zakup używanego auta.
- **Sezon:** ×6,4 dla całości, ×10,2 dla noclegów [SV]. Przychód skupia się w maju–sierpniu.
- **Brak płatnika w PL:** żaden program wynajmu nie jest potwierdzony dla Polski; afiliacja noclegów i sprzętu niepotwierdzona co do stawek. Przy leadach zależność od tego, czy wypożyczalnie same się zgłoszą (bez zimnych maili).
- **Treści prawne blisko rdzenia:** w 8 z 20 SERP-ów PAA zadaje pytania prawne („Czy w kamperze można spać podczas jazdy?”, „Czy w Polsce można spać w kamperze na parkingu?”, „Jaki mandat za spanie w kamperze podczas jazdy?”, „Ile wynosi podatek od przyczepy kempingowej?”, „Czy na glamping potrzebne są pozwolenia na budowę?”) [SERP]. AIO przy zabudowie busa ma osobną sekcję o akcyzie i rejestracji. Autorzy muszą świadomie to omijać.
- **Kafelki map:** koszt dostawcy map nieznany.
- **Aktualność cen:** cenniki zmieniają się co sezon; nieaktualna cena w porównywarce szkodzi zaufaniu bardziej niż jej brak.

### Omijamy (autorzy nie ruszają)

Wolumen fraz prawnych odrzuconych z mapy: 67 fraz, 7 820/mies. [LABS].

- Prawo jazdy (kat. B, C), DMC 3,5 t, „jaki kamper na kat. B”, przyczepy do 750 kg i „DMC przyczepy”.
- Rejestracja i homologacja zabudowy, przeróbka busa „przepisy”, akcyza, kod PKD, badania techniczne.
- Ubezpieczenia (OC, AC, ubezpieczenie kaucji), leasing, kredyt, podatki (w tym od przyczepy).
- Gdzie wolno stać i spać (parking, „na dziko”, mandaty, zakazy), spanie w kamperze podczas jazdy.
- Program „Zanocuj w lesie” (zasady, zgłoszenia, ograniczenia) oraz biwakowanie w parkach narodowych i rezerwatach.
- Opłata miejscowa i klimatyczna, winiety, opłaty drogowe, strefy czystego transportu.
- Pozwolenia na budowę glampingu i prowadzenie kempingu.
- Obowiązkowe wyposażenie pojazdu, przewóz butli gazowych w świetle przepisów.
- Wzory umów najmu, protokołów zdawczo-odbiorczych i regulaminów (do pobrania): zakaz.

---

## 8. Werdykt

**WARUNKOWO. Wynik 3,0 / 5** (wg [METODA.md](../METODA.md)).

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 3 | 594 910/mies. w 853 frazach [SV], ale trend r/r −1,9% (grupa B), „wynajem kampera” −26% r/r |
| Słabość SERP | 25% | 3,5 | 16 z 20 SERP-ów słabych wg kryterium ścisłego; huby z Local Pack i OLX |
| Zarobek | 25% | 2 | brak potwierdzonego programu wynajmu dla PL; 35 zł (ostrożny) i 1 950 zł (realny) miesięcznie po 12 mies. |
| Fosa danych / narzędzia | 15% | 4 | OSM (1 813 + 273 + 111 obiektów, ODbL, komercyjnie dozwolone) + własna baza cenników, której nikt nie ma |
| Niskie ryzyko | 15% | 3 | YMYL niskie, ale tematy prawne w PAA, AIO 9 z 20, sezon ×6,4 |

Wynik ważony: 3×0,2 + 3,5×0,25 + 2×0,25 + 4×0,15 + 3×0,15 = 3,03.

**Trzy powody:**

1. **Za:** przy frazach z pieniędzmi (wynajem, cenniki, noclegi w regionie) wygrywają małe firmy, nikt nie ma porównywarki cenników, a AIO cytuje małe serwisy (7 z 9).
2. **Przeciw:** płatnika w Polsce nie potwierdziłem. Programy wynajmu (CamperDays, Goboony, PaulCamper, Yescapa) działają dla innych krajów lub są zamknięte, więc realny przychód to ok. 1 950 zł/mies. po roku, w tym 879 zł z leadów, które dziś są tylko założeniem.
3. **Za, z zastrzeżeniem:** baza OSM i baza cenników to prawdziwa fosa, a kalkulator kosztu wynajmu ma sens. Rdzeń tematu ociera się jednak o prawo (kat. B, parkowanie, Zanocuj w lesie), więc część popytu i najdroższe frazy odpadają.

**Warunki „tak”:**

- Właściciel akceptuje model „porównywarka cenników + zapytania do wypożyczalni, które same się zgłoszą”.
- Właściciel (nie my) sprawdzi w panelach Awin, CJ i TradeTracker, czy wydawca z PL może promować CamperDays (camperdays.pl), Eurocampings (eurocampings.pl) i Booking.com, i z jaką stawką.
- Akceptujemy, że przychód przez pierwszy rok będzie mały, a serwis jest inwestycją w bazę danych.

Bez tych warunków: **NIE** jako główny serwis.

---

## Czego nie sprawdziłem

- Stawek i dostępności dla PL: Booking.com (strona wymaga JavaScript), Eurocampings PL, CamperDays PL, Pitchup, Decathlon PL, sklepów kempingowych, Travelpayouts dla wydawców z PL.
- RPM reklam w PL (brak źródła; założenie).
- Ile obiektów OSM ma nazwę i atrybuty (Overpass i Geofabrik blokowane przez proxy; liczby tylko z taginfo).
- Ile wypożyczalni publikuje pełny cennik (szacunek 100–150).
- Kosztu kafelków map u dostawców.
- Cen płatnych wyróżnień u konkurencji (BookingCamper, CampRest).
- Trendu r/r dla nowej mapy (biorę z oceny grupy B).

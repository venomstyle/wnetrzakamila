# Słowa kluczowe i popyt: wnetrzakamila.pl

Stan na 18.10.2026. Wszystkie liczby pochodzą z DataForSEO (rynek: Polska, `location_code` 2616, język `pl`), pobranych 18.10.2026. Dane surowe są w `analiza/dane/`.

## Skąd są liczby (legenda źródeł)

| Kod | Endpoint DataForSEO | Co z niego bierzemy |
|---|---|---|
| [RK] | `/v3/dataforseo_labs/google/ranked_keywords/live` | frazy i pozycje wnetrzakamila.pl |
| [DRO] | `/v3/dataforseo_labs/google/domain_rank_overview/live` | liczba fraz i szacowany ruch domeny |
| [SV] | `/v3/keywords_data/google_ads/search_volume/live` | średni wolumen, 12 miesięcy (paź 2025 – wrz 2026), CPC, konkurencja w Google Ads |
| [KD] | `/v3/dataforseo_labs/google/bulk_keyword_difficulty/live` | trudność frazy (0–100) |
| [KO] | `/v3/dataforseo_labs/google/keyword_overview/live` | intencja, elementy SERP z ostatniego zrzutu Labs, średnia ranga domen i liczba domen linkujących do stron z top 10 |
| [KS] | `/v3/dataforseo_labs/google/keyword_suggestions/live`, `/keyword_ideas/live` | rozszerzanie listy fraz |
| [SERP] | `/v3/serp/google/organic/live/advanced` (telefon, depth 20–40) | wyniki na żywo 18.10.2026 |
| [CP] | `/v3/on_page/content_parsing/live` | lista wpisów na stronie głównej i zawartość działu kalkulatorów |
| [BTE] | `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` | szacowany ruch konkurencji |

Uwagi do danych:
- CPC jest w USD, tak zwraca je DataForSEO.
- Google Ads łączy bliskie warianty. „japandi” i „styl japandi” albo „kalkulator budowlany” i „kalkulatory budowlane” mają identyczne serie. W sumach klastrów taką serię liczę raz.
- Trudność [KD] jest prawie bezużyteczna na polskim rynku: 305 z 397 sprawdzonych fraz ma KD = 0, a 52 nie ma wyniku. Dlatego trudność oceniam głównie po SERP-ach [SERP] i po średniej randze domen w top 10 [KO] (skala DataForSEO 0–1000, niżej znaczy słabsze domeny).
- Elementy SERP z [KO] pochodzą z wcześniejszych zrzutów Labs: 235 z 344 zrzutów jest z sierpnia–października 2026, część jest starsza (nawet z 2021 r.). Na żywo [SERP] AI Overview pojawia się częściej, np. przy „kalkulator betonu” i „projektant wnętrz online”, gdzie Labs go nie pokazuje.
- Trend to 12 słupków od października 2025 do września 2026 [SV]. Min i max to najniższy i najwyższy miesiąc.

## 1. Obecna widoczność

| Wskaźnik | Wartość | Źródło |
|---|---|---|
| Frazy w top 100 Google | 2 | [DRO], [RK] |
| Szacowany ruch organiczny (ETV) | 0,75 wizyty/mies. | [DRO] |
| Pozycje 31–40 | 1 fraza | [DRO] |
| Pozycje 71–80 | 1 fraza | [DRO] |
| Frazy nowe / utracone od poprzedniego pomiaru | 2 / 1 | [DRO] |
| Adresy pokazane przez Google dla `site:wnetrzakamila.pl` | 10 | [SERP] |

Frazy, na które strona się dziś pokazuje [RK]:

| Fraza | Wolumen [RK] | Pozycja (grupa / absolutna) | Strona | Pomiar SERP |
|---|---:|---|---|---|
| bardzo mały salon w bloku | 720 | 37 / 48 | /jak-urzadzic-maly-salon-w-bloku-praktyczny-poradnik-na-kazda-kieszen/ | 03.10.2026 |
| jak urządzić małą kuchnię | 390 | 73 / 83 | /jak-urzadzic-mala-kuchnie-praktyczny-poradnik-krok-po-kroku/ | 30.09.2026 |

Wolumen w [RK] pochodzi z Labs. Google Ads [SV] dla „bardzo mały salon w bloku” podaje 590.

W 14 SERP-ach sprawdzonych na żywo 18.10.2026 [SERP] wnetrzakamila.pl nie ma w top 20, także dla fraz, pod które są już wpisy („jak urządzić mały balkon”, „jaki kolor ścian do szarych mebli”).

Co jest na stronie [CP], [SERP site:]:
- 10 wpisów: mały balkon, mały salon w bloku, mała kuchnia, pokój młodzieżowy, pokój dziecka, ile kosztuje projekt domu, kolor ścian do szarych mebli, jak pomalować sufit bez smug, jak pomalować salon nowocześnie, ile kosztuje wizualizacja mieszkania. Do tego strona „O mnie”.
- Dział **Kalkulatory budowlane** (`/tematy/kalkulatory-budowlane/`) jest pusty. Strona zwraca kod 200 i tekst „No results found.” [CP]. Na stronie głównej są też nagłówki działów „Wnętrza”, „Remont”, „Ogród”.

Konkurencja dla porównania (szacowany ruch organiczny miesięcznie, ETV) [BTE]:

| Domena | Typ | ETV | Fraz |
|---|---|---:|---:|
| komfort.pl | sklep z blogiem | 248 802 | 13 829 |
| dobrykalkulator.pl | serwis kalkulatorów (ogólny) | 82 736 | 5 530 |
| muratordom.pl | portal budowlany | 75 501 | 17 329 |
| kb.pl | portal budowlany z kalkulatorami | 54 576 | 15 671 |
| dobrzemieszkaj.pl | portal wnętrzarski | 36 463 | 7 827 |
| kalkulatorxxl.pl | serwis kalkulatorów (ogólny) | 28 837 | 2 910 |
| czasnawnetrze.pl | blog wnętrzarski | 26 220 | 3 963 |
| tylkobeton.pl | mały serwis tematyczny (beton) | 1 786 | 131 |
| jakie-posadzki.pl | mały serwis tematyczny | 977 | 148 |
| kalkulato.pl | mały serwis kalkulatorów | 881 | 289 |
| ogarnijremont.pl | mały serwis remontowy | 136 | 64 |
| kalkulatorremontu.pl | jeden kalkulator | 61 | 13 |
| usefulhub.cloud, wizerunkowo.app, codegeek.com.pl | strony z pojedynczym kalkulatorem | 0,35–5,2 | 2–9 |
| wnetrzakamila.pl | ten blog | 0,75 | 2 |

Wniosek: strony z jednym kalkulatorem i prawie zerowym ruchem stoją dziś w top 10 dla „kalkulator płytek” [SERP]. Małe serwisy tematyczne (tylkobeton.pl, jakie-posadzki.pl) zbierają po kilkaset do ponad tysiąca wizyt miesięcznie [BTE].

## 2. Popyt według grup tematycznych

Zbadałem 415 fraz: 278 z listy startowej, 130 znalezionych przez [KS] i 7 o usługach projektowych [SV]. Każdą przypisałem do grupy i klastra (klaster = jedna przyszła strona). Popyt grupy to suma średnich miesięcznych wolumenów fraz w grupie [SV].

### 2.1 Grupy

| Grupa | Fraz | Popyt/mies. (suma) | Najsłabszy – najmocniejszy miesiąc | Trend paź 25 → wrz 26 | CPC śr. (USD) | Śr. ranga domen w top 10 | AI Overview (frazy) |
|---|---:|---:|---|---|---:|---:|---:|
| Kalkulatory i ilości materiałów | 103 | 42 250 | 33 170 (gru 25) – 57 910 (mar 26) | ▇▆▅▆▆██▇▆▆▅▅ | 0,62 | 328 | 29/76 |
| Ceny materiałów | 4 | 7 000 | 2 830 (sty 26) – 10 600 (kwi 26) | ▅▄▃▃▃███▇▇▇▆ | 0,47 | – | 3/4 |
| Koszty prac i remontu („ile kosztuje”) | 45 | 39 610 | 28 700 (wrz 26) – 52 790 (lut 26) | ▆▆▅▇██▇▆▇▆▆▅ | 0,59 | 387 | 30/37 |
| Remont: poradniki | 27 | 22 390 | 15 210 (gru 25) – 39 660 (lut 26) | ▅▅▄▄█▇▅▅▄▅▄▄ | 0,60 | 398 | 15/22 |
| Malowanie i kolory | 73 | 62 800 | 47 370 (gru 25) – 77 020 (mar 26) | ▇▇▅▇▇█▇▇▆██▆ | 0,21 | 409 | 44/65 |
| Aranżacja pomieszczeń | 79 | 120 930 | 85 310 (cze 26) – 154 990 (sty 26) | ██▆██▇▇▆▅▆▆▆ | 0,23 | 448 | 18/74 |
| Ogród, balkon (rośliny), taras | 53 | 234 620 | 80 800 (gru 25) – 499 860 (mar 26) | ▃▂▂▂▃█▇▇▅▄▄▄ | 0,26 | 415 | 19/43 |
| Usługi projektowe (projekt wnętrz) | 31 | 65 120 | 44 080 (wrz 26) – 94 430 (sty 26) | ▇▇▅█▇█▇▅▄▅▅▄ | 0,91 | 413 | 9/22 |


Źródła: wolumen, miesiące i CPC [SV]; ranga domen i AI Overview [KO]. „AI Overview (frazy)” = w ilu frazach z danymi Labs widział AI Overview.

Co z tego wynika:
- **Ogród** ma największy popyt, ale ponad połowa to trzy frazy zakupowe: „kostka brukowa” 74 000, „altana ogrodowa” 33 100, „pergola” 27 100 [SV]. Sezon jest bardzo silny: marzec 2026 to 499 860, grudzień 2025 to 80 800.
- **Aranżacja** jest stabilna, ze szczytem w styczniu (154 990) i dołkiem w czerwcu (85 310). Blisko połowa popytu (54 610 z 120 930) to style wnętrz i „garderoba”.
- **Kalkulatory** mają 42 250 wyszukiwań miesięcznie i najsłabsze domeny w top 10 (średnia ranga 328, przy 448 dla aranżacji) [KO]. Szczyt przypada na marzec (57 910), dołek na grudzień (33 170).
- **Usługi projektowe** mają najwyższy CPC (średnio 0,91 USD; „projektant wnętrz” 2,53 USD) [SV], ale to popyt na firmę z ofertą.
- **Malowanie i kolory** to 62 800 wyszukiwań, równo przez cały rok. Pasuje do istniejących wpisów.

### 2.2 Klastry (jedna linia = jedna strona do zrobienia albo istniejąca)

Kolumny: popyt [SV], trend [SV], CPC [SV], KD mediana/maks. [KD], ranga domen w top 10 [KO], AIO = ile fraz z AI Overview / ile fraz z danymi [KO], „strona dziś” wg [CP].


**Kalkulatory i ilości materiałów**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Kalkulatory ciesielskie (drewno, więźba, schody, dach, taras) | 9 | 8 570 | 6 980 (sty 26) – 10 960 (mar 26, maj 26) | █▇▆▆▆███▇▆▆▆ | 0,54 | 0/0 | 415 | 3/8 | **brak** |
| Kalkulator stali / zbrojenia / blachy (budowa) | 7 | 6 200 | 4 860 (sie 26) – 7 730 (mar 26) | ▇▆▆▇▇██▇▆▆▆▆ | 0,95 | 0/0 | 251 | 1/5 | **brak** |
| Kalkulator betonu (m3, worki, cement) | 9 | 6 170 | 2 710 (sty 26) – 9 210 (kwi 26) | ▇▅▄▃▃██▇▇▇▆▆ | 0,56 | 0/0 | 280 | 3/6 | **brak** |
| Kalkulator m2 / m3 / powierzchni | 4 | 4 920 | 3 660 (wrz 26) – 6 300 (paź 25, mar 26) | █▇▆▆▆██▇▆▆▆▅ | 0,01 | 0/0 | 334 | 0/4 | **brak** |
| Kalkulator styropianu / ocieplenia | 6 | 2 830 | 1 920 (gru 25) – 4 850 (mar 26) | ▆▄▄▄▅█▆▅▄▅▅▆ | 0,16 | 4/23 | 299 | 2/4 | **brak** |
| Kalkulator płytek + kleju + fugi | 11 | 2 830 | 2 240 (wrz 26) – 3 350 (paź 25) | ██▆▇▇██▇▆▇▇▆ | 0,25 | 0/49 | 338 | 5/8 | **brak** |
| Kalkulatory instalacyjne (pompa, PV, grzejnik, klima, kabel) | 7 | 2 200 | 1 430 (wrz 26) – 3 320 (mar 26) | ▆▆▅▇▇█▆▅▅▅▄▄ | 0,70 | 4/16 | 328 | 2/6 | **brak** |
| Kalkulator murowania (pustaki, cegły, bloczki) | 8 | 1 800 | 1 350 (wrz 26) – 2 640 (mar 26) | ▇▇▆▅▅█▇▆▅▅▅▅ | 1,09 | 0/0 | 270 | 3/5 | **brak** |
| Kalkulator kosztów remontu / wykończenia / budowy | 8 | 1 720 | 790 (wrz 26) – 2 690 (mar 26) | ▆▇▅███▇▅▄▄▃▃ | 0,79 | 0/46 | 251 | 2/6 | **brak** |
| Kalkulator farby (ile farby na m2 / pokój) | 8 | 1 550 | 1 030 (wrz 26) – 2 080 (mar 26) | ▇▇▅▇▇██▆▅▆▆▄ | 0,21 | 0/13 | 321 | 2/6 | **brak** |
| Kalkulator wylewki / gładzi / tynku | 8 | 920 | 590 (wrz 26) – 1 250 (mar 26) | ▇▇▅█▇██▇▆▅▄▄ | 0,18 | 0/0 | 247 | 3/6 | **brak** |
| Hub: kalkulatory budowlane | 3 | 810 | 520 (cze 26, sie 26) – 1 020 (mar 26) | ▇▇▆█▇█▇▇▅▆▅▅ | 0,72 | 0/0 | 390 | 1/3 | jest, pusta |
| Kalkulator ogrodzenia | 2 | 600 | 260 (gru 25) – 1 110 (mar 26) | ▄▃▂▃▅█▇▇▅▅▅▅ | 0,60 | 4/7 | 213 | 1/2 | **brak** |
| Kalkulator kostki brukowej (+ podsypka) | 6 | 580 | 180 (sty 26) – 1 000 (mar 26) | ▄▃▂▂▃███▆▆▅▄ | 0,52 | 0/0 | 341 | 1/2 | **brak** |
| Kalkulator paneli i listew | 4 | 340 | 260 (gru 25, wrz 26) – 440 (sty 26, mar 26) | ██▅███▆▆▆▇▇▅ | 0,72 | 0/32 | 318 | 0/3 | **brak** |
| Kalkulator tapety | 3 | 220 | 150 (wrz 26) – 340 (lis 25) | ▇█▆▇▆▇▆▆▅▅▅▄ | 3,39 | 0/0 | 279 | 0/2 | **brak** |

**Ceny materiałów**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Ceny materiałów (beton, cement, piasek) | 4 | 7 000 | 2 830 (sty 26) – 10 600 (kwi 26) | ▅▄▃▃▃███▇▇▇▆ | 0,47 | 0/0 | – | 3/4 | **brak** |

**Koszty prac i remontu („ile kosztuje”)**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Koszty instalacji i drobnych prac (pojedyncze poradniki) | 9 | 10 720 | 7 330 (wrz 26) – 20 410 (cze 26) | ▄▄▃▅▅▅▄▄█▄▅▃ | 0,68 | 0/0 | 332 | 7/8 | **brak** |
| Ile kosztuje malowanie (pokój, ściany, m2) | 7 | 6 530 | 4 090 (gru 25) – 8 380 (mar 26) | ▆▅▄▆▇███▇██▇ | 0,49 | 0/0 | 417 | 5/5 | **brak** |
| Koszt budowy domu | 4 | 4 920 | 3 200 (wrz 26) – 10 600 (lut 26) | ▄▃▃▅█▅▅▄▃▄▄▃ | 0,53 | 0/0 | 466 | 3/4 | **brak** |
| Koszt remontu / wykończenia mieszkania | 7 | 4 760 | 1 410 (wrz 26) – 9 610 (lut 26) | ▄▄▃▅█▇▆▄▃▃▂▂ | 1,04 | 0/0 | 384 | 4/5 | **brak** |
| Koszt remontu łazienki | 4 | 4 590 | 3 560 (wrz 26) – 6 510 (mar 26) | ▇▆▅▇▇█▇▆▆▆▅▅ | 0,36 | 0/0 | 411 | 3/4 | **brak** |
| Cennik robocizny: panele, płytki, gładź, cyklinowanie | 8 | 3 550 | 2 920 (cze 26) – 4 340 (sty 26) | ██▆███▇▇▆▇▇▆ | 0,43 | 0/0 | 353 | 4/5 | **brak** |
| Kuchnia i szafa na wymiar: ceny | 3 | 2 890 | 2 240 (cze 26) – 4 220 (sty 26) | ▇▇▆█▇▇▆▅▅▅▅▅ | 0,42 | 0/0 | 381 | 1/3 | **brak** |
| Ile kosztuje projekt domu | 2 | 1 260 | 700 (wrz 26) – 1 690 (sty 26) | ▆▆▆█▇█▇▆▅▅▄▄ | 0,51 | 0/0 | 398 | 2/2 | jest |
| Koszt remontu kuchni | 1 | 390 | 320 (maj 26, cze 26) – 480 (paź 25, sty 26) | █▇▇███▇▆▆▆▇▆ | 0,45 | 0/0 | – | 1/1 | **brak** |

**Remont: poradniki**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Ile schnie / ile waży (krótkie odpowiedzi) | 9 | 6 830 | 4 380 (sty 26) – 8 590 (lip 26) | █▇▅▅▅▇▇█▆███ | 0,23 | 0/0 | 387 | 8/8 | **brak** |
| Remont ogólnie (łazienka, mieszkanie) | 2 | 6 300 | 2 900 (wrz 26) – 16 500 (lut 26) | ▃▃▂▄█▇▄▃▂▃▂▂ | 1,24 | 0/0 | 473 | 0/2 | **brak** |
| Kolejność prac remontowych / remont krok po kroku | 7 | 4 350 | 2 480 (gru 25) – 10 480 (lut 26) | ▄▃▂▃█▄▄▄▄▄▄▃ | 0,15 | 0/0 | 358 | 5/6 | **brak** |
| Poradniki wykończeniowe (panele, płytki, tapeta, gładź) | 8 | 4 190 | 3 410 (gru 25) – 4 700 (mar 26) | ▇█▆▇██▇▇▇██▇ | 0,16 | 0/0 | 329 | 1/5 | **brak** |
| Odliczenie remontu od podatku (temat prawny) | 1 | 720 | 110 (cze 26) – 3 600 (lut 26) | ▂▁▂▃█▃▂▁▁▁▁▁ | 0,00 | 0/0 | 330 | 1/1 | **brak** |

**Malowanie i kolory**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Kolory ścian: odcienie (szałwia, beż, greige, oliwka…) | 15 | 23 220 | 18 080 (gru 25) – 28 210 (lip 26) | ▇▇▆▇▇██▇▇██▇ | 0,13 | 0/0 | 383 | 7/12 | **brak** |
| Farby i narzędzia (porównania, afiliacja) | 7 | 13 050 | 10 600 (gru 25) – 15 970 (mar 26) | ▇▇▆▇▇█▇█▇▇█▇ | 0,38 | 0/3 | 396 | 3/7 | **brak** |
| Jak malować ściany (krok po kroku) | 15 | 9 670 | 7 000 (gru 25) – 12 390 (mar 26) | ▇▇▅▆▇█▇▇▅▇▇▅ | 0,28 | 0/0 | 442 | 9/12 | **brak** |
| Malowanie sufitu | 6 | 4 410 | 2 800 (gru 25) – 5 620 (mar 26) | ▆▆▄▆▆█▇▆▅█▇▆ | 0,15 | 0/48 | 415 | 2/6 | jest |
| Malowanie mebli, płytek, drzwi, kominka | 7 | 2 900 | 1 840 (cze 26) – 3 810 (paź 25) | ██▆███▇▆▄▆▆▅ | 0,24 | 0/0 | 464 | 5/7 | **brak** |
| Kolor ścian do mebli (białe, brązowe, dąb sonoma, kaszmir) i zasłon | 6 | 2 380 | 1 630 (gru 25) – 2 850 (lis 25) | ██▅███▇▇▆▇█▇ | 0,10 | 0/0 | 499 | 6/6 | **brak** |
| Modne kolory ścian 2026 | 2 | 2 290 | 460 (paź 25) – 3 620 (mar 26) | ▂▃▃▇██▇▆▆▆▅▅ | 0,13 | 0/0 | 355 | 1/1 | **brak** |
| Kolor ścian w sypialni | 3 | 1 630 | 950 (cze 26) – 1 990 (lut 26) | ██▅███▇▆▄▆▆▆ | 0,15 | 0/0 | 484 | 2/3 | **brak** |
| Kolor ścian w kuchni | 4 | 1 180 | 730 (cze 26) – 1 450 (lis 25) | ██▅███▇▆▅▆▆▅ | 0,09 | 0/0 | 404 | 4/4 | **brak** |
| Kolor ścian w salonie | 3 | 1 130 | 640 (cze 26) – 1 570 (mar 26) | ██▅███▇▅▄▅▅▄ | 0,12 | 0/0 | 380 | 2/3 | **brak** |
| Kolor ścian do szarych mebli | 3 | 620 | 400 (cze 26) – 830 (mar 26) | ██▅▇▇█▆▆▄▆▆▆ | 0,11 | 0/0 | 294 | 1/2 | jest |
| Jak pomalować salon | 2 | 320 | 180 (wrz 26) – 530 (lis 25, mar 26) | ▇█▄▇▇█▇▅▃▄▄▃ | 0,20 | 0/0 | 409 | 2/2 | jest |

**Aranżacja pomieszczeń**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Style wnętrz (boho, japandi, skandynawski…) | 9 | 41 920 | 33 980 (cze 26) – 50 980 (sty 26) | █▇▆█▇▇▇▇▆▇▇▇ | 0,26 | 0/2 | 424 | 3/9 | **brak** |
| Garderoba | 2 | 12 690 | 8 420 (cze 26) – 15 680 (paź 25) | ██▇██▇█▆▅▆▇▇ | 0,28 | 1/2 | 471 | 0/2 | **brak** |
| Sypialnia (mała, przytulna, na poddaszu) | 6 | 11 520 | 7 610 (cze 26) – 15 080 (lis 25) | ██▅██▇▇▅▅▅▅▅ | 0,21 | 0/0 | 438 | 1/6 | **brak** |
| Jak urządzić salon (hub) | 5 | 10 350 | 5 610 (cze 26) – 15 190 (lis 25) | ▇█▆█▇▇▆▄▃▄▄▄ | 0,25 | 0/0 | 399 | 2/5 | **brak** |
| Mała kuchnia | 6 | 5 940 | 3 500 (cze 26) – 7 950 (sty 26) | ██▆██▇▇▅▄▅▅▅ | 0,10 | 0/49 | 564 | 1/6 | jest |
| Mała łazienka w bloku | 5 | 5 640 | 3 650 (wrz 26) – 8 380 (sty 26) | █▇▆█▇▇▆▅▄▅▅▄ | 0,16 | 0/0 | 481 | 1/5 | **brak** |
| Salon z aneksem kuchennym | 4 | 4 770 | 3 940 (cze 26) – 6 390 (paź 25) | █▇▆█▇▇▇▆▅▆▇▆ | 0,09 | 0/0 | 464 | 1/4 | **brak** |
| Przedpokój w bloku | 4 | 4 530 | 2 590 (cze 26) – 6 210 (sty 26) | ██▅██▆▅▄▄▅▅▅ | 0,17 | 0/0 | 471 | 2/4 | **brak** |
| Pokój dla dziewczynki | 1 | 4 400 | 2 900 (cze 26) – 6 600 (sty 26) | ▇▇▅█▇▆▆▅▄▆▆▅ | 0,16 | 0/0 | 527 | 0/1 | **brak** |
| Pokój młodzieżowy | 8 | 4 230 | 2 400 (cze 26) – 6 190 (sty 26) | ██▆█▇▇▅▅▄▅▅▄ | 0,20 | 0/18 | 487 | 1/6 | jest |
| Pokój dla chłopca | 1 | 2 900 | 1 600 (cze 26) – 4 400 (paź 25, sty 26) | █▇▅██▇▇▅▃▅▆▄ | 0,15 | 0/0 | 491 | 0/1 | **brak** |
| Pokój dziecka | 5 | 2 740 | 1 510 (wrz 26) – 3 940 (sty 26) | ▇▇▅█▇▇▆▅▄▄▅▄ | 0,20 | 2/18 | 469 | 1/4 | jest |
| Mały pokój, pokój 2x3, pokój ze skosami | 5 | 2 320 | 1 280 (cze 26) – 3 070 (sty 26) | ██▆██▇▆▅▄▅▆▅ | 0,32 | 0/0 | 348 | 1/5 | **brak** |
| Domowe biuro | 3 | 2 300 | 1 630 (gru 25) – 2 900 (mar 26) | ▇▆▅▆▇█▇▆▆▇▇▆ | 0,27 | 0/0 | 361 | 2/2 | **brak** |
| Mały balkon | 7 | 2 150 | 400 (gru 25) – 5 030 (mar 26) | ▁▁▁▂▃███▅▄▃▂ | 0,15 | 0/0 | 441 | 1/6 | jest |
| Mały salon w bloku | 4 | 1 720 | 1 000 (cze 26) – 2 760 (lis 25) | ██▅█▇▆▅▄▃▅▅▄ | 0,15 | 0/0 | 410 | 1/4 | jest |
| Kawalerka i małe mieszkanie | 4 | 810 | 480 (cze 26) – 1 110 (sty 26) | ▇█▆███▇▅▄▄▅▅ | 0,31 | 0/0 | 423 | 0/4 | **brak** |

**Ogród, balkon (rośliny), taras**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Kostka brukowa (poradnik) | 3 | 80 700 | 36 090 (gru 25) – 147 800 (mar 26) | ▄▃▂▂▃██▇▆▆▅▅ | 0,15 | 0/1 | 485 | 0/3 | **brak** |
| Altana i pergola | 3 | 61 080 | 24 520 (gru 25) – 136 100 (maj 26) | ▂▂▂▂▃▇▇█▆▅▄▃ | 0,59 | 16/27 | 355 | 0/3 | **brak** |
| Kalendarz ogrodnika (kiedy sadzić / przycinać) | 6 | 31 300 | 4 550 (gru 25) – 102 100 (mar 26) | ▄▂▁▁▄█▃▂▁▂▂▄ | 0,07 | 0/0 | 431 | 6/6 | **brak** |
| Aranżacja ogrodu (mały ogród, rabata, żywopłot) | 14 | 22 210 | 7 480 (gru 25) – 63 120 (mar 26) | ▂▂▁▂▃█▅▅▃▃▃▄ | 0,22 | 0/51 | 351 | 4/12 | **brak** |
| Rośliny i kwiaty na balkon | 6 | 14 250 | 1 230 (gru 25) – 56 700 (maj 26) | ▁▁▁▁▁▄▅█▄▂▂▁ | 0,07 | 3/52 | 392 | 0/5 | **brak** |
| Trawnik (siew, nawożenie, trawa z rolki) | 11 | 11 330 | 1 660 (gru 25) – 35 850 (mar 26) | ▂▁▁▁▂█▅▄▃▂▃▃ | 0,13 | 0/1 | 365 | 4/5 | **brak** |
| Taras (drewniany, z kostki, z desek) | 5 | 8 240 | 2 910 (gru 25) – 15 650 (maj 26) | ▃▃▂▃▃▇▇█▆▅▄▃ | 0,25 | 0/0 | 425 | 2/5 | **brak** |
| Warzywnik i podwyższone grządki | 2 | 3 200 | 1 040 (gru 25) – 9 000 (mar 26) | ▂▂▁▃▄█▆▅▃▃▂▂ | 0,31 | 0/0 | 308 | 2/2 | **brak** |
| Kostka brukowa: cena z ułożeniem | 3 | 2 310 | 980 (sty 26) – 4 310 (mar 26) | ▅▄▃▂▄█▇▆▅▄▅▅ | 0,52 | 0/0 | 394 | 1/2 | **brak** |

**Usługi projektowe (projekt wnętrz)**

| Klaster (strona) | Fraz | Popyt/mies. | Min – max (miesiąc) | Trend | CPC (USD) | KD med./max | Ranga top 10 | AIO | Strona dziś |
|---|---:|---:|---|---|---:|---|---:|---:|---|
| Usługa: projekt wnętrz / kuchni / łazienki | 8 | 46 300 | 31 580 (wrz 26) – 64 400 (sty 26) | ▇▇▅█▇█▇▆▅▅▅▄ | 1,07 | 8/18 | 410 | 0/8 | **brak** |
| Projektowanie wnętrz online i programy 3D | 10 | 16 130 | 10 320 (cze 26) – 26 460 (sty 26) | ▆▇▅█▇▆▅▄▄▄▄▄ | 0,51 | 4/22 | 434 | 7/10 | **brak** |
| Ile kosztuje projekt wnętrza (cennik) | 11 | 2 280 | 1 400 (wrz 26) – 3 190 (mar 26) | ▇▇▅███▇▆▄▅▅▄ | 0,79 | 0/0 | 249 | 2/4 | **brak** |
| Wizualizacja mieszkania | 2 | 410 | 270 (cze 26, wrz 26) – 490 (mar 26, kwi 26) | █▇▆▇▇██▇▅▆▆▅ | 0,68 | –/– | – | 0/0 | jest |


### 2.3 Największe frazy w każdej grupie

Kolumny: średnia, min–max, miesiąc szczytu, trend i CPC [SV]; KD [KD]; intencja i AIO [KO]. Pełna lista 415 fraz z 12 miesiącami: `analiza/dane/frazy_wolumeny.csv`.


**Kalkulatory i ilości materiałów**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| kalkulator betonu | 4 400 | 1 900 – 6 600 | mar 26, kwi 26 | ▇▅▄▃▃██▇▇▇▆▆ | 0,56 | 0 | informational | nie |
| kalkulator ciesielski | 3 600 | 2 400 – 5 400 | paź 25, maj 26 | █▇▅▄▄▆▇█▇▆▆▇ | 0,26 | 0 | informational | tak |
| kalkulator stali | 2 900 | 2 400 – 3 600 | mar 26 | ▇▆▆▇▇█▇▇▆▆▆▆ | 1,07 | 0 | informational | nie |
| kalkulator styropianu | 1 900 | 1 300 – 3 600 | mar 26 | ▆▄▃▃▄█▆▅▄▅▄▅ | 0,08 | 9 | informational | nie |
| kalkulator metrów kwadratowych | 1 900 | 1 300 – 2 400 | paź 25, mar 26 | █▇▆▇▆█▇▇▆▆▆▅ | – | 0 | informational | nie |
| kalkulator blachy | 1 900 | 1 300 – 2 400 | mar 26, kwi 26 | ▇▇▆▇▇██▇▅▆▅▅ | 1,20 | 0 | informational | tak |
| kalkulator schodów | 1 300 | 1 000 – 1 600 | sty 26, mar 26, kwi 26 | ▇▇▇█▅██▇▅▅▅▅ | 0,78 | 0 | informational | tak |
| kalkulator drewna | 1 300 | 880 – 2 400 | mar 26 | ▅▅▄▄▆█▇▆▅▄▄▃ | 0,74 | 0 | informational | nie |
| kalkulator powierzchni | 1 300 | 1 000 – 1 600 | paź 25, mar 26, kwi 26 | █▇▅▇▇██▇▇▅▅▅ | – | 0 | informational | nie |
| kalkulator m2 | 1 000 | 880 – 1 300 | paź 25, lis 25, mar 26 | ██▇▇▇███▇▆▇▆ | 0,01 | 0 | informational | nie |

**Ceny materiałów**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| ile kosztuje kubik betonu | 1 900 | 880 – 2 900 | mar 26, kwi 26, maj 26 | ▅▄▃▃▄███▆▇▇▆ | 0,96 | 0 | informational | tak |
| ile kosztuje worek cementu | 1 900 | 480 – 2 900 | kwi 26, maj 26 | ▄▃▂▂▂▇██▇▇▇▇ | 0,08 | 0 | informational | nie |
| ile kosztuje tona piasku | 1 900 | 720 – 2 900 | mar 26, kwi 26, maj 26 | ▄▃▂▃▃████▇▇▆ | 0,32 | 0 | informational | tak |
| ile kosztuje metr sześcienny betonu | 1 300 | 590 – 1 900 | kwi 26 | ▆▅▄▃▄▇█▇▆▆▆▆ | 0,54 | 0 | informational | tak |

**Koszty prac i remontu („ile kosztuje”)**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| ile kosztuje pompa ciepła | 2 900 | 1 600 – 5 400 | sty 26 | ▆▅▄█▇▆▅▄▃▄▄▄ | 0,61 | 0 | informational | nie |
| ile kosztuje malowanie pokoju | 2 400 | 1 600 – 2 900 | paź 25, mar 26 | █▇▅▇▇█▇▆▆▇▇▆ | 0,40 | 0 | informational | tak |
| ile kosztuje klimatyzacja do domu | 2 400 | 320 – 14 800 | cze 26 | ▁▁▁▁▁▁▁▁█▂▃▁ | 0,70 | 0 | informational | tak |
| koszt budowy domu | 1 900 | 1 000 – 4 400 | lut 26 | ▄▃▃▅█▅▄▃▂▃▃▂ | 0,62 | 0 | informational | nie |
| ile kosztuje malowanie ścian | 1 900 | 1 000 – 2 900 | maj 26, lip 26, sie 26 | ▃▄▄▆▆▇▇█▇██▇ | 0,44 | 0 | informational | tak |
| ile kosztuje remont łazienki | 1 600 | 1 300 – 1 900 | sty 26, lut 26 | ▇▇▆██▇▇▆▆▆▆▆ | 0,50 | 0 | informational | tak |
| ile kosztuje ocieplenie domu | 1 600 | 1 000 – 1 900 | sty 26, mar 26 | ▇▇▆█▇█▇▇▅▆▅▅ | 0,51 | 0 | informational | tak |
| remont łazienki koszt robocizny | 1 600 | 1 300 – 2 400 | mar 26 | ▇▆▅▅▆█▇▇▇▇▇▆ | 0,07 | 0 | commercial | tak |
| koszt remontu mieszkania | 1 300 | 210 – 2 900 | mar 26 | ▃▃▂▅▆█▇▄▂▂▂▁ | 0,99 | 0 | informational | tak |
| koszt remontu łazienki | 1 300 | 590 – 2 400 | mar 26 | ▅▅▃▇▇█▇▅▃▃▂▂ | 0,56 | 0 | commercial | tak |

**Remont: poradniki**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| remont łazienki | 4 400 | 1 900 – 12 100 | lut 26 | ▃▃▂▄█▇▃▃▂▂▂▂ | 0,85 | 0 | commercial | nie |
| jakie panele podłogowe wybrać | 1 900 | 1 300 – 2 400 | mar 26 | ▆▆▅▅▆█▇▇▇▇▇▆ | 0,16 | 0 | informational | nie |
| remont kuchni od czego zacząć | 1 900 | 1 300 – 2 400 | mar 26 | ▇▆▅▅▆█▇▇▇▇▇▆ | 0,02 | 0 | informational | tak |
| remont mieszkania | 1 900 | 1 000 – 4 400 | lut 26 | ▃▃▂▄█▆▅▄▂▃▂▂ | 2,13 | 0 | informational | nie |
| ile waży kubik betonu | 1 900 | 720 – 2 400 | kwi 26, maj 26, lip 26 | ▇▇▅▃▃▇██▇█▇█ | – | 0 | informational | tak |
| remont starego domu od czego zacząć | 1 600 | 1 000 – 1 900 | paź 25, mar 26, kwi 26 | █▇▅▆▇██████▇ | – | 0 | informational | tak |
| ile schnie grunt | 1 300 | 880 – 1 600 | paź 25, lip 26, sie 26 | █▇▅▅▅▇▇▇▅██▇ | – | 0 | informational | tak |
| panele winylowe czy laminowane | 1 000 | 720 – 1 600 | lut 26 | ▅▅▅▇█▅▅▅▄▅▅▅ | 0,22 | 0 | transactional | tak |
| co można odliczyć od podatku remont | 720 | 110 – 3 600 | lut 26 | ▂▁▂▃█▃▂▁▁▁▁▁ | 0,00 | 0 | informational | tak |
| ile schnie wylewka samopoziomująca | 720 | 590 – 1 000 | lip 26 | █▆▅▆▆▆▆▆▆███ | 0,37 | 0 | informational | tak |

**Malowanie i kolory**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| agregat malarski | 9 900 | 8 100 – 12 100 | mar 26, maj 26, sie 26 | ▇▇▆▇▇█▇█▇▇█▇ | 0,44 | 3 | informational | nie |
| kolor szałwiowy | 8 100 | 4 400 – 9 900 | mar 26, kwi 26, maj 26 | ▆▆▄▆▇██████▇ | 0,10 | 0 | informational | tak |
| butelkowa zieleń | 5 400 | 4 400 – 6 600 | paź 25, lis 25, gru 25 | ████▇▇▇▇▆▇▇▇ | 0,26 | 0 | transactional | nie |
| malowanie ścian | 3 600 | 2 400 – 5 400 | mar 26 | ▆▆▄▆▇█▇▆▅▆▅▄ | 0,51 | 0 | informational | tak |
| szałwiowa zieleń | 2 400 | 880 – 4 400 | lip 26 | ▂▂▃▃▅▇▆▅▆█▆▅ | 0,10 | 0 | informational | nie |
| modne kolory ścian 2026 | 1 900 | 390 – 2 900 | lut 26, mar 26 | ▂▃▃▇██▇▆▆▆▆▅ | 0,12 | 0 | informational | tak |
| jak malować sufit | 1 900 | 1 300 – 2 400 | lip 26, sie 26 | ▆▇▅▅▆▇▆▆▆██▇ | 0,15 | 15 | informational | nie |
| malowanie sufitu | 1 600 | 880 – 2 400 | mar 26 | ▅▅▃▆▆█▇▅▃▆▅▃ | 0,18 | 0 | informational | tak |
| gruntowanie ścian | 1 600 | 1 300 – 1 900 | paź 25, lis 25, mar 26 | ██▆▆▆█▇▇▆██▇ | 0,10 | 0 | informational | tak |
| beżowe ściany | 1 300 | 720 – 1 600 | paź 25, lis 25, sty 26 | ██▅█▇▇▇▅▄▇▇▅ | 0,09 | 0 | transactional | nie |

**Aranżacja pomieszczeń**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| garderoba | 12 100 | 8 100 – 14 800 | paź 25, lis 25, sty 26 | ██▇██▇█▆▅▆▇▇ | 0,28 | 2 | informational | nie |
| styl boho | 8 100 | 5 400 – 12 100 | kwi 26 | ▇▅▄▆▅▅█▇▆▇▆▄ | 0,12 | 0 | informational | nie |
| styl japandi | 8 100 | 6 600 – 9 900 | sty 26 | ▆▇▆█▇▇▇▆▆▆▇▇ | 0,24 | 0 | informational | tak |
| japandi | 8 100 | 6 600 – 9 900 | sty 26 | ▇▇▆█▇▇▇▇▆▇▇▆ | 0,45 | 0 | informational | tak |
| aranżacja salonu | 6 600 | 3 600 – 9 900 | lis 25, sty 26 | ▇█▆█▇▇▆▄▃▄▄▄ | 0,28 | 0 | informational | nie |
| aranżacja sypialni | 5 400 | 2 900 – 6 600 | paź 25, lis 25, sty 26 | ██▅██▇▇▅▄▅▅▅ | 0,20 | 0 | informational | nie |
| pokój dla dziewczynki | 4 400 | 2 900 – 6 600 | sty 26 | ▇▇▅█▇▆▆▅▄▆▆▅ | 0,16 | 0 | transactional | nie |
| styl rustykalny | 4 400 | 3 600 – 5 400 | paź 25, sty 26 | █▇▆█▇▇▆▆▆▆▆▆ | 0,26 | 0 | informational | nie |
| styl skandynawski | 3 600 | 2 900 – 4 400 | paź 25, lis 25, sty 26 | ██▇██▇▇▆▆▆▆▆ | 0,21 | 0 | informational | nie |
| styl hampton | 3 600 | 1 900 – 8 100 | wrz 26 | ▃▂▂▅▃▃▃▃▂▃▇█ | 0,38 | 0 | informational | tak |

**Ogród, balkon (rośliny), taras**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| kostka brukowa | 74 000 | 33 100 – 135 000 | mar 26, kwi 26 | ▄▃▂▂▃██▇▆▆▅▅ | 0,09 | 1 | transactional | nie |
| altana ogrodowa | 33 100 | 12 100 – 74 000 | maj 26 | ▂▂▂▂▃▇▇█▆▅▄▂ | 0,32 | 16 | transactional | nie |
| pergola | 27 100 | 12 100 – 60 500 | maj 26 | ▃▂▂▂▂▆▇█▇▆▅▃ | 0,93 | 0 | transactional | nie |
| kwiaty na balkon | 12 100 | 720 – 49 500 | maj 26 | ▁▁▁▁▁▃▅█▃▂▂▁ | 0,06 | 3 | informational | nie |
| żywopłot | 8 100 | 2 400 – 33 100 | mar 26 | ▂▁▁▁▂█▃▃▂▂▂▅ | 0,08 | 0 | informational | nie |
| kiedy przycinać hortensje | 8 100 | 720 – 40 500 | mar 26 | ▂▂▁▁▅█▁▁▁▁▁▁ | 0,04 | 0 | informational | tak |
| kiedy przycinać tuje | 8 100 | 1 000 – 27 100 | mar 26 | ▂▁▁▁▂█▃▃▂▃▃▃ | 0,07 | 0 | informational | tak |
| taras drewniany | 6 600 | 2 400 – 12 100 | maj 26 | ▃▃▂▃▃▇▇█▆▅▄▃ | 0,27 | 0 | transactional | nie |
| projekt ogrodu | 5 400 | 2 400 – 12 100 | mar 26 | ▃▃▂▃▄█▇▆▃▃▃▂ | 0,48 | 26 | informational | nie |
| kiedy siać trawę | 5 400 | 720 – 22 200 | mar 26 | ▂▁▁▁▂█▄▂▁▁▂▂ | 0,11 | 0 | informational | tak |

**Usługi projektowe (projekt wnętrz)**

| Fraza | Śr./mies. | Min – max | Szczyt | Trend | CPC (USD) | KD | Intencja | AIO |
|---|---:|---|---|---|---:|---:|---|---|
| projekt kuchni | 12 100 | 8 100 – 18 100 | sty 26 | ▇▆▅█▆▆▆▄▄▄▄▄ | 0,26 | 0 | informational | nie |
| projekt łazienki | 9 900 | 6 600 – 14 800 | sty 26 | ▇▇▆█▇▇▇▆▅▅▅▄ | 0,49 | 0 | informational | nie |
| projektowanie wnętrz | 8 100 | 6 600 – 12 100 | sty 26, mar 26 | ▇▇▅█▇█▇▆▅▅▅▅ | 1,35 | 7 | informational | nie |
| projektant wnętrz | 5 400 | 4 400 – 8 100 | mar 26 | ▇▇▅▇▇█▇▅▅▅▅▅ | 2,53 | 9 | informational | nie |
| program do projektowania wnętrz | 5 400 | 2 900 – 9 900 | sty 26 | ▆▇▅█▆▆▅▃▃▃▄▃ | 0,59 | 0 | informational | tak |
| architekt wnętrz | 4 400 | 2 400 – 6 600 | mar 26 | ▇▆▃▆▇█▇▆▄▅▄▃ | 2,15 | 13 | informational | nie |
| projektant wnętrz online | 2 900 | 1 900 – 4 400 | lis 25, sty 26, mar 26 | ▇█▆█▇█▇▅▅▅▅▄ | 0,41 | 15 | commercial | nie |
| projekt mieszkania | 2 400 | 1 300 – 4 400 | mar 26 | ▆▆▄▇▆█▇▅▃▄▃▃ | 0,79 | 0 | informational | nie |
| aranżacja wnętrz | 2 400 | 1 300 – 3 600 | mar 26 | ▆▆▄▇▇█▇▆▃▅▃▃ | 0,99 | 18 | informational | nie |
| projekt kuchni online | 1 900 | 1 300 – 2 900 | sty 26 | ▆▇▅█▇▆▅▄▄▄▄▄ | 0,46 | 0 | informational | tak |

## 3. Mapa fraz: fraza → strona

Pełne przypisanie każdej frazy do klastra i strony: kolumny `klaster` i `strona` w `analiza/dane/frazy_wolumeny.csv`. Zbiorczo: `analiza/dane/klastry.csv`.

### 3.1 Istniejące strony

| Istniejąca strona | Główne frazy, wolumen/mies. [SV] | Popyt klastra [SV] | Pozycja dziś | Co zrobić |
|---|---|---:|---|---|
| /jak-urzadzic-maly-balkon-… | jak urządzić balkon 590, aranżacja małego balkonu 390, balkon w bloku aranżacja 390, jak urządzić mały balkon 260, jak urządzić balkon w bloku 260 | 2 150 | poza top 20 [SERP] | Sezon: grudzień 400, marzec 5 030. Odświeżyć i podlinkować przed lutym. |
| /jak-urzadzic-maly-salon-w-bloku-… | bardzo mały salon w bloku 590, aranżacja małego salonu 480, jak urządzić mały salon 390, mały salon w bloku 260 | 1 720 | 37 dla „bardzo mały salon w bloku” [RK] | Najlepsza pozycja wśród wpisów. Osobna strona „salon z aneksem kuchennym” (4 770). |
| /jak-urzadzic-mala-kuchnie-… | mała kuchnia 2 400, mała kuchnia w bloku 1 900, aranżacja małej kuchni 590, jak urządzić kuchnię 590, jak urządzić małą kuchnię 390 | 5 940 | 73 dla „jak urządzić małą kuchnię” [RK] | W top 10 najsilniejsze domeny w całym zbiorze (ranga 564 [KO]). Celować w „mała kuchnia w bloku”. |
| /jak-urzadzic-pokoj-mlodziezowy-… | pokój młodzieżowy 2 900, pokój młodzieżowy dla dziewczynki 720, jak urządzić pokój nastolatce 210, pokój młodzieżowy dla chłopaka 170 | 4 230 | brak [RK] | Dodać sekcje „dla dziewczynki” i „dla chłopaka”. |
| /jak-urzadzic-pokoj-dziecka-… | pokój dziecka 1 600, aranżacja pokoju dziecka 590, jak urządzić pokój dziecka 260, pokój dla rodzeństwa 260 | 2 740 | brak [RK] | Brakuje stron „pokój dla dziewczynki” (4 400) i „pokój dla chłopca” (2 900). |
| /ile-kosztuje-projekt-domu-… | ile kosztuje projekt domu 1 000, projekt domu cena 260 | 1 260 | brak [RK] | Ceny tylko ze źródłem i datą (zasada z CLAUDE.md). |
| /jaki-kolor-scian-do-szarych-mebli/ | jaki kolor ścian do szarych mebli 390, jaki kolor ścian do szarej kanapy 140, szara kanapa jaki kolor ścian 90 | 620 | poza top 20 [SERP] | Zrobić z niego część huba „kolor ścian do mebli” (razem 6 320, patrz 3.2). |
| /jak-pomalowac-sufit-bez-smug/ | jak malować sufit 1 900, malowanie sufitu 1 600, farba do sufitu 480, jaka farba do sufitu 210, jak pomalować sufit bez smug 110 | 4 410 | brak [RK] | Tytuł celuje w „bez smug” (110). Poszerzyć o „jak malować sufit” (1 900). |
| /jak-pomalowac-salon-nowoczesnie/ | jak pomalować salon 210, jak pomalować salon nowocześnie 110 | 320 | brak [RK] | Mały popyt. Podlinkować do huba kolorów (kolor ścian w salonie 1 130). |
| /ile-kosztuje-wizualizacja-mieszkania/ | wizualizacja mieszkania 390, ile kosztuje wizualizacja mieszkania 20 | 410 | brak [RK] | Fraza z tytułu ma 20 wyszukiwań. Niski priorytet. |
| /tematy/kalkulatory-budowlane/ (pusta) | kalkulator budowlany 720, kalkulatory budowlane 720 (ta sama seria), kalkulator materiałów budowlanych 90 | 810 | brak [RK] | Strona pusta [CP]. Hub dla wszystkich kalkulatorów z 3.2. |

### 3.2 Brakujące strony, w kolejności priorytetu

Priorytet łączy popyt [SV], słabość SERP-u [SERP], [KO] i dopasowanie do bloga. Typ „narzędzie” oznacza działający kalkulator z krótkim poradnikiem pod spodem.

**A. Kalkulatory na start (słabe SERP-y, popyt przez cały rok)**

| Strona do zrobienia | Typ | Popyt/mies. [SV] | Min – max [SV] | Konkurencja | CPC [SV] |
|---|---|---:|---|---|---:|
| Kalkulator betonu (m3, worki, ile cementu na m3) | narzędzie | 6 170 | 2 710 (sty) – 9 210 (kwi) | małe serwisy: tylkobeton.pl, jakie-posadzki.pl, kalkulato.pl, chippy.tools; AI Overview na 1. miejscu [SERP]; ranga 280 [KO] | 0,56 |
| Kalkulator m2 / m3 / powierzchni | narzędzie | 4 920 | 3 660 – 6 300 | ranga 334, bez AI Overview w [KO]; SERP nie sprawdzony na żywo | 0,01 |
| Kalkulator płytek + kleju + fugi | narzędzie | 2 830 | 2 240 – 3 350 | bardzo słaba: codegeek.com.pl, usefulhub.cloud, remontomat.podziel.pl, wizerunkowo.app w top 20 [SERP], ich ETV 0,17–5 [BTE] | 0,25 |
| Kalkulator murowania (pustaki, cegły, bloczki) | narzędzie | 1 800 | 1 350 – 2 640 (mar) | ranga 270 [KO] | 1,09 |
| Kalkulator farby (ile farby na m2, na pokój) | narzędzie | 1 550 | 1 030 – 2 080 (mar) | kalkulatorxxl.pl, kb.pl, muratordom.pl, ale też budowlanek.com i kalkulatorfarby.pl z ETV ok. 2 [SERP], [BTE] | 0,21 |
| Kalkulator wylewki / gładzi / tynku | narzędzie | 920 | 590 – 1 250 (mar) | ranga 247 [KO] | 0,18 |
| Kalkulator ogrodzenia | narzędzie | 600 | 260 – 1 110 (mar) | ranga 213 [KO] | 0,60 |
| Kalkulator kostki brukowej + podsypki | narzędzie | 580 | 180 – 1 000 (mar–maj) | producenci (Wienerberger, Polbruk) i małe strony (obslugabudowy.pl, oblicz24.pl) [SERP] | 0,52 |
| Kalkulator paneli + listew | narzędzie | 340 | 260 – 440 | ranga 318 [KO] | 0,72 |
| Kalkulator tapety | narzędzie | 220 | 150 – 340 | ranga 279 [KO] | 3,39 |

Razem grupa A: około 19 900 wyszukiwań miesięcznie (suma klastrów [SV]).

**B. Kalkulatory trudniejsze albo poza profilem**

| Strona | Popyt [SV] | Dlaczego później |
|---|---:|---|
| Kalkulatory ciesielskie (drewno, więźba, schody, dach) | 8 570 | odbiorca zawodowy; „kalkulator ciesielski” 3 600, jego intencji nie sprawdzałem w SERP |
| Kalkulator stali / blachy / zbrojenia | 6 200 | odbiorca zawodowy, poza tematem wnętrz |
| Kalkulator styropianu / ocieplenia | 2 830 | top 10 to producenci i hurtownie: styro24.pl, yetico.com, Knauf, Austrotherm [SERP]; średnio 49,7 domen linkujących [KO] |
| Kalkulator kosztów remontu / wykończenia / budowy | 1 720 | SERP słaby (kb.pl, kalkulatorremontu.pl, ogarnijremont.pl [SERP]), ale wynik wymaga cen; ceny bez źródła są zakazane (CLAUDE.md), więc decyzja właściciela |
| Kalkulatory instalacyjne (pompa ciepła, fotowoltaika, grzejnik, klimatyzacja) | 2 200 | poza profilem bloga |

**C. Poradniki (dobry popyt, konkurencja średnia)**

| Strona | Popyt [SV] | Uwagi |
|---|---:|---|
| Kolory ścian: odcienie (kolor szałwiowy 8 100, butelkowa zieleń 5 400, szałwiowa zieleń 2 400, beżowe ściany 1 300, greige 1 300, oliwkowy 590, kaszmirowy 590) | 23 220 | popyt równy przez rok; w SERP marki farb i portale; ranga 383 [KO]; dużo grafiki |
| Hub „kolor ścian do mebli i pomieszczeń” (do mebli 2 380, w sypialni 1 630, w kuchni 1 180, w salonie 1 130) | 6 320 | rozwija istniejący wpis o szarych meblach |
| Jak malować ściany (malowanie ścian 3 600, gruntowanie ścian 1 600, jak malować ściany 1 300, jak pomalować ściany 1 000) | 9 670 | pasuje do wpisów o suficie i salonie; AI Overview w 9 z 12 fraz [KO] |
| Ile schnie / ile waży (ile schnie grunt 1 300, ile waży kubik betonu 1 900, ile schnie fuga 720, wylewka 720, klej do płytek 480) | 6 830 | AI Overview w 8 z 8 fraz [KO]; lepiej jako sekcje stron kalkulatorów |
| Salon z aneksem kuchennym | 4 770 | SERP: sklepy meblowe, małe pracownie, forum [SERP]; ranga 464 |
| Mała łazienka w bloku | 5 640 | ranga 481 |
| Przedpokój w bloku | 4 530 | ranga 471 |
| Sypialnia (aranżacja sypialni 5 400, sypialnia na poddaszu 1 900, przytulna sypialnia 1 600) | 11 520 | ranga 438 |
| Pokój dla dziewczynki / dla chłopca | 4 400 / 2 900 | intencja „transactional” [KO], dużo sklepów |
| Kolejność prac remontowych, od czego zacząć remont (remont kuchni od czego zacząć 1 900, remont starego domu od czego zacząć 1 600) | 4 350 | szczyt w lutym (10 480); SERP: czasnawnetrze.pl, dobrzemieszkaj.pl, budujemydom.pl, marki kuchni [SERP] |
| Panele i wykończenie (jakie panele podłogowe wybrać 1 900, panele winylowe czy laminowane 1 000, jak położyć panele 590, jak kłaść tapetę 390) | 4 190 | ranga 329 [KO]; nadaje się do afiliacji |
| Modne kolory ścian 2026 | 2 290 | szczyt marzec 3 620, dołek październik 460; temat co roku od nowa |
| Mały pokój, pokój 2x3, pokój ze skosami | 2 320 | ranga 348 |
| Domowe biuro | 2 300 | ranga 361 |
| Malowanie mebli, płytek, drzwi | 2 900 | malowanie mebli kuchennych 720, malowanie płytek 880 |

**D. Trudne albo do decyzji właściciela**

| Obszar | Popyt [SV] | Dlaczego |
|---|---:|---|
| Style wnętrz (styl boho 8 100, japandi 8 100, rustykalny 4 400, skandynawski 3 600, hampton 3 600) | 41 920 | duże portale; ranga 424 [KO] |
| Usługi projektowe (projekt kuchni 12 100, projekt łazienki 9 900, projektowanie wnętrz 8 100, projektant wnętrz 5 400, architekt wnętrz 4 400) | 46 300 | wymaga oferty; Local Pack w 5 z 8 fraz [KO] |
| Koszty prac „ile kosztuje…” | 39 610 | AI Overview w 30 z 37 fraz [KO]; ceny tylko ze źródłem |
| Ceny materiałów (kubik betonu, worek cementu, tona piasku po 1 900) | 7 000 | ceny zmienne, bez źródła nie wolno publikować |
| Ogród: kostka brukowa, altana, pergola | 141 780 | frazy zakupowe, w SERP sklepy |
| Ogród poradnikowy: kalendarz ogrodnika, trawnik, rośliny na balkon, aranżacja ogrodu | 79 090 | duży, ale bardzo sezonowy (marzec–maj); AI Overview częsty |
| Farby i narzędzia (agregat malarski 9 900) | 13 050 | frazy produktowe; tylko z afiliacją |
| Odliczenie remontu od podatku | 720 | temat prawny, decyzja właściciela |

### 3.3 Usługi projektowe (gdyby właściciel chciał sprzedawać)

| Fraza | Śr./mies. | Min – max | Szczyt | CPC (USD) |
|---|---:|---|---|---:|
| projektowanie wnętrz | 8 100 | 6 600 – 12 100 | sty, mar 26 | 1,35 |
| projektant wnętrz | 5 400 | 4 400 – 8 100 | mar 26 | 2,53 |
| architekt wnętrz | 4 400 | 2 400 – 6 600 | mar 26 | 2,15 |
| projektant wnętrz online | 2 900 | 1 900 – 4 400 | lis 25, sty, mar 26 | 0,41 |
| projekt wnętrz | 1 600 | 880 – 2 400 | – | 1,87 |
| projekt wnętrz online / projekt wnętrza online | 720 | 260 – 1 000 | – | 0,59 |
| ile kosztuje projektant wnętrz | 480 | 320 – 720 | – | 0,95 |
| ile kosztuje projekt kuchni | 390 | 260 – 720 | lut 26 | 0,54 |
| ile kosztuje projekt łazienki | 390 | 260 – 590 | sty 26 | 0,51 |
| projekt wnętrza cena | 260 | 140 – 480 | – | 0,96 |
| ile kosztuje projekt wnętrza | 210 | 110 – 320 | – | 0,78 |
| projektowanie wnętrz cennik | 210 | 70 – 390 | mar 26 | 1,10 |
| projekt wnętrz cena za m2 | 40 | 20 – 70 | sty 26 | 0,47 |

Źródło: [SV], 18.10.2026. Szczyt popytu na usługi wypada od stycznia do marca, dołek we wrześniu.

SERP [SERP]: „ile kosztuje projekt wnętrza” wygrywają cenniki pracowni (wnetrzewdomu.pl, oliwiadrobnicka.pl, florkiewiczstudio.com, houselab.pl). „projektant wnętrz online” wygrywają pracownie online (abrys.net, artehaus.pl, kotestudio.pl), Allegro i homebook.pl; jest też panel wiedzy i opinie Google. Blog bez własnej oferty, portfolio i opinii nie ma tu realnych szans. Strona z cennikiem ma sens dopiero, gdy właściciel potwierdzi usługę i ceny.

## 4. Obraz SERP-ów

Sprawdzone na żywo 18.10.2026 [SERP], Google Polska, telefon, top 20 wyników organicznych. Wolumen [SV]. Pełne listy: `analiza/dane/serp_top20.csv`.

| Fraza (wolumen) | Elementy SERP | AI Overview | Kto wygrywa w top 10 | Słabe domeny w top 10? |
|---|---|---|---|---|
| kalkulator betonu (4 400) | AI Overview, aplikacje, grafika, „ludzie szukają też” | tak, 1. miejsce | małe serwisy kalkulatorów i betonu (domonline.pl, chippy.tools, tylkobeton.pl, jakie-posadzki.pl, betonplus.pl, kalkulato.pl), Castorama, wideo z Facebooka | tak |
| ile farby na m2 (720) | AI Overview, PAA, grafika | tak, 1. miejsce | kalkulatorxxl.pl, budowlanek.com, YouTube, kb.pl, mojabudowa.pl, kalkulatorfarby.pl, notatnikbudowlany.pl, muratordom.pl | tak (budowlanek.com, kalkulatorfarby.pl: ETV ok. 2 [BTE]) |
| kalkulator płytek (320) | aplikacje na 1. miejscu, AI Overview | tak, 4. miejsce | mexen.pl (blog sklepu), codegeek.com.pl, usefulhub.cloud, banyo.pl, YouTube, producenci płytek, remontomat.podziel.pl, estile.pl | tak, najsłabszy SERP w próbie |
| kalkulator styropianu (1 900) | AI Overview, PAA | tak, 5. miejsce | producenci i hurtownie: styro24.pl, hurtowniastyropianu.pl, yetico.com, styroneo.pl, Knauf, Austrotherm | nie, mocne marki |
| kalkulator kostki brukowej (170) | AI Overview, grafika, aplikacje | tak, 2. miejsce | dalis-granit.pl, obslugabudowy.pl, Wienerberger, kb.pl, oferteo.pl, YouTube, kostbet.pl, kalkulatorxxl.pl | częściowo |
| kalkulator remontu (140) | AI Overview, wyszukiwania powiązane | tak, 5. miejsce | kb.pl, kalkulatorremontu.pl, kolbuild.pro, ogarnijremont.pl, mivare.pl, dkor.pl, dobrykalkulator.pl; od 10. miejsca wyniki nie na temat | tak |
| ile kosztuje malowanie pokoju (2 400) | AI Overview, wideo, PAA, grafika | tak, 1. miejsce | wykonawcy (aropos1.pl, kowalbud.com), kb.pl, zleca.pl, oferteo.pl, fakt.pl, YouTube, Facebook | częściowo |
| remont kuchni od czego zacząć (1 900) | AI Overview, wideo, PAA, grafika | tak, 1. miejsce | czasnawnetrze.pl, sklepy meblowe (Aksent, BRW, Bogart), dobrzemieszkaj.pl, budujemydom.pl, domni.pl | nie |
| jak urządzić mały salon z aneksem (1 600) | grafika na 1. miejscu, AI Overview, wideo, PAA | tak, 2. miejsce | sklepy meblowe (idzczakmeble.pl, BRW, plmeble.pl), e-wystroj-wnetrz.pl, weranda.pl, forum.gazeta.pl, małe pracownie | częściowo (forum, małe pracownie) |
| jak urządzić mały balkon (260) | grafika na 1. miejscu, PAA, wideo | nie | blogi sklepów: modu.pl, vokato.com, alena-firany.pl, morele.net, merkurymarket.pl, edaxo.pl, BRW | częściowo; wnetrzakamila.pl poza top 20 |
| jaki kolor ścian do szarych mebli (390) | AI Overview, grafika, PAA | tak, 1. miejsce | blogi marek: komfort.pl (3 wyniki), magnatfarby.pl (2), aksent.pl, BRW, homebook.pl | nie; wnetrzakamila.pl poza top 20 |
| ile kosztuje projekt wnętrza (210) | AI Overview, grafika, PAA | tak, 1. miejsce | cenniki pracowni projektowych, archiweb.pl, Facebook, LinkedIn | nie dla bloga bez oferty |
| projektant wnętrz online (2 900) | AI Overview, panel wiedzy, opinie Google, PAA | tak, 1. miejsce | pracownie online, Allegro, homebook.pl, eplytki.pl | nie dla bloga bez oferty |
| kiedy siać trawę (5 400) | AI Overview, wideo, krótkie wideo, PAA | tak, 1. miejsce | sklepy ogrodnicze, Leroy Merlin, Kiloutou, dom.wprost.pl, muratordom.pl | częściowo |

Co widać:
- **AI Overview** był w 13 z 14 SERP-ów, zwykle na 1. miejscu. Wyjątek: „jak urządzić mały balkon”. W kalkulatorach AI Overview często odsyła do narzędzi (np. przy płytkach do Paradyża, Leroy Merlin, eplytki.pl), czyli działający kalkulator ma szansę być cytowany.
- **Local Pack** nie pojawił się w żadnym z 14 SERP-ów na żywo. W danych Labs [KO] jest przy 12 frazach, m.in. przy 5 z 8 fraz usługowych (projektowanie wnętrz, projektant wnętrz, architekt wnętrz), przy „remont łazienki”, „remont mieszkania” i „kostka brukowa”.
- **Grafika** jest w prawie każdym SERP-ie o aranżacji i kolorach. Tu liczą się własne zdjęcia i dobre opisy alt.
- **Wideo** (YouTube, Facebook) stoi w top 10 przy malowaniu, płytkach i remoncie.
- **Portale typu muratordom.pl, Castorama, Leroy Merlin** są obecne, ale nie dominują w kalkulatorach. Dominują w nich małe, wąskie serwisy. W aranżacji i kolorach dominują blogi sklepów meblowych i marek farb.

## 5. Wnioski: gdzie nowa, słaba domena może wygrać

### Da się wygrać

1. **Kalkulatory materiałów pod wnętrza i remont.** To najlepszy kierunek. Dowody: w top 10 dla „kalkulator płytek” stoją strony z ruchem bliskim zera (codegeek.com.pl ETV 0,35, usefulhub.cloud 2,2 [BTE]); średnia ranga domen w top 10 dla kalkulatorów to 328 wobec 448 dla aranżacji [KO]; popyt jest równy przez rok z wiosennym szczytem [SV]. Kolejność: beton (6 170), płytki z klejem i fugą (2 830), farba (1 550), murowanie (1 800), wylewka i gładź (920), panele (340), tapeta (220), a do tego prosty kalkulator m2/m3 (4 920).
2. **Hub kalkulatorów w pustym dziale.** Strona `/tematy/kalkulatory-budowlane/` już istnieje i jest w menu, ale nie ma treści [CP]. Fraza „kalkulator budowlany” ma 720 wyszukiwań [SV], ranga top 10 to 390 [KO].
3. **Krótkie pytania przy kalkulatorach.** „ile cementu na m3 betonu” 590, „ile worków betonu na m3” 390, „ile kleju na m2 płytek” 480, „ile fugi na m2” 390, „ile pustaków na m2” 480, „ile schnie grunt” 1 300 [SV]. Najlepiej jako sekcje stron narzędzi, bo AI Overview odpowiada na nie wprost [KO].
4. **Malowanie i kolory z linkami do kalkulatora farby.** Blog ma już 3 wpisy o malowaniu. Klaster „sufit” to 4 410 wyszukiwań, a obecny wpis celuje w 220. Hub kolorów (6 320) i „jak malować ściany” (9 670) to rozsądny drugi etap. Konkurencja jest średnia (ranga 383–442 [KO]).
5. **Niszowe frazy aranżacyjne z „w bloku”, „2x3”, „ze skosami”.** Np. „jak urządzić pokój 2x3” 880, „jak urządzić mały pokój w bloku” 320, „jak urządzić pokój na poddaszu ze skosami” 320 [SV]; ranga top 10 dla tego klastra to 348 [KO].

### Trudno albo nie teraz

1. **Ogólne frazy aranżacyjne i style** („aranżacja salonu” 6 600, „styl boho” 8 100, „garderoba” 12 100) [SV]. W top 10 duże portale i sklepy, ranga 399–471 [KO]. Obecne wpisy nie mieszczą się w top 20 [SERP].
2. **Frazy zakupowe w ogrodzie** („kostka brukowa” 74 000, „altana ogrodowa” 33 100, „pergola” 27 100) [SV]. To popyt na produkt i sklep.
3. **„Ile kosztuje…”**: 39 610 wyszukiwań, AI Overview w 30 z 37 fraz [KO], a ceny wymagają źródła z datą (zasada z CLAUDE.md). Bez wiarygodnego źródła cen (np. cennika producenta lub raportu) lepiej nie zaczynać.
4. **Usługi projektowe**: duży popyt i najwyższe CPC, ale SERP-y wygrywają pracownie z ofertą, cennikiem i opiniami [SERP]. Blog obecnie nie ma oferty.
5. **Kalkulatory, w których wygrywają producenci** (styropian, ocieplenie) i kalkulatory dla zawodowców (stal, blacha, więźba).

### Kalendarz (kiedy publikować, z danych [SV])

| Temat | Dołek | Szczyt | Publikować najpóźniej |
|---|---|---|---|
| Kalkulatory budowlane | grudzień 2025 (33 170) | marzec 2026 (57 910) | styczeń |
| Remont: koszty i kolejność | wrzesień–grudzień | luty 2026 (remont łazienki 12 100, remont mieszkania 4 400, klaster kolejności prac 10 480) | grudzień–styczeń |
| Aranżacja | czerwiec 2026 (85 310) | styczeń 2026 (154 990) | listopad–grudzień |
| Mały balkon, rośliny na balkon | grudzień (400 i 1 230) | marzec (5 030) i maj (56 700) | luty |
| Ogród (trawnik, kalendarz) | grudzień | marzec (35 850 i 102 100) | styczeń–luty |
| Malowanie i kolory | grudzień 2025 (47 370) | marzec 2026 (77 020), równo przez rok | dowolnie |
| Usługi projektowe | wrzesień 2026 (44 080) | styczeń 2026 (94 430) | grudzień |

### Monetyzacja (z danych [SV])

- Średni CPC: kalkulatory 0,62 USD, remont 0,60, koszty 0,59, aranżacja 0,23, malowanie i kolory 0,21 USD. Kalkulatory i remont są warte reklamodawcom mniej więcej trzy razy więcej niż aranżacja. W całym serwisie przychód z reklam na wizytę będzie jednak niski.
- Najwyższe CPC: „kalkulator tapety” 3,39 USD (220 wyszukiwań), „projektant wnętrz” 2,53, „architekt wnętrz” 2,15, „remont mieszkania” 2,13 USD.
- Afiliacja ma pokrycie w frazach: „agregat malarski” 9 900, „program do projektowania wnętrz” 5 400, „jakie panele podłogowe wybrać” 1 900, „panele winylowe czy laminowane” 1 000, „najlepsza farba do ścian” 480, „ranking farb do ścian” 390. Kalkulator może podać wynik w opakowaniach i odesłać do sklepu.

### Ryzyka i ograniczenia

- AI Overview był w 13 z 14 SERP-ów. Może zabierać kliknięcia; tego nie mierzyłem.
- Wolumeny Google Ads są zaokrąglane do progów i łączą warianty pisowni [SV].
- Trudność [KD] nie różnicuje polskich fraz (305 z 397 to 0). Ocena trudności opiera się na SERP-ach i randze domen.
- Strona ma dziś 2 frazy w top 100 i ruch 0,75 wizyty miesięcznie [DRO]. Pierwsze efekty zależą też od wyników analizy technicznej i linków (osobne raporty).

### Pytania do właściciela

1. Czy budujemy kalkulatory (grupa A) jako główny kierunek bloga?
2. Czy kalkulator kosztów remontu wchodzi, skoro wymaga cen ze źródłem? Jeśli tak, z jakiego źródła cen korzystamy?
3. Czy temat odliczenia remontu od podatku (720, szczyt w lutym 3 600) jest dozwolony? To treść prawna.
4. Czy właściciel chce kiedyś sprzedawać projekty wnętrz? Od tego zależy, czy robić stronę z cennikiem.
5. Czy ogród zostaje w zakresie bloga? Popyt jest duży, ale sezonowy i w dużej części zakupowy.

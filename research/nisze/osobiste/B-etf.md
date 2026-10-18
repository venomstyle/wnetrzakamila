# Nisza B: ETF-y dla polskiego inwestora (badanie z 18.10.2026)

Zakres: baza ETF-ów UCITS dostępnych u brokerów działających w Polsce (XTB, mBank, IBKR, Trading 212, Revolut, Finax, DM BOŚ) jako strony encji (TER, replikacja, akumulacja lub dystrybucja, waluta, indeks, wielkość funduszu), porównania z kryteriami bez rekomendacji, kalkulatory (koszt całkowity, procent składany, przewalutowanie) i porównanie brokerów pod ETF-y (opłaty z datą). Metoda: `research/nisze/METODA.md` i `research/nisze/osobiste/BRIEF.md`. Wszystkie liczby pobrane 18.10.2026.

**Oznaczenia źródeł:**
- **[W]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live` (location 2616, pl, `date_from` 2024-10-01): średnia z 12 mies. (10.2025–09.2026), 24 miesiące historii, CPC w USD.
- **[K]** `/v3/dataforseo_labs/google/keyword_suggestions/live`, ziarno „etf” (4 567 fraz w bazie, pobrane 2 700 największych), ziarno „broker” (2 548 fraz, 300 przejrzanych).
- **[S]** `/v3/serp/google/organic/live/advanced`, depth 10, desktop, `load_async_ai_overview`.
- **[B]** `/v3/backlinks/bulk_referring_domains/live` dla 60 domen i 77 URL-i z top 10.
- **[T]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (ETV, ruch organiczny szacowany).
- **[CP]** `/v3/on_page/content_parsing/live` (strona czytana u źródła). **[WS]** WebSearch (wynik wyszukiwarki, strona nieczytana w całości).
- Kurs USD: 3,8952 zł (średni NBP z 15.10.2026, wg tvp.info, odczyt przez [WS]); API NBP zablokowane przez proxy.

Dane: `dane/B-wolumeny.csv` (1 831 fraz z typem strony; kolumna `zrodlo`: W = [W], K = [K]), `dane/B-wolumeny-24m.csv`, `dane/B-serp-top10.csv`, `dane/B-serp-podsumowanie.csv`, `dane/B-backlinki.csv`, `dane/B-ruch-konkurencji.csv`, `dane/B-programy.csv`, `dane/B-zrodla-danych.csv`, `dane/B-rachunek.csv`, `dane/B-cfd.csv`. Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/os-B/` (`klas.py`, `trend.py`, `serp_sum.py`, `rachunek.py`, `eksport.py`).

---

## Werdykt w skrócie

**WARUNKOWO, wynik 2,8 / 5. Bez spełnienia warunków 1 i 2: NIE.** Dopasowanie do profilu właściciela: **4 / 5**.

1. **Popyt jest duży i rósł, ale wzrost wyhamował.** Mapa niszy (bez marek brokerów i nawigacji) to 2 198 fraz i **267 460 wyszukiwań/mies.** [W][K]. Panel 248 fraz z 24 miesiącami historii: **+26,7%** (12 mies. do 09.2026 wobec 12 mies. wcześniej), ale lipiec–wrzesień 2026 wobec 2025 już tylko **+13,1%**, a wrzesień do września +1,9%. Szczyt był w 01.2026 (285 210), potem spadek do 176 540 w 09.2026 [W].
2. **Produkt, który opisuje brief, już istnieje po polsku.** atlasETF (atlasetf.pl, od 2022) ma bazę ponad 3 000 ETF-ów, skaner, porównywarkę, portfele, akademię i ranking brokerów [CP][WS]. Stoi na 1. miejscu dla „vwce” i jest cytowany w AI Overview [S]. Fraza „atlas etf” ma 9 900 wyszukiwań/mies. [K]. justETF nie ma wersji polskiej (`/pl/` zwraca 404) [CP].
3. **Główny model zarobku jest prawnie niepewny i bez jawnych stawek.** UKNF w stanowisku z 11.10.2023 r. pisze, że klienci firmy inwestycyjnej i nieregulowani pośrednicy nie mogą w ramach programów poleceń i partnerskich prowadzić zindywidualizowanych działań pozyskujących klientów usług maklerskich [WS: knf.gov.pl, ispb.pl]. XTB i IBKR mają programy, ale stawek nie publikują; programu Trading 212 nie potwierdziłem, a Finax, mBank i DM BOŚ nie mają publicznych programów [CP][WS].
4. **Rachunek po 12 mies.: ok. 290 zł/mies. (ostrożny) i ok. 5 150 zł/mies. (realny).** Realny wariant w 95% opiera się na CPA brokera, którego dziś nie umiem potwierdzić. Bez afiliacji zostają reklamy: ok. 20 i 270 zł/mies.

**Warunki „tak”:** (1) opinia prawnika o stanowisku UKNF dla serwisu z linkami do brokerów (temat do decyzji właściciela, nie treść strony); (2) właściciel loguje się do programów XTB, IBKR (CPC) i Revolut (Impact) i potwierdza stawki dla PL; (3) wyróżnik wobec atlasETF: dostępność konkretnego ETF-u u konkretnego brokera w PL i koszt całkowity w złotych (TER + prowizja + przewalutowanie) z datą.

---

## 1. Ocena

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 4 | 267 460/mies. w mapie, +26,7% r/r w 24 mies., ale III kw. tylko +13,1% i spadek od szczytu 01.2026 [W] |
| Słabość SERP | 25% | 2,5 | URL-e słabe (w 8 z 11 SERP-ów co najmniej 8 wyników ma <10 domen linkujących), ale domeny silne: mediana 2 036–14 910 w SERP-ach encji; tylko 5 z 11 SERP-ów ma ≥2 wyniki z domen <300 [B][S]; slot „baza ETF po polsku” zajęty przez atlasETF |
| Zarobek | 25% | 2,5 | CPC ważone 1,87 USD, „etf” 3,01, „vwce” 4,17 [W]; stawek brokerów brak, stanowisko UKNF ogranicza afiliację [WS][CP] |
| Fosa danych / narzędzia | 15% | 3 | ESMA FIRDS do użytku komercyjnego z podaniem źródła (ISIN, nazwa, CFI z polityką dochodową, rynki) [CP]; TER, indeks, AUM tylko z KID emitentów, ręcznie; justETF i dane MSCI odpadają [CP] |
| Niskie ryzyko | 15% | 2 | YMYL bez eksperta z twarzą, AI Overview w 9 z 11 SERP-ów [S], ryzyko rekomendacji (MAR), stanowisko UKNF, sąsiedztwo CFD |
| **Wynik ważony** | | **2,8** | 0,8 + 0,625 + 0,625 + 0,45 + 0,3 |

**Dopasowanie do profilu: 4 / 5.** Inwestowanie, trading i obligacje to dokładnie ten temat, a UX/UI przydaje się przy porównywarce i kalkulatorach. Punkt mniej za YMYL bez twarzy: konkurenci to rozpoznawalni autorzy (Marcin Iwuć, Inwestomat, założyciele atlasETF Jacek Lempart i Artur Wiśniewski [WS: sii.org.pl]).

## 2. Popyt i trend [W][K]

| Typ strony | Frazy | Wolumen/mies. | Przykłady (wolumen, CPC USD) |
|---|---|---|---|
| Encja: ETF UCITS | 1 328 | 124 110 | vwce 5 400 (4,17), vwra 3 600 (1,90), iwda 3 600 (1,31), isac etf 2 900, vuaa 2 900 (2,88), cspx 2 400 (1,70), etf msci world 1 600 (2,21), cndx 1 300 (3,14), etf na złoto 880, sxr8 390 (3,19) |
| Encja: ETF na GPW | 154 | 21 920 | etf beta 1 900, beta etf dywidenda plus 1 600, etf wig20 880, beta etf mwig40tr 590, etf sp500 gpw 590 |
| Edukacja | 315 | 52 530 | etf co to 14 800 (0,57), co to jest etf 1 900, jak inwestować w etf 720, etf dla początkujących 590 (2,40), etf akumulacyjny 260 |
| Hub | 3 | 25 100 | etf 22 200 (3,01), fundusze etf 1 000, fundusz etf 1 900 |
| Narzędzie | 41 | 19 660 | procent składany 6 600 (1,96), kalkulator inwestycji 6 600 (1,11), kalkulator procent składany 1 900, kalkulator etf 390 (1,21), skaner etf 260, porównywarka etf 110, etf overlap 170 |
| Ranking / porównanie | 123 | 10 660 | ranking etf 720 (0,94), jaki etf wybrać 480, najlepsze etf 390 (1,91), etf vs etc 210, najlepszy etf na sp500 70 |
| Broker pod ETF | 234 | 13 480 | etf gdzie kupić 720, bossa etf 720, mbank etf 590, xtb etf 480, mbank etf lista 320, ranking brokerów 170, najlepszy broker 140 (11,25) |
| **Razem w mapie** | **2 198** | **267 460** | CPC ważone **1,87 USD** |

Poza mapą: marki brokerów 316 740 („xtb” 246 000, „bossa” 33 100, „interactive brokers” 9 900, „xtb opinie” 5 400, „trading 212” 4 400, „finax” 2 900, „mbank emakler” 1 600), nawigacja do konkurentów 16 930 („atlas etf” 9 900, „justetf” 5 400), ETF-y z USA niedostępne jako UCITS 12 450 („voo etf” 720, „qqq etf” 720, „schd etf” 390), angielskie 4 070, CFD i lewar 1 570, podatki i IKE/IKZE 1 090, krypto 1 080 [K].

**Ważne dla pomysłu z briefu:**
- **Porównania „X vs Y” między ETF-ami prawie nie mają popytu:** „vwce vs iwda” 10, „vwce vs vwra” 20, „msci world etf vs sp500” 10, „najlepszy etf na sp500” 70 [W][K]. Popyt mają porównania pojęć: „etf vs etc” 210, „cfd vs etf” 90, „etf czy akcje” 70 [K].
- **Encje mają popyt, ale rozproszony:** tylko 19 fraz-encji ma ≥1 000/mies. (część to odmiany tej samej nazwy); reszta to długi ogon tickerów i nazw funduszy [K].
- **Kalkulatory ETF są małe:** „kalkulator etf” 390, „etf kalkulator” 110, „kalkulator inwestycji etf” 70, „kalkulator dca” 10 [W][K]. Duże są ogólne: „procent składany” 6 600 i „kalkulator inwestycji” 6 600 [W].
- **Porównanie brokerów pod ETF jest małe:** „ranking brokerów” 170, „najlepszy broker” 140, „porównanie brokerów” 30 [W]. Duży popyt idzie na marki („xtb opinie” 5 400) [W].

**Trend 24 mies. (panel 248 fraz bez marek i nawigacji, `dane/B-wolumeny-24m.csv`) [W]:**
- 12 mies. 10.2025–09.2026: średnio 211 168/mies.; 12 mies. wcześniej: 165 871/mies., czyli **+26,7%**.
- Lipiec–wrzesień 2026 wobec 2025: **+13,1%**. Wrzesień 2026 wobec września 2025: 176 540 wobec 173 320, czyli +1,9%.
- Sezon: najmocniej w styczniu (01.2026: 285 210), najsłabiej latem (06.2025: 130 300). Od stycznia 2026 każdy miesiąc jest słabszy od poprzedniego poza kwietniem i majem.
- Po grupach (12 mies. r/r): encje, edukacja, hub i rankingi +31,0%; narzędzia +6,3%; frazy „broker pod ETF” −3,1% (III kw. −23,2%); marki brokerów +27,0%.

## 3. Jedenaście SERP-ów [S][B]

Pełne dane: `dane/B-serp-top10.csv`, podsumowanie: `dane/B-serp-podsumowanie.csv`. „Mediana” to mediana domen linkujących do domen z top 10.

| Fraza | Wol. [W] | Typ | AIO | Mediana | Wyniki z domen <300 | Forum/wideo/aplikacja/PDF | Sprzed 2023 | Kto wygrywa |
|---|---|---|---|---|---|---|---|---|
| vwce | 5 400 | encja | tak | 2 649 | 1 | 0 | 1 | **atlasetf.pl (1.)**, TradingView, Deutsche Börse, justETF, stooq, XTB, BiznesRadar, Yahoo, Vanguard PL |
| isac etf | 2 900 | encja | tak | 14 910 | 0 | 0 | 0 | BlackRock, BiznesRadar, XTB, Bloomberg, stooq ×2, Yahoo, iShares, atlasetf.pl (9.) |
| etf sp500 | 2 900 | encja/ranking | tak | 2 036 | 0 | 1 | 0 | XTB ×2, TMS ×2, justETF, mdm.pl, YouTube, Investing, atlasetf.pl (lista S&P 500) |
| etf msci world | 1 600 | encja | tak | 2 649 | 1 | 2 | 0 | BlackRock ×3 (w tym PDF), TMS, analizy.pl (PDF), Investing ×2, j2t, stooq |
| ranking etf | 720 | ranking | tak | 14 910 | 2 | 4 | 4 | YouTube ×4 (Stockbroker, Inwestomat), XTB, inwestomat.eu (2020, 2022), akademia.atlasetf.pl, stockbroker.pl (2022) |
| kalkulator procent składany | 1 900 | narzędzie | tak | 54 | **5** | 2 | 0 | jakubkurek.pl (54 dom.), portfelik.com, kontomaniak, finasfera.pl (48), kalkulatorbox.pl (7), kalkulatorki.pl (34), niezbednikfinansowejwolnosci.pl (0) |
| kalkulator etf | 390 | narzędzie | tak | 11 394 | 2 | 3 | 1 | accuratecalculators, etf.lv, Google Play ×2, betasecurities.pl (2020), i24app, XTB, App Store, justETF |
| etf co to | 14 800 | edukacja | nie | 3 514 | 1 | 0 | 0 | analizy.pl, ING, Wikipedia, Saxo, fondee.pl, marciniwuc.com, Raisin, BOŚ Bank |
| etf akumulacyjny | 260 | edukacja | tak | 8 242 | 2 | 2 | 2 | VanEck, Reddit, marciniwuc.com, PZU, XTB, YouTube, agiofunds.pl, inwestomat.eu (2020) |
| gdzie kupić etf | 720 | broker | nie | 4 677 | 1 | 0 | 1 | inwestomat.eu (12.2025), Bankier, marciniwuc.com (2019), BNP, ING, XTB, Raisin, akademia.atlasetf.pl, mBank, Alior |
| xtb opinie | 5 400 | broker | tak | 12 728 | 2 | 5 | 2 | forum Investing, BrokerChooser, YouTube (2022), forum Bankier ×2, topinwestycje.pl, XTB, gieldowe-emocje.pl (2021); reklama capital.com (CFD) |

**Wnioski:**
- **Na poziomie URL SERP-y są słabe:** w 8 z 11 SERP-ów co najmniej 8 wyników ma <10 domen linkujących do konkretnego adresu [B]. Indeks linków widzi głównie strony główne, więc to kryterium słabo rozróżnia frazy.
- **Na poziomie domen encje są trudne.** Wygrywają emitenci (BlackRock, iShares, Vanguard), serwisy notowań (stooq 2 649 domen, TradingView PL 1 723, BiznesRadar 1 917, Investing PL 1 854), brokerzy (XTB 14 910) i atlasETF (631) [B]. Google pokazuje przy tickerach ramkę notowań i porównanie serwisów („stocks_box”, „compare_sites”) [S].
- **Edukację trzymają silne blogi i banki:** marciniwuc.com (2 720 domen, ETV 68 508), inwestomat.eu (522, ETV 10 506), analizy.pl, ING, Saxo [B][T].
- **Najsłabszy SERP to ogólny kalkulator procentu składanego:** 5 z 9 wyników z domen <300 linkujących [B]. Ale AI Overview wymienia z nazwy gotowe narzędzia (Omni Calculator, kalkulatorprocentow.pl, Saxo) [S].
- **Rankingi:** dużo wideo i starych wpisów (4 i 4 z 9), czyli miejsce dla aktualnej strony z datą. Popyt mały: 720/mies. [S][W].
- **AI Overview w 9 z 11 SERP-ów** (bez AIO tylko „etf co to” i „gdzie kupić etf”). Cytuje małe serwisy: atlasetf.pl (3 razy), etfkalkulator.pl (5 domen linkujących, ETV 253), kalkulatorprocentow.pl, portfelik.com, minikalkulator.pl, annabednarczyk.pl, topinwestycje.pl [S][B][T]. AIO przy „vwce” podaje cenę z sesji 16.10.2026, ISIN, TER 0,14% i typ replikacji, czyli odpowiada na intencję strony encji bez kliknięcia [S].
- **Kryterium metody** (≥2 wyniki z domen <300 linkujących albo ≥2 fora, wideo lub stare treści): spełnia 6 z 11 SERP-ów. Nie spełniają go „vwce”, „isac etf”, „etf sp500”, „etf co to” i „gdzie kupić etf”, czyli frazy z największym wolumenem [S][B].

## 4. Konkurencja: kto robi strony ETF-ów po polsku [T][B][CP][WS]

| Serwis | Co ma | Domeny linkujące | Ruch (ETV/mies.) | Uwagi |
|---|---|---|---|---|
| atlasetf.pl | baza >3 000 ETF-ów, skaner, porównywarka, portfele, rankingi EU/USA, ETF na GPW, akademia | 631 | 16 009 (517 fraz) | od 2022; autorzy z twarzą; strefa premium (cennika nie sprawdziłem); cytowany w AIO |
| inwestomat.eu | rankingi, lista ETF-ów u polskich brokerów, „gdzie kupić ETF” | 522 | 10 506 | autor z twarzą, YouTube; część wpisów z 2020–2022 |
| marciniwuc.com | edukacja ETF | 2 720 | 68 508 | autor z twarzą |
| stockwatch.pl | portal giełdowy | 4 057 | 202 600 | szeroki temat |
| rankia.pl | forum i poradniki | 313 | 13 945 | |
| etfkalkulator.pl | 8 kalkulatorów, 94 artykuły (wg AIO) | 5 | 253 | nowy, mały, a już cytowany w AIO |
| kalkulatorprocentow.pl | kalkulator procentu składanego | 112 | 20 979 | dowód, że narzędzie ogólne przynosi ruch |
| justETF | baza ETF-ów (EN/DE/IT/FR i in.) | 11 394 | nie mierzono | **brak wersji PL** (`justetf.com/pl/` = 404) |
| mBank, bossa | własne wyszukiwarki ETF | | | „bossa wyszukiwarka etf” 170, „wyszukiwarka etf mbank” 50 [K] |

stockwatch i rankia nie mają bazy ETF-ów jako stron encji (nie znalazłem ich w top 10 żadnego z 11 SERP-ów). Blogi stoją na edukacji i rankingach, a bazę encji po polsku ma jeden gracz.

## 5. Dane do stron encji (`dane/B-zrodla-danych.csv`)

| Źródło | Co daje | Licencja u źródła (18.10.2026) | Ocena |
|---|---|---|---|
| **ESMA FIRDS** (registers.esma.europa.eu) | ISIN, nazwa, kod CFI (zawiera politykę dochodową: akumulacja lub dystrybucja), waluta, rynki notowań (w tym GPW), emitent | „Reproduction of all information on this site (REGISTERS information) is authorised except as otherwise stated, provided the source is acknowledged” plus warunki: oznaczyć przetworzenie danych, nie sugerować poparcia ESMA [CP] | **OK** jako szkielet bazy |
| KID/KIID i karty funduszy emitentów | koszty bieżące, cel i indeks, ryzyko, replikacja, wielkość funduszu | regulaminów stron emitentów nie sprawdzałem pojedynczo; dokumenty są publiczne z mocy prawa | **ręcznie**, fakty własnymi słowami z linkiem i datą; masowe pobieranie to ryzyko prawa do bazy danych (do decyzji właściciela) |
| justETF | pełne profile | dane z Xignite, etfinfo i justETF; klauzula MSCI: „may only be used for your internal use, may not be reproduced or re-disseminated” [CP] | **odpada** |
| Dane indeksów MSCI | skład, poziomy | j.w. | **odpada** (nazwę indeksu można podać) |
| Xetra „All tradable instruments” CSV | lista ETF-ów na Xetra | brak wyraźnej zgody na użycie komercyjne; przewodniki: „all rights reserved” [WS] | **niepotwierdzone** |
| Listy ETF-ów i cenniki brokerów | dostępność u brokera, prowizje, przewalutowanie | fakty z linkiem i datą | **ręcznie**, 7 brokerów, odświeżanie co miesiąc |
| Kursy NBP | kalkulator przewalutowania | warunków ponownego użycia nie potwierdziłem; API zablokowane przez proxy | do sprawdzenia |

Przykład faktów do porównania brokerów (z SERP 18.10.2026): XTB „prowizja 0% do kwoty 100 000 EUR obrotu miesięcznie” (xtb.com/pl/etf), mBank „ETF-y z 0 zł prowizji” na IKE i IKZE eMakler (mbank.pl) [S]. Pełnego cennika 7 brokerów nie zbierałem.

**Wniosek:** FIRDS daje legalny szkielet kilku tysięcy stron (ISIN, akumulacja lub dystrybucja, waluta, rynek). Wszystko, czego szuka inwestor poza tym (TER, indeks, wielkość, replikacja), trzeba przepisać z KID i kart emitentów. atlasETF ma to już dla >3 000 funduszy. Własna przewaga może być tylko w warstwie „dostępność u brokera w PL + koszt całkowity w PLN z datą”, której nie widziałem u konkurentów w SERP-ach.

## 6. Zarobek (`dane/B-programy.csv`)

### Programy partnerskie (sprawdzone u źródła tam, gdzie się dało)

| Program | Model | Stawka | PL | Źródło |
|---|---|---|---|---|
| XTB Program Partnerski | „Otrzymuj prowizje zgodnie z uzgodnionym modelem rozliczeń” | nie opublikowano | tak, strona PL | xtb.com/pl/afiliacja-forex-kb [CP] |
| IBKR CPC Publisher Program | CPC z miesięcznym limitem (MRP), stawki indywidualne | nie opublikowano | PL nie jest na liście wykluczeń (Chiny, Korea, Japonia, Izrael, Chile, Portugalia, Hiszpania) | interactivebrokers.ie/en/general/about/affiliate-programs.php [CP] |
| Trading 212 Affiliates | CPA (2018: „do 1 000 USD”) | niepotwierdzone | niepotwierdzone | trading212affiliates.com przekierowuje na stronę główną [CP]; financemagnates.com 2018 [WS] |
| Revolut (Impact) | prowizja po rejestracji, KYC i zasileniu | nie opublikowano | niepotwierdzone | revolut.com/en-BE/become-a-revolut-affiliate [WS]; strona pusta dla crawlera [CP] |
| Finax, mBank eMakler, DM BOŚ | | | | publicznego programu nie znalazłem [WS] |
| Plus500 (CFD) | CPA | „do 800 USD za kwalifikowanego tradera” | tabela krajów nieodczytana | 500affiliates.com [CP] |

**Stanowisko UKNF z 11.10.2023 r. w sprawie programów poleceń oraz programów partnerskich** (knf.gov.pl, PDF; treść odczytana z [WS] i ispb.pl [CP], sam PDF zablokowany przez proxy):
- podstawa: art. 79 ust. 2a ustawy o obrocie instrumentami finansowymi; pozyskiwanie klientów usług maklerskich wykonuje tylko firma inwestycyjna albo jej agent;
- UKNF opisuje wprost programy partnerskie z youtuberami i blogerami, gdzie wynagrodzenie zależy od skuteczności, oraz linki afiliacyjne;
- według streszczenia: klienci firmy inwestycyjnej ani nieregulowani pośrednicy nie mogą prowadzić zindywidualizowanych działań w celu pozyskania klientów usług maklerskich;
- według rp.pl polskie firmy dostosowały się do stanowiska, a zagraniczne nie [WS].

Co z tego wynika dla serwisu, nie oceniam (to kwestia prawna). Fakt dla decyzji: model „link afiliacyjny do brokera za CPA” jest w Polsce pod lupą nadzoru, a polscy brokerzy nie publikują stawek. Przed startem potrzebna opinia prawnika.

### Reklamy i inne źródła

- **CPC rdzenia:** ważone 1,87 USD; „etf” 3,01, „vwce” 4,17, „justetf” 4,11, „ter etf” 6,26, „trading 212 opinie” 4,14, „najlepszy broker” 11,25 [W]. Reklamodawcy płacą dużo, ale RPM display dla PL **nie ma wiarygodnego źródła**; w rachunku to założenie.
- **Freemium:** atlasETF ma strefę premium (cennika i liczby użytkowników nie sprawdziłem) [WS]. Płatne narzędzie (portfel ETF z kosztem całkowitym, alerty zmian TER, eksport) jest możliwe, ale popytu na nie nie mierzyłem.

### CFD oceniam osobno: odradzam

- XTB na stronie programu partnerskiego: „77% rachunków inwestorów detalicznych odnotowuje straty pieniężne w wyniku handlu kontraktami CFD u niniejszego dostawcy CFD” [CP].
- Za klienta CFD płaci się najwięcej (Plus500: do 800 USD [CP]), a frazy są drogie: „forex” 9 900/mies. przy CPC 15,38 USD, „broker forex” 140 przy 33,39 USD, „cfd” 8 100 przy 6,41 USD [W].
- UKNF w stanowisku z 2023 r. wskazał właśnie rynek forex i CFD jako źródło problemu z programami partnerskimi [WS].
- Serwis o ETF-ach (długi termin, niskie koszty) zarabiałby wtedy na produkcie, na którym większość klientów traci. To kłóci się z zasadą uczciwości projektu. **Wniosek: CFD poza ofertą**, również jako reklama na stronie (np. capital.com wyświetla się przy „xtb opinie” [S]).

### Wybór modelu

1. **Reklamy display** jako podstawa, bo nie zależą od stanowiska UKNF. Mały przychód przy tym ruchu.
2. **IBKR CPC** (płatność za kliknięcie, nie za pozyskanie klienta) i **program XTB** dopiero po opinii prawnika i potwierdzeniu stawek przez właściciela. Tylko konta akcji i ETF.
3. **Freemium** po zbudowaniu ruchu: kalkulator kosztu całkowitego i portfel ETF jako narzędzie płatne w rozszerzonej wersji. Tu przydaje się UX/UI właściciela.

## 7. Rachunek po 12 miesiącach (`dane/B-rachunek.csv`)

Ruch = wolumen fraz × CTR pozycji × pokrycie fraz stronami × mnożnik AIO. Krzywa CTR: SEO Inc. 2025 (poz. 1 = 28,5%, poz. 5 = 6,1%, poz. 10 = 1,4%; https://seoinc.com/?p=9742); pozostałe pozycje interpolowane (założenie). Mnożnik AIO 0,7 dla encji, narzędzi i rankingów, 0,85 dla edukacji i brokerów (założenie na podstawie 9 z 11 SERP-ów z AIO).

| Parametr | Ostrożny | Realny |
|---|---|---|
| Pokrycie fraz stronami | 50% | 80% |
| Pozycja: encje / edukacja / narzędzia / rankingi / broker | 8 / 9 / 8 / 8 / 9 | 5 / 6 / 5 / 5 / 6 |
| Frazy-głowy ≥5 000 („etf”, „etf co to”, „vwce”, „procent składany”, „kalkulator inwestycji”) | poza top 10 | poz. 9 |
| **Sesje/mies.** | **1 794** | **7 862** |
| w tym encje | 1 231 | 4 876 |
| Klik do brokera (encja 3/5%, ranking 6/10%, broker 10/15%, reszta 2–3%) | 61 | 407 |
| Konwersja klik → zasilone konto | 3% | 4% |
| Wypłata za zasilone konto | 150 zł | 300 zł |
| **Afiliacja** | **273 zł** | **4 887 zł** |
| Reklamy (RPM 8 / 20 zł, 1,4 / 1,7 odsłony na sesję) | 20 zł | 267 zł |
| **Razem** | **ok. 290 zł/mies.** | **ok. 5 150 zł/mies.** |
| Bez afiliacji (tylko reklamy) | ok. 20 zł | ok. 270 zł |

Wszystkie wiersze poza wolumenem i trzema punktami krzywej CTR to założenia. Żadna stawka za konto nie jest potwierdzona dla PL; punkty odniesienia to Plus500 do 800 USD (CFD, odrzucone) i program poleceń IBKR „200 USD” za klienta z saldem 10 000 USD (program dla klientów, nie dla wydawców) [CP][WS]. 300 zł to ok. 77 USD przy kursie 3,8952. Pozycje dla nowej domeny YMYL bez autora z twarzą przyjąłem ostrożniej niż w niszach hobbystycznych. W styczniu ruch będzie ok. 1,35× średniej, latem ok. 0,85× [W].

## 8. Ryzyka i E-E-A-T

- **YMYL-finanse bez eksperta z twarzą.** W SERP-ach encji wygrywają emitenci i portale, a w edukacji blogi autorskie z 500–2 700 domenami linkującymi [B]. Co częściowo zastąpi twarz: każda liczba z linkiem do KID lub FIRDS i datą sprawdzenia; publiczna metodologia (skąd TER, jak liczymy koszt całkowity, kiedy odświeżamy); testy kalkulatorów na przykładach z wynikiem na stronie; przegląd niezależny każdej serii; jawna informacja o linkach partnerskich i brak CFD. Wobec atlasETF i Inwestomatu to nie wystarczy na frazy-głowy.
- **Rekomendacje (MAR, KNF).** „Ranking etf” i „najlepsze etf” to intencja „co kupić”. Zestawienie posortowane po TER lub wielkości może zostać odebrane jako sugestia inwestycyjna. Granicę ustala właściciel z prawnikiem; na stronie tylko kryteria i dane.
- **Stanowisko UKNF o programach partnerskich** (sekcja 6): główny model zarobku zależy od interpretacji prawnej.
- **AI Overview w 9 z 11 SERP-ów,** a przy tickerach odpowiada wprost (cena, ISIN, TER) [S].
- **Zależność od jednego gracza po stronie zarobku:** realny wariant opiera się na 1–2 brokerach z niejawnymi stawkami.
- **Dane MSCI i justETF** nie mogą trafić na stronę [CP].
- **Wiele pytań z SERP to podatki:** „Czy zakup ETF trzeba zgłosić do urzędu skarbowego?” (PAA przy „gdzie kupić etf”), AIO przy „etf akumulacyjny” opisuje podatek Belki [S]. Serwis bez podatków nie odpowie na część pytań odbiorców.

## 9. Omijamy

Podatki: podatek Belki, PIT-38 i PIT-8C, W-8BEN, podatek u źródła od dywidend funduszy, „czy zakup ETF trzeba zgłosić do urzędu skarbowego”, przewaga podatkowa ETF-ów akumulujących jako przepis. IKE, IKZE i PPK jako przepisy i limity („ike etf” 210, „ikze etf” 140, „mbank ike etf” 50 [K]). Przepisy PRIIPs jako temat (dlaczego VOO czy QQQ nie są dostępne). CFD, forex, ETF-y lewarowane i krótkie, krypto-ETP. Rankingi „co kupić”, prognozy, sygnały. Wzory dokumentów.

## 10. Czego nie sprawdziłem

- Stawek XTB, IBKR i Revolut dla PL (wymagają rejestracji, której brief zabrania) oraz tego, czy program Trading 212 dla wydawców jeszcze działa.
- Pełnego tekstu stanowiska UKNF (PDF na knf.gov.pl zablokowany przez proxy; korzystałem ze streszczeń w wyszukiwarce i z ispb.pl).
- Regulaminów stron emitentów (iShares, Vanguard, Amundi, Xtrackers) co do pobierania danych z KID.
- Cennika strefy premium atlasETF i jej popularności.
- Aktualnej listy funduszy zagranicznych notyfikowanych w KNF (znalazłem tylko raporty 2008–2018) i warunków użycia danych NBP.
- SERP-ów dla polskich ETF-ów z GPW (Beta ETF; 21 920/mies.) i dla fraz „procent składany” i „kalkulator inwestycji”.
- Reklamodawców w Google Ads dla fraz ETF i zasad weryfikacji reklam finansowych w Google dla PL.
- RPM reklam display dla finansów w PL.

---

## Streszczenie

- **Werdykt:** WARUNKOWO (bez opinii prawnika o stanowisku UKNF i bez potwierdzonych stawek: NIE).
- **Wynik:** 2,8 / 5 (popyt 4; SERP 2,5; zarobek 2,5; fosa 3; ryzyko 2).
- **Dopasowanie do profilu:** 4 / 5.
- **Model zarobku:** reklamy display + IBKR CPC i program XTB (tylko konta akcji i ETF, po potwierdzeniu) + później freemium narzędzi. CFD odrzucone.
- **Rachunek po 12 mies.:** ok. 290 zł/mies. (ostrożny), ok. 5 150 zł/mies. (realny, w 95% z niepotwierdzonego CPA); same reklamy: 20 i 270 zł.

1. Mapa niszy: 2 198 fraz, 267 460 wyszukiwań/mies., CPC ważone 1,87 USD; „etf” 22 200 przy CPC 3,01 USD [W][K].
2. Trend: +26,7% r/r w 24 mies., ale III kw. 2026 tylko +13,1%, a od szczytu w 01.2026 (285 210) spadek do 176 540 w 09.2026 [W].
3. Porównania ETF-ów „X vs Y” prawie nie mają popytu („vwce vs iwda” 10/mies.); popyt mają tickery (vwce 5 400, vwra 3 600, iwda 3 600) i edukacja („etf co to” 14 800) [W].
4. Baza ETF-ów po polsku już istnieje: atlasETF (>3 000 funduszy, porównywarka, skaner, 631 domen linkujących, ETV 16 009, 1. miejsce na „vwce”, cytowany w AIO). justETF nie ma wersji PL [CP][B][T][S].
5. AI Overview w 9 z 11 SERP-ów; przy tickerach podaje cenę, ISIN i TER bez kliknięcia. Najsłabszy SERP to ogólny „kalkulator procent składany” (5 z 9 wyników z domen <300 linkujących) [S][B].
6. Dane: ESMA FIRDS wolno używać komercyjnie z podaniem źródła (ISIN, akumulacja lub dystrybucja z kodu CFI, waluta, rynki); TER, indeks i wielkość tylko ręcznie z KID; justETF i dane MSCI odpadają [CP].
7. UKNF (11.10.2023): pozyskiwanie klientów usług maklerskich przez nieregulowanych pośredników w programach partnerskich jest kwestionowane; polscy brokerzy (XTB) nie publikują stawek, IBKR płaci za kliknięcie, Finax, mBank i DM BOŚ nie mają publicznych programów [WS][CP].
8. CFD odradzam: 77% rachunków detalicznych CFD w XTB traci pieniądze; najwyższe stawki (Plus500 do 800 USD) płyną właśnie za CFD [CP].

# F. Tematy z wcześniejszych czatów i repozytoriów (18.10.2026)

Właściciel poprosił, żeby przejrzeć jego wcześniejsze projekty i wyłowić z nich tematy pod nasz schemat serwisu: Astro, klastry poradników, narzędzia, strony encji, polski rynek. Profil i zasady: [BRIEF.md](BRIEF.md). Metoda: [../METODA.md](../METODA.md).

Źródła (czytane 18.10.2026, tylko tematy, bez danych osobowych i prywatnych treści):
- repo `venomstyle/saas`, gałąź `claude/research-ideas-2026-10`: `README.md`, `STATE.md`, `data/ranking_all.csv` (149 ocenionych pomysłów z 174), `reports/problem_map.md`;
- repo `venomstyle/tradingalgo`: `app/README.md`, `research/design/ux/03_WNIOSKI_POTRZEBY_IA_FLOWY.md`, `05_UPROSZCZENIE_JEDEN_EKRAN.md`, `UCITS_MAP.md`, `research/FACTOR_CATALOG_SUMMARY.md`, `research/prop_firm_rules.md`, `research/round86/ROUND86.md`;
- sesje Claude Code: TradingAlgo (`session_01T4Jjg9aLZZhLUvAmY4Z1aZ`), Gridling (`session_01R4riCD24UEKZRw44psSaU8`), badanie pomysłów (`session_01AY7EbTPqLM1TEVTmqrKdwn`); tylko podsumowania tur.

Dane: [dane/F-tematy.csv](dane/F-tematy.csv), [dane/F-wolumeny.csv](dane/F-wolumeny.csv), [dane/F-popyt-podsumowanie.csv](dane/F-popyt-podsumowanie.csv), [dane/F-serp-top10.csv](dane/F-serp-top10.csv), [dane/F-serp-podsumowanie.csv](dane/F-serp-podsumowanie.csv), [dane/F-ocena.csv](dane/F-ocena.csv). Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/os-F/` (`vol.py`, `serp.py`, `serp_manual.py`).

## Czym są projekty właściciela (krótko)

- **Saas (badanie pomysłów).** Pakiet wieloagentowy: 38 657 sygnałów z Reddita, recenzji aplikacji, forów i SERP-ów, 121 kart problemów (66 PL/UE), 174 pomysły. Badanie zatrzymano 5.10.2026 przed raportem końcowym. Ranking roboczy jest w `data/ranking_all.csv`. Większość pomysłów to SaaS lub aplikacje z kontami. Do naszego schematu pasują głównie kalkulatory (format `calculator`) i pomysły z danymi publicznymi.
- **TradingAlgo.** Badanie strategii (86 rund testów, katalog 277 czynników) i prototyp produktu **Rotacja**: portfel modelowy z ETF-ów UCITS, połowa stale w Nasdaq-100, druga połowa rotuje co kwartał, z alertami wyjść.
  - **Newsletter Rotacja:** maile „zmiana kwartału”, „alert”, „stan modelu” z gotową listą zleceń.
  - **Kalkulator zleceń:** przelicza skład modelu na całe jednostki UCITS u wybranego brokera dla kapitału wpisanego przez użytkownika.
  - **„Śledź model”:** ekran „Dziś” mówi, czy dziś trzeba coś kupić lub sprzedać.
- **Gridling.** Aplikacja: zdjęcie → wzór haftu krzyżykowego (PDF, zgodny z Pattern Keeper), płatna za wzór lub roczny dostęp, rynek anglojęzyczny.
- **Inne sesje (tytuły):** Mobbin i wtyczki Figmy (UX), port gry z iOS na Androida, „Randka” (randki i gry karciane), strona do planowania randek z motywem corgi.

### Rotacja i „śledź model” a prawo

Newsletter z sygnałami modelu, lista „sprzedaj X, kup Y” i ekran „śledź model” to w praktyce rekomendacja inwestycyjna. Podlega MAR i nadzorowi KNF, a przy dopasowaniu do klienta staje się doradztwem z licencją. Sam projekt to zauważa (`03_WNIOSKI…`, W6: „Disclaimer nie chroni”, „ostateczny kształt do potwierdzenia z kancelarią”). Zasady właściciela to wykluczają, więc **odrzucam ten produkt w obecnej formie.**

Co z tej wiedzy da się użyć publicznie bez rekomendacji:
1. **Laboratorium strategii (edukacja):** opisy znanych, publicznych strategii (GEM, momentum, średnia 10-miesięczna), metodologia backtestu i jego pułapki (wybór z wielu prób, przeżywalność spółek). Bez aktualnego składu i bez sygnałów. To dubluje niszę ETF-ów, którą bada inny agent, więc tylko to zaznaczam.
2. **Kalkulator rebalancingu bez modelu:** użytkownik wpisuje własne wagi docelowe, a narzędzie liczy zlecenia w całych jednostkach i resztę gotówki. To czysta arytmetyka, bez sygnału. Też nisza ETF.
3. **Mapa odpowiedników ETF z USA w UCITS** (`UCITS_MAP.md`): strony encji „odpowiednik QQQ w UCITS”. Nisza ETF.
4. **Wiedza o prop firmach** (`prop_firm_rules.md`): tego nie bada nikt inny. Zmierzyłem jako T2.

## Lista tematów

Dopasowanie do profilu (UX/UI, trading, majątek, obligacje, wideo) w skali 1–5. Pełna wersja z plikami: [dane/F-tematy.csv](dane/F-tematy.csv).

| # | Temat | Skąd | Dopasowanie | Schemat serwisu | Status |
|---|---|---|---|---|---|
| 1 | Kalkulatory tradera i encyklopedia wskaźników z backtestami | tradingalgo: FACTOR_CATALOG, ROUND86; saas I-046, I-032, I-033 | 5 | tak | zmierzony (T1) |
| 2 | Prop trading: baza zasad firm, kalkulator drawdownu | tradingalgo: `prop_firm_rules.md` | 5 | tak | zmierzony (T2) |
| 3 | Rotacja: portfel modelowy, newsletter, „śledź model” | tradingalgo: `app/README.md`, UX 03; sesja TradingAlgo | 5 | nie | odrzucony (rekomendacja) |
| 4 | Kalkulator zleceń (rebalancing do całych jednostek) | tradingalgo: `app/` | 5 | tak | dubluje ETF |
| 5 | Mapa odpowiedników ETF z USA w UCITS | tradingalgo: `UCITS_MAP.md` | 5 | tak | dubluje ETF |
| 6 | Haft krzyżykowy: przelicznik mulin, wzór ze zdjęcia | sesja Gridling | 3 | tak | zmierzony (T3) |
| 7 | Odmiana i pochodzenie nazwisk | saas I-058 (#13, 67 pkt) | 2 | tak | zmierzony (T4) |
| 8 | Randki i gry dla par | sesje „Randka”, „Date planning… corgi” | 3 | tak | zmierzony (T5) |
| 9 | Kalkulatory dla sprzedających, porównanie wysyłki | saas I-010, I-088, I-087, I-012 | 2 | tak | zmierzony (T6) |
| 10 | Nadpłacać kredyt czy inwestować | saas I-039 | 4 | tak | zmierzony (T7) |
| 11 | Czy książka jest w abonamencie (Legimi, Empik Go) | saas I-004 (#11) | 1 | częściowo | zmierzony (T8) |
| 12 | Kalkulatory IKE/IKZE/OKI, PIT-38, rejestr strat | saas I-029, I-030, I-028, I-048, I-045 | 5 | tak | omijamy (podatki) |
| 13 | Inwestycje vs inflacja i EDO; koszt DCA | saas I-047, I-049 | 5 | tak | dubluje obligacje i ETF |
| 14 | Opłacalność kanału bez twarzy, stawki twórcy | saas I-084, I-097, I-078 | 4 | tak | dubluje twórców wideo |
| 15 | UX fintech, wtyczki Figmy, Mobbin | tradingalgo FINTECH_DESIGN_RESEARCH; sesje Mobbin, Figma | 5 | tak | dubluje UX/UI |
| 16 | Wesele: koperty, budżet, plan stołów | saas I-057, I-056, I-059 | 1 | tak | już w RANKING (2,85) |
| 17 | Smart home: zgodność urządzeń | saas I-050, I-052 | 2 | tak | już w RANKING (2,55–2,65) |
| 18 | Budowa i wykończenie domu | saas I-063, I-062, I-070, I-064 | 1 | tak | wykluczone z góry |
| 19 | Cło na paczki spoza UE | saas I-101 | 1 | tak | omijamy (prawo) |
| 20 | Port gry iOS na Androida | sesja „iOS game Android port” | 2 | nie | niezmierzony |

## Pomiar 8 tematów

Wszystko z DataForSEO 18.10.2026, `location_code` 2616, `language_code` "pl".
- **Wolumeny:** `/v3/keywords_data/google_ads/search_volume/live`, `date_from` 2025-07-01. Średnia to X.2025–IX.2026. Trend r/r to suma VII–IX 2026 wobec VII–IX 2025.
- **SERP:** `/v3/serp/google/organic/live/advanced`, depth 10, 3 frazy na temat (24 SERP-y).
- **Linki:** `/v3/backlinks/bulk_referring_domains/live`, osobno dla 199 URL-i i 138 domen z top 10.

### Popyt

| Temat | Fraz | Suma śr. mies. | Trend r/r | Min / max miesiąc | Ważony CPC (USD) | Największe frazy |
|---|---|---|---|---|---|---|
| T1 Trading: wskaźniki, kalkulatory | 23 | 13 342 | −32,4%* | XII.2025 / IX.2026 | 4,10 | day trading 5 208; analiza techniczna 3 258; formacje świecowe 970 |
| T2 Prop trading | 11 z 13 | 25 114 | −9,8% | VII.2026 / I.2026 | 1,86 | ftmo 14 725; topstep 5 150; fundingpips 1 425 |
| T3 Haft krzyżykowy | 20 z 21 | 22 498 | −6,7% | VI.2026 / X.2025 | 0,17 | mulina 7 183; kanwa 5 650; haft krzyżykowy 4 592 |
| T4 Odmiana i pochodzenie nazwisk | 16 z 17 | 30 362 | −19,0% | VIII.2026 / X.2025 | 0,71 | odmiana nazwisk 17 508; pochodzenie nazwiska 4 125 |
| T5 Randki i gry dla par | 14 z 16 | 17 852 | −13,4% | VI.2026 / II.2026 (×6) | 0,27 | gry dla par 8 825; pomysły na walentynki 4 002; pytania dla par 3 350 |
| T6 Sprzedaż i wysyłka | 14 z 15 | 9 985 | −19,1% | VIII.2026 / III.2026 | 2,33 | kalkulator prowizji allegro 4 433; inpost cennik 2 442 |
| T7 Nadpłata kredytu | 10 z 11 | 34 628 | −34,2% | VI.2026 / I.2026 | 0,84 | kalkulator nadpłaty kredytu hipotecznego 14 525 |
| T8 Abonamenty e-book (bez nazw marek) | 8 z 9 | 7 721 | −36,8% | VI.2026 / XI.2025 | 0,68 | storytel cena 2 058; czytnik ebooków 1 742 |

\* T1 bez trzech fraz z nagłym skokiem w VII–IX 2026 („analiza techniczna” 3 900 → 17 900, „day trading” 4 200 → 27 900, „wstęgi bollingera” w VIII.2026 2 400). Z nimi wychodzi +160,6%, co uznaję za anomalię danych. Same frazy pod narzędzia są małe: „kalkulator pipsów” 102, „kalkulator pozycji forex” 63, „kalkulator wielkości pozycji” 20.

Kontekst poza rdzeniem: „tradingview” 120 417/mies., marki abonamentów (legimi, storytel, empik go…) 209 184, imiona dla dzieci 66 899, „kalkulator kredytu hipotecznego” 101 208, „diamond painting” 8 825.

### SERP

Mediana domen linkujących liczona dla **całych domen** w top 10, tak jak w pozostałych plikach. Liczone do konkretnych URL-i dają prawie same zera (mediana 0–1 we wszystkich tematach), więc nie różnicują nisz. „AIO” liczy też AI Overview ładowany asynchronicznie (bez treści w odpowiedzi API).

| Temat | Frazy SERP | Mediana domen (domena) | Domen < 50 | Fora/social/wideo | Stare (< 2023) lub PDF | AIO |
|---|---|---|---|---|---|---|
| T1 | kalkulator pipsów; wskaźnik rsi; średnia krocząca | 2 852 | 0 z 24 | 4 | 7 | 3 z 3 |
| T2 | prop trading; ftmo opinie; firmy prop tradingowe | 1 875 | 0 z 26 | 4 | 0 | 3 z 3 |
| T3 | wzory haftu krzyżykowego; przelicznik muliny dmc ariadna; haft krzyżykowy dla początkujących | 588 | 2 z 24 | 8 | 11 | 3 z 3 (2 asynchr.) |
| T4 | odmiana nazwisk; odmiana nazwisk na zaproszeniach; pochodzenie nazwiska | 170 | 4 z 28 | 4 | 8 | 2 z 3 |
| T5 | pomysły na randkę; gry dla par; pytania dla par | 1 001 | 1 z 26 | 1 | 7 | 3 z 3 (1 asynchr.) |
| T6 | kalkulator prowizji allegro; porównywarka kurierów; prowizja vinted | 533 | 2 z 26 | 5 | 2 | 3 z 3 |
| T7 | kalkulator nadpłaty kredytu hipotecznego; nadpłacać kredyt czy inwestować; zmniejszenie raty czy okresu | 1 503 | 2 z 25 | 4 | 1 | 3 z 3 (1 asynchr.) |
| T8 | legimi czy empik go; abonament na ebooki; czy książka jest w legimi | 4 945 | 2 z 25 | 8 | 4 | 3 z 3 (1 asynchr.) |

Co widać w SERP-ach:
- **T1:** kalkulatory pipsów mają wyłącznie brokerzy CFD i serwisy z nimi związane (dukascopy, fxpro, cashbackforex, fxtm). Przy wskaźnikach są wpisy z 2015–2019 (trading-academy.pl 2019, fxmag 2019, forum stockwatch 2015), ale na domenach z tysiącami linków.
- **T2:** mały serwis **propfirm.pl (69 domen)** jest na 2.–3. miejscu i AIO go cytuje. Obok są bankier, fxmag, forexclub, investing. Przy „ftmo opinie” reklamy kupują FTMO i FundedNext.
- **T3:** „przelicznik muliny dmc ariadna” to najsłabszy SERP w całym badaniu: forum.gazeta.pl z 2006 i 2009 roku, blogspot z 2010, senior.pl z 2010, Pinterest, docer i ulotka PDF. Fraza ma jednak 0 wyszukań w Google Ads, więc to raczej funkcja serwisu niż osobny cel. Przy „wzory haftu krzyżykowego” rankują sklepy (coricamo, kokardka) i krzyzykowo.pl z **1 domeną linkującą**.
- **T4:** rankują poradnie językowe (UW, UŁ, PWN 2007), blogi i dwa narzędzia: nlp.actaforte.pl i odmiananazwisk.pl (114 domen). „Odmiana nazwisk na zaproszeniach” nie ma AI Overview.
- **T5–T8:** w T5 rankują aplikacje i sklepy z grami. W T6 i T7 pierwsze miejsca zajmują oficjalne narzędzia (kalkulator Allegro, kalkulator UOKiK) oraz brokerzy kredytowi. W T8 dominują strony samego Legimi.

### Zarobek (sprawdzone 18.10.2026, bez rejestracji)

- **FTMO:** program partnerski płaci 8% (Bronze) do 20% (Platinum) opłaty za challenge. Progi miesięczne podaje strona programu ([ftmo.oanda.com/affiliate-program](https://ftmo.oanda.com/affiliate-program/), FAQ: [stawki](https://ftmo.oanda.com/faq/how-do-i-earn-commissions-and-what-are-the-commission-rates)). Wynik WebSearch, strony nie czytałem bezpośrednio.
- **TradingView:** 30% każdej płatności za subskrypcję poleconej osoby, jeśli kupi w ciągu 90 dni ([zasady programu](https://se.tradingview.com/partner-rules)). To jedyny płatnik w tradingu niezwiązany z CFD.
- **Brokerzy CFD:** XTB podaje, że 77% rachunków detalicznych traci na CFD (dane agenta B: [dane/B-cfd.csv](dane/B-cfd.csv)). Afiliację CFD oceniał osobno agent B, więc tu jej nie liczę.
- **Legimi:** afiliacja przez sieci (Awin, Admitad, Tradedoubler, model CPS, cookie 30 dni). Źródła podają sprzeczne stawki (25% albo 5–10%), dlatego stawki nie podaję.
- **Haft:** programu partnerskiego Coricamo nie znalazłem. Płatnikiem może być własny produkt właściciela (Gridling, według sesji płatny za wzór lub roczny dostęp). Wersji polskiej Gridlinga jeszcze nie ma.
- **Furgonetka i brokerzy kurierscy:** programu partnerskiego nie potwierdziłem.
- **Nazwiska, randki:** nie znalazłem płatnika poza reklamami display. Nie sprawdzałem programów drukarni zaproszeń.

### Fosa danych

- **T4:** na dane.gov.pl jest zbiór nazwisk z rejestru PESEL (stan 19.01.2024: ok. 380 tys. nazwisk męskich i ponad 400 tys. żeńskich, według [benchmark.pl](https://www.benchmark.pl/ile-osob-ma-takie-samo-nazwisko-jak-ty-7265372934074945a)). Daje to strony „nazwisko X: odmiana, ile osób nosi”. **Licencji nie potwierdziłem**, bo strona i API dane.gov.pl były dziś niedostępne przez proxy i DataForSEO.
- **T2:** tabela zasad Topstep, Lucid i Tradeify już istnieje w repo właściciela, ale pochodzi z wyników WebSearch i część pól ma znak [?]. To fosa pracy, a nie otwarte dane: zasady zmieniają się co kilka tygodni.
- **T3:** numery kolorów DMC i Ariadna są publiczne (karta Ariadna w PDF na ariadna.com.pl). Licencji tabel konwersji nie sprawdzałem.
- **T1, T6, T7, T8:** otwartych danych nie ma albo są płatne. WIBOR/WIRON publikuje GPW Benchmark na licencji. Cenniki Allegro i przewoźników trzeba by zbierać ręcznie.

### Ocena (METODA: popyt 20%, SERP 25%, zarobek 25%, fosa 15%, niskie ryzyko 15%)

| Temat | Popyt | SERP | Zarobek | Fosa | Ryzyko | **Wynik** | Dopasowanie | Werdykt |
|---|---|---|---|---|---|---|---|---|
| T3 Haft krzyżykowy | 4 | 4 | 3 | 4 | 4 | **3,75** | 3 | WARUNKOWO |
| T4 Odmiana i pochodzenie nazwisk | 3 | 4 | 2 | 4 | 4 | **3,30** | 2 | WARUNKOWO |
| T2 Prop trading | 3 | 3 | 4 | 3 | 2 | **3,10** | 5 | WARUNKOWO |
| T5 Randki i gry dla par | 3 | 3 | 2 | 3 | 4 | 2,90 | 3 | NIE |
| T6 Sprzedaż i wysyłka | 2 | 3 | 3 | 3 | 3 | 2,80 | 2 | NIE |
| T8 Abonamenty e-book | 2 | 2 | 3 | 2 | 3 | 2,40 | 1 | NIE |
| T1 Trading: wskaźniki, kalkulatory | 2 | 2 | 3 | 2 | 2 | 2,25 | 5 | jako dział T2 |
| T7 Nadpłata kredytu | 2 | 2 | 3 | 2 | 2 | 2,25 | 4 | NIE |

Uzasadnienie ocen ryzyka:
- **T2 (2):** YMYL finansowy. Prop firmy sprzedają płatne „egzaminy” na kontach demo i większość osób ich nie zdaje. SERP pokazuje wątki „FTMO przekręt?” (reddit) i „oszustwo czy szansa?” (bankier). Część pytań to podatki (PAA „Jak rozliczyć prop trading?”, akademialtca.pl, zasada-m.pl), których nie ruszamy.
- **T1 i T7 (2):** YMYL. W T1 płacą głównie brokerzy CFD. T7 zahacza o przepisy o prowizji za wcześniejszą spłatę.
- **T3, T4, T5 (4):** bez YMYL. Ryzyka to AI Overview i sezon: luty w T5, jesień przed świętami w T3.

### Rachunek po 12 miesiącach (tylko 3 tematy warunkowe; założenia, nie dane)

| Temat | Ruch mies. po 12 mies. (ostrożnie / realnie) | Konwersja i stawka (założenia) | Przychód mies. (ostrożnie / realnie) |
|---|---|---|---|
| T2 Prop trading | 1 500 / 5 000 | 0,5% / 1% kupuje challenge. Średnia opłata 150 USD (ceny 90–369 USD z `prop_firm_rules.md`, IX.2026), prowizja 8% / 10% | ok. 90 USD / ok. 750 USD |
| T3 Haft krzyżykowy | 3 000 / 10 000 | 0,3% / 0,8% kupuje wzór w Gridlingu za 4,99 EUR (cena z sesji Gridling) | ok. 45 EUR / ok. 400 EUR, wymaga polskiej wersji Gridlinga |
| T4 Odmiana nazwisk | 5 000 / 20 000 | reklamy display, RPM 3–6 zł (założenie) | ok. 15 zł / ok. 120 zł |

## Wnioski

1. **Najmocniejszy temat z czatów to haft krzyżykowy (3,75).** Wynik jest wyższy niż u finalistów z RANKING.md (kampery 3,70). Popyt to 22 498 wyszukań miesięcznie przy CPC 0,17 USD, a SERP-y są słabe (sklepy, fora z 2006–2010, krzyzykowo.pl z 1 domeną linkującą). Sens ma to tylko z płatnikiem: serwis byłby polskim lejkiem do Gridlinga, a polskiej wersji Gridlinga jeszcze nie ma. Afiliacji sklepów z haftem nie potwierdziłem.
2. **Prop trading najlepiej pasuje do profilu (5) i ma realnego płatnika.** FTMO płaci 8–20% opłaty, a mały propfirm.pl (69 domen) jest w top 3 i AIO go cytuje. Popyt to w większości frazy z nazwą marki (ftmo 14 725, topstep 5 150). Ryzyko etyczne i YMYL jest wysokie: większość kupujących challenge traci opłatę. Warunek: uczciwe strony firm i planów z danymi, ze źródłem i datą, zawsze z kosztem i odsetkiem niezdanych (jeśli firma go publikuje). Bez podatków i bez „najlepszej firmy” jako rekomendacji.
3. **Rotacja, newsletter i „śledź model” odpadają.** To sygnały inwestycyjne (MAR/KNF), co przyznaje sam projekt (UX 03, W6). Edukacyjne pozostałości (kalkulator rebalancingu bez modelu, mapa UCITS, opis strategii i backtestów) należą do niszy ETF. Przekazuję je agentowi ETF.
4. **Wiedza tradingowa sama w sobie słabo się sprzedaje w SEO (2,25).** Kalkulatory pipsów i pozycji mają po 20–110 wyszukań, a top 10 zajmują brokerzy CFD. Encyklopedię wskaźników warto robić tylko jako dział serwisu o prop tradingu, z afiliacją TradingView (30% subskrypcji). Afiliację brokerów CFD pomijam (XTB: 77% rachunków traci).
5. **Odmiana nazwisk ma słaby SERP i fosę danych, ale prawie nie zarabia (3,30).** Zbiór PESEL na dane.gov.pl daje setki tysięcy stron encji, a jeden SERP nie ma nawet AIO. Licencji zbioru dziś nie potwierdziłem, a reklamy display dają szacunkowo 15–120 zł miesięcznie. Nadaje się na dodatek albo tani eksperyment, nie na główny serwis.
6. **Kalkulatory z badania Saas (prowizje Allegro, nadpłata kredytu, abonamenty e-book) przegrywają z oficjalnymi narzędziami.** Kalkulator Allegro, kalkulator UOKiK i strony Legimi zajmują pierwsze miejsca, a trendy spadają o 19–37% r/r. Odrzucam.
7. **Randki i gry dla par (2,90):** spory popyt (17 852, w lutym ×6), ale brak płatnika i silni gracze (aplikacje z pytaniami, sklepy). Sens ma tylko wtedy, gdy właściciel wyda własną grę karcianą z projektu „Randka” jako produkt.
8. **Dublują inne nisze i tylko je zaznaczam:** kalkulatory IKE/IKZE/PIT-38 (podatki, omijamy), EDO vs inflacja (obligacje), koszt DCA, Rotacja edukacyjnie i mapa UCITS (ETF), opłacalność kanału bez twarzy (twórcy wideo), UX fintech i wtyczki Figmy (UX/UI).

## Omijamy

PIT-38 i rejestr strat, limity i zasady IKE/IKZE/OKI, rozliczanie prop tradingu (umowa zlecenie, działalność), DAC7 przy Vinted, cło na paczki spoza UE, prowizja za wcześniejszą spłatę kredytu jako przepis, sygnały i skład portfela Rotacji.

## Czego nie sprawdziłem

- Licencji zbioru nazwisk PESEL na dane.gov.pl (strona wymaga JavaScriptu, API zablokowane przez proxy).
- Bezpośrednio stron programów partnerskich FTMO i TradingView (dane z WebSearch), stawek Legimi (źródła sprzeczne), programów Furgonetki, sklepów z haftem i drukarni zaproszeń.
- Odsetka zdanych challenge'y w prop firmach.
- Ruchu konkurentów (propfirm.pl, odmiananazwisk.pl, krzyzykowo.pl): `bulk_traffic_estimation` nie był używany.

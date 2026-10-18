# Nisza A: obligacje skarbowe detaliczne i ochrona oszczędności przed inflacją (badanie z 18.10.2026)

Metoda: `research/nisze/METODA.md` i `research/nisze/osobiste/BRIEF.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie liczby pobrane 18.10.2026.

**Skróty źródeł** (każda liczba w tekście ma przy sobie jeden z nich):

- **[SV]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live`, 99 fraz, okres 10.2024–09.2026. Wolumen = średnia miesięczna z ostatnich 12 mies. CPC w USD.
- **[KS]** DataForSEO `/v3/dataforseo_labs/google/keyword_suggestions/live`, seed „obligacje”, 500 fraz o największym wolumenie (baza ma 2 726 fraz).
- **[SERP]** DataForSEO `/v3/serp/google/organic/live/advanced`, desktop, depth 10, z AI Overview, 6 fraz.
- **[BL]** DataForSEO `/v3/backlinks/bulk_referring_domains/live`, domeny linkujące do **całej domeny**.
- **[TE]** DataForSEO `/v3/dataforseo_labs/google/bulk_traffic_estimation/live`, szacowany ruch organiczny w PL (etv).
- **[CP]** DataForSEO `/v3/on_page/content_parsing/live` (strona czytana przez DataForSEO, bo proxy blokuje curl/WebFetch).
- **[TV]** TradingView `FX_IDC:EURPLN`, kurs 4,3671.

Surowe dane w `dane/`: `A-wolumeny.csv` (99 fraz, 24 mies.), `A-sugestie.csv` (500 fraz z [KS] z kategorią), `A-serp-top10.csv` (53 wyniki), `A-konkurencja.csv`, `A-programy.csv`, `A-zrodla-danych.csv`, `A-rachunek.csv`. Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/os-A/`.

## Werdykt

**NIE jako samodzielny serwis.** Popyt jest duży, ale w 82% nawigacyjny (ludzie szukają strony emitenta). Pomysł „strona każdej serii” nie ma popytu: 12 kodów serii daje razem 400 wyszukań miesięcznie [SV]. Kalkulatory i strony serii już robią nowe, małe serwisy (edolabs.pl ma „ponad 1000 serii”) [SERP]. Obligacji nie da się sprzedać afiliacyjnie, a AI Overview jest w 6 z 6 SERP-ów i podaje pełną tabelę oprocentowania [SERP]. Temat pasuje do właściciela (5/5), więc warto go użyć jako **modułu** szerszego serwisu oszczędnościowego, nie jako osobnej domeny.

## Tabela ocen

Skala 1–5, 5 = najlepiej. Wagi z METODA.md.

| Kryterium | Waga | Ocena | Uzasadnienie w skrócie |
|---|---|---|---|
| Popyt i trend | 20% | 3 | Rdzeń 230 100/mies., ale 187 710 to frazy nawigacyjne; r/r −12,7% [SV] |
| Słabość SERP | 25% | 2,5 | Kalkulatory słabe linkowo (mediana 31 domen), ale zajęte przez nowe serwisy; reszta to MF, PKO, portale; AIO 6/6 [SERP, BL] |
| Zarobek | 25% | 2,5 | Obligacje bez afiliacji; konta bankowe 20,60–144,01 EUR w MyLead, ale intencja „obligacje” słabo przechodzi w „załóż konto” |
| Fosa danych / narzędzia | 15% | 2,5 | Dane MF, GUS dostępne komercyjnie, ale te same dla wszystkich; edolabs.pl już ma bazę serii |
| Niskie ryzyko | 15% | 2 | YMYL-finanse bez eksperta; kalkulator netto wymaga podatku Belki (temat zakazany); AIO 6/6 |
| **Wynik ważony** | | **2,53** | |
| Dopasowanie do profilu (poza wagą) | | **5** | Obligacje i budowanie majątku to doświadczenie właściciela |

## Popyt

Zbiorczo [SV] (r/r = VII–IX 2026 wobec VII–IX 2025):

| Grupa | Fraz | Suma/mies. | Trend r/r | Szczyt / dołek | CPC mediana / ważone |
|---|---|---|---|---|---|
| Rdzeń „obligacje…” | 47 | 230 100 | −12,7% | I 2026: 275 210 / VI 2026: 190 900 | 0,61 / 0,83 USD |
| w tym nawigacyjne (obligacje skarbowe, …logowanie, …pko, …pekao) | 4 | 187 710 | −15,1% | | 0,77 / 0,82 USD |
| Kody serii (EDO1035, COI1030…) | 12 | 400 | 490 → 1 610 | IX 2026: 1 300 | brak CPC |
| Kalkulatory obligacji | 8 | 15 690 | +0,6% | I 2026: 19 310 / VI 2026: 14 420 | 0,33 / 0,25 USD |
| Kalkulator lokaty i inflacji | 2 | 25 100 | „kalkulator lokaty” 87 300 → 54 300 | | |
| Lokaty i konta oszczędnościowe | 12 | 124 680 | −18,8% | I 2026: 159 500 | 0,74 / 1,07 USD |
| Inflacja i stopy procentowe | 13 | 208 040 | −51,9% | XI 2025: 303 090 | 1,06 / 1,17 USD |
| Maklerskie i inne | 5 | 9 830 | +108,8% | | 1,25 / 1,91 USD |

Najważniejsze frazy [SV]:
- „obligacje skarbowe” 165 000 (CPC 0,82 USD), „obligacje” 18 100, „obligacje skarbowe logowanie” 18 100, „obligacje skarbowe pko” 4 400.
- Informacyjne: „obligacje skarbowe oprocentowanie” 3 600 (r/r 9 400 → 14 200), „obligacje edo” 2 400 (4 500 → 7 200), „jak kupić obligacje skarbowe” 2 400, „obligacje indeksowane inflacją” 2 400, „obligacje rodzinne” 1 900, „obligacje 10 letnie” 1 300 (2 760 → 5 000), „obligacje 800 plus” 720 (1 100 → 2 160).
- Kalkulatory: „kalkulator obligacji skarbowych” 6 600, „obligacje skarbowe kalkulator” 4 400, „kalkulator obligacji” 4 400, „ile można zarobić na obligacjach” 170, „kalkulator obligacji edo” 110.
- Serie: „edo1035” 140, „edo0936” 70 (w VII–IX 2026 razem 730), „coi0930” 20, „edo1036” 10, „ror1027”, „dor1028”, „ots0127” po 0 [SV]. W 500 sugestiach dla „obligacje” nie ma żadnego kodu serii [KS].
- Porównanie: „obligacje czy lokata” 260, „lokata czy obligacje” 260, „jak chronić oszczędności przed inflacją” 10 [SV].
- Popyt na **ofertę miesiąca** jest wyraźny: 23 frazy typu „obligacje skarbowe listopad 2025” (1 600), „…marzec 2026” (1 300), „…styczeń 2026” (1 300) dają razem 13 300/mies. [KS]. To argument za alertem nowych serii.
- Frazy do pominięcia (IKE/IKZE, podatki): 71 fraz, 32 810/mies., np. „ike obligacje” 5 400, „ikze obligacje” 2 900 [KS].
- „rentowność obligacji” 5 400 (r/r 5 700 → 30 200) dotyczy obligacji hurtowych i rynku, poza tą niszą [SV].

Wniosek: bez fraz nawigacyjnych zostaje ok. 42 400/mies. dla obligacji (rdzeń informacyjny 42 390 [SV]) plus 15 690 na kalkulatory. Trend rdzenia spada, kalkulatory stoją w miejscu, inflacja jako temat spadła o połowę.

## SERP

Frazy: „obligacje skarbowe oprocentowanie”, „kalkulator obligacji skarbowych” (narzędzie), „obligacje edo” i „edo1035” (encje), „obligacje czy lokata” (porównanie), „ranking kont oszczędnościowych” (zarobek) [SERP].

| Fraza | Mediana domen linkujących | Wyniki <50 domen | „Słabe”* | Kto wygrywa |
|---|---|---|---|---|
| obligacje skarbowe oprocentowanie | 5 206 | 0 z 9 | 0 | obligacjeskarbowe.pl, gov.pl (MF), pkobp.pl, pekao.com.pl, analizy.pl, kupfundusz.pl, bankier.pl |
| kalkulator obligacji skarbowych | 31 | 6 z 9 | 6 | bondito.pl (29), kalkulator.pl (426), edolabs.pl (31, trzy pozycje), finanse-arch.mf.gov.pl, blog-leadstar.pl, finwire.pl (49), zyskzobligacji.pl (18) |
| obligacje edo | 1 614 | 0 z 9 | 0 | obligacjeskarbowe.pl (3×), pkobp.pl, pekao.com.pl, gov.pl, analizy.pl, atlasetf.pl, subiektywnieofinansach.pl |
| edo1035 | 652 | 0 z 9 | 2 | 8 z 9 wyników to obligacjeskarbowe.pl, ale strony **innych** serii (EDO0423, EDO0818, EDO0821, EDO0122) i pliki tabel; brak strony EDO1035 |
| obligacje czy lokata | 9 387 | 2 z 8 | 6 | forbes.pl (2026), samorzad.pap.pl (2020), bunkierinwestora.pl (7), bank.pl (2014), wykop.pl, sprawdzonelokaty.pl (11), YouTube, bankier.pl |
| ranking kont oszczędnościowych | 2 101 | 0 z 9 | 1 | jakoszczedzic.pl (360), tanie-konto.pl (917), analizy.pl, doradca.tv (259), zgarnijpremie.pl (775), gazetaprawna.pl (2014), bankier.pl, moneteo.com (3 179) |

Razem 53 wyniki: mediana 652 domen linkujących, 8 wyników <50 domen, 15 „słabych” [SERP, BL].
\* „Słaby” = domena <50 domen linkujących albo forum/serwis społecznościowy/wideo albo wpis sprzed 2023 r. albo plik.

Co z tego wynika:
- **Kalkulator** to najsłabszy SERP linkowo, ale nie jest pusty. Zajmują go serwisy powstałe niedawno: edolabs.pl (wpis z 25.09.2026, „baza obejmuje ponad 1000 serii i jest aktualizowana co miesiąc”), bondito.pl („porównaj obligacje, lokaty i konta oszczędnościowe”, czyli dokładnie nasz pomysł), zyskzobligacji.pl, finwire.pl [SERP]. Ich szacowany ruch: finwire.pl 1 822/mies., edolabs.pl 1 748, bondito.pl 306, zyskzobligacji.pl 251 [TE]. To pokazuje sufit dla nowego serwisu w tej niszy.
- **Strony serii** (encje): Google nie ma strony EDO1035, więc konkurencja byłaby łatwa, ale nikt jej nie szuka (140/mies.) [SV, SERP]. edolabs.pl już ma strony serii pod adresami typu `/zysk-z-obligacji-skarbowych-kalkulator/ros/09/25` [SERP].
- **„Obligacje czy lokata”** to najsłabszy SERP treściowo (wpisy z 2014 i 2020 r., Wykop, YouTube, blogi z 7 i 11 domenami), ale popyt to 520/mies. [SV, SERP, BL].
- **Ranking kont** zajmują porównywarki i blogi afiliacyjne z setkami domen; moneteo.com ma szacowany ruch 97 312/mies. [BL, TE].

## AI Overview

- AI Overview w **6 z 6** SERP-ów [SERP].
- Dla „obligacje skarbowe oprocentowanie” AIO podaje pełną listę: OTS 2,00%, ROR 4,00%, DOR 4,15%, TOS 4,40%, COI 4,75%, EDO 5,35%, ROS 5,00%, ROD 5,60% (oferta październik 2026), z marżami i ceną 100 zł [SERP]. Odpowiedź kończy się w Google.
- Dla „ranking kont oszczędnościowych” AIO pokazuje tabelę 9 banków z oprocentowaniem i warunkami [SERP].
- AIO cytuje małe serwisy: zyskzobligacji.pl (18 domen), kredytowyporadnik.pl (112), zamknijkonto.pl (798), bankoweabc.pl (520) [SERP, BL]. Mała strona może trafić do cytatów, ale klik wtedy rzadko następuje.

## Zarobek

**Obligacje.** Programu partnerskiego dla detalicznych obligacji nie znalazłem (WebSearch, SERP DataForSEO, 18.10.2026). Obligacje sprzedaje agent emisji PKO BP, a strona obligacjeskarbowe.pl podkreśla „brak dodatkowych opłat i ukrytych prowizji” [CP]. Pekao też sprzedaje obligacje (link „Przejdź do serwisu” na obligacjeskarbowe.pl) [CP]. Obligacja sama nie zarobi.

**Konta oszczędnościowe i osobiste (sprawdzone u źródła, 18.10.2026)** (`dane/A-programy.csv`):
- **MyLead** publikuje strony programów ze stawkami: Erste Bank Polska 10 kampanii, 20,60–125,29 EUR; mBank do 111,05 EUR; PKO do 82,19 EUR (20 kampanii); Santander do 61,00 EUR; Bank Millennium do 51,37 EUR; Revolut do 144,01 EUR. Kategoria „Konto Oszczędnościowe” ma 10 kampanii [SERP, CP]. Przy kursie 4,3671 [TV] to 90–547 zł za Erste i do 629 zł za Revolut. Stawek dla pojedynczych kampanii nie widać bez logowania.
- **LeadStar** (AJA Media): ok. 600 kampanii; w październiku 2026 bonus 300 zł za każde 5 sprzedaży kont osobistych BNP Paribas i 250 zł za każde 3 Konta Smart Erste; stawki bazowe tylko po zalogowaniu [CP].
- **Afilo**: afilo.pl przekierowuje do idmnet.pl (programmatic IDM Net); finansowej sieci afiliacyjnej pod tą nazwą nie ma [CP].
- **Comperia**: comperia.pl/program-partnerski pokazuje formularz leadu kredytowego, bez programu dla wydawców [CP].
- **Webepartners**: w wynikach dla „program partnerski bank konto” tylko sklepy [SERP]. Programu bankowego nie znalazłem.
- **Bankier SMART**: to porównywarka konkurenta; jako sieci dla wydawców nie sprawdzałem.

**Maklerzy.** XTB ma program partnerski w modelu CPL/CPA, ale stawki ustala Partnership Manager po kontakcie [CP]. Kontakt z firmą jest poza zasadami, a XTB to dostawca CFD: „77% rachunków inwestorów detalicznych odnotowuje straty pieniężne w wyniku handlu kontraktami CFD” (xtb.com/pl, 18.10.2026) [CP]. **Ocena: afiliacji brokerów CFD nie łączyć z serwisem o ochronie oszczędności.** Odbiorca szuka bezpieczeństwa, a produkt z dźwignią przeczy obietnicy serwisu.

**Reklamy.** CPC: rdzeń obligacji 0,61 USD (mediana), kalkulatory 0,33 USD, „konto oszczędnościowe” 2,23 USD, „gdzie trzymać oszczędności” 2,52 USD, „konto maklerskie” 4,35 USD [SV]. RPM dla polskich finansów **nie potwierdziłem u źródła**; w rachunku to jawne założenie.

**Newsletter z alertem nowych serii.** Popyt jest (13 300/mies. na frazy z miesiącem [KS]); MF publikuje ofertę co miesiąc na gov.pl. Newsletter sam nie zarabia; zarabia link do konta oszczędnościowego w mailu.

**Główny problem zarobku:** kto szuka obligacji, już wybrał obligacje. Most do afiliacji to porównanie „obligacje czy lokata czy konto” (520/mies. [SV]) i „ranking kont” (27 100/mies. [SV]), ale ten drugi SERP jest zajęty przez porównywarki.

## Fosa danych

| Źródło | Dane | Licencja / warunki | Komercyjnie |
|---|---|---|---|
| MF na gov.pl (https://www.gov.pl/web/finanse/biezaca-oferta2) | komunikaty o ofercie miesiąca | teksty gov.pl na **CC BY-SA 4.0**, zdjęcia i wideo CC BY-NC-ND 4.0 (stopka gov.pl) [CP] | tak, z uznaniem autorstwa i na tych samych warunkach |
| obligacjeskarbowe.pl | listy emisyjne, tabele odsetkowe, oprocentowanie serii | brak strony z licencją; stopka „© Ministerstwo Finansów 2026” [CP] | liczby to fakty; plików tabel nie kopiować hurtem bez potwierdzenia |
| GUS (https://stat.gov.pl/copyright) | inflacja CPI (wyznacza COI, EDO, ROS, ROD od 2. roku) | GUS „nie ma zastrzeżeń co do kopiowania plików i stron… w tym do własnych opracowań, pod warunkiem, że będzie podane ich źródło” [CP] | tak, ze źródłem |
| NBP (api.nbp.pl, komunikaty RPP) | stopa referencyjna (ROR, DOR) | api.nbp.pl: „Wszystkie prawa zastrzeżone”; API obejmuje kursy i złoto, nie stopy [CP] | stopa to fakt z datą decyzji; licencji otwartej brak |
| Banki | oprocentowanie lokat i kont | brak licencji | tylko jako fakty z datą, zbierane ręcznie |

Narzędzia możliwe na tych danych: kalkulator „ile zarobię” z inflacją GUS, archiwum oprocentowania każdej serii, „realne oprocentowanie po inflacji”, alert nowej oferty. Słabość: dane są takie same dla każdego, a edolabs.pl, bondito.pl i zyskzobligacji.pl już je wykorzystują [SERP]. Fosa to tylko jakość i świeżość, nie dostęp.

## Ryzyko

- **YMYL-finanse bez eksperta z twarzą.** Osłabia E-E-A-T w temacie, gdzie wygrywają MF, PKO BP i portale z tysiącami domen [BL]. Co to zastąpi: liczby wyłącznie z MF, GUS, NBP z linkiem i datą; jawna metodologia kalkulatora (wzór z listu emisyjnego); test kalkulatora na tabelach odsetkowych MF (zgodność do grosza, wynik testu na stronie); przegląd niezależny każdej serii tekstów; brak afiliacji przy obligacjach jako dowód neutralności. To pomaga, ale nie zastąpi marki w SERP-ach z MF i PKO.
- **Podatki (zakazane).** Kalkulator „ile zarobię na rękę” wymaga 19% podatku od odsetek. Konkurenci i AIO liczą zysk netto z podatkiem i IKE [SERP]. Bez podatku nasz kalkulator pokaże tylko kwotę brutto, czyli gorszą odpowiedź. **Decyzja właściciela:** czy stawkę podatku można podać jako parametr z linkiem do źródła, bez opisu przepisów.
- **Rekomendacje (MAR, KNF).** Frazy „najkorzystniejsze obligacje skarbowe” (2 400 [KS]) i „czy warto” zachęcają do wskazania serii. Dozwolone: scenariusze z parametrami (inflacja X, horyzont Y) bez „kup”.
- **AIO 6/6** i pełne tabele oprocentowania w AIO [SERP].
- **Spadek tematów:** inflacja −51,9% r/r, lokaty −18,8%, rdzeń −12,7% [SV].
- **Zależność od jednego źródła:** cała niszowa treść zależy od comiesięcznego komunikatu MF.

## Omijamy

Podatek od odsetek (podatek Belki) i PIT; IKE-Obligacje i IKZE-Obligacje jako przepisy (limity, ulgi, zwroty); dziedziczenie obligacji; wykup przez spadkobierców; obligacje dla dzieci jako temat prawny (darowizny); „800 plus” jako przepisy programu (uprawnienia do ROS/ROD tylko jako fakt z listu emisyjnego z linkiem); wzory dyspozycji i wniosków; rankingi „najlepsza seria”; CFD, forex i dźwignia.

## Pomysł (gdyby jednak budować) i co z niego zostaje

- Strona każdej serii (EDO1035 itd.) z historią oprocentowania: **popytu brak** (400/mies. na 12 kodów [SV]), edolabs.pl już to ma.
- Kalkulator „ile zarobię” z inflacją: popyt 15 690/mies., SERP słaby linkowo, ale zajęty przez 4–5 młodych serwisów [SV, SERP]. Bez podatku przegrywa z konkurencją.
- Porównywarka obligacje vs lokaty vs konta z datą: bondito.pl już to robi (29 domen, 306 wizyt/mies. [BL, TE]).
- Strona „oferta obligacji [miesiąc] [rok]” + alert mailowy: najlepszy element (13 300/mies. [KS], powtarzalny co miesiąc), ale AIO odpowiada na nią tabelą.

## Rachunek po 12 miesiącach

Założenia (`dane/A-rachunek.csv`): ruch rośnie liniowo do miesiąca 12; 1,6 odsłony na wizytę; konta bankowe przez MyLead/LeadStar; RPM, CTR i konwersja to założenia, nie dane.

| | Ostrożny | Realny |
|---|---|---|
| Wizyty/mies. w 12. miesiącu | 1 500 (poziom bondito.pl ×5, poniżej edolabs.pl [TE]) | 4 000 (ok. 2× edolabs.pl i finwire.pl [TE]) |
| RPM reklam (założenie) | 10 zł | 25 zł |
| Klik w ofertę konta / konwersja | 1,5% / 3% | 3% / 5% |
| Stawka za konto | 90 zł (20,60 EUR, dolna granica Erste w MyLead) | 200 zł (ok. 46 EUR, poniżej maksimów 51–144 EUR) |
| **Przychód w 12. miesiącu** | **85 zł/mies.** | **1 360 zł/mies.** |
| **Suma za 12 miesięcy** | **551 zł** (reklamy 156, afiliacja 395) | **8 840 zł** (reklamy 1 040, afiliacja 7 800) |
| Subskrybenci newslettera po roku | ok. 100 | ok. 520 |

Koszty: hosting statyczny i narzędzie do newslettera w planie darmowym (założenie, cen nie sprawdzałem), domena. Budżet właściciela na reklamy nic tu nie zmienia: CPC fraz z intencją zakupu kont („konto oszczędnościowe” 2,23 USD [SV]) jest wyższe niż spodziewany przychód z kliknięcia.

## Dopasowanie do profilu: 5/5

Obligacje, budowanie majątku i inwestowanie to doświadczenie właściciela; UX/UI pomaga przy kalkulatorach. Udział pasywny jest możliwy (dane z MF raz w miesiącu, agent aktualizuje). Ograniczenia: brak twarzy w YMYL i zakaz podatków, który odcina najczęstsze pytanie „ile na rękę”.

## Czego nie sprawdziłem

- Stawek MyLead i LeadStar dla pojedynczych kampanii kont oszczędnościowych (wymagają logowania; rejestracja zakazana).
- RPM reklam dla polskich finansów (brak źródła u reklamodawcy).
- Bankier SMART jako programu dla wydawców.
- Licencji plików tabel odsetkowych na obligacjeskarbowe.pl (strona bez licencji; proxy blokuje bezpośredni dostęp).
- Bieżącej stopy referencyjnej NBP i inflacji GUS z września 2026 (niepotrzebne do oceny niszy).

## Streszczenie

- **Werdykt:** NIE jako samodzielny serwis; ewentualnie moduł (kalkulator + alert oferty miesiąca) w szerszym serwisie oszczędnościowym. **Wynik 2,53/5.** Dopasowanie do profilu 5/5.
- **Popyt:** rdzeń 230 100/mies., ale 187 710 to frazy nawigacyjne do MF i PKO; r/r −12,7%; kalkulatory obligacji 15 690/mies. (+0,6%); kody serii razem 400/mies. [SV].
- **SERP:** kalkulatory słabe linkowo (mediana 31 domen), ale zajęte przez nowe serwisy z tym samym pomysłem (edolabs.pl z >1000 serii, bondito.pl z porównywarką); oprocentowanie i EDO należą do MF, PKO, Pekao [SERP, BL].
- **AIO 6/6**, z pełną tabelą oprocentowania 8 typów obligacji i tabelą 9 kont [SERP].
- **Model zarobku:** afiliacja kont bankowych (MyLead: 20,60–144,01 EUR za konto; LeadStar: bonusy 250–300 zł), obligacje bez programu partnerskiego; CFD (XTB, 77% traci) odrzucone.
- **Rachunek 12 mies.:** ostrożny 551 zł (85 zł/mies. na koniec), realny 8 840 zł (1 360 zł/mies. na koniec), głównie afiliacja kont.
- **Dane:** MF na gov.pl (CC BY-SA 4.0), GUS (kopiowanie ze źródłem) są komercyjnie dostępne, ale identyczne dla konkurencji; NBP bez otwartej licencji.
- **Ryzyko:** YMYL bez eksperta, podatek potrzebny do „zysku na rękę” jest tematem zakazanym (do decyzji właściciela), pokusa rekomendacji „najlepsza seria”.

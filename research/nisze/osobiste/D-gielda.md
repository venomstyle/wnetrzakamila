# Giełda dla Polaków: dywidendy, spółki GPW, edukacja tradingowa (badanie z 18.10.2026)

Zakres: kalendarz dywidend ze spółkami jako encjami (stopa dywidendy z datą, historia wypłat, dzień ustalenia prawa), słownik i edukacja tradingowa (wskaźniki, formacje, czytanie wykresu, bez sygnałów i rekomendacji), kalkulatory (stopa dywidendy, średnia cena zakupu, wielkość pozycji, procent składany). Metoda: `research/nisze/METODA.md` i `research/nisze/osobiste/BRIEF.md`. Wszystkie liczby pobrane 18.10.2026.

**Oznaczenia źródeł:**
- **[SV]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live` (location_code 2616, pl, `date_from` 2024-10-01, 24 mies.). Wolumen = średnia z 12 mies. (X 2025–IX 2026), CPC w USD. Trend r/r: suma VII–IX 2026 wobec VII–IX 2025.
- **[KS]** DataForSEO `/v3/dataforseo_labs/google/keyword_suggestions/live` (nasiona: „dywidenda” 1000 fraz z 3 462, „akcje”, „spółki”, „konto maklerskie”, „kalkulator”, „formacja”, „wskaźnik”, „analiza techniczna”).
- **[S]** DataForSEO `/v3/serp/google/organic/live/advanced`, desktop, depth 10, `load_async_ai_overview`.
- **[BL]** DataForSEO `/v3/backlinks/bulk_referring_domains/live` (53 URL-e i 48 domen).
- **[T]** DataForSEO `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (ETV organiczny, PL).
- **[A]** DataForSEO `/v3/serp/google/ads_advertisers/live/advanced`.
- **[CP]** DataForSEO `/v3/on_page/content_parsing/live` (WebFetch nie rozwiązuje domen przez proxy).
- **[WS]** WebSearch (streszczenie wyników, bez otwierania źródła).
- **[TV]** TradingView `FX_IDC:USDPLN` = 3,8852.

Pliki w `dane/`: `D-frazy.csv` (154 frazy, 24 mies., status: rdzeń / marka / CFD / omijamy), `D-encje-dywidendy.csv` (383 spółki z [KS]), `D-serp-top10.csv`, `D-serp-podsumowanie.csv`, `D-konkurencja.csv`, `D-programy.csv`, `D-zrodla-danych.csv`, `D-rachunek.csv`. Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/os-D/`.

## Werdykt w skrócie

**NIE jako osobny serwis (wynik 2,45 / 5). Dopasowanie do profilu: 4 / 5.**

1. **Popyt jest duży, ale spada.** Rdzeń bez marek ma 126 fraz i 124 800 wyszukiwań/mies. [SV]. Do tego warstwa encji „[spółka] dywidenda [rok]”: 737 fraz po usunięciu odmian, ok. 83 650/mies. [KS]. Frazy bez roku w nazwie: **−15,3% r/r**. Pary rokowe („pzu dywidenda 2026” wobec „pzu dywidenda 2025”, I–IX): **−29,2%** [SV].
2. **Encje i kalendarz mają gospodarzy.** Strefainwestorow.pl, stockwatch.pl, biznesradar.pl, bankier.pl i notowania.pb.pl mają pełne bazy dywidend i są cytowane w AI Overview [S]. Słabe są tylko SERP-y kalkulatorów (mediana domen linkujących 268) [S][BL].
3. **Zarobek bez CFD jest niepewny.** U źródła potwierdziłem program XTB (stawki niejawne), TradingView (10–400 USD jednorazowo) i IBKR (CPC ustalane indywidualnie). Programu dla wydawców nie znalazłem w mBanku ani w DM BOŚ [CP][WS]. Najwyższe stawki brokerów dotyczą CFD, a u XTB 77% rachunków detalicznych CFD traci pieniądze [CP].
4. **Fosa danych jest płatna.** Publikacja kursów GPW, także opóźnionych o 15 minut, wymaga umowy licencyjnej z GPW [CP]. Bez kursu nie policzymy stopy dywidendy „z datą” na własnych danych.

Rachunek po 12 mies.: **ostrożnie 223 zł łącznie (34 zł w 12. miesiącu), realnie ok. 6 490 zł (ok. 1 000 zł w 12. miesiącu)**. Realny wariant opiera się na założonej stawce CPA, której nie da się dziś sprawdzić.

## Tabela ocen

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 3 | 124 800 + ok. 83 650 encji/mies., ale −15,3% r/r (bez roku) i −29,2% w parach rokowych [SV][KS] |
| Słabość SERP | 25% | 2,5 | mediana domen linkujących w top 10: 3 861; 5 z 53 wyników ma <50 domen; kalkulatory słabe (268) [BL] |
| Zarobek | 25% | 2,5 | CPC ważone rdzenia 2,09 USD [SV]; programy XTB i IBKR bez jawnych stawek, TradingView potwierdzony, ale mały [CP] |
| Fosa danych / narzędzia | 15% | 2 | dywidendy z raportów ESPI to fakty dostępne dla wszystkich; kursy GPW płatne [CP] |
| Niskie ryzyko | 15% | 2 | YMYL-finanse bez twarzy, AIO w 6 z 6 SERP-ów, sezon dywidendowy, sąsiedztwo MAR [S] |
| **Wynik ważony** | | **2,45** | 0,2·3 + 0,25·2,5 + 0,25·2,5 + 0,15·2 + 0,15·2 |

---

## 1. Popyt i trend [SV][KS] (`dane/D-frazy.csv`)

| Typ strony | Fraz | Wolumen/mies. | Przykłady (wolumen, CPC USD) |
|---|---|---|---|
| Hub | 10 | 41 920 | „dywidenda” 22 200 (3,21), „dywidendy 2026” 9 900, „wig20 spółki” 3 600, „spółki dywidendowe” 1 900 (1,85) |
| Narzędzie | 24 | 23 220 | „kalkulator procentu składanego” 8 100, „kalkulator inwestycyjny” 6 600, „procent składany kalkulator” 4 400, „komunikaty espi” 1 300, „kalendarz dywidend 2026” 720, „kalkulator dywidendy” 390, „position size calculator” 170 (7,75) |
| Encja: spółka | 25 | 20 460 | „pzu dywidenda 2026” 3 600, „orlen dywidenda 2026” 2 400, „pko bp dywidenda 2026” 1 300, „xtb dywidenda 2026” 1 300 |
| Edukacja | 36 | 17 450 | „analiza techniczna” 2 900, „rsi” 2 900, „stop loss” 1 600, „hossa i bessa” 1 600, „formacje świecowe” 880, „macd” 720 |
| Poradnik | 16 | 12 260 | „procent składany” 6 600, „jak inwestować na giełdzie” 1 300, „stopa dywidendy” 720, „dzień dywidendy” 260 |
| Komercyjna | 14 | 9 100 | „xtb opinie” 5 400 (3,11), „konto maklerskie” 1 600 (4,35), „konto maklerskie ranking” 320, „kurs tradingu” 260 (3,35) |
| Porównanie | 1 | 390 | „najlepsze spółki dywidendowe” 390 |
| **Rdzeń razem** | **126** | **124 800** | CPC ważone 2,09 USD |

Poza rdzeniem: marki konkurentów jako kontekst („stooq” 550 000, „bankier” 301 000, „xtb” 246 000, „tradingview” 135 000, „biznesradar” 40 500, „stockwatch” 14 800, „comparic” 14 800, „strefa inwestorów” 12 100), frazy wieloznaczne („wig20” 368 000, „trading” 18 100, „espi” 14 800), CFD i forex osobno („forex” 9 900, CPC 15,38; „cfd” 8 100; „dźwignia finansowa” 4 400) [SV].

**Warstwa encji [KS].** Z 1000 najczęstszych fraz z „dywidend*” (na 3 462 w bazie) 866 dotyczy konkretnej polskiej spółki, razem 104 600/mies. Po scaleniu odmian szyku zostaje 737 fraz i 83 650/mies. dla ok. 383 nazw spółek. Najwięcej: PZU 13 410, Orlen 12 010, PKO BP 7 510 (plus „pkobp” 1 470 i „pko” 1 940), XTB 4 730, Pekao 4 470, KGHM 3 310, Kruk 1 800, Stalexport 1 740 (`dane/D-encje-dywidendy.csv`). Frazy z rokiem żyją kilka miesięcy: „pzu dywidenda 2025” miała 19 700 w VII–IX 2025 i 450 w VII–IX 2026 [SV].

**Trend [SV].** Frazy rdzenia bez roku: 237 880 (VII–IX 2026) wobec 280 860 (VII–IX 2025), czyli −15,3%. Pary rokowe I–IX: 248 960 wobec 351 510, −29,2%. Spadki: „kalkulator procentu składanego” −22%, „xtb opinie” −39%, „spółki dywidendowe” −37%, „jak kupić akcje” −52%. Wzrost: „analiza techniczna” 3 900 → 17 900 (+359%, jednorazowy skok, przyczyny nie sprawdzałem), „procent składany” +15%, „stopa dywidendy” +139% [SV].

**Sezon [SV].** Rdzeń w ostatnich 12 mies.: maksimum V 2026 (159 950), minimum VIII 2026 (93 310). W 24 mies. szczyt III 2025 (182 670). Popyt rośnie w styczniu i w sezonie walnych zgromadzeń (III–VI).

**Frazy narzędziowe z briefu są małe [SV]:** „kalkulator wielkości pozycji” 20, „średnia cena zakupu akcji” 10, „kalkulator średniej ceny zakupu akcji” 0, „kalkulator ryzyka trading” 0, „kalkulator pipsów” 110, „kalkulator giełdowy” 480. Duży jest tylko procent składany (8 100 + 4 400 + 6 600 „procent składany”).

## 2. SERP i AI Overview [S][BL] (`dane/D-serp-podsumowanie.csv`, `dane/D-serp-top10.csv`)

„Słaby wynik” = domena z <50 domenami linkującymi, social/wideo/PDF albo treść sprzed 2023 r.

| Fraza [SV] | Typ | Mediana RD domeny | Domeny <50 RD | Social/wideo/PDF | Sprzed 2023 | Słabe | AIO | Kto wygrywa |
|---|---|---|---|---|---|---|---|---|
| dywidendy 2026 (9 900) | hub/kalendarz | 4 057 | 0 | 2 | 0 | 2 z 9 | tak | strefainwestorow.pl ×3, stockwatch.pl ×2, biznesradar.pl, bankier.pl, YouTube ×2 |
| pzu dywidenda 2026 (3 600) | encja | 18 400 | 1 | 1 | 0 | 2 z 9 | tak | notowania.pb.pl, bankier.pl ×2, pzu.pl, businessinsider.com.pl ×2, strefainwestorow.pl, blog.squaber.com (44 RD) |
| kalkulator procentu składanego (8 100) | narzędzie | 268 | 2 | 0 | 0 | 2 z 9 | tak | home.saxo, minikalkulator.pl, portfelik.com, ppcg.com.pl, kalkulatorprocentow.pl, omnicalculator.com, finansowykalkulator.pl (13 RD), finwire.pl (49 RD) |
| kalkulator dywidendy (390) | narzędzie | 6 127 | 2 | 1 | 2 | 5 z 9 | tak | dywidenciarz.pl (34 RD), ey.com (sp. z o.o.), kalkulatorbox.pl (7 RD), omnicalculator.com, gofin.pl (2017), sii.org.pl (2016) |
| formacje świecowe (880) | edukacja | 4 286 | 0 | 2 | 2 | 2 z 8 | tak | bossa.pl, edukacjagieldowa.pl (GPW), xtb.com, liteforex.pl, stockwatch.pl, forex.com, PDF z 2018, YouTube z 2018 |
| konto maklerskie ranking (320) | komercyjna | 1 871 | 0 | 1 | 3 | 4 z 9 | tak | comperia.pl (stary ranking), obserwatorgospodarczy.pl, marciniwuc.com, mojaprzyszlaemerytura.pl (2017), direct.money.pl (2024), moneteo.com |

**Razem:** 53 wyniki, mediana domen linkujących 3 861, 5 domen z <50 RD, 17 słabych wyników [BL]. Linki do samych podstron są rzadkie: 44 z 52 URL-i ma 0–2 domeny linkujące [BL], więc wygrywa siła domeny i baza danych, nie linki do strony.

**Najwięksi gracze [T][BL]:** bankier.pl ETV 3 480 600 (20 861 RD), xtb.com 236 450 (14 909), stooq.pl 236 330 (2 649), biznesradar.pl 206 890 (1 917), stockwatch.pl 202 600 (4 057), strefainwestorow.pl 66 210 (3 861), comparic.pl 46 390 (3 467), kontomaniak.pl 42 160 (1 024). Małe serwisy z narzędziami: minikalkulator.pl 32 950 (423 RD), liczgrupa.pl 25 390 (65 RD), squaber.com 22 890, kalkulatorprocentow.pl 20 980 (112 RD), inwestomat.eu 10 510 (522 RD), ppcg.com.pl 6 820 (268 RD), dywidenciarz.pl 227 (34 RD).

**AI Overview [S]:** w 6 z 6 SERP-ów. Małe serwisy cytuje w 3 z 6: kalkulator procentu składanego (ppcg.com.pl, kalkulatorprocentow.pl, portfelik.com, minikalkulator.pl, mathema.me), kalkulator dywidendy (dywidenciarz.pl, liczgrupa.pl), „dywidendy 2026” (ppcg.com.pl obok strefainwestorow.pl i stockwatch.pl). Przy encji „pzu dywidenda 2026” AIO podaje kwotę 4,80 zł, dzień dywidendy 17.09.2026 i dzień wypłaty 08.10.2026 z pzu.pl i portali, więc odpowiedź na pytanie „kiedy i ile” zostaje w Google.

**Reklamy [A]:** XTB S.A. ma zweryfikowane konto reklamodawcy z ok. 700 reklamami w PL. Dla fraz „konto maklerskie” i „kurs tradingu” endpoint nie zwrócił reklamodawców.

## 3. Zarobek (`dane/D-programy.csv`)

| Program | Potwierdzone u źródła | Model i stawki |
|---|---|---|
| XTB Program Partnerski | tak, program istnieje [CP: xtb.com/pl/afiliacja-forex-kb] | „Otrzymuj prowizje zgodnie z uzgodnionym modelem rozliczeń”. Stawek na stronie nie ma. Tabele w serwisach trzecich (200–600 USD dla CFD, mniej dla akcji/ETF) są niepotwierdzone [WS] |
| TradingView | tak [CP: pl.tradingview.com/partner-rules, zasady z 30.09.2026, w mocy od 30.10.2026] | jednorazowo za pierwszą subskrypcję w wersji web: Essential 10/60 USD, Plus 25/100 USD, Premium 50/120 USD, Ultimate 200/400 USD (mies./rok). Cookie 90 dni, wypłata PayPal, płatne reklamy tylko za pisemną zgodą, zakaz przedstawiania narzędzi jako rekomendacji |
| Interactive Brokers | tak, program istnieje [CP: interactivebrokers.ie affiliate-programs] | CPC z miesięcznym limitem, stawki ustalane indywidualnie; płatność 30 dni od faktury; cel: „Open & Funded Accounts” |
| Trading 212 | **nie** | strona affiliates przekierowuje na stronę główną [CP]; artykuł z 2018 r. podaje do 1 000 USD za klienta CFD i ok. 100 USD za konto akcji [WS] |
| mBank eMakler | nie znaleziono | brak programu dla wydawców w wynikach [WS] |
| DM BOŚ (bossa.pl) | nie znaleziono | brak programu w wynikach [WS] |
| Kursy tradingowe | nie znaleziono | brak polskiego programu ze stawkami; strona afiliacyjna Udemy nie dała się odczytać [WS][CP] |

**CPC [SV]:** „dywidenda” 3,21 USD, „trading” 6,38, „swing trading” 7,86, „konto maklerskie” 4,35, „xtb opinie” 3,11, „position size calculator” 7,75, „kalkulator pipsów” 9,67, „forex” 15,38. Najdroższe frazy prowadzą do CFD i forex.

**Własny produkt:** płatne alerty dywidendowe albo „premium kalendarz” (kalendarz to dane, bez rekomendacji). Konkurenci dają to samo za darmo (biznesradar.pl, stockwatch.pl, strefainwestorow.pl), więc popytu na płatną wersję nie zakładam.

**CFD ocenione osobno: odradzam.** Ostrzeżenie XTB na stronie programu: „77% rachunków inwestorów detalicznych odnotowuje straty pieniężne w wyniku handlu kontraktami CFD u niniejszego dostawcy CFD” [CP]. Dla Trading 212 serwisy trzecie podają 75–76%, czego nie potwierdziłem u źródła [WS]. Stawki za klienta CFD są kilka razy wyższe niż za konto akcji (Trading 212 w 2018 r.: 1 000 USD wobec ok. 100 USD [WS]), więc serwis zarabiałby głównie na produkcie, na którym większość klientów traci. To kłóci się z zasadą uczciwości projektu i podnosi ryzyko regulacyjne (reklama CFD, finfluencerzy). Wniosek: afiliacja tylko kont akcji i ETF, CFD poza ofertą.

## 4. Fosa danych (`dane/D-zrodla-danych.csv`)

- **Dywidendy (kwota na akcję, dzień dywidendy, dzień wypłaty):** pochodzą z raportów bieżących ESPI (system KNF) i EBI (GPW) oraz ze stron relacji inwestorskich, np. pzu.pl/relacje-inwestorskie/akcje-i-obligacje/dywidenda [S][WS]. Otwartej licencji nie ma. Kwoty i daty to fakty z raportu, więc da się je zebrać agentem i podlinkować raport. Tekstów raportów nie kopiujemy. Tę samą bazę mają już biznesradar.pl, stockwatch.pl, strefainwestorow.pl, bankier.pl i notowania.pb.pl [S].
- **Kursy GPW (do stopy dywidendy „z datą”):** gpw.pl/dane-rynkowe: „Jeśli firma zamierza udostępnić dane giełdowe opóźnione o 15 minut, zobowiązana jest uprzednio podpisać z GPW Umowę Licencyjną na Dane Rynkowe (jest to taka sama umowa jak w przypadku dystrybucji danych w czasie rzeczywistym)” [CP]. Cenniki są na 1.10.2026 i 1.01.2027 (PDF-ów nie odczytałem). Według Bankier.pl od 2018 r. roczna opłata za dane opóźnione wynosiła 24 tys. zł [WS]. Bez licencji stopa dywidendy może być tylko w kalkulatorze z ceną wpisaną przez użytkownika albo z ceną z raportu spółki.
- **Stooq:** regulaminu nie odczytałem (strona zwraca pusty HTML robotom, WebSearch nie pokazał treści) [CP][WS]. Kursy w Stooq pochodzą z GPW, więc ich publikacja i tak podlega licencji GPW. Do stron encji się nie nadaje.
- **KDPW:** jest instrukcja wypłaty dywidendy dla emitentów (kdpw.pl/uploads/attachments/wyplata-dywidendy.pdf), publicznej listy wypłat nie znalazłem [WS].
- **Kalkulatory (procent składany, wielkość pozycji, średnia cena zakupu, stopa dywidendy z ceną wpisaną ręcznie)** nie potrzebują żadnych danych. To jedyna część bez bariery licencyjnej, ale też bez fosy: robi je już 8 serwisów w top 10 [S].

## 5. Ryzyko i E-E-A-T

- **YMYL-finanse bez eksperta z twarzą.** W encjach i kalendarzu wygrywają portale z 2 000–20 000 domen linkujących i redakcjami [BL]. Brak autora z twarzą osłabia E-E-A-T. Co to częściowo zastąpi: każda dywidenda z linkiem do raportu ESPI lub strony IR i datą sprawdzenia; jawna metodologia i wzory kalkulatorów z testami; przegląd niezależny każdej serii; brak afiliacji CFD jako dowód neutralności. Wobec stockwatch.pl czy strefainwestorow.pl to nie wystarczy.
- **Rekomendacje (MAR, KNF):** kalendarz i edukacja są bezpieczne. Ryzykowne są rankingi „najlepsze spółki dywidendowe” (390/mies. [SV]) i „spółki z potencjałem”: łatwo przejść w rekomendację. Te frazy pomijamy albo dajemy tylko kryteria i dane.
- **AI Overview** jest w 6 z 6 SERP-ów; dla encji odpowiada wprost kwotą i datą [S].
- **Sezon i rok w frazie:** strony „[spółka] dywidenda 2026” tracą ruch po wypłacie i co roku trzeba je odnawiać [SV].
- **Zależność od jednego programu:** realny zarobek opiera się na XTB, którego stawek nie znamy.

## 6. Dopasowanie do profilu: 4 / 5

Plus: trading, inwestowanie i budowanie majątku to doświadczenie i hobby właściciela, UX/UI pomoże w kalkulatorach. Budżet na start nie kupi przewagi: CPC „konto maklerskie” 4,35 USD [SV] jest wyższe niż spodziewany przychód z kliknięcia, a licencja danych GPW to stały koszt roczny. Minus: zakaz twarzy i wideo w temacie, w którym rośnie YouTube (2 wyniki YouTube w „dywidendy 2026” [S]).

## 7. Rachunek po 12 miesiącach (`dane/D-rachunek.csv`)

Założenia: ruch rośnie liniowo do 12. miesiąca; 1,6 odsłony na wizytę; RPM, CTR, konwersje i stawka CPA brokera to **założenia, nie dane**. Popyt rdzenia i encji to ok. 208 450/mies.; wariant realny zakłada ok. 3,8% tego ruchu, ostrożny ok. 1%.

| | Ostrożny | Realny |
|---|---|---|
| Wizyty w 12. mies. | 2 000 | 8 000 |
| RPM reklam (założenie) | 10 zł | 25 zł |
| Broker: CTR / konwersja / CPA | 0,5% / 3% / 0 zł (stawka XTB niejawna) | 1% / 5% / 150 zł (założenie, tylko konta akcji i ETF) |
| TradingView: CTR / zakup / prowizja | 0,3% / 1% / 10 USD | 0,5% / 2% / 25 USD (stawki 10–400 USD [CP], kurs 3,8852 [TV]) |
| Przychód w 12. mies. | 34 zł | 998 zł |
| **Suma 12 mies.** | **223 zł** | **6 485 zł** |

W wariancie realnym 60% przychodu w 12. miesiącu to CPA brokera (4 zasilone konta × 150 zł). Bez potwierdzonej stawki XTB ten wariant jest życzeniem.

## Omijamy

Podatki od dywidend (podatek Belki, „kalkulator dywidendy netto” 90/mies., „podatek od dywidendy kalkulator” 140, „dywidenda podatek” 210), PIT-38 i PIT-8C („pit 38 dywidenda zagraniczna wzór” 140), IKE/IKZE jako przepisy i limity, przepisy MAR jako treść, wypłata dywidendy w spółce z o.o. (kalkulator EY, gofin.pl), wzory dokumentów, CFD i forex jako produkt afiliacyjny, rankingi „spółki z potencjałem”.

## Czego nie sprawdziłem

- Stawek CPA XTB i IBKR (wymagają rejestracji, której brief zabrania) oraz aktualnego programu Trading 212.
- Treści cenników GPW z 1.10.2026 i 1.01.2027 (PDF nie dał się odczytać) i regulaminu Stooq.
- RPM reklam dla polskich finansów.
- Licencji danych w widżetach TradingView.
- Przyczyny skoku „analiza techniczna” w 2026 r.

## Streszczenie

- **Werdykt:** NIE jako osobny serwis. Kalkulatory (procent składany, wielkość pozycji, średnia cena zakupu) mogą być modułem innej niszy finansowej, np. obligacji.
- **Wynik:** 2,45 / 5 (popyt 3, SERP 2,5, zarobek 2,5, fosa 2, ryzyko 2).
- **Dopasowanie do profilu:** 4 / 5.
- **Model zarobku:** afiliacja kont akcji/ETF (XTB, IBKR; stawki niejawne), TradingView 10–400 USD jednorazowo, reklamy. Bez CFD.
- **Rachunek 12 mies.:** ostrożnie 223 zł (34 zł/mies. na koniec), realnie 6 485 zł (998 zł/mies. na koniec).
- **Popyt:** rdzeń 124 800/mies. + ok. 83 650 encji, trend −15,3% r/r, pary rokowe −29,2%.
- **SERP:** kalendarz i encje zajęte przez portale z pełnymi bazami; słabe tylko kalkulatory (mediana 268 RD); AIO 6 z 6.
- **Dane:** dywidendy z ESPI są dostępne, ale nie dają przewagi; kursy GPW, także opóźnione, wymagają płatnej licencji.

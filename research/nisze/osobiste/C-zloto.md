# Złoto i srebro inwestycyjne: porównywarka cen dealerów, strony monet i sztabek, kalkulatory (18.10.2026)

Brief: `osobiste/BRIEF.md`, metoda: `../METODA.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie dane pobrano 18.10.2026.

**Znaczniki źródeł:**

- **[V]** `/v3/keywords_data/google_ads/search_volume/live` z `date_from 2024-10-01`, czyli 24 miesiące (10.2024–09.2026). Wolumen to średnia z ostatnich 12 mies. podana przez Google Ads, CPC w USD. Dane: `dane/C-zloto-frazy.csv`, `dane/C-zloto-popyt-podsumowanie.csv`, `dane/C-zloto-popyt-miesiecznie.csv`.
- **[S]** `/v3/serp/google/organic/live/advanced`, desktop, depth 10, `load_async_ai_overview`. Dane: `dane/C-zloto-serp-top10.csv`, `dane/C-zloto-serp-podsumowanie.csv`.
- **[B]** `/v3/backlinks/bulk_referring_domains/live` dla 49 domen (poziom domeny, nie podstrony).
- **[T]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (ETV organiczne w PL). Dane: `dane/C-zloto-konkurencja.csv`.
- **[P]** `/v3/on_page/content_parsing/live` (strony, których WebFetch nie otwiera: numitracker.com, metalsradar.com, spotprice.pl, tavex.pl/regulamin, api.nbp.pl, bullionvault.com, webepartners.pl).
- **[A]** `/v3/serp/google/ads_advertisers/live/advanced` (Google Ads Transparency).
- **[TV]** TradingView `OANDA:XAUUSD` i `OANDA:XAGUSD`, świece miesięczne 09.2024–10.2026. Dane: `dane/C-zloto-ceny-spot.csv`.
- **[W]** WebSearch. Programy: `dane/C-zloto-programy.csv`. Źródła danych i licencje: `dane/C-zloto-zrodla-danych.csv`. Rachunek: `dane/C-zloto-rachunek.csv`.

---

## Werdykt w skrócie

**NIE, wynik 2,40 / 5.** Dopasowanie do profilu właściciela: 4/5.

1. **Popyt jest duży, ale idzie za ceną złota.** 77 fraz (bez marek dealerów i prognoz) ma 1,41 mln wyszukiwań/mies. To 2 razy więcej niż rok wcześniej [V]. Szczyt był w 01–03.2026, gdy złoto doszło do 5 602 USD/oz, a srebro do 121,67 USD/oz [TV]. Od szczytu popyt spadł o 57%. Frazy zakupowe („gdzie kupić złoto” i podobne) są w 07–09.2026 o 46% niżej niż rok temu.
2. **Porównywarka już istnieje, i to trzy razy.** numitracker.com (ceny co 15 min, 1 800 domen linkujących, ok. 43 tys. wizyt/mies.), spotprice.pl (3 517 ofert od 55 dealerów, 6. miejsce na „cena złota”) i metalsradar.com (10 dealerów, 1 961 domen) [P][B][T]. AI Overview na „porównywarka cen złota” cytuje dwie z nich [S].
3. **Pieniądze są cienkie.** Potwierdziłem tylko dwa programy: Goldenmark w sieci webePartners (stawka niepubliczna) i program poleceń BullionVault (25% prowizji BullionVault, czyli ok. 0,125% wartości transakcji, tylko metal w skarbcu). CPC fraz o cenie: 0,13–0,24 USD [V]. Rachunek po 12 mies.: ok. 30 zł/mies. (ostrożnie) do ok. 600 zł/mies. (realnie).
4. **Danych dealerów nie da się dziś zdobyć czysto.** Brak publicznych API. Tavex w regulaminie zabrania kopiowania treści sklepu bez pisemnej zgody [P]. Zostaje feed afiliacyjny (jeden dealer) albo umowy z dealerami, a kontakt z firmami jest wykluczony.

Kalkulatory (uncja, gram, próba, wartość złota na cenie NBP) da się zrobić czysto. To jednak tylko ok. 14,6 tys. wyszukiwań/mies. [V]. Pasują jako dodatek do innego serwisu finansowego. Na osobny biznes to za mało.

---

## 1. Popyt i trend (24 mies.)

**Jak zbudowano:** 90 fraz w 8 grupach (cena/kurs, sztabki, monety, narzędzia, „gdzie kupić”, skup, marki dealerów, prognozy). 6 fraz Google Ads zwrócił bez danych: „filharmonik złoty cena”, „liść klonu srebrny”, „srebrny orzeł bielik”, „kalkulator wartości złota”, „spread złota”, „złota moneta 1 oz cena”. Zostały 84 frazy z danymi [V].

| Grupa | Fraz | Śr. mies. 10.2025–09.2026 | Śr. mies. rok wcześniej | Zmiana 24 mies. | 07–09.2026 vs 07–09.2025 | 09.2026 vs szczyt 01–03.2026 | Ważony CPC |
|---|---|---|---|---|---|---|---|
| Cena/kurs (rdzeń) | 22 | 1 217 412 | 560 280 | +117% | +56,0% | −57,6% | 0,171 USD |
| Sztabki (encje) | 11 | 93 723 | 66 651 | +41% | +10,5% | −46,1% | 0,40 USD |
| Monety (encje) | 24 | 49 940 | 34 794 | +44% | +0,6% | −51,9% | 0,49 USD |
| Skup | 4 | 28 988 | 20 539 | +41% | −20,3% | −65,7% | 0,35 USD |
| Narzędzia/przeliczniki | 10 | 14 611 | 11 467 | +27% | −9,4% | −39,7% | 0,29 USD |
| Gdzie kupić / porównanie | 6 | 7 912 | 6 759 | +17% | **−46,0%** | −69,6% | 0,62 USD |
| **Razem (bez marek i prognoz)** | 77 | **1 412 585** | 700 490 | **+102%** | **+44,5%** | **−56,9%** | 0,20 USD |
| Marki dealerów (nawigacja) | 6 | 485 017 | 292 025 | +66% | +3,6% | −56,9% | 0,22 USD |

**Sezonowość:** popyt rośnie i spada razem z ceną kruszcu, kalendarz ma mały wpływ. Suma bez marek: 10.2024 679 340 → szczyt 03.2026 2 553 060 → 09.2026 969 960 (`dane/C-zloto-popyt-miesiecznie.csv`) [V]. Najsłabszy miesiąc ostatnich 12: 07.2026 (887 370).

**Złoto bije rekordy?** Biło do stycznia 2026 [TV]:

| | 09.2024 | Szczyt | 16.10.2026 | Od szczytu |
|---|---|---|---|---|
| Złoto XAU/USD | 2 634,69 | 5 602,23 (01.2026) | 4 165,42 | −25,6% |
| Srebro XAG/USD | 31,16 | 121,67 (01.2026) | 56,97 | −53,2% |

Wykres wyszukiwań idzie za tą krzywą: „kurs srebra” miał 301 000 w 01.2026 i 49 500 w 09.2026 [V]. Ruch takiego serwisu rośnie przy rekordach i spada przy korekcie.

**Największe frazy [V]:** „kurs złota” 550 000 (CPC 0,14 USD), „cena złota” 368 000 (0,18), „kurs srebra” 110 000, „cena złota wykres” 90 500, „cena srebra” 74 000, „sztabki złota” 49 500, „złoto inwestycyjne” 27 100 (0,65), „sztabka złota 1g” 14 800, „monety bulionowe” 14 800, „cena uncji złota” 14 800. Frazy o cenie to ok. 86% popytu. Ich intencja to „sprawdź kurs”; zakup to mały margines.

**Encje: monety i sztabki [V]:**
- Monety: Krugerrand 8 100 + „krugerrand 1 oz” 5 400 + „krugerrand cena” 4 400; „britannia 1 oz” 1 600; „kangur 1 oz” 880; „maple leaf” 720; „liść klonu 1 oz” 590; Wiedeński Filharmonik 390 („filharmonik” 260, „filharmonik 1 oz” 140); Orzeł Bielik 320; „kanadyjski liść klonu” 20; „american eagle moneta” 70.
- Sztabki: 1 g 14 800; 10 g 6 600; 5 g 6 600; 20 g 1 900; 50 g 1 600; „sztabka złota 100g cena” 880; „sztabka złota 1 oz” 390; „sztabka srebra 1kg” 2 900; „sztabka srebra 100g” 1 900.
- Wniosek: poza Krugerrandem i małymi sztabkami encje są małe. Orzeł Bielik i Liść Klonu po polsku prawie nikt nie szuka.

**Narzędzia [V]:** „ile kosztuje gram złota 585” 5 400, „próba złota 585” 2 900, „uncja trojańska” 1 300, „ile waży uncja złota” 1 300, „złoto 585 cena za gram” 880, „kalkulator złota” 720, „próba złota 750” 720, „uncja ile gram” 590. Fraza „porównywarka cen złota” ma 390/mies. przy najwyższym CPC w zestawie (1,31 USD).

---

## 2. Kto wygrywa: SERP (7 fraz)

Pełne dane: `dane/C-zloto-serp-top10.csv`, `dane/C-zloto-serp-podsumowanie.csv` [S][B].

| Fraza | Wol. | Typ | AIO | Mediana domen linkujących | Wyniki <50 domen | Fora/FB/Allegro | Stare <2023 | Dealerzy w top 10 | Kto wygrywa |
|---|---|---|---|---|---|---|---|---|---|
| cena złota | 368 000 | hub cen | nie | 367 | 0 | 0 | 0 | 4 | idfmetale.pl, goldco.pl, bullionvault, tavex, goldtrader.pl, **spotprice.pl (6.)** |
| porównywarka cen złota | 390 | narzędzie | **tak** | 1 800 | 0 | 1 | 0 | 4 | metalelokacyjne.pl, NBP, **metalsradar.com, numitracker.com** |
| krugerrand | 8 100 | encja | nie | 353 | 0 | 1 | 3 | 9 | sklepy dealerów + blok Google Shopping (16 722 zł za 1 oz) |
| kalkulator złota | 720 | narzędzie | **tak** | 83 | 3 | 0 | 0 | 4 | **liczgrupa.pl (65 domen)**, metalmarket.eu, bullionvault, mennicaszczepanska.pl (9 domen) |
| sztabka złota 1g | 14 800 | encja | nie | 450,5 | 0 | 0 | 0 | 7 | sklepy dealerów, 2× Ceneo, numitracker.com |
| ile kosztuje gram złota 585 | 5 400 | pytanie/kalkulator | nie | 847,5 | 1 | 3 | 0 | 2 | kantory, skupy, 2 grupy FB, Allegro |
| gdzie kupić złoto | 6 600 | gdzie kupić | nie | 773 | 1 | 0 | 1 | 6 | dealerzy, local pack, marciniwuc.com (ekspert z twarzą) |

**Wnioski:**
- **Encje wygrywają sklepy.** Na „krugerrand” 9 z 10 wyników to dealerzy, a nad nimi stoi blok produktów Google Shopping z cenami. Na „sztabka złota 1g” 7 z 10 to dealerzy. Strona encji bez ceny w koszyku przegrywa z kartą produktu.
- **Head terms o cenie są zajęte, ale nie betonowe.** Mediana ok. 370 domen linkujących, za to spotprice.pl wszedł na 6. miejsce „cena złota” ze 142 domenami [B]. Okno istniało, i ktoś już je wykorzystał.
- **Najsłabszy SERP to kalkulatory:** 3 z 9 wyników mają poniżej 50 domen. Popyt jest tu jednak mały (720 + frazy o próbie).
- Fora i stare wpisy: tylko na „ile kosztuje gram złota 585” (2 grupy FB, Allegro) i 3 stare wpisy na „krugerrand” (2014, 2018, 2022).

**Porównywarki, które już działają [P][B][T]:**

| Serwis | Domeny linkujące | ETV PL/mies. | Co mówi o sobie |
|---|---|---|---|
| numitracker.com | 1 800 | 43 004 | „odświeżamy je co 15 minut”; „Ceny pobieramy automatycznie, bezpośrednio ze stron internetowych sprzedawców”; alerty cenowe, premia ponad spot, weryfikacja NIP/REGON, działa od 2023 |
| spotprice.pl | 142 | 13 962 | „3517 ofert od 55 dealerów”; czas ostatniego odczytu przy każdej ofercie; marża vs spot; cena z dostawą |
| metalsradar.com | 1 961 | 585 | „Regularnie pobieramy ceny ze sklepów 10 dealerów”; „Nikt nie płaci za wyższą pozycję” |

Do tego Ceneo ma karty sztabek, a liczgrupa.pl (25 394 ETV) i goldtrader.pl (7 453) robią kalkulatory i strony cen [T]. Pomysł z briefu (ceny ze źródłem i godziną, spread vs spot) spotprice.pl realizuje dziś niemal 1:1.

**Dealerzy (dla skali) [B][T][A]:** tavex.pl 433 870 ETV / 1 435 domen; goldenmark.com 257 655 / 3 100 (ok. 2 000 reklam w Google Ads); mennica.com.pl 209 139 / 2 234; mennicaskarbowa.pl 128 620 / 809 (ok. 700 reklam); mennicakapitalowa.pl 63 336 / 466. Tavex ma ok. 200 reklam w PL.

---

## 3. AI Overview

AIO wystąpił w **2 z 7** SERP-ów: „porównywarka cen złota” i „kalkulator złota” [S]. Na frazach o cenie i encjach go nie było.

AIO cytuje małe serwisy: na „kalkulator złota” mennicaszczepanska.pl (9 domen linkujących), skup.sefina.pl (7) i liczgrupa.pl (65) [S][B]. Na „porównywarka cen złota” wymienia z nazwy NumiTracker i Metals Radar. Nowy serwis mógłby tam trafić, ale miejsce dla porównywarek już ktoś zajął.

---

## 4. Dane: ceny dealerów i cena spot

### Ceny dealerów

| Droga | Czy legalnie | Czy technicznie | Wniosek |
|---|---|---|---|
| Publiczne API dealerów | nie znalazłem żadnego (Tavex, Goldenmark, Mennica Skarbowa) [W] | — | odpada |
| Scraping stron (tak robią numitracker i spotprice) | Tavex: „Kopiowanie i rozpowszechnianie wszelkich treści zawartych w Sklepie Internetowym … bez pisemnej zgody Tavex, jest zabronione” [P]; regulaminów innych dealerów nie sprawdziłem; dochodzi ochrona baz danych | tak | wbrew zasadzie projektu, odpada |
| Feed afiliacyjny w sieci | tak, w granicach programu | tak, po rejestracji wydawcy | obejmuje tylko dealerów z programem; potwierdzony 1 (Goldenmark w webePartners) |
| Umowa lub feed od dealera | tak | tak | wymaga kontaktu z firmami, a to dziś wykluczone |

Bez pełnych cen porównywarka z jednym dealerem nie jest porównywarką. To główna przeszkoda tego pomysłu.

### Cena spot i ceny referencyjne

- **NBP Web API** (`https://api.nbp.pl/api/cenyzlota/`): „wyliczona w NBP cena 1 g złota (w próbie 1000)”, raz dziennie, archiwum od 2 stycznia 2013 r., do 93 dni na zapytanie, JSON/XML bez klucza [P]. Na stronie API nie ma licencji, jest tylko „Copyright © 2024 Narodowy Bank Polski … Wszystkie prawa zastrzeżone”. Kalkulatory w top 10 (np. liczgrupa.pl) korzystają z ceny NBP. **Do decyzji właściciela:** czy brak wyraźnej licencji wystarczy przy podaniu źródła. NBP podaje też kurs USD/PLN (tabela A), więc można liczyć ceny w zł.
- **Ograniczenie NBP:** to jedna cena dziennie. Spreadu dealera względem ceny bieżącej z nią nie policzysz uczciwie w ciągu dnia.
- **LBMA Gold/Silver Price:** płatne. „Any party using the LBMA Gold Price for valuation and pricing activities requires a usage licence with IBA”. Publicznie cena jest dostępna z opóźnieniem do północy czasu Londynu [W]. Stawek nie znalazłem.
- **Spot na żywo (XAU/USD):** wymaga dostawcy danych rynkowych. Warunków i cen konkretnych dostawców nie sprawdzałem.
- **Dane o monetach** (waga, próba, średnica, mennica) to fakty ze stron mennic emitentów. Zdjęć nie wolno kopiować bez licencji.

---

## 5. Zarobek

**Programy partnerskie** (`dane/C-zloto-programy.csv`):

| Program | Status | Stawka | Cookie / okres |
|---|---|---|---|
| Goldenmark (webePartners) | potwierdzony: „Generuj linki afiliacyjne … i zarabiaj prowizję w programie partnerskim Goldenmark” [P] | **niepubliczna** (widać po rejestracji) | niepubliczne |
| BullionVault | potwierdzony na stronie programu [P] | 25% prowizji BullionVault (z mark-up/mark-down) + 6,25% z drugiego poziomu; prowizja BullionVault to 0,50% poniżej 75 000 USD obrotu rocznie [W], więc dla nas ok. **0,125% obrotu** | cookie 2 mies., prowizja przez 2 lata od założenia konta; „Coin and bar sales are excluded” |
| Tavex, Mennica Skarbowa, Goldsaver, Metal Market, StoneX | programu nie znalazłem [W] | — | — |
| Mennica Polska | niepotwierdzony (serwis z kodami wspomina „opcje cashback” bez stawki) | — | — |

**Marże są małe, więc prowizje też.** Najtańsza uncja złota u dealerów kosztowała 18.10.2026 marżę +1,2% (Krugerrand, 16 381,37 zł) do +1,6% nad wartość kruszcu, a sztabka 100 g +0,9% [P, spotprice.pl]. Z takiej marży dealer nie odda kilku procent partnerowi. Srebro ma marże +15–19%, więc tam prowizja mogłaby być wyższa, ale jej nie znamy.

**Reklamy:** CPC fraz o cenie 0,13–0,24 USD, ważony CPC rdzenia 0,171 USD [V]. Reklamodawcy to sami dealerzy (Goldenmark ok. 2 000 reklam, Mennica Skarbowa ok. 700, Tavex ok. 200) [A].

**Leady i płatne profile:** numitracker.com sprzedaje dealerom „profil zweryfikowanego sprzedawcy” [P]. U nas wymagałoby to kontaktu z firmami, więc tylko na zapytania przychodzące i po decyzji właściciela.

**CFD na złoto (oceniam osobno, jak każe brief):** frazy „kurs złota” przyciągają brokerów CFD. XTB podaje: „77% rachunków inwestorów detalicznych odnotowuje straty pieniężne w wyniku handlu kontraktami CFD u niniejszego dostawcy CFD” (starsze strony XTB: 74%) [W]. Freenance cytuje zakres 76–90% dla rynku. **Rekomendacja: nie.** Taka afiliacja kłóci się z obietnicą „uczciwej porównywarki” i podnosi ryzyko YMYL.

---

## 6. Ryzyko, YMYL i „Omijamy”

- **YMYL-finanse bez eksperta z twarzą.** Na „gdzie kupić złoto” w top 10 jest marciniwuc.com (ekspert z twarzą, 2 720 domen) i dealerzy z wieloletnią historią [S][B]. Zamiast eksperta: cena NBP jako źródło, jawna metodologia (skąd cena, kiedy odczyt, jak liczony spread), data przy każdej liczbie, ranking tylko po cenie, przegląd niezależny i jawne oznaczenie linków partnerskich. To pomoże przy kalkulatorach. Przy porównywarce i tak przegrywa z pełnością danych konkurencji.
- **Ryzyko danych:** nieaktualna cena przy produkcie za 16 000 zł wprowadza w błąd. Porównywarka musi odświeżać ceny często, a my nie mamy legalnego źródła.
- **Ryzyko cyklu:** ruch spadł o 57% od szczytu w pół roku [V]. Przychód z ruchu zależy od tego, czy złoto znów pobije rekord.
- **Zależność od jednego programu:** sklepowo tylko Goldenmark.
- **Prawo:** scraping wbrew regulaminom i ochrona baz danych; licencja NBP do potwierdzenia.

**Omijamy (treści prawne, podatkowe i rekomendacje):**
- VAT na srebro i zwolnienie złota inwestycyjnego z VAT.
- Podatek przy sprzedaży złota i srebra, PIT, terminy, ulgi.
- Przepisy o obrocie: limity płatności gotówką, identyfikacja klienta (AML), przepisy o przechowywaniu.
- Prognozy cen („cena złota prognoza” 2 900/mies. [V]), „czy warto kupić złoto”, „złoto czy srebro” jako rada inwestycyjna.
- Afiliacja CFD i dźwignia na złocie.
- Wzory umów sprzedaży złota.

---

## 7. Ocena

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 4 | 1,41 mln/mies., +102% w 24 mies., +44,5% r/r; minus: −57% od szczytu, frazy zakupowe −46% r/r, 86% to „sprawdź kurs” |
| Słabość SERP | 25% | 2 | 3 porównywarki już działają (2 z ok. 1 800–1 960 domenami); encje wygrywają sklepy i Google Shopping; tylko 5 z 67 wyników ma <50 domen |
| Zarobek | 25% | 2 | 1 program sklepowy ze stawką niepubliczną, BullionVault ok. 0,125% obrotu; marże 1 oz złota 1,2–1,6%; CPC rdzenia 0,17 USD |
| Fosa danych / narzędzia | 15% | 2 | NBP raz dziennie, bez wyraźnej licencji; LBMA płatne; cen dealerów nie da się pobrać czysto; konkurent ma 55 dealerów |
| Niskie ryzyko | 15% | 2 | YMYL-finanse bez eksperta, ryzyko scrapingu, cykl rynku, AIO 2 z 7 |
| **Wynik ważony** | | **2,40** | 0,8 + 0,5 + 0,5 + 0,3 + 0,3 |

Dla porównania: numizmatyka w `../RANKING.md` ma 2,95.

---

## 8. Dopasowanie do profilu właściciela: 4/5

- **Pasuje:** inwestowanie, trading i obligacje to ten sam świat; UX/UI to przewaga przy porównywarce i kalkulatorach; model jest pasywny (dane, bez twarzy, bez wideo).
- **Nie pasuje:** przewaga budżetu niewiele daje, bo barierą jest dostęp do danych; jedyna czysta droga do cen (umowy z dealerami) wymaga kontaktu z firmami. Zakup gotowego serwisu (np. spotprice.pl) to decyzja właściciela; nie sprawdzałem, czy jest na sprzedaż, i nie kontaktowałem się z nikim.

---

## 9. Rachunek po 12 mies.

Wszystkie wejścia poza stawką BullionVault to **założenia**. Pełne wyliczenie: `dane/C-zloto-rachunek.csv`, skrypt `rachunek.py` w scratchpadzie.

| Założenie (12. miesiąc) | Ostrożnie | Realnie | Podstawa |
|---|---|---|---|
| Wizyty/mies. | 4 000 | 15 000 | spotprice.pl ma ETV 13 962 przy 142 domenach [T][B] |
| Odsłony na wizytę | 1,5 | 1,5 | założenie |
| Przychód z reklam na 1000 odsłon | 5 zł | 10 zł | założenie; CPC rdzenia 0,13–0,24 USD [V] |
| Kliknięcia do sklepu | 5% | 10% | założenie |
| Część kliknięć do Goldenmark | 10% | 20% | założenie; ranking tylko po cenie, 55 dealerów na rynku |
| Konwersja w sklepie | 2% | 3% | założenie |
| Średnie zamówienie | 3 000 zł | 6 000 zł | założenie; 1 g od ok. 571 zł, 1 oz od ok. 16 381 zł |
| Prowizja Goldenmark | 0,3% | 0,7% | **niepubliczna**, założenie |
| Nowe konta BullionVault / wizytę | 0,02% | 0,05% | założenie |
| Roczny obrót polecanego | 8 000 zł | 15 000 zł | założenie; prowizja 0,125% [P][W] |

| Wynik w 12. miesiącu | Ostrożnie | Realnie |
|---|---|---|
| Reklamy | 30 zł | 225 zł |
| Goldenmark | 4 zł (0,4 zamówienia) | 378 zł (9 zamówień) |
| BullionVault | 1 zł | 12 zł |
| **Razem** | **ok. 34 zł/mies.** | **ok. 615 zł/mies.** |

Nawet podwojenie ruchu w realnym wariancie daje ok. 1 200 zł/mies. To za mało na serwis, który musi codziennie odświeżać ceny i nie ma czystego źródła danych.

---

## 10. Co musiałoby się zmienić, żeby wrócić do tematu

1. Dealerzy dają legalny feed cen (umowy albo kilka programów w sieciach afiliacyjnych z feedem produktów).
2. Właściciel potwierdza, że cenę NBP wolno używać komercyjnie z podaniem źródła.
3. Złoto znów bije rekord i popyt wraca. Na tym nie da się planować.

Rozsądna wersja minimum: 5–8 kalkulatorów (uncja ↔ gram, próba 333/585/750/999, wartość złota i srebra na cenie NBP, różnica ceny sprzedaży i skupu podanej przez użytkownika) jako dział innego serwisu finansowego. Popyt ok. 14,6 tys./mies., SERP najsłabszy w niszy (mediana 83 domeny), AIO cytuje małe serwisy.

## Czego nie sprawdziłem

- Stawki i cookie Goldenmark (wymaga rejestracji w webePartners).
- Regulaminów dealerów poza Tavex w kwestii pobierania cen.
- Warunków i cen dostawców spotu na żywo oraz stawek licencji LBMA/IBA.
- Wieku spotprice.pl i tego, jak zarabiają porównywarki (w linkach na stronie głównej spotprice.pl nie widać parametrów partnerskich).
- Zasad dane.gov.pl dla zbiorów NBP (WebSearch nic nie zwrócił).

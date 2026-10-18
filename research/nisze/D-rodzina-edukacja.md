# Nisze D: rodzina i edukacja (18.10.2026)

Metoda: `research/nisze/METODA.md`. Wszystkie dane pobrano 18.10.2026. Rynek: Polska (location_code 2616, język pl).

Skróty źródeł (wszystkie DataForSEO, 18.10.2026):

- **[SV]** `/v3/keywords_data/google_ads/search_volume/live`, 229 fraz w jednym zadaniu, miesiące 2025-07 do 2026-09. Wolumen to średnia miesięczna z 12 miesięcy, CPC w USD. Google Ads zaokrągla wolumeny do przedziałów, więc trend r/r jest przybliżony.
- **[KS]** `/v3/dataforseo_labs/google/keyword_suggestions/live` (rozszerzenie fraz).
- **[SERP]** `/v3/serp/google/organic/live/advanced`, desktop, depth 10, z ładowaniem AI Overview.
- **[BL]** `/v3/backlinks/bulk_referring_domains/live` (liczba domen linkujących do całej domeny).
- **[TE]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (szacowany ruch organiczny, ETV).

Surowe dane: `dane/D-wolumeny.csv` [SV], `dane/D-rozszerzenia.csv` [KS], `dane/D-serp.csv` i `dane/D-serp-mediany.csv` [SERP+BL], `dane/D-backlinki.csv` [BL].

## Tabela ocen

Skala 1–5, 5 = najlepiej. Wagi z metody: popyt 20%, słabość SERP 25%, zarobek 25%, fosa 15%, niskie ryzyko 15%.

| Nisza | Popyt i trend | Słabość SERP | Zarobek | Fosa danych / narzędzia | Niskie ryzyko | **Wynik ważony** |
|---|---|---|---|---|---|---|
| 4. Zwierzęta domowe (rasy, karmy, koszty) | 4 | 3,5 | 3,5 | 2,5 | 2,5 | **3,30** |
| 5. Zabawki i LEGO | 4 | 2,5 | 3 | 3 | 4 | **3,23** |
| 3. Wesele | 3 | 3 | 3 | 2 | 3 | **2,85** |
| 2. Studia | 3 | 2 | 3 | 3 | 3 | **2,75** |
| 1. Rekrutacja do szkół średnich | 3 | 2 | 2 | 3 | 3 | **2,50** |

Zbiorcze liczby, z których wynikają oceny:

| Nisza | Suma wolumenu rdzenia [SV] | Rdzeń bez fraz nawigacyjnych i produktowych [SV] | Trend r/r (VII–IX 2026 vs VII–IX 2025) [SV] | Mediana median domen linkujących w 5 SERP [SERP+BL] | AI Overview [SERP] | Wyniki sprzed 2023 / fora w top 10 [SERP] | Średni CPC ważony wolumenem [SV] |
|---|---|---|---|---|---|---|---|
| 1. Szkoły średnie | 131 640 (39 fraz) | 40 140 | −27,5% | 1 643 | 5 z 5 | 1 / 0 | 0,93 USD |
| 2. Studia | 203 250 (39 fraz) | 30 450 | +14,0% (rdzeń −14,6%) | 539,5 | 4 z 5 | 1 / 3 | 1,79 USD |
| 3. Wesele | 370 960 (50 fraz) | 113 260 | −7,9% | 345 | 4 z 5 | 6 / 3 | 0,74 USD |
| 4. Zwierzęta | 1 134 930 (54 frazy, 4 bez danych) | 903 630 | −12,3% | 405 | 3 z 5 | 9 / 1 | 0,34 USD |
| 5. LEGO i zabawki | 1 689 690 (47 fraz, 2 bez danych) | 1 034 090 | −2,8% | 6 880,5 | 0 z 5 | 1 / 4 | 0,15 USD |

„Rdzeń bez fraz nawigacyjnych” wyklucza frazy, na które nowy serwis nie ma szans albo które są czysto produktowe (np. „egzamin ósmoklasisty”, „studia online”, „irk uw”, „weterynarz”, „lego”, „cobi”, „pierścionek zaręczynowy”). Wykluczone frazy dla każdej niszy podaję w jej sekcji.

---

## 1. Rekrutacja do szkół średnich (kalkulator punktów, progi, terminy)

### Popyt

- Suma rdzenia: 131 640 wyszukiwań miesięcznie z 39 fraz; bez „egzamin ósmoklasisty”, „arkusze” i „wyniki” zostaje 40 140 [SV].
- Trend r/r: −27,5% (VII–IX 2026: 255 750, VII–IX 2025: 352 860) [SV]. Przykład: „kalkulator punktów do liceum” w lipcu 2025 miał 40 500, w lipcu 2026 33 100 [SV].
- Sezon: szczyt w maju 2026 (435 640), dołek w sierpniu 2026 (30 260). Różnica ponad 14 razy [SV].
- Top frazy [SV, KS]:
  - egzamin ósmoklasisty: 74 000 (CPC 1,05 USD)
  - kalkulator punktów do liceum: 14 800 (CPC 0,91 USD)
  - kalkulator punktów: 14 800 [KS]
  - arkusze egzaminu ósmoklasisty: 12 100
  - rekrutacja do szkół ponadpodstawowych: 6 600 (CPC 1,23 USD)
  - kalkulator punktów e8: 5 400 [KS]
  - szkoła branżowa: 4 400; test predyspozycji zawodowych: 2 900
  - progi punktowe: 1 300; progi punktowe licea warszawa 2026: 720 [KS]; kraków 2026: 390; wrocław, gdańsk, poznań 2026: po 320 [KS]
- Długi ogon: 5 285 fraz zawierających „progi punktowe” (szkoły i uczelnie razem), top 300 to 48 330 wyszukiwań [KS].

### SERP

| Fraza | Wolumen | AIO | Mediana domen linkujących | Wyniki <50 domen | Kto wygrywa |
|---|---|---|---|---|---|
| kalkulator punktów do liceum (narzędzie) | 14 800 | tak | 944 | 0 | opinieouczelniach.pl, małe kalkulatory, strony miast |
| progi punktowe licea warszawa 2026 (hub miasta) | 720 | tak | 1 643 | 2 | PDF urzędu, waszaedukacja.pl, otouczelnie.pl, licea-progi.pl, dostanesie.pl, rankingedukacji.pl |
| rekrutacja do szkół ponadpodstawowych | 6 600 | tak | 637 | 1 | 8 z 9 to systemy naboru i urzędy |
| ile punktów do liceum | 720 | tak | 1 717 | 2 | portale parentingowe, licea-progi.pl |
| progi punktowe technikum (encja szkoły) | 70 | tak | 1 717 | 1 | waszaedukacja.pl ×3, otouczelnie.pl ×4 (strony pojedynczych szkół) |

Źródło: [SERP], [BL], 18.10.2026.

- Rynek programmatic jest zajęty. Szacowany ruch [TE]: otouczelnie.pl 740 638 (16 209 fraz), waszaedukacja.pl 340 150, takzdam.pl 125 570 (153 frazy, głównie kalkulator), dostanesie.pl 32 519, rankingedukacji.pl 21 743.
- Nowe serwisy wchodzą szybko: licea-progi.pl ma 3 domeny linkujące [BL] i już jest w top 10 dwóch fraz. To dowód, że SERP przyjmuje nowych, ale też że konkurencja rośnie.
- AI Overview w 5 z 5 SERP. Cytuje małe serwisy (takzdam.pl, egzaminzcnb.pl, licea-progi.pl, rankingedukacji.pl) [SERP].
- Stare wyniki: 1 (zestawienie cdzdm.pl z danymi z naboru 2017/2018). Fora: 0 [SERP].

### Zarobek

- CPC niskie: 0,91 USD dla kalkulatora, 1,23 USD dla rekrutacji [SV].
- Programy partnerskie: nie znaleziono polskiego programu dla kursów E8 ani korepetycji (nie sprawdzono szczegółowo). W SERP pojawiają się firmy kursowe (egzaminzcnb.pl, korepetycje-swb.com), co sugeruje możliwą współpracę, ale bez potwierdzenia.
- Własny produkt: trudny. Odbiorca (rodzic ósmoklasisty) szuka raz w życiu dziecka.
- Ocena: 2.

### Fosa danych

- RSPO (rejestr szkół): wyszukiwarka rspo.gov.pl z eksportem CSV, API api.rspo.gov.pl dostępne na wniosek e-mailem z akceptacją regulaminu ([cie.gov.pl/rspo](https://cie.gov.pl/rspo/), [api.rspo.gov.pl](https://api.rspo.gov.pl/)). Zbiór na dane.gov.pl (nr 839) wskazuje [wiki OpenStreetMap](https://wiki.openstreetmap.org/wiki/Pl:Rejestr_Szk%C3%B3%C5%82_i_Plac%C3%B3wek_O%C5%9Bwiatowych); licencji nie potwierdzono dziś, bo dane.gov.pl jest zablokowane przez proxy.
- Progi punktowe: miasta publikują je same, np. Warszawa „Minimalna liczba punktów 2026” w PDF i Excelu ([edukacja.um.warszawa.pl](https://edukacja.um.warszawa.pl/-/minimalna-liczba-punktow-1), widoczne w AIO [SERP]). Każde miasto ma inny format.
- Wyniki egzaminu per szkoła (CKE/OKE): nie potwierdzono, czy są do pobrania jako zbiór (wyszukiwanie znalazło tylko komunikaty i raporty regionalne).
- Ocena: 3. Dane istnieją, ale konkurenci mają te same.

### Ryzyko

- YMYL: brak. Treści prawne: niewiele (zasady rekrutacji wynikają z rozporządzeń, ale to opis procedury).
- AIO w 5 z 5 SERP, ekstremalna sezonowość (maj–lipiec), spadek r/r.
- Ocena: 3.

### Pomysł na serwis

Kalkulator punktów E8 z porównaniem do progów wybranej klasy. Strony encji: każda szkoła z progami z 3 lat (dane miast) i adresem z RSPO, huby per miasto i typ szkoły. Kalendarz terminów rekrutacji per województwo.

### Werdykt

**Nie.** Popyt jest, ale trzy duże serwisy programmatic (otouczelnie.pl, waszaedukacja.pl, dostanesie.pl) i dwa nowe (licea-progi.pl, rankingedukacji.pl) robią dokładnie ten pomysł. Zarobek słaby, ruch skupiony w 3 miesiącach roku.

---

## 2. Studia (progi, kierunki, kalkulatory per uczelnia, koszty)

### Popyt

- Suma rdzenia: 203 250 z 39 fraz [SV]. Bez fraz nawigacyjnych i ofertowych („studia online”, „studia podyplomowe”, „studia zaoczne”, „irk uw”, „wyniki matur”) zostaje 30 450.
- Trend r/r: +14,0% (659 400 → 751 440), ale wzrost robi „studia online” (lipiec 74 000 → 110 000). Rdzeń bez tych fraz: −14,6% [SV].
- Sezon: szczyt w lipcu 2026 (404 750), dołek w grudniu 2025 (117 360) [SV].
- Top frazy [SV, KS]:
  - studia online: 110 000 (CPC 1,44 USD)
  - studia podyplomowe: 22 200 (CPC 3,13 USD)
  - wyniki matur: 18 100; irk uw: 18 100
  - kierunki studiów: 8 100
  - kalkulator punktów na studia: 8 100 [KS]
  - studia psychologia: 4 400 (CPC 4,28 USD); studia zaoczne: 4 400 (CPC 3,10 USD); studia informatyka: 1 000 (CPC 3,45 USD)
  - agh progi punktowe: 1 900 [KS]; uw kalkulator punktów: 720 [KS]; agh kalkulator punktów: 720 [KS]
  - ile kosztują studia: 590; ile kosztuje akademik: 320
- Kalkulator per uczelnia: każda uczelnia ma 140–720 wyszukiwań miesięcznie (np. sggw 390, wat 390, uj 390, sgh 320, pwr 260) [KS]. 217 fraz z „kalkulator punktów”, razem 63 730 (łącznie ze szkołami średnimi) [KS].

### SERP

| Fraza | Wolumen | AIO | Mediana domen linkujących | Wyniki <50 domen | Kto wygrywa |
|---|---|---|---|---|---|
| kalkulator punktów na studia (narzędzie) | 8 100 | tak | 944 | 0 | otouczelnie.pl ×4 (strony uczelni z kalkulatorem) |
| progi punktowe agh (encja uczelni) | 880 | tak | 520,5 | 0 | strony AGH ×4, otouczelnie.pl |
| ile kosztują studia | 590 | tak | 377 | 0 | cus.slupsk.pl ×3, uczelnia prywatna, edukacja.rp.pl (2022) |
| progi punktowe lekarski 2026 | 480 | tak | 590 | 0 | namedycyne.pl ×2, reddit, facebook |
| studia podyplomowe | 22 200 | nie | 539,5 | 2 | same uczelnie, local pack |

Źródło: [SERP], [BL], 18.10.2026.

- otouczelnie.pl ma programmatic kalkulator dla każdej uczelni [SERP]. Ruch 740 638 [TE].
- Uczelnie same publikują progi i kalkulatory (AGH 4 z 8 wyników) [SERP].
- AI Overview w 4 z 5 SERP, poda wzór rekrutacyjny i progi wprost (np. wzór AGH) [SERP].

### Zarobek

- Najwyższe CPC w całym badaniu: studia psychologia 4,28 USD, studia informatyka 3,45 USD, studia podyplomowe 3,13 USD, studia zaoczne 3,10 USD [SV]. To znaczy, że uczelnie (głównie prywatne) płacą za klienta.
- Programy CPL dla uczelni: wyszukiwanie nie znalazło polskiego programu afiliacyjnego dla studiów (18.10.2026). Sprzedaż leadów wymagałaby bezpośrednich umów z uczelniami, a zimny kontakt z firmami jest zakazany w zasadach projektu.
- Ocena: 3.

### Fosa danych

- ELA (ekonomiczne losy absolwentów, [ela.nauka.gov.pl](https://ela.nauka.gov.pl)): dane o zarobkach absolwentów per kierunek i uczelnia, edycja 11 z 17.06.2026 ([gov.pl/web/nauka](https://www.gov.pl/web/nauka/rzucili-studia-i-co-dalej-nowe-dane-w-systemie-ela-juz-dostepne)). Licencji surowych danych nie potwierdzono.
- POL-on / RAD-on (kierunki, uczelnie): nie sprawdzono dziś.
- Progi i wzory rekrutacyjne: publikują uczelnie w uchwałach i na stronach rekrutacji, trzeba je zbierać ręcznie co roku.
- Ocena: 3. ELA to dobra fosa (zarobki po kierunku), jeśli licencja pozwoli.

### Ryzyko

- YMYL: lekko (decyzje życiowe, finanse studenta), bez zdrowia.
- AIO w 4 z 5 SERP, sezon lipcowy, silny lider programmatic.
- Ocena: 3.

### Pomysł na serwis

Strony encji „kierunek × uczelnia” z progiem z 3 lat, wzorem rekrutacyjnym i zarobkami absolwentów z ELA. Kalkulator punktów, który od razu pokazuje, gdzie wynik wystarczał rok temu. Huby per miasto z kosztami życia studenta (akademiki z cenników uczelni).

### Werdykt

**Raczej nie jako samodzielny serwis.** otouczelnie.pl ma już ten produkt i ogromny ruch. Wyróżnikiem mogłoby być połączenie progów z zarobkami z ELA, ale to wymaga potwierdzenia licencji ELA i nie rozwiązuje problemu zarobku bez leadów.

---

## 3. Wesele (koszt, kalkulator, sale, checklisty)

### Popyt

- Suma rdzenia: 370 960 z 50 fraz [SV]. Bez fraz produktowych (pierścionek, suknie, obrączki, zaproszenia, „wesele”) zostaje 113 260.
- Trend r/r: −7,9% (1 171 340 → 1 079 340) [SV].
- Sezon słaby: szczyt w styczniu 2026 (462 860), dołek w grudniu 2025 (295 450) [SV].
- Top frazy [SV, KS]:
  - pierścionek zaręczynowy: 90 500 (CPC 1,66 USD)
  - wesele: 60 500; sala weselna: 49 500 (CPC 0,40 USD)
  - zaproszenia ślubne: 40 500; suknie ślubne: 33 100; obrączki ślubne: 33 100 (CPC 0,88 USD)
  - dom weselny: 12 100; podziękowania dla gości: 12 100; sale weselne: 8 100
  - ile kosztuje talerzyk na weselu: 1 600
  - ile dać na wesele: 720 (CPC 2,69 USD); koperta na wesele: 720; ile dać do koperty na wesele: 260
  - ile kosztuje wesele: 480; koszt wesela: 210
  - kalkulator wesela: 30; kalkulator kosztów wesela: 30; kalkulator alkoholu na wesele: 390
- Sale per region: 853 frazy z „sale weselne”, top 300 to 42 810 [KS]. Przykłady: szczyrk 2 400, śląsk 880, podkarpacie 480, warszawa 480.
- Wniosek: popyt na kalkulator kosztów jest bardzo mały (30). Duży popyt to produkty i miejsca.

### SERP

| Fraza | Wolumen | AIO | Mediana domen linkujących | Wyniki <50 domen | Kto wygrywa |
|---|---|---|---|---|---|
| ile kosztuje wesele | 480 | tak | 345 | 0 | blogi sal i fotografów, wpis z lat 2021/2022 |
| kalkulator alkoholu na wesele (narzędzie) | 390 | tak | 115 | 2 | sklepy z alkoholem |
| sale weselne kraków (hub regionu) | 390 | nie | 1 757,5 | 0 | katalogi: weselezklasa.pl, wedding.pl, gdziewesele.pl, saleweselne.com |
| ile kosztuje talerzyk na weselu | 1 600 | tak | 142,5 | 2 | sale weselne piszące o własnych cenach |
| ile dać na wesele | 720 | tak | 2 485 | 1 | hotel, reddit, facebook, wpisy z 2020 i 2022 |

Źródło: [SERP], [BL], 18.10.2026.

- Siła wesele.pl i mlodapara.pl: obie domeny praktycznie nie istnieją w Google. wesele.pl: 104 domeny linkujące [BL], ruch 4 [TE], 1 fraza. mlodapara.pl: 71 domen [BL], ruch 12 [TE], 3 frazy.
- Prawdziwi gracze [TE, BL]: weselezklasa.pl (ruch 150 148, 4 936 domen), wedding.pl (92 322, 1 575), gdziewesele.pl (34 582, 2 565), saleweselne.com (22 210, 2 366).
- Treści poradnikowe są słabe: 6 wyników sprzed 2023 i 3 fora/social w 5 SERP [SERP].
- AIO w 4 z 5 SERP, cytuje małe serwisy (bedzieslub.app, wspomnieniazwesela.pl) [SERP].

### Zarobek

- CPC niskie: sala weselna 0,40 USD, obrączki 0,88 USD, pierścionek 1,66 USD [SV]. Wyjątek: „ile dać na wesele” 2,69 USD [SV].
- Model katalogów (weselezklasa.pl, gdziewesele.pl) to sprzedaż wpisów salom i usługodawcom. To wymaga sprzedaży bezpośredniej, czyli kontaktu z firmami.
- Afiliacja biżuterii i sukien: nie znaleziono polskiego programu w wyszukiwaniu (18.10.2026), nie potwierdzono.
- Alkohol: kalkulator alkoholu przyciąga sklepy z wódką, ale reklama napojów spirytusowych w Polsce jest ograniczona ustawą. Wymaga oceny prawnej przed jakąkolwiek afiliacją.
- Ocena: 3.

### Fosa danych

- Sale weselne: brak otwartego rejestru. Dane z Map Google wolno nam używać tylko zbiorczo (zasady projektu), więc strony encji sal odpadają.
- Ceny (talerzyk, fotograf, DJ): podają same sale i usługodawcy, bez weryfikowalnego źródła. Zasada projektu „każda liczba ma źródło” mocno to ogranicza.
- GUS BDL (liczba małżeństw per powiat): istnieje, licencji nie potwierdzono dziś.
- Ocena: 2.

### Ryzyko

- YMYL: brak. Treści prawne: dokumenty do ślubu cywilnego, opłaty USC (do decyzji właściciela).
- Ceny nie do potwierdzenia u źródła, alkohol, AIO 4 z 5.
- Ocena: 3.

### Pomysł na serwis

Kalkulator budżetu wesela (liczba gości × talerzyk × dodatki) i kalkulator koperty, oba z jawnym założeniem i datą. Huby per województwo z danymi GUS o ślubach i przeglądem typów miejsc. Checklisty i harmonogram przygotowań jako narzędzie do odhaczania.

### Werdykt

**Średnio.** SERP poradnikowy jest słaby, a wesele.pl i mlodapara.pl nie są konkurencją. Brakuje jednak danych do stron encji i uczciwego źródła cen, a pieniądze w tej niszy są w sprzedaży wpisów salom, czego nie robimy.

---

## 4. Zwierzęta domowe (rasy, karmy, koszty, zdrowie) (YMYL weterynaryjny)

### Popyt

- Suma rdzenia: 1 134 930 z 54 fraz (4 frazy bez danych: kot brytyjski, kot bengalski, kastracja psa cena, czy kot może pić mleko) [SV]. Bez „weterynarz”, „weterynarz całodobowy” i „schronisko” zostaje 903 630.
- Trend r/r: −12,3% (3 658 370 → 3 209 250) [SV]. Spadek głównie w nazwach ras (golden retriever: lipiec 165 000 → 110 000).
- Sezon słaby: szczyt w listopadzie 2025 (1 274 920), dołek w czerwcu 2026 (944 210) [SV].
- Top frazy [SV]:
  - weterynarz: 201 000
  - golden retriever: 135 000; maine coon: 135 000; shih tzu: 90 500; ragdoll: 90 500
  - rasy psów: 60 500; labrador, owczarek niemiecki, buldog francuski: po 60 500
  - karma dla psa: 33 100 (CPC 1,90 USD); karma dla kota: 18 100 (CPC 1,09 USD)
  - rasy kotów: 33 100; york: 27 100; żwirek dla kota: 22 200
  - ubezpieczenie psa: 5 400 (CPC 2,49 USD); podatek od psa: 2 900
  - najlepsza karma dla psa: 1 600 (CPC 1,24 USD); ranking karm dla psów: 1 000 (CPC 1,76 USD)
  - biegunka u psa: 2 400; kleszcz u psa: 2 900; pchły u psa: 1 900
  - kalkulator wieku psa: 390; ile kosztuje utrzymanie psa: 170
- Wniosek: ogromny popyt na encje (rasy), średni na karmy, mały na koszty i kalkulatory.

### SERP

| Fraza | Wolumen | AIO | Mediana domen linkujących | Wyniki <50 domen | Kto wygrywa |
|---|---|---|---|---|---|
| golden retriever (encja rasy) | 135 000 | nie (panel wiedzy) | 1 588 | 1 | blogi sklepów, OLX, hodowla, psibufet.com |
| najlepsza karma dla psa (porównanie) | 1 600 | nie (moduł produktów) | 154 | 1 | małe serwisy rankingowe: najlepsza-karma.pl, recenzjekarm.pl, karmopedia.pl |
| kalkulator wieku psa (narzędzie) | 390 | tak | 571 | 0 | blogi producentów karm i sklepów |
| biegunka u psa (zdrowie, YMYL) | 2 400 | tak | 197 | 1 | blogi sklepów i producentów leków |
| ile kosztuje utrzymanie psa | 170 | tak | 405 | 2 | psy.pl (2018), forum.gazeta.pl (2011), psy24.pl (2016), dogway.pl (2019) |

Źródło: [SERP], [BL], 18.10.2026.

- Najwięcej starych wyników w całym badaniu: 9 sprzed 2023 [SERP].
- Serwisy rankingowe karm są małe [BL, TE]: karmopedia.pl 85 domen, ruch 7 094; najlepsza-karma.pl 154 domeny, ruch 1 482; recenzjekarm.pl 18 domen, ruch 1 610.
- Strony ras: brak silnego serwisu encji. Wygrywają blogi sklepów (zooart.com.pl, karusek.com.pl z 2021) i psibufet.com (2 190 domen, ruch 41 615) [SERP, BL, TE].
- AIO w 3 z 5 SERP, przy zdrowiu daje gotową instrukcję postępowania [SERP].

### Zarobek

- CPC: karma dla psa 1,90 USD, ranking karm 1,76 USD, ubezpieczenie psa 2,49 USD [SV].
- zooplus: program przez AWIN, wg strony AWIN 3% za pierwsze 3 zamówienia i 1% za kolejne, okno 30 dni; strona zooplus podaje do 4% CPA ([ui.awin.com](https://ui.awin.com/merchant-profile/10247), [zooplus.com](https://www.zooplus.com/content/affiliate_programme)). Warunków nie weryfikowano w panelu.
- Karma to zakup powtarzalny, co podnosi wartość klienta.
- Ubezpieczenie psa: program partnerski nie sprawdzony.
- Ocena: 3,5.

### Fosa danych

- Rasy: Wikidata (licencja CC0, nie weryfikowano dziś konkretnych pól). Wzorce FCI i ZKwP są dokumentami chronionymi, nie kopiujemy.
- Karmy: brak otwartej bazy składów. Składy trzeba przepisywać z etykiet producentów.
- Podatek od psa: uchwały rad gmin w dziennikach urzędowych województw. Dane publiczne, ale rozproszone (ok. 2,5 tys. gmin). To potencjalna programmatic seria z popytem 2 900 na frazę główną [SV].
- Ocena: 2,5.

### Ryzyko

- **YMYL weterynaryjny**: zdrowie zwierząt (biegunka, kleszcze, leki, szczepienia). Treści zdrowotne wymagają recenzji lekarza weterynarii albo trzeba je pominąć.
- AIO w 3 z 5 SERP, spadek r/r −12,3%.
- Ocena: 2,5.

### Pomysł na serwis

Strony encji ras psów i kotów: dane z Wikidata plus nasz własny wyliczony koszt utrzymania (porcja karmy wg masy × ceny dziś, podatek, szczepienia z cenników). Narzędzia: kalkulator dziennej porcji i miesięcznego kosztu oraz porównywarka karm po składzie z afiliacją zooplus. Huby: rasy małe, duże, dla alergika, dla rodziny; zdrowie tylko z recenzją weterynarza.

### Werdykt

**Tak, warunkowo (najwyższy wynik).** Popyt na encje jest ogromny, SERP porównań karm i kosztów jest słaby i stary, a jest działający program partnerski. Warunek: właściciel decyduje, czy wchodzimy w zdrowie (YMYL). Bez działu zdrowia serwis nadal ma sens (rasy, karmy, koszty).

---

## 5. Zabawki i LEGO (zestawy jako encje, ceny, premiery, wartość)

### Popyt

- Suma rdzenia: 1 689 690 z 47 fraz (2 bez danych: „lego wartość zestawów”, „ile warte są stare klocki lego”) [SV]. Bez „lego”, „cobi”, „promoklocki” i „sklep lego” zostaje 1 034 090.
- Trend r/r: −2,8% (3 801 580 → 3 696 250) [SV].
- Sezon mocny: szczyt w grudniu 2025 (4 013 150), dołek w lipcu 2026 (1 135 670) [SV].
- Top frazy [SV]:
  - lego: 550 000
  - lego technic, star wars, ninjago, minecraft, kwiaty: po 90 500
  - lego friends: 60 500; klocki lego, lego city, lego harry potter, lego botanical, cobi: po 49 500
  - **promoklocki: 49 500** (wyszukiwania samej marki konkurenta)
  - kalendarz adwentowy lego: 27 100; zabawki dla 3 latka: 27 100; prezent dla 7 latka: 27 100; zabawki dla 5 latka: 14 800
  - lego promocje: 6 600; lego nowości: 2 900
  - lego inwestycja: 70; lego wycofane zestawy: 30
- Encje (numery zestawów): 4 295 fraz typu „lego 12345”, top 300 to 236 810 wyszukiwań miesięcznie, każda z top 300 ma co najmniej 100 [KS]. Przykłady: lego 60470: 2 900; lego 77256: 2 400; lego 43020: 2 400; lego 75192: 1 300.
- CPC bardzo niskie: średnio 0,15 USD [SV].

### SERP

| Fraza | Wolumen | AIO | Mediana domen linkujących | Wyniki <50 domen | Kto wygrywa |
|---|---|---|---|---|---|
| lego 60470 (encja zestawu) | 2 900 | nie | 1 045,5 | 0 | 6 sklepów, moduł porównywarek (Ceneo, Skąpiec, Bigshopper) |
| lego promocje | 6 600 | nie | 6 880,5 | 0 | ceneo.pl, sklepy, blog fanowski fanklockow.pl, grupa FB |
| lego nowości | 2 900 | nie | 107 505 | 0 | lego.com ×4, blogi fanowskie |
| lego inwestycja | 70 | nie | 1 617 535 | 0 | YouTube ×2, wnioskomat.com, noweklocki.pl (2021), reddit (5 wyników) |
| zabawki dla 5 latka (hub prezentów) | 14 800 | nie | 428 | 0 | sklepy z kategoriami i rankingami, moduł produktów Google |

Źródło: [SERP], [BL], 18.10.2026. Wysokie mediany przy „lego nowości” i „lego inwestycja” wynikają z lego.com, YouTube i reddit.

- Siła promoklocki.pl [BL, TE]: 650 domen linkujących, ruch organiczny 156 814, 3 350 fraz. Do tego 49 500 wyszukiwań samej nazwy [SV]. To silny lider w okazjach cenowych.
- promoklocki.pl nie ma go w top 10 frazy „lego promocje” ani strony zestawu „lego 60470” [SERP]. Strony zestawów wygrywają sklepy.
- Inne serwisy informacyjne są małe [TE]: fanklockow.pl 21 641, faniklockow.pl 6 849, noweklocki.pl 3 408.
- AI Overview w 0 z 5 SERP. Google pokazuje tu moduły produktów i porównywarki [SERP].

### Zarobek

- CPC 0,13–0,51 USD [SV], więc reklamy dają mało.
- Allegro Polecam zamknięto w grudniu 2023; następca Allegro Share daje punkty i kupony, opisywana stawka 1,67% (nie potwierdzono, czy działa w 2026) ([tabletowo.pl](https://www.tabletowo.pl/?p=850672)).
- Program LEGO.com przez Rakuten: istnieje w części krajów, dla Polski nie potwierdzono ([strackr.com](https://strackr.com/blog/lego-affiliate-program)).
- Programy Ceneo, Empik, Smyk, Media Expert: nie sprawdzono.
- Wartość koszyka wysoka (ceny zestawów w SERP od ok. 33 zł do ponad 3 000 zł), ale prowizje w zabawkach są zwykle niskie (do potwierdzenia).
- Ocena: 3.

### Fosa danych

- Katalog zestawów: Rebrickable (pliki CSV do pobrania) i Brickset (API z kluczem) ([rebrickable.com/api](https://rebrickable.com/api/), [pakiet brickset](https://cran.rstudio.com/web/packages/brickset/refman/brickset.html)). Licencji komercyjnej nie potwierdzono, strony są zablokowane przez proxy.
- Ceny: potrzebne feedy produktowe z sieci afiliacyjnych albo zbieranie cen ze sklepów. Własna historia cen w PLN to realna fosa, bo rośnie z czasem.
- Znak towarowy LEGO: nazwa nie może być w domenie ani logo, potrzebna informacja, że LEGO Group nie wspiera serwisu.
- Ocena: 3.

### Ryzyko

- YMYL: brak. „Wartość kolekcjonerska” i „inwestycja” ocierają się o porady finansowe; lepiej pokazywać historię cen bez rekomendacji.
- Brak AIO w 5 z 5 SERP to plus.
- Zależność od kilku programów partnerskich i od sezonu IV kwartału.
- Ocena: 4.

### Pomysł na serwis

Baza zestawów LEGO: każda strona encji ma numer, serię, liczbę elementów, cenę dziś w kilku sklepach, historię ceny w PLN, cenę za element i datę wycofania. Narzędzia: alert ceny, kalkulator ceny za klocek i wartości kolekcji. Huby per seria i per wiek dziecka („zabawki dla 5 latka”, „prezent dla 7 latka”) z poradnikami prezentowymi.

### Werdykt

**Tak, warunkowo.** Popyt na encje jest duży i stały (4 295 numerów zestawów), AI Overview nie ma, ryzyko niskie. Warunek przed startem: potwierdzić dostęp do feedów cen i programów partnerskich w PL oraz licencję katalogu (Rebrickable/Brickset). Bez danych cenowych nie wygramy ze sklepami na stronach zestawów, a z promoklocki.pl na okazjach.

---

## Czego nie sprawdzono

- Licencji: dane.gov.pl (RSPO, zbiór 839), ELA, GUS BDL, Rebrickable, Brickset. WebFetch i curl są blokowane przez proxy, a content_parsing nie zwrócił treści (dane.gov.pl wymaga JavaScriptu, rebrickable.com zwrócił pustą odpowiedź).
- Programów partnerskich: LEGO.com dla Polski, Ceneo, Empik, Smyk, Allegro Share w 2026, ubezpieczenia zwierząt, biżuteria ślubna, kursy E8, leady dla uczelni.
- Reklamodawców w Google Ads (`ads_advertisers`), pole opcjonalne w metodzie.
- Wolumenów 6 fraz, dla których Google Ads nie zwrócił danych [SV].

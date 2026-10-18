# Terrarystyka (z akwarystyką jako dodatkiem): badanie „tak/nie” (18.10.2026)

Brief: `finalisci/BRIEF.md`. Wcześniejsza ocena: `C-rolnictwo-dzialka.md`, sekcja 5 (3,60). Rynek: Polska (location_code 2616, język pl). Wszystkie dane pobrano 18.10.2026.

**Znaczniki źródeł:**

- **[V]** `/v3/keywords_data/google_ads/search_volume/live`, średnia z 12 mies. (10.2025–09.2026), CPC w USD, miesiące od 07.2025. Dane: `dane/terrarystyka-mapa.csv`.
- **[L]** `/v3/dataforseo_labs/google/keyword_suggestions/live` (rozszerzanie rdzenia, 18 ziaren).
- **[S]** `/v3/serp/google/organic/live/advanced`, desktop, z `load_async_ai_overview`; analizowano 10 pierwszych wyników organicznych. Dane: `dane/terrarystyka-serp-top10.csv`, `dane/terrarystyka-serp-podsumowanie.csv`.
- **[B-URL]** `/v3/backlinks/bulk_referring_domains/live` dla 188 konkretnych URL-i. **[B-dom]** to samo dla 96 domen.
- **[T]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live`. Dane: `dane/terrarystyka-konkurencja.csv`.
- **[P]** `/v3/on_page/content_parsing/live` (strony, których WebFetch nie otwiera).
- **[W]** WebSearch. Programy partnerskie: `dane/terrarystyka-zarobek-programy.csv`.

---

## Werdykt w skrócie

**WARUNKOWO, wynik 3,20 / 5.** Ruch jest do wzięcia, pieniądze są słabe.

1. **Za:** duży, stabilny popyt na strony gatunków (636 tys. wyszukiwań/mies. w 412 frazach terrarystyki, r/r +0,2%) i SERP-y, w których prawie żaden wygrywający URL nie ma linków (197 z 200 URL-i ma mniej niż 10 domen linkujących).
2. **Przeciw:** zarobek. Jedyny potwierdzony program to zooplus w Awin: 3% za pierwsze 3 zamówienia klienta, potem 1%. Średni ważony CPC terrarystyki to 0,115 USD, więc reklamy dadzą mało. Rachunek po 12 mies.: ok. 230 zł/mies. (ostrożnie) do ok. 3 300 zł/mies. (realnie, z własnym PDF-em).
3. **Ryzyko konkurencji:** sklepy piszą te same poradniki i mają własny towar. naszezoo.pl (sklep Grupy K365) publikuje od 10.2026 klaster terrarystyczny w stylu bardzo podobnym do naszego i jest już cytowany w 2 z 4 AI Overview.

**Warunek „tak”:** właściciel akceptuje serwis jako aktywo ruchu z niskim przychodem w 1. roku i zgadza się przetestować własny produkt (płatna karta startowa / planer kosztów). Bez tego to nisza na ruch, bez biznesu.

---

## 1. Mapa fraz

**Jak zbudowano:** 18 ziaren w `keyword_suggestions` [L] (gekon, agama, aksolotl, terrarium, ptasznik, wąż, żółw, kameleon, patyczak, pyton, legwan, modliszka, scynk, akwarium, jaszczurka, żaba, ślimak, karaczan, gad) dało 2 437 fraz po filtrach szumu. `keyword_ideas` zwróciło śmieci (np. „alkomat allegro”, „kilof minecraft”), więc go nie użyto. Do tego ręcznie dodano ok. 120 fraz (gatunki, sprzęt, karmówki, narzędzia, rdzeń akwarystyki z pliku grupy C). 733 frazy przeszły przez [V].

**Co usunięto** (`dane/terrarystyka-usuniete.csv`, 150 fraz):
- wieloznaczne: „skorpion” (27 100, znak zodiaku), „karaczan” (8 100, szkodnik), „wąż domowy”, „świerszcze”, „mączniki”, „wylinka”;
- prawne lub dzikie gatunki chronione w PL: „rzekotka” (5 400), „traszka” (9 900), żółwie z listy inwazyjnych (np. „żółw ozdobny”, „żółw żółtobrzuchy”); wcześniej odfiltrowano też żółwia czerwonolicego, błotnego, węża Eskulapa, jaszczurkę zwinkę, modliszkę zwyczajną;
- formikaria (osobna nisza) i 10 fraz z wolumenem 0;
- 118 fraz z najniższym wolumenem, żeby zmieścić się w 500.
Bliskie warianty (np. „gekon orzesiony” / „gekon orzęsiony”) scalono w kolumnie `warianty_scalone`, bez sumowania.

**Wynik: 500 fraz** (`dane/terrarystyka-mapa.csv`) [V]:

| Dział | Fraz | Suma wolumenu/mies. | Trend r/r (07–09) | Najsłabszy / najmocniejszy miesiąc | Ważony CPC |
|---|---|---|---|---|---|
| Terrarystyka | 412 | **635 970** | +0,2% (bez skoków newsowych: −1,4%) | 06.2026: 540 110 / 08.2026: 736 710 | 0,115 USD |
| Akwarystyka (dodatek) | 88 | 268 850 | **−12,2%** | 06.2026: 189 730 / 01.2026: 360 310 | 0,328 USD |

Skok w 08.2026 to dwie frazy newsowe: „modliszka” (18 100 w 06 → 90 500 w 08) i „pyton birmański” (1 600 → 22 200) [V]. Bez nich szczyt terrarystyki to 10.2025 (657 640), dołek 06.2026 (520 410): sezonowość łagodna, ok. −21% od szczytu.

**Typy stron (frazy):** terrarystyka: encja 283, poradnik 87, hub 24, porównanie/ranking 15, narzędzie 3. Po zgrupowaniu w URL-e: 85 stron encji, 63 poradniki, 15 porównań, 12 hubów, 1 narzędzie z wieloma frazami. Akwarystyka: 14 encji, 11 poradników, 36 porównań (sprzęt), 2 huby, 1 narzędzie. Kolumna `docelowy_url` to robocza propozycja.

**Największe strony encji** (suma fraz na jeden URL) [V]: aksolotl 75 610, gekon lamparci 36 320, agama brodata 34 180, gekon orzęsiony 27 150, wąż zbożowy 25 870, ptaszniki 21 660, legwan 20 330, pyton królewski 19 750, ślimak afrykański 14 690, boa dusiciel 9 880, żółw stepowy 8 080, żółw grecki 7 960, żaba rogata 7 510.

**Intencje, które karmią narzędzie i produkt** (terrarystyka) [V]: „cena / ile kosztuje” 56 fraz, 37 180/mies. (np. „aksolotl cena” 5 400, CPC 1,06 USD; „gekon lamparci cena” 2 400); „terrarium dla … / jakie terrarium” 83 frazy, 57 900; „ile żyje” 14 fraz, 8 630; „co je” 10 fraz, 5 490. Frazy z „kalkulator” są małe: „kalkulator akwarium” 590, „kalkulator pojemności akwarium” 170, „kalkulator terrarium” 0, „koszt utrzymania gekona” 0, „ile kosztuje utrzymanie gekona lamparciego” 20.

---

## 2. SERP: 20 fraz

Wybrano 12 stron encji, 3 zapytania o cenę i długość życia, 3 poradniki/sprzęt, 1 narzędzie, 1 ranking [S]. Pełne dane: `dane/terrarystyka-serp-podsumowanie.csv`.

| Fraza | Wol. | AIO | URL-e <10 dom. | Mediana dom. domeny (bez platform) | Stare <2023 / fora | Kto wygrywa | Ocena |
|---|---|---|---|---|---|---|---|
| aksolotl | 60 500 | nie | 10 | 126 | 4 / 0 | blogi sklepów, wideo, Minecraft wiki | trudno |
| gekon lamparci | 27 100 | nie | 10 | 563 | 1 / 0 | blogi sklepów (gadzisklep, animalhotels, terrarium.com.pl) | tak |
| agama brodata | 27 100 | nie | 9 | 563 | 0 / 1 | blogi sklepów, gadyzbroda.pl | tak |
| gekon orzęsiony | 22 200 | nie | 10 | 159 | 1 / 0 | sklepy, zooperia, rynekzoologiczny | tak |
| wąż zbożowy | 22 200 | nie | 10 | 377 | 0 / 1 | blogi, naszezoo.pl, forum terrarium.pl | tak |
| pyton królewski | 14 800 | nie | 10 | 93 | 2 / 0 | vantisterra, terranpolska, akwarysta.pl | tak |
| patyczak | 18 100 | nie | 10 | 310 | 0 / 0 | Wikipedia, patychuck.pl (2 domeny!), blogi | tak |
| ślimak afrykański | 12 100 | nie | 10 | 286 | 1 / 0 | sklepy (anthunter, zmiennocieplne), blogi | tak |
| żółw stepowy | 6 600 | nie | 10 | 279 | 0 / 0 | Wikipedia, sklepy, gadzisklep | tak |
| legwan | 12 100 | nie | 10 | 563 | 1 / 0 | strony tagów, wideo, stary serwis prv.pl | trudno |
| ptasznik goliat | 6 600 | nie | 9 | 131 | 0 / 0 | sklepy z pająkami, blogi | tak |
| modliszka storczykowa | 8 100 | nie | 10 | 85 | 0 / 0 | sklepy (karty produktów), blogi | tak |
| aksolotl cena | 5 400 | **tak** | 9 | 377 | 2 / 1 | blogi + OLX/Allegro | tak |
| terrarium dla gekona lamparciego | 1 600 | nie | 10 | 170 | 0 / 0 | sklepy + poradniki (strefaegzotyki.pl: 18 domen) | tak |
| terrarium dla patyczaków | 2 900 | nie | 10 | 329 | 2 / 1 | 7 z 10 to Allegro/OLX | **nie** |
| gekon lamparci ile żyje | 880 | **tak** | 10 | 1 227 | 1 / 0 | 8 poradników (zooart, naszezoo) | trudno |
| gekon lamparci cena | 2 400 | **tak** | 10 | 494 | 1 / 0 | poradniki + marketplace | tak |
| mata grzewcza do terrarium | 1 900 | nie | 10 | 148 | 1 / 0 | 7 sklepów + blok produktów | **nie** |
| kalkulator akwarium | 590 | **tak** | 10 | 128 | 1 / 0 | 9 kalkulatorów, słabe domeny | tak |
| ptasznik dla początkujących | 390 | nie | 10 | 84 | 0 / 0 | sklepy z pająkami, blogi | tak |

**Liczby zbiorcze** [S][B-URL][B-dom]:
- **Linki do URL-i:** 197 z 200 wyników ma mniej niż 10 domen linkujących, 173 ma zero. Najwięcej: Wikipedia „Ambystoma meksykańska” (28), „Pogona vitticeps” (14), „Drapieżnica goliat” (11). W tej niszy strony wygrywają domeną i treścią, linki do konkretnego URL-a prawie nie grają roli.
- **Linki do domen:** mediana top 10 to 563, bez platform 153 (132 wyniki); 70 z nich ma domenę z <200 domenami linkującymi, 10 z <50.
- **Typy wyników (200):** poradnik/blog (zwykle blog sklepu) 80, sklep 38, marketplace (OLX, Allegro, Sprzedajemy, Ceneo, Erli) 32, wideo/social 25, encyklopedie 12, narzędzia 9, fora/grupy 4. Platformy zajmują 69 z 200 miejsc.
- **Wiek treści:** datę ma 68 wyników; 18 z nich sprzed 2023 (najstarszy 2012), 33 z lat 2025–2026.
- **AI Overview: 4 z 20** (aksolotl cena, gekon lamparci ile żyje, gekon lamparci cena, kalkulator akwarium). Cytuje małe serwisy: fera.pl, zoofaster.pl, zooart.com.pl, naszezoo.pl, skleprafa.com.pl (72 domeny linkujące) [S][B-dom]. AIO pojawia się przy pytaniach o cenę i długość życia, czyli dokładnie w długim ogonie, który chcemy brać.
- **Panel wiedzy (Wikipedia)** jest przy 12 z 12 nazw gatunków; nad wynikami są też wideo i krótkie filmy [S].

**Na ile fraz wejdzie nowa domena w 6–12 mies.:**
- według kryterium z briefu (≥2 URL-e z <10 domenami albo fora/PDF/stare): **20 z 20**. Kryterium jest tu mało czułe, bo prawie nikt nie ma linków do URL-a;
- ocena jakościowa: **15 z 20 tak, 3 trudno** (aksolotl, legwan, gekon lamparci ile żyje), **2 nie** (terrarium dla patyczaków, mata grzewcza: intencja zakupowa, sklepy i marketplace).

**Kto realnie konkuruje** [T][B-dom]: zoofaster.pl (ETV 47 869/mies., 865 domen), alezwierzaki.pl (42 552), gadzisklep.pl (33 989 przy 152 domenach), terrarium.com.pl (21 728; serwis z kartami gatunków pod adresami typu `/gekon-lamparci/`), zooperia.pl (17 953), naszezoo.pl (2 502, ale nowy i szybki). To sklepy albo serwisy z małym profilem linków. Da się z nimi wygrać jakością karty gatunku, a przegrać na sprzedaży.

---

## 3. Zarobek (potwierdzony u źródła)

### Programy partnerskie

| Program | Warunki | Status |
|---|---|---|
| **zooplus.pl (Awin, ID 10247)** | „standardową prowizję w wysokości 3% za pierwsze 3 zamówienia klienta (…). Od czwartego zamówienia obowiązuje standardowa prowizja 1%”; cookie 30 dni; weryfikacja zamówień co 21 dni; AOV 229,00 PLN; „średni współczynnik konwersji powyżej 10%” (deklaracja sklepu) | **potwierdzone** [P] ui.awin.com/merchant-profile/10247 |
| zooplus.pl (Tradedoubler, ID 226970) | wg opisu w wynikach: okres oczekiwania 60 dni | niepotwierdzone [W] |
| Maxi Zoo PL (Awin „Maxi Zoo PL – Temporary”) | katalog zewnętrzny podaje status „otwarty”, bez stawek | niepotwierdzone [W] |
| Allegro Share | ok. 1,67% w punktach na kupony (artykuł prasowy) | odpada: brak gotówki, nie potwierdzono u źródła [W] |
| Amazon.pl | stawka dla kategorii zwierząt nieznana; domena programu niedostępna przez proxy i [P] | niepotwierdzone |
| Ceneo | 0,20 zł/przeklik wg agregatora, kampania wstrzymana wg Cuelinks | niepotwierdzone [W] |
| Kakadu, Krakvet, Zooart, Fera, apetete, sklepy terrarystyczne (gadzisklep, vantisterra, terrarex, exo-factory, bioterr) | programu nie znaleziono | [W] |

Nie rejestrowano się w żadnym programie.

**Wniosek:** afiliacja to w praktyce jeden sklep z prowizją 3% (pierwsze zamówienia) i 1% (kolejne). zooplus ma mały wybór sprzętu terrarystycznego w porównaniu ze sklepami specjalistycznymi; tego nie sprawdzano liczbowo.

### Reklamy

- CPC terrarystyki: ważony 0,115 USD (317 fraz z CPC); najdroższe: „aksolotl cena” 1,06 USD, „mata grzewcza” 0,76 USD [V]. Akwarystyka: 0,328 USD [V].
- **RPM dla PL: brak wiarygodnego źródła z datą** [W]. W rachunku RPM to **założenie**: 8 zł (ostrożnie) i 15 zł (realnie) na 1000 odsłon. Niski CPC wskazuje raczej na dolną granicę.

### Własny produkt i leady

- **Płatna karta startowa gatunku / planer kosztów (PDF lub strona za paywallem, ok. 29 zł):** lista sprzętu z parametrami, plan pierwszych 30 dni, kalendarz karmienia, koszty jednorazowe i miesięczne liczone przez czytelnika. Realność: średnia. Popyt na „ile kosztuje” jest duży (37 180/mies.) [V]. Nie sprawdzano, czy ktoś w PL sprzedaje podobne materiały ani czy ktoś za nie zapłaci. To założenie do testu.
- **Ogłoszenia płatne przez hodowle lub sklepy:** odradzamy. Wymaga kontaktu z firmami (zakaz właściciela) i ciągnie w stronę sprzedaży zwierząt.
- **Leady:** brak sensownego odbiorcy (weterynarze od egzotyków to usługa lokalna; kontakt z nimi wykluczony).

### Wybór modelu

- **Główny: własny produkt** (karta startowa / planer kosztów), sprzedawany przy stronach „ile kosztuje”, „terrarium dla …” i w kalkulatorze kosztów startu. Uzasadnienie: to jedyne źródło z marżą bliską 100%, a intencja „ile kosztuje / co kupić” ma 95 tys. wyszukiwań/mies. w mapie [V].
- **Dodatkowy: afiliacja zooplus (Awin) na sprzęt i karmę + reklamy display.** Uzasadnienie: potwierdzone, ale słabe (3%/1%, RPM-założenie).
- Afiliacji nie łączymy ze zwierzętami: zero linków do zakupu żywych zwierząt.

---

## 4. Rachunek przychodu po 12 mies. (miesięcznie, w 12. miesiącu)

**Krok 1: frazy „do wzięcia”** [V], podział mapy:

| Segment | Terrarystyka | Akwarystyka |
|---|---|---|
| Ogon (<5 000/mies.) | 229 970 (335 fraz) | 63 710 (40) |
| Głowa (≥5 000/mies.) | 340 200 (22) | 133 300 (10) |
| Sprzęt, SERP-y sklepowe | 65 800 (55) | 71 840 (38) |

**Krok 2: CTR.** Krzywa CTR to **założenie** oparte na badaniu Backlinko (poz. 1 = 27,6% wg wyników [W] z backlinko.com/google-ctr-stats; pozostałe pozycje z tego samego badania nie potwierdzone dziś). Przyjęto średnie CTR dla segmentu:

| Założenie | Ostrożny | Realny |
|---|---|---|
| Dział | tylko terrarystyka | terrarystyka + akwarystyka |
| Pokrycie fraz opublikowanymi i zaindeksowanymi stronami | 50% | 80% |
| CTR ogon (śr. poz. ok. 7 / ok. 4) | 4% | 8% |
| CTR głowa (poz. ok. 10 / ok. 7) | 1,5% | 3% |
| CTR sprzęt | 0% | 1% |
| **Ruch/mies.** | **7 150** | **31 260** (23 410 + 7 850) |

**Krok 3: przychód.**

| Źródło | Ostrożny | Realny |
|---|---|---|
| Display: odsłony/wizytę × RPM | 7 150 × 1,3 = 9 295 odsłon × 8 zł/1000 = **74 zł** | 31 260 × 1,4 = 43 764 × 15 zł/1000 = **656 zł** |
| zooplus: klik do sklepu × konwersja × AOV × 3% | 7 150 × 2% = 143 × 5% = 7,2 zam. × 229 zł × 3% = **49 zł** | 31 260 × 4% = 1 250 × 10% = 125 zam. × 229 zł × 3% = **859 zł** |
| Własny PDF 29 zł | 7 150 × 0,05% = 3,6 szt. = **104 zł** | 31 260 × 0,2% = 62,5 szt. = **1 813 zł** |
| **Razem/mies.** | **ok. 227 zł** | **ok. 3 328 zł** |

**Wszystkie założenia jawnie:** pokrycie fraz, CTR segmentów, odsłony na wizytę (1,3 / 1,4), RPM (8 / 15 zł), odsetek klików do sklepu (2% / 4%), konwersja w sklepie (5% / 10%; 10% to deklaracja zooplus), prowizja 3% (górna granica: od 4. zamówienia klienta 1%), konwersja PDF (0,05% / 0,2%) i cena PDF 29 zł. AOV 229 zł pochodzi ze strony programu [P]. Przychód z PDF jest najmniej pewny i najbardziej wpływa na wynik: bez niego wariant realny to ok. 1 515 zł/mies.

---

## 5. Dane do stron encji

| Źródło | URL | Licencja (cytat ze strony źródła, 18.10.2026) | Co daje | Ocena |
|---|---|---|---|---|
| **Wikidata** | wikidata.org/wiki/Wikidata:Licensing | „All structured data (i.e. the main, Property, Lexeme, and EntitySchema namespaces) is released into the public domain under Creative Commons Zero.” [P] | nazwa naukowa, polskie nazwy, rodzina, status IUCN, czasem długość/masa/długość życia | **OK (CC0)**, ale bez parametrów hodowli |
| **GBIF** | gbif.org/terms | wg wyników [W]: zbiory mają licencję CC0, CC BY albo CC BY-NC, przypisaną do zbioru | taksonomia, występowanie | **tylko zbiory CC0/CC BY**; CC BY-NC odpada; do hodowli mało przydatne. Strony GBIF nie otworzyły się przez [P] (strona w JS) |
| **The Reptile Database** | reptile-database.org | „Copyright © 1995-2026 by Peter Uetz.”; na stronie pobierania: „More recent versions are available for academic collaborators upon request.” Brak otwartej licencji na stronie źródła [P] | taksonomia gadów (11 940 gatunków wg komunikatu z 2022) | **odpada** (CC BY 4.0 podają tylko katalogi wtórne, np. marineinfo.org) |
| FishBase | — | CC BY-NC (plik grupy C) | ryby | **odpada** |
| Wikimedia Commons (zdjęcia) | — | licencja per plik; nie sprawdzano dziś | zdjęcia gatunków | tylko pliki CC0 / CC BY / CC BY-SA, sprawdzane pojedynczo |

**Wniosek:** gotowej bazy parametrów hodowli z licencją komercyjną nie ma. Wikidata daje szkielet (nazwy, taksonomia, status), a **parametry hodowli trzeba zbierać ręcznie** jako fakty z publikacji (naukowych, weterynaryjnych, hodowlanych), każdą liczbę z linkiem, bez kopiowania tekstu.

**Liczba encji:** 85 adresów encji w mapie terrarystyki (nasz szacunek: ok. 40 to gatunki z wyraźnym popytem, reszta to odmiany barwne i wąskie gatunki) + 14 w akwarystyce [V]. Pokrycia tych gatunków w Wikidata nie sprawdzono (SPARQL zablokowany przez proxy).

**Praca ręczna (szacunek):** karta gatunku ma ok. 12 pól (temperatura dzień/noc, wilgotność, UVB, min. wymiary terrarium, dorosła długość, długość życia, dieta, częstotliwość karmienia, aktywność, poziom trudności, czas opieki/dzień, „nie dla kogo”), każde z 2–3 źródeł. Ok. 1,5 h na gatunek z przeglądem → **40 gatunków na start ≈ 60 h**, 85 po 6 mies. ≈ 130 h. **Aktualizacja:** przegląd kart raz w roku; ceny sprzętu w kalkulatorze bez kwot (linki „sprawdź w sklepie”) albo z datą i źródłem, odświeżane co miesiąc.

---

## 6. Szkic serwisu

**Działy:** Gatunki (encje) · Zanim kupisz (decyzja, koszty, porównania gatunków) · Terrarium i sprzęt · Karmienie (karmówki, suplementy) · Codzienna opieka i sygnały do weterynarza (bez leczenia) · Narzędzia · później Akwarium.

| Typ | Na start | Po 6 mies. |
|---|---|---|
| Encje (karty gatunków) | 12 | 60 |
| Poradniki | 20 | 70 |
| Huby | 4 | 12 |
| Porównania / rankingi | 3 | 15 |
| Narzędzia | 2 | 5 |
| **Razem** | **41** | **162** |

**Narzędzia:**
1. **Kalkulator kosztów startu i utrzymania** (gatunek → lista sprzętu, koszt jednorazowy i miesięczny, prąd = W × h × stawka z rachunku). Karmi frazy „ile kosztuje …” (37 180/mies.) [V] i prowadzi do płatnej karty.
2. **Dobór terrarium** (gatunek, liczba zwierząt → minimalne wymiary ze źródłem). Frazy „terrarium dla …” (57 900/mies.) [V].
3. **Test „Czy to dobry moment na gada?”** (czas, budżet, miejsce, wyjazdy, długość życia). Jedna z odpowiedzi to „jeszcze nie”.
4. **Kalkulator prądu terrarium** (mata, lampa, termostat).
5. Później: **kalkulator akwarium** (litraż 7 kształtów, waga, podłoże); SERP słaby, ale popyt 590 + 170 [V][S].

**Pierwszy klaster:** „Gekon lamparci od decyzji do terrarium”: karta gatunku + ile kosztuje + jakie terrarium + co je + ile żyje + gekon czy agama + kalkulator kosztów. Start publikacji **4.11.2026**: szczyt sezonu to 10–01, a w grudniu dochodzi tekst „Gad na prezent? Zanim kupisz” (dobrostan, przed świętami). Drugi klaster od 12.2026: agama brodata, potem aksolotl, wąż zbożowy, gekon orzęsiony.

**Nazwa i domena (tylko pomysły, dostępności nie sprawdzano):** Zanim Kupisz Gada (zanimkupiszgada.pl), Karta Gatunku (kartagatunku.pl), Terrarium od Zera (terrariumodzera.pl), Gadzi Start (gadzistart.pl), Łuska i Pancerz (luskaipancerz.pl).

### Dobrostan: jak nie zachęcać do impulsywnego kupna

- Każda karta gatunku zaczyna się od ramki „Zanim kupisz”: długość życia, minimalne miejsce, koszt startu i miesięczny, czas dziennie, „nie dla kogo”.
- Zero linków afiliacyjnych i ogłoszeń do żywych zwierząt; zero odesłań do OLX/Allegro ze zwierzętami. Afiliacja tylko dla sprzętu i karmy, pod sekcjami o warunkach.
- Odpowiedź na „ile kosztuje gekon” zawsze z pełnym kosztem startu i utrzymania; cena zwierzęcia nie jest haczykiem sprzedażowym.
- Test gotowości kończy się także wynikiem „jeszcze nie” i listą rzeczy do sprawdzenia.
- Teksty sezonowe: „zwierzę to nie prezent” przed świętami i Dniem Dziecka.
- Bez stron o gatunkach, których dom nie zapewni (pyton siatkowy, birmański: tylko jeśli w ogóle, to jako ostrzeżenie, bez monetyzacji).
- Bez porad leczenia; tylko sygnały, przy których trzeba jechać do lekarza weterynarii.

---

## 7. Ryzyka

- **AIO:** dziś 4 z 20 SERP-ów, ale wszystkie przy pytaniach o cenę, długość życia i kalkulator, czyli tam, gdzie mieliśmy brać ruch i sprzedawać kartę [S]. Panel wiedzy z Wikipedii stoi przy każdej nazwie gatunku.
- **Konkurencja sklepów:** gadzisklep.pl, zoofaster.pl, alezwierzaki.pl, terrarium.com.pl; nowy naszezoo.pl pisze bardzo podobnie i linkuje do własnych produktów [T][P].
- **Zależność od jednego programu:** potwierdzony jest tylko zooplus (3%/1%) [P].
- **Sezonowość:** łagodna (−21% od szczytu do dołka bez newsów), akwarystyka spada r/r −12,2% [V].
- **Platformy:** 69 z 200 miejsc w top 10 to YouTube, Facebook, OLX, Allegro, Wikipedia [S].
- **Reputacja i dobrostan:** treść o „cenie zwierzęcia” łatwo odebrać jako zachętę do kupna; patrz zasady wyżej.
- **Ruch z dzieci:** „aksolotl” miesza intencje (Minecraft, maskotki); część ruchu nie kupi niczego.

### Omijamy (tematy prawne: autorzy ich nie ruszają)

- CITES: załączniki, dokumenty pochodzenia, świadectwa, „czy gatunek jest na CITES”;
- rejestracja zwierząt w starostwie i obowiązki zgłoszeniowe;
- gatunki obce inwazyjne (lista unijna i krajowa), w tym żółw czerwonolicy i żółtolicy: zakazy, kary, „co zrobić z żółwiem”;
- gatunki niebezpieczne: zezwolenia, zakazy posiadania (duże dusiciele, jadowite węże, jadowite pajęczaki), „czy mogę mieć w domu”;
- rodzime gatunki chronione (traszki, rzekotka, jaszczurka zwinka, żółw błotny, wąż Eskulapa, modliszka zwyczajna): ich trzymanie i „czy można złapać”;
- sprzedaż, rozmnażanie na sprzedaż, giełdy terrarystyczne, wysyłka i transport zwierząt;
- karmienie żywymi kręgowcami w świetle przepisów, ustawa o ochronie zwierząt, kary;
- import, zwierzęta z wakacji, ubezpieczenia, „czy to legalne”;
- leczenie, dawki leków, zabiegi (to YMYL; zostają tylko sygnały do wizyty u lekarza).

Przepisów nie sprawdzano dziś; lista służy do omijania tematów.

---

## 8. Werdykt i ocena (METODA.md)

| Kryterium (waga) | Ocena | Uzasadnienie |
|---|---|---|
| Popyt i trend (20%) | 4 | 635 970/mies. w 412 frazach, r/r +0,2% (bez newsów −1,4%) [V] |
| Słabość SERP (25%) | 4 | 197/200 URL-i <10 domen; mediana domen bez platform 153; 15 z 20 fraz realnych [S][B] |
| Zarobek (25%) | 2 | tylko zooplus 3%/1%; CPC 0,115 USD; RPM nieznany; własny produkt nieprzetestowany |
| Fosa danych / narzędzia (15%) | 2 | Wikidata CC0 to tylko szkielet; parametry ręcznie (ok. 60–130 h); kalkulatory mają mały popyt bezpośredni |
| Niskie ryzyko (15%) | 4 | niski YMYL, AIO 4/20; tematy prawne łatwo wydzielić; ryzyko dobrostanu do opanowania zasadami |
| **Wynik ważony** | **3,20** | 0,8 + 1,0 + 0,5 + 0,3 + 0,6 |

**WARUNKOWO.** Trzy powody:
1. **Ruch tak:** największa w badaniu przestrzeń encji (aksolotl, gekony, agama, węże) i SERP-y wygrywane przez blogi sklepów bez linków do URL-i.
2. **Pieniądze słabo:** jeden potwierdzony program z prowizją 3%→1%, bardzo niski CPC; 12. miesiąc to ok. 230–3 300 zł/mies., a górna wartość wisi na nieprzetestowanym PDF-ie.
3. **Konkurencja ma towar:** sklepy (w tym nowy naszezoo.pl) robią ten sam typ treści i zarabiają na koszyku, nie na prowizji.

**Co musi być prawdą, żeby „tak”:** (a) właściciel chce aktywa ruchu z niskim przychodem na start; (b) test karty startowej / planera kosztów w pierwszym klastrze (gekon lamparci) da choć 0,1% konwersji; (c) właściciel akceptuje listę „Omijamy” i zasady dobrostanu.

---

## Czego nie sprawdzono (wprost)

- Stawek Amazon.pl, warunków Maxi Zoo PL, programu Allegro u źródła; programów sklepów terrarystycznych na ich stronach (tylko WebSearch).
- RPM dla Polski (brak źródła z datą); CTR pozycji 2–10 z badania Backlinko (potwierdzono tylko poz. 1 przez wyniki wyszukiwania).
- Licencji GBIF na stronie źródła (strona w JS nie otworzyła się) i pokrycia gatunków w Wikidata (SPARQL zablokowany).
- Licencji zdjęć Wikimedia Commons (per plik).
- Asortymentu terrarystycznego zooplus.pl.
- Przepisów (CITES, gatunki inwazyjne, niebezpieczne, chronione): celowo pominięte.
- SERP-y z jednego zrzutu (desktop, 18.10.2026); dwa przebiegi „gekon lamparci” w odstępie kilku minut dały różne top 10, więc wyniki są zmienne.

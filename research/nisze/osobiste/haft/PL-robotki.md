# Haft i robótki w Polsce: jak rozszerzyć niszę pod Gridling (18.10.2026)

Punkt wyjścia: temat T3 z [../F-z-czatow.md](../F-z-czatow.md). Haft krzyżykowy dostał 3,75/5 przy popycie 22 498 wyszukań miesięcznie. Właściciel uważa, że to za mało na długi termin. Sprawdzam dwie drogi rozszerzenia: (1) „zdjęcie → wzór” w innych technikach, gdzie da się użyć silnika siatkowego Gridlinga, (2) szeroki serwis o robótkach ręcznych.

Metoda i wagi: [../../METODA.md](../../METODA.md). Zasady: [../BRIEF.md](../BRIEF.md). Bez treści prawnych, bez kontaktu z firmami, każda liczba ma endpoint albo URL i datę 18.10.2026.

Dane w [dane/](dane/):
- popyt: [PL-wolumeny.csv](dane/PL-wolumeny.csv) (346 fraz, 24 miesiące), [PL-popyt-podsumowanie.csv](dane/PL-popyt-podsumowanie.csv), [PL-labs-ogon.csv](dane/PL-labs-ogon.csv);
- SERP: [PL-serp-top10.csv](dane/PL-serp-top10.csv), [PL-serp-podsumowanie.csv](dane/PL-serp-podsumowanie.csv);
- rynek: [PL-ceny-zestawow.csv](dane/PL-ceny-zestawow.csv), [PL-reklamodawcy.csv](dane/PL-reklamodawcy.csv), [PL-konkurencja-ruch.csv](dane/PL-konkurencja-ruch.csv), [PL-programy.csv](dane/PL-programy.csv), [PL-zrodla-danych.csv](dane/PL-zrodla-danych.csv);
- wynik: [PL-ocena.csv](dane/PL-ocena.csv), [PL-rachunek.csv](dane/PL-rachunek.csv).

Skrypty: `/tmp/claude-0/-home-user/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/haft-1/` (`groups.py`, `vol.py`, `labs.py`, `serp_parse.py`, `serp_all.py`, `serp_csv.py`, `rachunek.py`, surowe odpowiedzi w `raw/` i `pages/`).

## Jak liczyłem

- **Popyt:** `/v3/keywords_data/google_ads/search_volume/live`, `location_code` 2616, `language_code` "pl", `date_from` 2024-10-01. Średnia to X.2025–IX.2026. „Zmiana 12m” to średnia z ostatnich 12 miesięcy wobec 12 wcześniejszych. „Trend r/r” to VII–IX 2026 wobec VII–IX 2025, jak w F.
- **Duplikaty:** Google Ads oddaje tę samą serię dla bliskich wariantów („włóczka” i „włóczki”, „haft krzyżykowy” i „haft półkrzyżykowy”). Frazę z identyczną serią 24 miesięcy (średnia ≥ 90) liczę raz. Dotyczy 9 fraz.
- **Anomalia:** „frywolitka” ma w III.2026 74 000 wyszukań przy medianie 1 900. Zastąpiłem ten miesiąc medianą (prawdopodobnie hasło z krzyżówki lub teleturnieju).
- **Brak danych:** 53 frazy nie mają danych w Google Ads (np. „kocyk na szydełko”, „koraliki prasowalne”, „lego mozaika ze zdjęcia”). Dla części dodałem formy, które Google liczy („na szydełku”, „koraliki do prasowania”).
- **Kontekst:** frazy szersze niż robótki („pasmanteria” 83 625, „gobelin” 6 092, „haft maszynowy”, „rękodzieło”) pokazuję osobno i nie wliczam do rdzenia.
- **Ogon:** `/v3/dataforseo_labs/google/keyword_suggestions/live` dla 14 słów bazowych. Labs przypisuje wolumen klastra wariantom, więc sumy traktuję jako górną granicę ([PL-labs-ogon.csv](dane/PL-labs-ogon.csv)).
- **SERP:** `/v3/serp/google/organic/live/advanced`, depth 10, z AI Overview ładowanym asynchronicznie, 11 fraz. Linki: `/v3/backlinks/bulk_referring_domains/live` dla 82 URL-i i 59 domen. Ruch konkurencji: `/v3/dataforseo_labs/google/bulk_traffic_estimation/live`.
- **Reklamy:** `/v3/serp/google/ads_advertisers/live/advanced` (wyszukiwarka reklamodawców po nazwie) i `/v3/serp/google/ads_search/live/advanced` (reklamy domeny w Google Ads Transparency, region PL).
- **Ceny:** strony sklepów czytane przez `/v3/on_page/content_parsing/live`, bo WebFetch nie rozwiązywał domen (ENOTFOUND).

## Oś 1: „zdjęcie → wzór” w innych technikach

### Popyt (średnio X.2025–IX.2026)

| Technika | Fraz z danymi | Średnio mies. | Zmiana 12m | Trend r/r | Min / max miesiąc | XI–XII w roku | Ważony CPC (USD) | Największe frazy |
|---|---|---|---|---|---|---|---|---|
| Haft krzyżykowy (T3, punkt odniesienia) | 20 | 22 498 | −12,7% | −6,7% | VI.2026 / X.2025 | 21,4% | 0,17 | mulina 7 183; kanwa 5 650; haft krzyżykowy 4 592 |
| Diamentowa mozaika | 20 | 28 932 | −28,3% | −6,8% | VI.2026 / XII.2025 | 24,9% | 0,19 | haft diamentowy 10 217; diamond painting 8 825; mozaika diamentowa 3 092 |
| Malowanie po numerach | 17 | 62 487 | −28,2% | −19,4% | VI.2026 / I.2026 | 25,0% | 0,36 | malowanie po numerach 33 367; obrazy do malowania po numerach 6 625; kolorowanie po numerach 6 525 |
| Koraliki prasowalne (Hama) | 11 | 18 326 | −16,6% | −4,9% | VI.2026 / XI.2025 | 22,4% | 0,17 | koraliki do prasowania 11 225; koraliki do prasowania wzory 3 925 |
| Pixel art | 17 | 49 565 | −26,9% | −24,3% | V.2026 / I.2026 | 16,6% | 0,53 | pixel art 32 833; pixel art pinterest 5 800; rysunki w kratkę 2 475 |
| Mozaika z klocków | 13 | 7 387 | +12,6% | +53,7% | X.2025 / XII.2025 | 28,7% | 0,17 | lego art 5 933 (linia LEGO Art); lego mozaika 260; obraz z klocków lego 255 |
| Szydełko i druty z obrazka | 14 | 2 066 | +33,4% | +59,5% | V.2026 / I.2026 | 20,2% | 0,31 | koc ze zdjęciem 630; filet crochet 519; tapestry crochet 367 |
| Haft matematyczny i string art | 6 | 3 699 | −11,0% | −26,6% | VII.2026 / XI.2025 | 21,8% | 0,19 | string art 2 050; haft matematyczny 990 |
| Haft ze zdjęcia | 8 | 1 491 | +0,1% | +25,4% | VIII.2026 / XI.2025 | 23,5% | 0,61 | haft na zamówienie 481; bluzy z haftem ze zdjęcia 458; haft ze zdjęcia 197; haft krzyżykowy ze zdjęcia 144 |
| **Razem oś 1 (bez T3, bez kontekstu)** | 106 | **173 953** | −24,7% | −15,1% | VI.2026 / I.2026 | 22,3% | 0,34 | |
| Kontekst: prezent ze zdjęciem | 11 | 31 739 | −3,0% | +2,5% | VII.2026 / XII.2025 | 28,0% | 0,97 | puzzle ze zdjęcia 7 933; karykatura ze zdjęcia 4 392; obraz ze zdjęcia 3 725 |

Źródło: `/v3/keywords_data/google_ads/search_volume/live`, 18.10.2026; szczegóły w [PL-popyt-podsumowanie.csv](dane/PL-popyt-podsumowanie.csv).

Co z tego wynika:
- **Rynek jest spory, ale spada.** Diamentowa mozaika i malowanie po numerach straciły po 28% w 12 miesięcy, pixel art 27%. Rośnie tylko mozaika z klocków (+12,6%, głównie linia LEGO Art) i drobne frazy o kocach ze zdjęciem.
- **Szczyt to grudzień i styczeń.** XI–XII to 22–29% rocznego popytu. Malowanie po numerach w I.2026 miało 95 200 wyszukań wobec 33 700 w VI.2026.
- „Haft diamentowy” i „diamond painting” mają różne serie, więc liczę je osobno. Mogą się jednak częściowo pokrywać, więc suma diamentowej mozaiki może być zawyżona.

### Podział intencji

Każdą frazę przypisałem do jednej intencji ([PL-wolumeny.csv](dane/PL-wolumeny.csv), kolumna `intencja`).

| Technika | Zestaw lub sklep | Wzór do zrobienia samemu | Gotowe ze zdjęcia (prezent) |
|---|---|---|---|
| Haft krzyżykowy (T3) | 15 801 | 1 987 | 0 (frazy „ze zdjęcia” liczę w wierszu „Haft ze zdjęcia”) |
| Diamentowa mozaika | 28 231 | 0 | 701 |
| Malowanie po numerach | 51 176 | 7 977 (głównie kolorowanki po numerach dla dzieci) | 3 334 |
| Koraliki prasowalne | 12 045 | 6 281 | 0 (brak danych dla „ze zdjęcia”) |
| Pixel art | 0 | 49 565 (rysowanie, Minecraft, Pinterest) | 0 |
| Mozaika z klocków | 5 933 | 446 | 1 008 |
| Szydełko i druty z obrazka | 0 | 1 436 | 630 |
| Haft matematyczny | 0 | 3 699 | 0 |
| Haft ze zdjęcia | 0 | 200 | 1 291 |

**Popyt, który naprawdę pasuje do Gridlinga, jest mały.** Frazy „ze zdjęcia” we wszystkich technikach dają razem 6 964 wyszukań miesięcznie. Z frazami o wzorach (bez pixel art i kolorowanek) wychodzi 21 033, czyli tyle, ile cały T3. Największy kawałek to „malowanie po numerach ze zdjęcia” (1 875) i „malowanie po numerach własne zdjęcie” (758). Reszta popytu to zakup gotowych zestawów w sklepach, Action, Pepco i na Allegro (np. „diamond painting action” 880 według Labs).

### Kto sprzedaje zestawy ze zdjęcia i za ile

| Technika | Sprzedawca | Cena | Uwagi |
|---|---|---|---|
| Malowanie po numerach | [wymalujtosam.pl](https://www.wymalujtosam.pl/malowanie-po-numerach-obraz-z-wlasnego-zdjecia/) | od 176,90 zł | 40x50 do 80x120 cm; na stronie także 316,90 zł i 381,90 zł; zwykłe zestawy od 84,90 zł |
| Malowanie po numerach | [picarta.pl](https://picarta.pl/produkt/malowanie-po-numerach-ze-zdjecia-obraz-na-plotnie/) | 196–319 zł | 40x40 cm za 196 zł; kurier 9,90 zł |
| Malowanie po numerach i haft diamentowy | [zuty.pl](https://www.zuty.pl/obraz-z-wlasnej-fotografii/) | cena ładowana skryptem, nie odczytałem | 40x50 i 80x100 cm; dodatkowy projekt 25 zł |
| Malowanie po numerach | [brushme.com/pl](https://brushme.com/pl/product/custom-paint-by-numbers) | nie odczytałem | komunikat: „Tymczasowo nie możemy przyjmować ani przetwarzać nowych zamówień” |
| Diamentowa mozaika | [diamentowapasja.pl](https://www.diamentowapasja.pl/haft-diamentowy-z-wlasnego-twojego-zdjecia-50-x-40-cm-diamond-painting-obrazy-diamentowe-z-diamencikami-p-94.html) | 155,00 zł | 50x40 cm, wysyłka 10 dni |
| Diamentowa mozaika | [swynk.com/pl](https://swynk.com/pl/products/diamond-painting-z-wlasnego-zdjecia) | 35 USD (dane strukturalne strony) | sklep z Holandii, realizacja ok. 20 dni |
| Haft krzyżykowy | [haftkrzyzykowy.com.pl](https://haftkrzyzykowy.com.pl/257-hafty-ze-zdj%C4%99%C4%87) | 360 zł i 460 zł | 30x40 i 40x50 cm; kanwa z nadrukiem i wzór, opracowanie ręczne |
| Haft krzyżykowy | [haftyzezdjecia.pl](https://haftyzezdjecia.pl/) | wycena indywidualna | ten sam właściciel (PH Gobelinek) |
| Mozaika z klocków, koraliki | nie znalazłem polskiej oferty z ceną | | SERP „lego mozaika” to zestaw LEGO 40179 na Allegro i porównywarce |

Wszystkie ceny: `/v3/on_page/content_parsing/live`, 18.10.2026 ([PL-ceny-zestawow.csv](dane/PL-ceny-zestawow.csv)).

Ważny wniosek: **sam wzór ze zdjęcia jest w Polsce darmowy.** AI Overview dla „haft krzyżykowy ze zdjęcia” poleca darmowe generatory pic2pat, Homiwork, HaftiX i PictureCraftwork, a w top 10 jest stitchmate.app z polską stroną z 10.10.2026. Dla malowania po numerach AI Overview poleca darmowy generator Davincified z PDF. Ludzie płacą 155–460 zł za fizyczny zestaw, a nie za plik.

### Kto płaci za reklamy

| Domena | Reklamodawca | Kreacji w PL | Ostatnio wyświetlona |
|---|---|---|---|
| hobbii.pl | Hobbii A/S | 300 | 18.10.2026 |
| brushme.pl | HOBBY ART TRADE sp. z o.o. | 68 | 18.03.2026 |
| wymalujtosam.pl | Honkee s.r.o. | 57 | 18.10.2026 |
| zuty.pl | Westlogic s.r.o. | co najmniej 40 | 18.10.2026 |
| coricamo.pl | MEGAT Dariusz Branny | 26 | 18.10.2026 |

Źródło: `/v3/serp/google/ads_search/live/advanced`, region PL, 18.10.2026 ([PL-reklamodawcy.csv](dane/PL-reklamodawcy.csv)).

- Dwaj najwięksi sprzedawcy zestawów ze zdjęcia to firmy czeskie (Honkee, Westlogic). Reklamują się nieprzerwanie od 2021–2022 roku, więc ten model im się opłaca.
- Wyszukiwarka reklamodawców dla „haft” zwraca firmy haftu komputerowego na odzieży (Haftkomp: 43 reklamy). To usługa B2B, nie robótki.
- CPC dla intencji „ze zdjęcia” jest wyższy niż dla haftu: „malowanie po numerach z własnego zdjęcia” 0,93 USD, „obraz po numerach ze zdjęcia” 0,78 USD, „haft na zamówienie” 0,79 USD. Dla porównania „haft krzyżykowy ze zdjęcia” ma 0,06 USD.

## Oś 2: szeroki serwis o robótkach

### Popyt grup (bez fraz kontekstowych)

| Grupa | Fraz | Średnio mies. | Zmiana 12m | Trend r/r | Min / max | Ważony CPC (USD) | Największe frazy |
|---|---|---|---|---|---|---|---|
| Szydełko | 34 | 55 453 | −23,3% | −15,4% | VI.2026 / I.2026 | 0,11 | szydełkowanie 9 892; torebka na szydełku 4 408; granny square 3 840 |
| Druty | 30 | 28 455 | −16,5% | −13,6% | VI.2026 / I.2026 | 0,09 | najpiękniejsze wzory na drutach 3 483; wzory na drutach 3 125 |
| Włóczka (sklepowe) | 19 | 35 043 | −5,5% | +1,9% | VI.2026 / XI.2025 | 0,21 | włóczka 10 417; kordonek 6 042; włóczka merino 2 523 |
| Makrama i frywolitka | 16 | 25 863 | −21,1% | −11,7% | VI.2026 / XI.2025 | 0,15 | makrama 10 742; sznurek do makramy 3 150; frywolitka 2 008 |
| Haft (inne techniki) | 20 | 19 166 | −7,9% | −25,1% | VII.2026 / I.2026 | 0,24 | haftowanie 2 500; punch needle 2 492; haft kaszubski 1 600; richelieu 1 900 |
| Robótki ogólnie | 7 | 12 525 | −2,5% | +2,1% | VI.2026 / XI.2025 | 0,16 | patchwork 8 450; filcowanie na sucho 1 445 |
| Amigurumi | 8 | 4 903 | −27,2% | −22,0% | VI.2026 / I.2026 | 0,14 | amigurumi 2 642; darmowe wzory amigurumi po polsku 757 |
| **Razem oś 2** | 134 | **181 408** | −16,3% | −11,9% | VI.2026 / I.2026 | 0,17 | |

Kontekst poza rdzeniem: „pasmanteria” 83 625, „gobelin” 6 092, „haft” 4 100, „szydełko” 3 542 (nawigacyjne lub niejednoznaczne).

Długi ogon jest duży. Labs zna 7 142 frazy z „na szydełku”, 3 471 z „na drutach” i 1 786 z „makrama” ([PL-labs-ogon.csv](dane/PL-labs-ogon.csv)). To dobra baza pod strony encji typu „czapka na szydełku” albo „bombka na szydełku 8 cm”, ale wolumeny Labs są zawyżone.

Formy z „na szydełko” (biernik) w Google Ads w większości nie mają danych, ale te same frazy z „na szydełku” mają: „torebka na szydełku” 4 408, „czapka na szydełku” 2 948. Pisząc treści, trzeba celować w formę z miejscownikiem.

### Kto wygrywa (11 SERP-ów, poziom URL)

| Fraza | Mediana domen do URL | Mediana domen do domeny bez platform | Domen < 50 | Wideo/social/forum/PDF | Stare (< 2023) lub PDF | Sklepy i marketplace | AIO |
|---|---|---|---|---|---|---|---|
| malowanie po numerach ze zdjęcia | 8 | 206 | 0 z 7 | 0 | 2 | 6 | tak |
| haft diamentowy ze zdjęcia | 0 | 0* | 2 z 8 | 1 | 1 | 7 | tak |
| haft krzyżykowy ze zdjęcia | 0 | 157 | 0 z 8 | 2 | 3 | 4 | tak |
| koraliki do prasowania wzory | 0 | 639 | 0 z 8 | 6 | 2 | 1 | nie |
| pixel art generator | 154 | 991 | 1 z 9 | 0 | 0 | 0 | tak |
| lego mozaika | 0 | 650 | 0 z 6 | 1 | 0 | 4 | nie |
| wzory na drutach | 0 | 494 | 1 z 9 | 5 | 4 | 1 | nie |
| czapka na szydełku | 0 | 50 | 0 z 7 | 5 | 5 | 1 | tak |
| amigurumi wzory | 0 | 123 | 0 z 8 | 4 | 1 | 3 | tak |
| makrama dla początkujących | 0 | 199 | 0 z 6 | 2 | 2 | 3 | tak (asynchr.) |
| ściegi na drutach | 0 | 1 853 | 1 z 8 | 3 | 6 | 1 | nie |

\* diamentowapasja.pl: 0 domen według `bulk_referring_domains` dla domeny bez „www”.

Źródło: `/v3/serp/google/organic/live/advanced` i `/v3/backlinks/bulk_referring_domains/live`, 18.10.2026 ([PL-serp-top10.csv](dane/PL-serp-top10.csv)). „Bez platform” pomija YouTube, Facebook, Pinterest, Reddit, Scribd, iStock, Allegro, Etsy, Empik i Domestika.

- **Konkretne podstrony nie mają linków.** Mediana domen linkujących do URL-a to 0 w 9 z 11 SERP-ów. Wygrywają domeny, a nie artykuły.
- **Robótki to wideo.** W „wzory na drutach” 5 z 9 wyników to YouTube (kanał Lousy Apostolopoulou: 4 filmy). W „czapka na szydełku” YouTube i Facebook zajmują 5 z 7 miejsc. W „ściegi na drutach” 6 z 8 wyników jest sprzed 2023 roku. Tekstowy serwis konkuruje tu z filmem, a nie ze słabym artykułem.
- **Wzory koralików to Pinterest.** 4 z 8 wyników „koraliki do prasowania wzory” to tablice Pinterest z 0 linków, obok blogu lecibocian.pl (2023). To najsłabszy SERP w badaniu.
- **„Ze zdjęcia” to sklepy.** W „malowanie po numerach ze zdjęcia” 6 z 7 wyników to sklepy (brushme, wymalujtosam, venuspuzzle, zuty, picarta). W „haft diamentowy ze zdjęcia” są 3 listingi Allegro.
- **Pixel art to globalne narzędzia AI** z setkami i tysiącami domen (dinopixel 2 157, pixilart 17 164). Polski serwis tu nie wejdzie bez dużego budżetu na linki.
- **AI Overview** jest w 7 z 11 SERP-ów (4 z 6 na osi 1, 3 z 5 na osi 2). Przy frazach „ze zdjęcia” AIO od razu wymienia darmowe generatory i sklepy, więc zabiera część kliknięć.

Ruch największych graczy jest umiarkowany (`bulk_traffic_estimation`, szacunek miesięczny): garnstudio.com (DROPS) 26 332, lecibocian.pl 18 718, ipicasso.pl 9 999, pasart.pl 7 989, e-dziewiarka.pl 7 904, brushme.pl 6 158, hobbii.pl 5 871, coricamo.pl 4 809, wymalujtosam.pl 3 043, zuty.pl 2 453 ([PL-konkurencja-ruch.csv](dane/PL-konkurencja-ruch.csv)). Generatory wzorów haftu mają w Polsce mały ruch: pic2pat.com 79, stitchmate.app 54, krzyzykowo.pl 34.

### Programy partnerskie (sprawdzone 18.10.2026, bez rejestracji)

| Program | Sieć | Stawka | Potwierdzone u źródła |
|---|---|---|---|
| Mila Druciarnia (włóczki, sznurki, kordonki) | webePartners | nie podano | tak, [strona programu](https://webepartners.pl/en/programy-partnerskie/mila-druciarnia-2/) |
| Hobbii | CJ Affiliate | 8%, cookie 14 dni | nie: tylko katalogi stron trzecich ([uppromote.com](https://uppromote.com/affiliate-program-directory/hobbii)); jeden podaje region „US only” |
| Hobbii #hobbiiCreators | program twórców | bez prowizji: darmowa włóczka i 10% kod rabatowy | tak, [hobbii.fi](https://hobbii.fi/pages/hobbii-creators) |
| Etsy | Awin | „case by case”, źródła trzecie podają 4% | częściowo: parser zwrócił pustą stronę [regulaminu](https://www.etsy.com/affiliates/terms) |
| Coricamo, wymalujtosam, zuty, picarta, artimento | | | programów nie znalazłem (WebSearch) |

Afiliacja w robótkach jest cienka: jeden potwierdzony polski program bez jawnej stawki. Największy reklamodawca (Hobbii, 300 kreacji) prowadzi program twórców za włóczkę, a nie za prowizję.

### Otwarte dane

- **Mulina DMC:** nie znalazłem tabeli z otwartą licencją. Same numery kolorów to fakty, ale wartości RGB z cudzych tabel mogą być chronione jako baza danych. Gridling ma już paletę DMC zgodną z Pattern Keeper, więc tę część ma pokrytą.
- **Mulina Ariadna:** producent publikuje PDF-y ([katalog 2025](https://ariadna.com.pl/wp-content/uploads/2026/03/Katalog-zdobnicze-2025.pdf), ulotka muliny z 2020). Licencji w nich nie ma. Narzędzie [FlossVerter](https://github.com/JuliaSzulc/flossverter) szuka zamienników DMC→Ariadna; licencji repozytorium nie sprawdziłem.
- **Oznaczenia ściegów:** standard symboli szydełkowych publikuje [Craft Yarn Council](https://craftyarncouncil.com/standards/crochet-chart-symbols). Warunków ponownego użycia nie znalazłem, więc rysunki symboli trzeba zrobić samemu.
- **Palety Hama, Artkal, Perler:** nie sprawdzałem. Bez nich Gridling nie zrobi wzoru koralików.

Wniosek: fosą jest silnik Gridlinga i własne palety, a nie otwarte dane. Czy używać numerów DMC i Ariadna z tabel producentów, decyduje właściciel ([PL-zrodla-danych.csv](dane/PL-zrodla-danych.csv)).

## Warianty i ocena

Skala popytu, którą stosuję: 5 to ponad 100 tys. w rdzeniu i trend nie gorszy niż −10%, 4 to ponad 20 tys. albo ponad 100 tys. przy mocniejszym spadku. Pół punktu oznacza, że wariant łączy części o różnych ocenach.

| Wariant | Popyt rdzenia (średnio mies.) | Popyt | SERP | Zarobek | Fosa | Ryzyko | **Wynik** | Dopasowanie do Gridlinga | Dopasowanie do profilu |
|---|---|---|---|---|---|---|---|---|---|
| A: tylko haft krzyżykowy | 22 498 (−12,7%) | 4 | 4 | 3 | 4 | 4 | **3,75** | 5 | 3 |
| B: haft + „zdjęcie → wzór” (bez pixel art) | 146 886 (−22,2%), z tego zdjęcie i wzory ok. 21 033 | 4 | 3,5 | 3,5 | 5 | 4 | **3,90** | 5 | 3 |
| C: pełne robótki (B + pixel art + oś 2) | 377 859 (−20,2%) | 4,5 | 3 | 3,5 | 4 | 4 | **3,73** | 3 | 3 |

Źródło ocen: [PL-ocena.csv](dane/PL-ocena.csv). Ocena A pochodzi z F, żeby dało się porównać.

Uzasadnienie:
- **SERP.** A: fora z 2006–2010 i krzyzykowo.pl z 1 domeną (F). B: frazy o wzorach słabe (Pinterest z 0 linków), frazy „ze zdjęcia” zajęte przez sklepy ze 150–650 domenami, plus AIO. C: dominacja YouTube w szydełku i drutach, DROPS z 18 467 domenami.
- **Zarobek.** A: tylko Gridling PL, którego jeszcze nie ma. B: ten sam Gridling plus wyższy CPC (0,34 USD wobec 0,17) i dowód, że ludzie płacą 155–460 zł za zestaw ze zdjęcia. C: dochodzi afiliacja włóczek, ale potwierdzony jest jeden program bez stawki, a CPC robótek to 0,09–0,24 USD.
- **Fosa.** B dostaje 5, bo jeden silnik obsłuży haft krzyżykowy, diamentową mozaikę, malowanie po numerach, koraliki i wzory szydełkowe (tapestry, C2C). Tego nie ma żaden polski konkurent w SERP. Wymaga to palet dla każdej techniki.
- **Ryzyko.** Żaden wariant nie jest YMYL ani nie wymaga treści prawnych. Wspólne ryzyka to AIO, spadek trendu (−20% do −28% w technikach „zestawowych”) i sezon (XI–I).

## Rachunek po 12 miesiącach (założenia, nie dane)

| Scenariusz | Ruch mies. | Wzory Gridling | Zestawy ze zdjęcia (marża) | Afiliacja | Reklamy | **Razem / mies.** | Bez zestawów |
|---|---|---|---|---|---|---|---|
| B ostrożny | 4 000 | 12 szt. = 254 zł | 0 | 0 | 18 zł | **272 zł** | 272 zł |
| B realny | 12 000 | 96 szt. = 2 036 zł | 18 szt. = 1 296 zł | 14 zł | 108 zł | **3 454 zł** | 2 158 zł |
| C ostrożny | 8 000 | 16 szt. = 339 zł | 0 | 19 zł | 36 zł | **395 zł** | 395 zł |
| C realny | 25 000 | 125 szt. = 2 651 zł | 25 szt. = 1 800 zł | 288 zł | 225 zł | **4 964 zł** | 3 164 zł |

Założenia ([PL-rachunek.csv](dane/PL-rachunek.csv), skrypt `rachunek.py`):
- **Ruch:** B 4 000 / 12 000, C 8 000 / 25 000 wizyt miesięcznie po 12 miesiącach. W F dla samego haftu przyjęto 3 000 / 10 000. B ma więcej popytu, ale frazy „ze zdjęcia” zajmują sklepy, więc podnoszę ruch ostrożnie.
- **Wzory:** konwersja 0,3% / 0,8% (B) i 0,2% / 0,5% (C, bo dużo ruchu z poradników), cena 4,99 EUR za wzór (sesja Gridling), kurs 4,25 zł/EUR. Kursu NBP nie pobrałem, bo API było zablokowane przez proxy. Rocznego dostępu nie liczę, bo nie znam jego ceny.
- **Zestawy:** tylko w wariancie realnym i tylko gdy właściciel zdecyduje się na druk i wysyłkę z dostawcą. Cena 180 zł (środek obserwowanych cen wejściowych 155–196 zł), marża 40%, konwersja 0,15% (B) i 0,1% (C).
- **Afiliacja:** CTR do sklepu 1–4%, konwersja 2–3%, koszyk 120 zł, stawka 5–8%. Stawki Mila Druciarnia nie znam.
- **Reklamy display:** 1,5 odsłony na wizytę, RPM 3 / 6 zł, jak w F.
- **Płatne reklamy Gridlinga:** 1 000 kliknięć po 0,30 USD przy konwersji 1% daje 10 wzorów (49,90 EUR) za 300 USD. Przy 0,74 USD i 2% to 20 wzorów (99,80 EUR) za 740 USD. Pojedynczy wzór za 4,99 EUR nie zwraca kosztu kliknięcia; reklamy mają sens tylko dla zestawów albo rocznego dostępu.

## Werdykt

**WARUNKOWO: wariant B, budowany od haftu krzyżykowego.** Serwis „wzór ze zdjęcia” dla haftu krzyżykowego, diamentowej mozaiki, malowania po numerach i koralików prasowalnych, z Gridlingiem PL jako produktem. Pełne robótki (C) dają 2,5 razy więcej popytu, ale ten ruch słabo zarabia i trafia na SERP-y zdominowane przez YouTube.

Warunki:
1. **Polska wersja Gridlinga** i palety dla nowych technik (diamenciki DMC, farby z numerami, koraliki Hama). Bez tego B nie ma płatnika.
2. **Decyzja o zestawach fizycznych.** Pieniądze w tej niszy są w zestawach (155–460 zł, reklamodawcy z Czech od 2021 roku), a nie w plikach, bo generatory plików są darmowe. Jeśli właściciel nie chce druku i wysyłki, realny przychód to ok. 2 158 zł zamiast 3 454 zł miesięcznie.
3. **Przewaga nad darmowymi generatorami** musi być widoczna na stronie: zgodność z Pattern Keeper, czytelny PDF, lista muliny DMC i Ariadna. Inaczej użytkownik zostaje przy pic2pat albo Stitchmate.
4. **Start przed sezonem.** Szczyt to XI–I, więc strony narzędzi i przewodniki powinny być zaindeksowane we wrześniu.

Rekomendowany zakres na start:
- narzędzie „zdjęcie → wzór” w 4 technikach (haft krzyżykowy, diamentowa mozaika, malowanie po numerach, koraliki prasowalne);
- strony encji: kolory muliny DMC i Ariadna z zamiennikami (fakty o numerach, własne próbki kolorów), wzory koralików według motywu (najsłabszy SERP w badaniu);
- poradniki T3 z F i krótkie przewodniki „jak wybrać zdjęcie”, „jaki rozmiar i ile kolorów” (pytania z PAA i AIO);
- szydełko i druty tylko tam, gdzie pracuje silnik: tapestry crochet, C2C, żakard, filet (rdzeń 2 066, +33% w 12 miesięcy).

Nie polecam na start: pixel art (globalne narzędzia AI z tysiącami domen, intencja dziecięca), ogólnych poradników szydełka i drutów (YouTube), mozaiki z klocków (popyt głównie na zestawy LEGO Art).

## Czego nie sprawdziłem

- Cen zuty.pl i brushme (ładowane skryptem) oraz ofert na Allegro (parser ich nie czyta).
- Stawki Mila Druciarnia i oficjalnej strony programu Hobbii; programów Empik i Allegro.
- Licencji palet Hama, Artkal i Perler oraz repozytorium FlossVerter.
- Ceny rocznego dostępu do Gridlinga i kosztu zestawów u dostawców (bez kontaktu z firmami).
- Kursu EUR/PLN z NBP (API zablokowane przez proxy).
- Ruchu z Pinteresta i YouTube, który w robótkach może być większy niż z Google.

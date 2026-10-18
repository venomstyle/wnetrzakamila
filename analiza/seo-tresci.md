# Analiza SEO on-page i treści: wnetrzakamila.pl

Data badania: **18.10.2026**. Wszystkie liczby pochodzą z DataForSEO, pobrane 18.10.2026. Przy każdej liczbie podaję endpoint w nawiasie:

- `[IP]` = `/v3/on_page/instant_pages` (enable_javascript, load_resources),
- `[CP]` = `/v3/on_page/content_parsing/live` (treść i nagłówki),
- `[CRAWL]` = zadanie `/v3/on_page/task_post` (crawl całej domeny, 49 adresów) i odczyty `/summary`, `/pages`, `/links`, `/non_indexable`, `/raw_html`,
- `[SERP]` = `/v3/serp/google/organic/live/advanced` („site:wnetrzakamila.pl”, Polska, pl),
- `[LABS]` = `/v3/dataforseo_labs/google/ranked_keywords/live`,
- `[KW]` = `/v3/keywords_data/google_ads/search_volume/live` (Polska, pl).

Bezpośrednie wejście na stronę (curl, przeglądarka) blokuje proxy sesji, więc cała analiza idzie przez DataForSEO. Na stronie niczego nie zmieniałem.

## Podsumowanie

1. **Blog ma 31 wpisów i ani jednego kalkulatora.** Lista bloga ma 4 strony i 31 tytułów [IP, CP], crawler znalazł 44 strony HTML [CRAWL]. Dział „Kalkulatory budowlane” jest w menu na każdej stronie (46 linków przychodzących [CRAWL]), a jego archiwum jest puste: 13 słów i komunikat „No results found.” [CP, CRAWL].
2. **20 z 31 wpisów to teksty „Ile kosztuje…?” z cenami bez źródeł i dat.** 25 wpisów nie ma ani jednego linku zewnętrznego, a 6 pozostałych linkuje do sklepów i portali, nie do cenników [CRAWL /links]. Według zasad projektu te kwoty nie mogą zostać na stronie w obecnej formie.
3. **Wpisy wyglądają na pisane masowo według jednego szablonu.** 31 tekstów opublikowano w 6 dni między 17.11 a 19.12.2025, w tym 10 wpisów 18.11.2025 w niecałe 6 godzin i 5 wpisów 19.12.2025 w 10 minut [IP: article:published_time]. Te same metafory (samochód, puzzle), te same zwroty („na czynniki pierwsze”, „tu wygrywasz lub przegrywasz”) i te same nagłówki powtarzają się w wielu tekstach [CP, IP]. Od 19.12.2025 nie ma nowych wpisów.
4. **Persona autora jest sprzeczna i niepotwierdzona.** /o-mnie/ mówi „pasjonat wnętrz… od kilku lat dzielę się poradami”, a stopka na każdym wpisie „absolwent architektury wnętrz, który po latach pracy w studio projektowym…” [CP]. Wpisy dodają historie z życia autora („rozmowy z klientami”, „setki litrów farby”, „mój nowy dom”). Nad tekstem nie ma podpisu autora, w schemacie autor to „kamil” małą literą [CRAWL /raw_html].
5. **Meta opisy i tytuły są słabe.** 19 z 31 wpisów nie ma meta opisu, a z 12 opisanych 10 przekracza 160 znaków; dwa opisy to wklejony pierwszy akapit (330 i 278 znaków) [IP]. 9 tytułów ma ponad 60 znaków, a strona główna ma tytuł „Home - Wnętrza Kamila” [IP].
6. **Wpisy liczą od 1147 do 2016 słów (mediana 1555) [IP], ale nie odpowiadają od pierwszego zdania.** W żadnym z 20 wpisów „Ile kosztuje…?” pierwsze zdanie nie podaje kwoty; wstępy zaczynają się od pytań do czytelnika („Marzysz o…”, „Zastanawiasz się…”, „Planujesz…”) [CP, IP: og:description].
7. **Liczby w różnych wpisach są ze sobą sprzeczne**, np. malowanie sufitu: „od 12 do 25 zł za metr kwadratowy” w jednym wpisie i „20-30 zł/m2” w drugim [CP]. Do tego są literówki i nieaktualne lata („w 2025 roku”, „Trendy … w 2024 i 2025 roku”) [CP, IP].
8. **Obrazy:** każdy wpis ma tylko zdjęcie główne, w treści nie ma zdjęć. 10 wpisów ma zdjęcie główne z pustym alt, a sprawdzone zdjęcia nowszych wpisów mają angielskie alty w stylu banków zdjęć („brown pencil on white printing paper”) [IP, CRAWL /raw_html]. Plus: obrazy idą przez CDN ShortPixel jako WebP z `srcset` i wymiarami [CRAWL /raw_html].

## Skąd dane i co objęło badanie

- **Lista wpisów:** mapa strony istnieje (`/sitemap_index.xml`, typ sitemap, 200 [IP]), ale DataForSEO nie zwraca treści XML. Pełną listę wziąłem z `/blog/` i `/blog/page/2–4/` (10 + 10 + 10 + 1 = 31 wpisów) [IP, CP] i potwierdziłem crawlem: 49 adresów, z tego 44 strony HTML z kodem 200 i 5 przekierowań 301 [CRAWL /summary]. Wpisów jest mniej niż 60, więc zbadałem wszystkie.
- **Wszystkie 31 wpisów** przeszły przez `[IP]` (tytuł, opis, H1–H3, słowa, obrazy, linki, kontrole). Pełną treść czytałem w `[CP]` dla 4 wpisów (projekt domu, sufit bez smug, ile kosztuje malowanie sufitu, ile kosztuje m2 malowania) i dla strony głównej, /o-mnie/, /blog/ i archiwum kalkulatorów. Wstępy pozostałych wpisów bez meta opisu sprawdziłem w `og:description`, które WordPress wypełnia pierwszymi zdaniami tekstu [IP]. Surowy HTML sprawdziłem dla 2 wpisów [CRAWL /raw_html].
- **Technologia (tylko jako tło):** WordPress z Yoast (schemat `@graph`), motyw GeneratePress/GenerateBlocks, generator „Elementor 4.3.5”, serwer LiteSpeed, hosting cyber_Folks (certyfikat), obrazy przez ShortPixel [IP, CRAWL /summary, /raw_html].

### Działy (kategorie) [CRAWL /links]

| Dział | Wpisów | Uwagi |
|---|---|---|
| Wnętrza (`/tematy/wnetrza/`) | 16 | 2 strony archiwum; część wpisów jest też w Remoncie |
| Remont (`/tematy/remont/`) | 21 | 3 strony archiwum; 15 z 21 to „Ile kosztuje…?” |
| Ogród (`/tematy/ogrod/`) | 4 | same koszty: projekt ogrodu, założenie ogrodu, trawnik, taras. Balkon jest w Wnętrzach |
| Kalkulatory budowlane | 0 | puste archiwum, link w menu na każdej stronie |

## Tabela zbadanych wpisów

Źródła kolumn: tytuł, długość title (z dopiskiem „ - Wnętrza Kamila”), opis, H1, słowa, „obraz bez alt” (kontrola `no_image_alt`), linki wewnętrzne wychodzące i data publikacji z `[IP]`; linki przychodzące z `[CRAWL /pages]` (`inbound_links_count`); dział z `[CRAWL /links]`. Dział: W = Wnętrza, R = Remont, O = Ogród. Każdy wpis ma dokładnie jeden H1, równy tytułowi wpisu.

| # | URL (ścieżka) | Tytuł strony (= H1) | Dział | Dł. title | Opis (dł.) | H1 | Słowa | Obraz bez alt | Linki wewn. | Linki przych. | Publikacja | Uwagi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | /ile-kosztuje-remont-mieszkania-60m2/ | Ile kosztuje remont mieszkania 60m2? | R | 53 | nie | 1 | 1816 | tak | 26 | 14 | 2025-11-17 | Brak opisu; głębokość kliknięć 3 |
| 2 | /ile-kosztuje-remont-dachu/ | Ile kosztuje remont dachu? | R | 43 | nie | 1 | 1475 | tak | 22 | 9 | 2025-11-17 | Brak opisu; ceny bez źródeł |
| 3 | /ile-kosztuje-remont-lazienki-kompletny-przewodnik-po-cenach-i-planowaniu/ | Ile kosztuje remont łazienki? | R | 46 | nie | 1 | 1463 | tak | 24 | 11 | 2025-11-17 | Brak opisu; slug dłuższy niż tytuł; czas czytania „1 minuta” przy 1463 słowach |
| 4 | /ile-kosztuje-remont-kuchni-kompletny-przewodnik-po-kosztach-i-planowaniu/ | Ile kosztuje remont kuchni? Kompletny przewodnik po kosztach i planowaniu | R | 90 | tak (330) | 1 | 1508 | tak | 24 | 19 | 2025-11-17 | Opis 330 zn. = 1. akapit; 5 „komentarzy” to pingbacki |
| 5 | /jaki-kolor-do-salonu-praktyczny-przewodnik-po-wyborze-idealnej-palety/ | Jaki kolor do salonu? Praktyczny przewodnik po wyborze idealnej palety | W+R | 87 | tak (278) | 1 | 1337 | tak | 19 | 31 | 2025-11-17 | Opis 278 zn. z literówką „rosie panika”; H2 „na 2025 rok” |
| 6 | /ile-kosztuje-wizualizacja-mieszkania/ | Ile kosztuje wizualizacja mieszkania? | W+R | 54 | nie | 1 | 1551 | nie | 27 | 9 | 2025-11-18 | Brak opisu; ceny bez źródeł |
| 7 | /ile-kosztuje-malowanie-drzwi/ | Ile kosztuje malowanie drzwi? | R | 46 | nie | 1 | 1867 | nie | 25 | 11 | 2025-11-18 | Brak opisu; najdłuższy czas czytania (11 min) |
| 8 | /ile-kosztuje-m2-malowania/ | Ile kosztuje m2 malowania? | W+R | 43 | nie | 1 | 1706 | nie | 26 | 20 | 2025-11-18 | Brak opisu; „w 2025 roku”; stawki sprzeczne z wpisem o suficie |
| 9 | /ile-kosztuje-malowanie-sufitu/ | Ile kosztuje malowanie sufitu? | W+R | 47 | nie | 1 | 1754 | nie | 26 | 24 | 2025-11-18 | Brak opisu; komentarze to 2 pingbacki |
| 10 | /ile-kosztuje-malowanie-elewacji/ | Ile kosztuje malowanie elewacji? | R | 49 | nie | 1 | 1600 | nie | 23 | 13 | 2025-11-18 | Brak opisu; ceny bez źródeł |
| 11 | /ile-kosztuje-projekt-lazienki/ | Ile kosztuje projekt łazienki? | W+R | 47 | nie | 1 | 2016 | tak | 24 | 12 | 2025-11-18 | Brak opisu; „słyszę… przy każdej rozmowie z klientami” |
| 12 | /ile-kosztuje-projekt-ogrodu/ | Ile kosztuje projekt ogrodu? | O | 45 | nie | 1 | 1882 | tak | 22 | 11 | 2025-11-18 | Brak opisu; nakłada się z założeniem ogrodu |
| 13 | /ile-kosztuje-projekt-kuchni/ | Ile kosztuje projekt kuchni? | W | 45 | nie | 1 | 1983 | tak | 24 | 11 | 2025-11-18 | Brak opisu; zdjęcie WebP z nazwą UUID |
| 14 | /ile-kosztuje-wymiana-okna/ | Ile kosztuje wymiana okna? | R | 43 | nie | 1 | 1766 | tak | 26 | 9 | 2025-11-18 | Brak opisu; ceny bez źródeł |
| 15 | /ile-kosztuje-umeblowanie-mieszkania/ | Ile kosztuje umeblowanie mieszkania? | W+R | 53 | nie | 1 | 1493 | tak | 25 | 14 | 2025-11-18 | Brak opisu; „Pamiętam moment, gdy pierwszy raz stanąłem…” |
| 16 | /ile-kosztuje-zrobienie-tarasu/ | Ile kosztuje zrobienie tarasu? | O | 47 | nie | 1 | 1312 | nie | 21 | 6 | 2025-11-19 | Brak opisu; ceny bez źródeł; 6 linków przychodzących |
| 17 | /ile-kosztuje-zalozenie-trawnika/ | Ile kosztuje założenie trawnika? | O | 49 | nie | 1 | 1550 | nie | 20 | 6 | 2025-11-19 | Brak opisu; „Sam pamiętam, jak stałem przed moim nowym domem” |
| 18 | /ile-kosztuje-zalozenie-ogrodu-przez-firme/ | Ile kosztuje założenie ogrodu przez firmę? | O | 59 | nie | 1 | 1597 | nie | 20 | 8 | 2025-11-19 | Brak opisu; nakłada się z projektem ogrodu i trawnikiem |
| 19 | /ile-kosztuje-wyniesienie-mebli-z-mieszkania/ | Ile kosztuje wyniesienie mebli z mieszkania? | R | 61 | nie | 1 | 1701 | nie | 23 | 6 | 2025-11-19 | Brak opisu; ceny bez źródeł |
| 20 | /ile-kosztuja-meble-kuchenne-na-wymiar/ | Ile kosztują meble kuchenne na wymiar? | W+R | 55 | nie | 1 | 1615 | nie | 23 | 8 | 2025-11-19 | Brak opisu; nakłada się z remontem i projektem kuchni |
| 21 | /jaki-kolor-scian-do-szarych-mebli/ | Jaki kolor ścian do szarych mebli? | W+R | 51 | tak (217) | 1 | 1474 | nie | 25 | 9 | 2025-11-23 | Opis 217 zn.; brak linków zewn. |
| 22 | /jak-pomalowac-sufit-bez-smug/ | Jak pomalować sufit bez smug? | R | 46 | tak (236) | 1 | 1614 | nie | 27 | 8 | 2025-11-23 | Nakłada się z „ile kosztuje malowanie sufitu”; „setki litrów farby” |
| 23 | /jak-pomalowac-salon-nowoczesnie/ | Jak pomalować salon nowocześnie? | W+R | 49 | tak (257) | 1 | 1555 | nie | 25 | 16 | 2025-11-23 | Nakłada się z „jaki kolor do salonu” |
| 24 | /jak-pomalowac-meble-kuchenne/ | Jak pomalować meble kuchenne? | R | 46 | tak (247) | 1 | 1417 | nie | 24 | 8 | 2025-11-23 | H2 powtarzane z innych wpisów („Wybór oręża”) |
| 25 | /jak-pomalowac-plytki-w-lazience/ | Jak pomalować płytki w łazience? | R | 49 | nie | 1 | 1546 | nie | 28 | 7 | 2025-11-23 | Brak opisu; H2 jak w meblach kuchennych |
| 26 | /ile-kosztuje-projekt-domu-kompletny-przewodnik-po-cenach/ | Ile kosztuje projekt domu? Kompletny przewodnik po cenach | W+R | 74 | tak (148) | 1 | 1147 | nie | 23 | 8 | 2025-12-18 | Ceny bez źródła i daty; opis „w 2025”; tytuł >60 |
| 27 | /jak-urzadzic-maly-balkon-praktyczny-poradnik-krok-po-kroku/ | Jak urządzić mały balkon? Praktyczny poradnik krok po kroku | W | 76 | tak (164) | 1 | 1155 | nie | 20 | 36 | 2025-12-19 | Balkon w dziale Wnętrza, nie w Ogrodzie; tytuł >60; opis >160 |
| 28 | /jak-urzadzic-maly-salon-w-bloku-praktyczny-poradnik-na-kazda-kieszen/ | Jak urządzić mały salon w bloku? Praktyczny poradnik na każdą kieszeń | W | 86 | tak (188) | 1 | 1218 | nie | 20 | 36 | 2025-12-19 | Jedna z 2 fraz w top 100 (poz. 48); tytuł 86 |
| 29 | /jak-urzadzic-mala-kuchnie-praktyczny-poradnik-krok-po-kroku/ | Jak urządzić małą kuchnię? Praktyczny poradnik krok po kroku | W | 77 | tak (177) | 1 | 1571 | nie | 21 | 36 | 2025-12-19 | Jedna z 2 fraz w top 100 (poz. 83); H2 „Trendy … w 2024 i 2025 roku” |
| 30 | /jak-urzadzic-pokoj-mlodziezowy-praktyczny-poradnik-dla-rodzicow/ | Jak urządzić pokój młodzieżowy – praktyczny poradnik dla rodziców | W | 82 | tak (169) | 1 | 1586 | nie | 22 | 8 | 2025-12-19 | Brak zdjęcia głównego (brak og:image) |
| 31 | /jak-urzadzic-pokoj-dziecka-praktyczny-poradnik-dla-rodzicow/ | Jak urządzić pokój dziecka – praktyczny poradnik dla rodziców | W | 78 | tak (160) | 1 | 1166 | nie | 23 | 7 | 2025-12-19 | Struktura jak u pokoju młodzieżowego (strefy snu/nauki) |

### Strony, które nie są wpisami

| URL | Tytuł | Dł. title | Opis | H1 | Słowa | Linki przych. | Uwagi |
|---|---|---|---|---|---|---|---|
| / | Home - Wnętrza Kamila | 21 | nie | „Piękne Wnętrza, Krok po Kroku” | 167 | 45 | Tytuł bez frazy; brak opisu; obraz bez alt [IP] |
| /o-mnie/ | O mnie - Wnętrza Kamila | 23 | nie | brak (pierwszy nagłówek to H2 „Cześć, jestem Kamil”) [CP] | 91 | 45 | Bio sprzeczne ze stopką [CP] |
| /blog/ (+ /page/2–4/) | Blog - Wnętrza Kamila | 21 | nie | brak [IP] | 59 | 16 | `og:url` strony 2 wskazuje na /blog/ [IP] |
| /tematy/remont/ (+2 strony) | Archiwa Remont - Wnętrza Kamila | 31 | nie | - | 60 | 46 | Brak wstępu do działu [CRAWL] |
| /tematy/wnetrza/ (+1 strona) | Archiwa Wnętrza - Wnętrza Kamila | 32 | nie | - | 60 | 46 | jw. |
| /tematy/ogrod/ | Archiwa Ogród - Wnętrza Kamila | 30 | nie | - | 29 | 46 | 4 wpisy [CRAWL] |
| /tematy/kalkulatory-budowlane/ | Archiwa Kalkulatory budowlane - Wnętrza Kamila | 46 | nie | - | 13 | 46 | Puste: „No results found.” [CP] |

Słowa i linki przychodzące: `[CRAWL /pages]`. Crawler oznaczył 8 stron list (archiwa i /blog/) jako duplikaty treści, bo poza tytułami wpisów prawie nie mają tekstu [CRAWL /summary, /pages].

## Problemy

### 1. Ceny bez źródeł i dat (zasada projektu)

- 20 wpisów ma w tytule „Ile kosztuje/kosztują”, a kolejne mają sekcje z kosztami (np. „Ile to wszystko kosztuje?” w /jak-pomalowac-sufit-bez-smug/, „Ile to kosztuje? Realne spojrzenie na budżet” w /jak-pomalowac-salon-nowoczesnie/) [IP].
- Linki zewnętrzne ma tylko 6 wpisów (15 linków w całym serwisie), wszystkie do sklepów i portali: IKEA, Westwing, Homebook, Murator, Meble.pl, Dobrzemieszkaj, Twój Ogródek, Archipelag, Extradom, Izba Architektów [CRAWL /summary, /links]. Żaden nie jest źródłem podanej kwoty.
- **Wpis /ile-kosztuje-projekt-domu-kompletny-przewodnik-po-cenach/** (opublikowany 18.12.2025, zmieniony 18.12.2025 [IP]) podaje m.in.: gotowy projekt „od 2000 złotych… nawet 6000-8000 złotych”, adaptacja „od 1500 do 3500 złotych”, projekt indywidualny „od około 15 000 złotych… 50 000-80 000 złotych”, mapa do celów projektowych „1000-2000 złotych”, badania geotechniczne „od 800 do 2500 złotych”, projekt wnętrz „od 5000 do 20 000 złotych”, dokumentacja dla domu 120–150 m² „8000-25 000 złotych” [CP]. **Żadna kwota nie ma źródła ani daty sprawdzenia.** Linki do Archipelagu i Extradomu wskazują tylko, gdzie kupić projekt, a link do Izby Architektów dotyczy rady „wybieraj architektów z uprawnieniami” [CP]. Meta opis mówi „Ile kosztuje projekt domu w 2025?”, więc jest już nieaktualny [IP]. Podsumowanie każe doliczyć „minimum 3000-5000 złotych na mapę, badania gruntu i uzgodnienia”, a dolne granice podane wyżej to razem ok. 1800 zł plus „od kilkudziesięciu” zł za uzgodnienie [CP]. Rachunek się nie zgadza.
- Teksty podają też procenty bez źródła, np. „W stolicy możesz zapłacić nawet o 30% więcej niż w miejscowości powiatowej” i robocizna „stanowi 60-70% całkowitego kosztu” (/ile-kosztuje-m2-malowania/), „90% sukcesu … leży w przygotowaniu powierzchni” (/jak-pomalowac-sufit-bez-smug/), „Tysiące Polaków boryka się z tym samym wyzwaniem” (balkon) [CP].
- Wpis o projekcie domu omawia też formalności (pozwolenie na budowę, uzgodnienia, projekt budowlany i wykonawczy) [CP]. Treści prawne są w tym projekcie do decyzji właściciela.

### 2. Liczby sprzeczne między wpisami

Wszystkie cytaty z `[CP]`:

| Temat | Wpis A | Wpis B |
|---|---|---|
| Robocizna, malowanie sufitu | /ile-kosztuje-malowanie-sufitu/: „od 12 do 25 zł za metr kwadratowy” | /ile-kosztuje-m2-malowania/: „Malowanie sufitów: 20-30 zł/m2” |
| Cena farby | /ile-kosztuje-malowanie-sufitu/: „farbę emulsyjną za 20-30 zł za litr” oraz „Przyzwoita farba sufitowa kosztuje 30-50 zł za litr” | /ile-kosztuje-m2-malowania/: „Farba emulsyjna to koszt około 10-25 złotych za litr”; /jak-pomalowac-sufit-bez-smug/: „Dobra farba sufitowa (10l): ok. 150-250 zł” |
| Dwie warstwy na ścianach | /ile-kosztuje-m2-malowania/: „Dwie warstwy: 28-35 zł/m2” | ten sam wpis, podsumowanie: „średnio 25-35 złotych za standardowe malowanie dwoma warstwami” |

### 3. Sygnały masowego generowania treści

Z zewnątrz nie da się stwierdzić, jak teksty powstały. Poniższe wzorce są jednak typowe dla treści pisanych seryjnie według szablonu:

- **Tempo publikacji** [IP: article:published_time]: 17.11.2025: 5 wpisów; 18.11.2025: 10 wpisów w godzinach 07:35–13:20 (projekt ogrodu i projekt łazienki w odstępie 1,5 minuty); 19.11.2025: 5; 23.11.2025: 5; 18.12.2025: 1; 19.12.2025: 5 w godzinach 16:12–16:22. Od tamtej pory nie ma nowych wpisów.
- **Te same metafory** [CP, LABS: fragment z wyników]: „Pomyśl o tym jak o zakupie samochodu” (projekt domu), „to jak z zakupem samochodu. Możesz kupić używaną Fabię albo nową Tesłę” (m2 malowania), „remont kuchni to jak budowanie samochodu” (remont kuchni); „Remont kuchni to jak układanie puzzli” (remont kuchni), „To trochę jak składanie puzzli” (malowanie sufitu), „Mała kuchnia to jak puzzle” (mała kuchnia).
- **Te same zwroty**: „na czynniki pierwsze” we wstępach lub nagłówkach 6 wpisów: m2 malowania, malowanie drzwi, wizualizacja, remont łazienki, malowanie sufitu i remont kuchni (H2 „Rozbijamy koszty na czynniki pierwsze”) [CP, IP].
- **Te same nagłówki** [IP]: „Przygotowanie – tu wygrywasz lub przegrywasz” (meble kuchenne, płytki) i „Przygotowanie podłoża – tu wygrywasz lub przegrywasz” (sufit); „Wybór oręża” (meble kuchenne, płytki); „(Nie bądź leniwy!)” (salon nowocześnie, meble kuchenne); „Podsumowanie – ile tak naprawdę wydasz?” (4 wpisy); „Ukryte koszty, o których musisz wiedzieć” (3 wpisy); „Dodatkowe koszty, o których musisz wiedzieć” w drobnych wariantach („warto pamiętać”, „musisz pamiętać”, „warto wiedzieć”) (7 wpisów); „Błędy, których warto unikać” (3 wpisy).
- **Ten sam schemat tytułów**: „Ile kosztuje X?” (20), „Jak urządzić X – praktyczny poradnik…” (5), „Kompletny przewodnik po…” (2 tytuły i 1 slug) [IP].
- **Literówki i błędy, których nikt nie poprawił** [CP, IP]: „nową Tesłę”, „ta różnica widać gołym okiem”, „Brzmi kuszącą, prawda?”, „stare folię” (m2 malowania); „farba schnąć za szybko”, „Malowanie dwukrotnym kolorem” (malowanie sufitu); „czujesz, jak rosie panika” (meta opis „jaki kolor do salonu”).
- **Ogólniki zamiast konkretu**, np. „Szybkie, konkretne porady, dzięki którym stworzysz przestrzeń idealnie dopasowaną do Ciebie” (strona główna), „Odpowiedź brzmi: to zależy” (malowanie sufitu, m2 malowania) [CP].

### 4. Zaufanie i E-E-A-T

- **Sprzeczne bio.** /o-mnie/: „Pasjonat wnętrz… Od kilku lat dzielę się praktycznymi poradami” (91 słów, bez konkretów o wykształceniu czy pracy) [CP, CRAWL]. Stopka i panel boczny na każdym wpisie: „Kamil to absolwent architektury wnętrz, który po latach pracy w studio projektowym postanowił podzielić się swoją wiedzą” [CP].
- **Niepotwierdzone historie autora w tekstach** [CP, IP: og:description]: „Jako ktoś, kto w życiu wypaprał setki litrów farby” (sufit bez smug), „To pytanie słyszę niemal przy każdej rozmowie z klientami” i H2 „Moje osobiste doświadczenia i rada na koniec” (projekt łazienki), „Sam pamiętam, jak stałem przed moim nowym domem” (trawnik), „Pamiętam moment, gdy pierwszy raz stanąłem przed pustym mieszkaniem” (umeblowanie), „Kiedy sam zaczynałem myśleć o zagospodarowaniu przestrzeni wokół domu” (projekt ogrodu), „Z mojego doświadczenia wiem” (malowanie sufitu). Zasady projektu dopuszczają tylko fakty potwierdzone przez właściciela.
- **Fałszywa obietnica:** „ODKRYJ BLOGA. Znajdziesz tam setki porad” (sufit bez smug), a blog ma 31 wpisów [CP]. Ten sam wpis odsyła do „naszych kalkulatorów budowlanych”, czyli do pustego archiwum [CP].
- **Brak podpisu autora i daty aktualizacji.** Nad tekstem jest tylko data publikacji, np. „18 grudnia, 2025”; autora nie ma [CRAWL /raw_html]. W schemacie Article autor to „kamil” małą literą, a wydawcą jest ta sama osoba [CRAWL /raw_html].
- **Brak stron kontakt i polityki prywatności** wśród 44 stron HTML znalezionych przez crawler [CRAWL /pages], choć formularz komentarzy zbiera imię i e-mail [CP]. Treści prawne należą do decyzji właściciela; tu chodzi o sygnał zaufania.
- **„Komentarze” to pingbacki z własnych wpisów.** Na przykład „5 komentarzy” pod remontem kuchni to 5 wpisów „Pingback: …” z tego samego bloga, podobnie pod m2 malowania (2) i malowaniem sufitu (2) [CP, CRAWL /raw_html]. Linki pingbacków mają `nofollow`, przez co crawler oznacza 17 wpisów jako „link relation conflict” [CRAWL /summary, /non_indexable]; same wpisy mają `index, follow` [CRAWL /raw_html].
- **Nieaktualne daty w treści:** „w 2025 roku” (m2 malowania), „Trendy w urządzaniu małych kuchni w 2024 i 2025 roku” (mała kuchnia), „Modne połączenia kolorystyczne na 2025 rok” (kolor do salonu), „w 2025?” (opis projektu domu) [CP, IP].
- **Zdjęcia nie są własne**, więc nie budują doświadczenia. Patrz punkt 8.

### 5. Tytuły i meta opisy [IP]

- Każdy tytuł ma dopisek „ - Wnętrza Kamila” (17 znaków). 9 tytułów ma ponad 60 znaków (74–90), w 8 z nich DataForSEO zgłasza `title_too_long` [IP, CRAWL /summary]. Najdłuższy ma 90 znaków: „Ile kosztuje remont kuchni? Kompletny przewodnik po kosztach i planowaniu - Wnętrza Kamila”.
- Wszystkie 31 tytułów są różne i zawierają frazę główną [IP]. Tytuły „Ile kosztuje X?” nie mają jednak żadnej zachęty ani konkretu (zakresu, roku sprawdzenia, kalkulatora).
- Doklejki „Praktyczny poradnik krok po kroku”, „na każdą kieszeń”, „dla rodziców” zajmują miejsce w wynikach: Google ucina dwa tytuły do „Praktyczny poradnik na ...” i „praktyczny poradnik dla ...” [SERP].
- Meta opis: brak w 19 z 31 wpisów, na stronie głównej, w /o-mnie/, /blog/ i archiwach (razem 32 strony [CRAWL /summary]). Z 12 opisanych wpisów 10 ma ponad 160 znaków (164–330). Dwa opisy to przeklejony pierwszy akapit: remont kuchni (330 zn.) i kolor do salonu (278 zn., z literówką).
- Strona główna: tytuł „Home - Wnętrza Kamila”, H1 „Piękne Wnętrza, Krok po Kroku”, czyli bez frazy, o której jest serwis [IP].

### 6. Nagłówki i odpowiedź na intencję

- Każdy wpis ma jeden H1 równy tytułowi i spis treści [IP, CP]. Ten porządek jest w porządku.
- Szablon motywu dokłada do każdego wpisu nagłówki niezwiązane z tekstem: H2 „Podobne wpisy”, H2 „Witaj na moim blogu!”, H3 „Powiązane wpisy:”, H3 z trzema tymi samymi tytułami (balkon, salon w bloku, mała kuchnia) i H3 „Dodaj komentarz” [IP]. Liczba komentarzy też trafia do H2 („5 komentarzy do…”).
- Blog nie ma H1, /o-mnie/ zaczyna się od H2; crawler znalazł 5 stron bez H1 [IP, CP, CRAWL /summary].
- **Odpowiedź od pierwszego zdania:** w żadnym z 20 wpisów kosztowych pierwsze zdanie nie podaje kwoty [CP, IP: og:description]. Przykłady wstępów: „Marzysz o własnym domu, ale nie wiesz, od czego zacząć?” (projekt domu), „Stoisz w swoim salonie, patrzysz w górę i widzisz sufit, który widział lepsze czasy.” (malowanie sufitu), „Remont kuchni to jak układanie puzzli” (remont kuchni). Kwoty pojawiają się dopiero pod nagłówkami, po wstępie i spisie treści. W /ile-kosztuje-wymiana-okna/ i remoncie łazienki wstęp wspomina kwoty tylko w anegdocie („Jeden powie 500 złotych, drugi 2000”; „Jedna osoba wyremontuje małą łazienkę za 10 tysięcy, inna wyda 50 tysięcy”) [IP: og:description].
- Wpis o remoncie łazienki ma w danych „Szacowany czas czytania: 1 minuta” przy 1463 słowach [IP: twitter:data2], co sugeruje, że wtyczka nie widzi treści.

### 7. Linkowanie wewnętrzne

- Wpisy mają 19–28 linków wewnętrznych, ale większość to nawigacja: menu (w wersji na komputer i telefon), 4 „Powiązane wpisy” i stały blok „Podobne wpisy” [IP, CP].
- **Blok „Podobne wpisy” zawsze pokazuje te same 3 teksty** z 19.12.2025 (balkon, salon w bloku, mała kuchnia) [IP]. Dlatego mają one po 36 linków przychodzących, a taras, trawnik i wyniesienie mebli po 6 [CRAWL /pages].
- 7 wpisów jest 3 kliknięcia od strony głównej (projekt łazienki, projekt kuchni, remont 60 m², remont kuchni, umeblowanie, remont dachu, remont łazienki) [CRAWL /pages: click_depth].
- Linki w treści istnieją (np. sufit bez smug → wymiana okna, malowanie sufitu, m2 malowania, projekt ogrodu) [CP], ale część prowadzi do archiwów działów z ogólnym anchorem: „remontu”, „remontów”, „remont”, „wnętrz”, „wnętrza” [CP]. Do pustych „kalkulatorów” linkuje menu na każdej stronie i tekst wpisu o suficie [CRAWL /links, CP].
- Wzmianka bez linku: „zajrzyj do mojego artykułu o tym, ile kosztuje projekt łazienki” (sufit bez smug) nie ma odnośnika, choć taki wpis istnieje [CP].
- 5 linków prowadzi do przekierowań 301 (np. `/blog` bez ukośnika ze strony głównej i z wpisu o umeblowaniu; `/tematy/...` bez ukośnika ze strony głównej) [CRAWL /links, /summary: has_links_to_redirects 5].
- Brak hubów: archiwa działów to same listy tytułów bez wstępu (29–60 słów) [CRAWL /pages].

### 8. Obrazy [IP, CRAWL /raw_html]

- **W treści wpisów nie ma zdjęć.** Każdy wpis ma tylko zdjęcie główne; `[IP]` liczy 1–2 obrazy na stronę. W surowym HTML dwóch wpisów poza zdjęciem głównym są tylko miniatury „Podobnych wpisów” i dekoracyjna grafika `flower.svg` (alt „Flower”). Wpis o pokoju młodzieżowym nie ma zdjęcia głównego (brak `og:image`) [IP].
- **10 wpisów ma zdjęcie główne z pustym alt** (kontrola `no_image_alt` [IP]; w remoncie kuchni potwierdzone `alt=""` [CRAWL /raw_html]). To 10 najstarszych wpisów (17–18.11.2025) z nazwami plików typu `remont-kuchni-scaled.jpg` oraz `14f55b17-…webp` (projekt kuchni) [IP: og:image].
- **20 nowszych wpisów ma nazwy plików z 11 losowych znaków** (np. `fter0e2bzko.jpg`, `1viezivk1as.jpg`) [IP: og:image]. **Alty sprawdzonych 4 takich zdjęć są po angielsku**: „brown pencil on white printing paper” (projekt domu), „2 brown wooden armchairs beside white wall”, „gray fabric loveseat near brown wooden table”, „white and black gas range oven” [CRAWL /raw_html]. Taki format nazw i opisów jest typowy dla zdjęć z banku Unsplash, ale źródło musi potwierdzić właściciel. Alt po angielsku nie pomaga w polskim wyszukiwaniu.
- **Format i rozmiar są dobre:** obrazy idą przez CDN ShortPixel z konwersją do WebP (`to_webp`), mają `srcset`, `width` i `height` [CRAWL /raw_html]. Oryginały to JPEG do 2560 px (`-scaled.jpg`) [IP: og:image]. AVIF nie jest używany.
- **Leniwe ładowanie obejmuje też zdjęcie główne:** element ma jednocześnie `fetchpriority="high"` i `data-lazyloaded="1"` (LiteSpeed), czyli obraz z górnej części strony ładuje się dopiero przez skrypt [CRAWL /raw_html]. To może opóźniać LCP; szczegóły dla analizy technicznej.

### 9. Adresy URL

- Adresy są czytelne, po polsku bez znaków diakrytycznych, bez parametrów [IP: seo_friendly_url].
- 8 slugów ma doklejki z tytułu: „-praktyczny-poradnik-krok-po-kroku”, „-praktyczny-poradnik-na-kazda-kieszen”, „-praktyczny-poradnik-dla-rodzicow”, „-kompletny-przewodnik-po-cenach(-i-planowaniu)”, „-praktyczny-przewodnik-po-wyborze-idealnej-palety”. Najdłuższe mają 74 znaki ścieżki [IP: relative_url_length].
- /ile-kosztuje-remont-lazienki-kompletny-przewodnik-po-cenach-i-planowaniu/ ma tytuł „Ile kosztuje remont łazienki?”, więc slug nie zgadza się z tytułem [IP].
- Wpisy rankują słabo i mają mało linków z zewnątrz, więc skracanie slugów niewiele daje. Jeśli właściciel się zdecyduje, potrzebne są przekierowania 301.

### 10. Treści cienkie, duplikaty i kanibalizacja

- **Wpisy nie są cienkie** (1147–2016 słów [IP]). Cienkie są strony list: archiwa i blog (13–60 słów), /o-mnie/ (91), strona główna (167) [CRAWL /pages]. Puste archiwum kalkulatorów może być uznane przez Google za stronę bez wartości (soft 404).
- **Ryzyko kanibalizacji.** Dziś serwis ma tylko 2 frazy w top 100 [LABS], więc kanibalizacji nie da się zmierzyć w wynikach. Tematy nakładają się jednak tak, że przy wzroście widoczności strony będą ze sobą konkurować:
  - **Sufit:** /jak-pomalowac-sufit-bez-smug/ (ma sekcję „Ile to wszystko kosztuje?”), /ile-kosztuje-malowanie-sufitu/ (ma sekcje „Czy warto malować sufit samodzielnie?” i „Kiedy najlepiej malować sufit?”) i /ile-kosztuje-m2-malowania/ (ma stawki za sufity) [IP, CP]. Do tego sprzeczne liczby (punkt 2).
  - **Kolor salonu:** /jaki-kolor-do-salonu-…/, /jak-pomalowac-salon-nowoczesnie/ (H2 „Kolory, które rządzą nowoczesnym salonem”) i /jaki-kolor-scian-do-szarych-mebli/ („odmień swój salon”) [IP].
  - **Ogród:** /ile-kosztuje-projekt-ogrodu/, /ile-kosztuje-zalozenie-ogrodu-przez-firme/ (H3 „Projekt ogrodu”, „Trawnik”) i /ile-kosztuje-zalozenie-trawnika/ [IP].
  - **Kuchnia:** /ile-kosztuje-remont-kuchni-…/, /ile-kosztuja-meble-kuchenne-na-wymiar/ i /ile-kosztuje-projekt-kuchni/: każdy podaje własne budżety [IP].
  - **Pokój dziecka i młodzieżowy:** ten sam układ („Strefa snu i odpoczynku”, „Strefa nauki”) [IP]. Intencje są różne, więc wystarczy różnicować treść.

### 11. Kalkulatory

- **Na stronie nie ma żadnego kalkulatora.** Archiwum `/tematy/kalkulatory-budowlane/` ma tytuł „Archiwa Kalkulatory budowlane - Wnętrza Kamila”, 13 słów, komunikat „No results found.” i 0 wpisów [CP, CRAWL /pages, /links]. Nie da się więc sprawdzić, czy kalkulatory działają bez JS ani czy mają treść wokół.
- Link „Kalkulatory budowlane” jest w menu każdej strony i w treści wpisu o suficie [CRAWL /links, CP], więc użytkownik trafia na pustą stronę.
- Popyt na takie narzędzia istnieje (miesięczne wyszukiwania w Polsce [KW, 18.10.2026]): „kalkulator betonu” 4400, „kalkulator styropianu” 1900, „kalkulator budowlany” 720, „ile farby na m2” 720, „kalkulator płytek” 320, „kalkulator farby” 260, „kalkulator paneli podłogowych” 210, „kalkulator tapety” 210, „kalkulator kostki brukowej” 170, „kalkulator gładzi” 30. Konkurencji w SERP nie badałem.

### 12. Luki tematyczne względem działów

Na podstawie tytułów 31 wpisów i przypisania do działów [IP, CRAWL /links]:

- **Kalkulatory:** 0 treści przy dziale w menu (punkt 11).
- **Ogród:** 4 wpisy, wszystkie o kosztach. Nie ma poradników (zakładanie i pielęgnacja trawnika krok po kroku, rośliny, nawadnianie, taras krok po kroku). Wpis o balkonie jest w Wnętrzach.
- **Remont:** 15 z 21 wpisów to koszty. Poradniki „jak zrobić” dotyczą tylko malowania (4 wpisy). Nie ma tematów typu gładzie, panele, płytki, fugi, tapetowanie, ile materiału kupić, kolejność prac.
- **Wnętrza:** są salon, mała kuchnia, balkon, pokój dziecka i młodzieżowy, kolory. Nie ma sypialni, łazienki (aranżacja), przedpokoju, oświetlenia, stylów, przechowywania.
- Luki opisuję tylko według tytułów; wolumeny tych fraz trzeba sprawdzić przy planie treści.

## Lista problemów z priorytetem

P1 = najpierw (uczciwość, zasady projektu, puste sekcje), P2 = ważne dla SEO, P3 = porządki.

| # | Priorytet | Problem | Zakres | Rekomendacja | Decyzja właściciela? |
|---|---|---|---|---|---|
| 1 | P1 | Ceny i procenty bez źródeł i dat | 20 wpisów „Ile kosztuje” + sekcje kosztów w poradnikach | Każdą kwotę potwierdzić dziś u źródła (cennik, raport) z datą sprawdzenia albo zastąpić „sprawdź w cenniku” z linkiem. Do czasu poprawy rozważyć `noindex` lub zdjęcie wpisów z samymi szacunkami | Tak: co zdjąć, co poprawić |
| 2 | P1 | Sprzeczne i niepotwierdzone bio autora oraz historie „z życia” | Stopka, /o-mnie/, min. 7 wpisów | Ustalić z właścicielem prawdziwe fakty o autorze; usunąć zdania o studiu, klientach, „setkach litrów farby”, własnym domu, jeśli nie są prawdziwe | Tak |
| 3 | P1 | Pusty dział „Kalkulatory budowlane” w menu | Menu na 46 stronach, wpis o suficie | Do czasu zbudowania kalkulatorów usunąć pozycję z menu i link z tekstu albo ustawić `noindex` na archiwum. Kalkulatory budować jako osobne strony z opisem metody i treścią wokół (działające bez JS przynajmniej w podstawowym wyniku) | Tak: czy kalkulatory wchodzą do planu |
| 4 | P1 | Treść seryjna: wspólne metafory, zwroty, nagłówki, literówki | Prawie wszystkie wpisy | Przepisać według zasad stylu projektu (odpowiedź w pierwszym zdaniu, konkret, źródła, bez ozdobników); zacząć od tekstów, które mają szansę rankować | Tak: zakres przepisania |
| 5 | P1 | Sprzeczne liczby między wpisami | Malowanie: sufit, m2, sufit bez smug | Ujednolicić dane z jednego potwierdzonego źródła i linkować do jednego wpisu kosztowego | Nie |
| 6 | P2 | Brak odpowiedzi w pierwszym zdaniu | 20 wpisów kosztowych | Zacząć od zakresu z datą i źródłem albo od odesłania do cennika; potem wyjaśnienie | Nie |
| 7 | P2 | Brak meta opisów lub opisy za długie | 19 wpisów bez opisu, 10 za długich, strona główna, archiwa | Napisać opisy 120–155 znaków z frazą i konkretem; usunąć przeklejone akapity i literówkę | Nie |
| 8 | P2 | Za długie tytuły i doklejki „praktyczny poradnik…” | 9 tytułów | Skrócić do ok. 60 znaków; przenieść konkret (zakres, rok sprawdzenia) do tytułu; tytuł strony głównej zmienić z „Home” | Nie |
| 9 | P2 | Nakładające się tematy (kanibalizacja) | Sufit, kolor salonu, ogród, kuchnia | Dla każdej intencji jedna strona główna tematu; resztę zawęzić albo scalić z 301 | Tak przy scalaniu |
| 10 | P2 | Nieaktualne lata w treści | 4 wpisy | Usunąć „2025” albo zaktualizować po sprawdzeniu źródeł; dodać widoczną datę aktualizacji | Nie |
| 11 | P2 | Brak podpisu autora, autor „kamil” w schemacie | Wszystkie wpisy | Dodać podpis i datę aktualizacji nad tekstem; poprawić nazwę autora w profilu WordPress (np. „Kamil …” po zgodzie) | Tak: jak się podpisywać |
| 12 | P2 | Zdjęcia: puste alty, angielskie alty, brak zdjęć w treści | 10 wpisów bez alt, 20 ze zdjęciami w stylu Unsplash (angielskie alty potwierdzone na 4), 1 bez zdjęcia | Polskie alty opisujące zdjęcie; potwierdzić licencję i źródło zdjęć; dodać zdjęcia lub schematy w treści tam, gdzie pomagają | Tak: wybór zdjęć i grafik |
| 13 | P2 | Stały blok „Podobne wpisy” i pingbacki jako komentarze | Wszystkie wpisy | Blok ustawić na wpisy z tego samego tematu; wyłączyć pingbacki z własnej domeny i usunąć istniejące | Nie |
| 14 | P2 | Luki w działach Ogród, Remont, Wnętrza | 3 działy | Plan treści z danymi o wolumenach (metoda klaster-tresci); wstępy do archiwów działów jako huby | Tak: plan |
| 15 | P3 | Ogólne anchory do archiwów, wzmianka bez linku, linki do 301 | Kilka wpisów, strona główna | Linkować do konkretnych wpisów opisowym anchorem; poprawić adresy na wersje z ukośnikiem | Nie |
| 16 | P3 | Nagłówki widżetów w H2/H3, brak H1 na /blog/ i /o-mnie/ | Szablon | Zamienić nagłówki widżetów na zwykły tekst lub niższy poziom; dodać H1 | Nie |
| 17 | P3 | Długie slugi, slug niezgodny z tytułem (remont łazienki) | 8 wpisów | Zostawić; zmieniać tylko przy scalaniu treści, zawsze z 301 | Tak |
| 18 | P3 | Leniwe ładowanie zdjęcia głównego | Wszystkie wpisy | Wyłączyć lazyload dla pierwszego obrazu (do analizy technicznej) | Nie |
| 19 | P3 | Brak strony kontakt i polityki prywatności | Serwis | Dodać stronę kontakt; politykę prywatności jako temat prawny zostawić decyzji właściciela | Tak |
| 20 | P3 | Wpis o projekcie domu dotyka formalności budowlanych | 1 wpis | Ustalić, czy treści prawne są dopuszczalne w tym projekcie (w niechcieznajda były zakazane w poradnikach) | Tak |

## Widoczność dla porządku

Według `[LABS]` (18.10.2026) domena ma 2 frazy w top 100 Google w Polsce: „bardzo mały salon w bloku” (720 wyszukań/mies., pozycja 48, /jak-urzadzic-maly-salon-w-bloku-…/) i „jak urządzić małą kuchnię” (390 wyszukań/mies., pozycja 83, /jak-urzadzic-mala-kuchnie-…/). Zapytanie „site:wnetrzakamila.pl” zwróciło 10 wyników organicznych, w tym /o-mnie/ i 9 wpisów [SERP].

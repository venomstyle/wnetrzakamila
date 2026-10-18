# SEO techniczne: wnetrzakamila.pl

Stan na 18.10.2026. Proxy sesji blokuje bezpośrednie połączenia z domeną, więc wszystkie dane pochodzą z DataForSEO. Każda liczba ma w nawiasie kod źródła z tabeli poniżej. Wszystkie zapytania wykonałem 18.10.2026.

## W skrócie

- **Technicznie strona jest zdrowa.** 44 strony HTML odpowiadają kodem 200, nie ma błędów 404, zepsutych linków ani łańcuchów przekierowań. Każda strona ma własny canonical, a robots.txt niczego nie blokuje (S1, S2, S3, S5, S8).
- **Największy problem to szybkość strony głównej na telefonie.** LCP wynosi 10,4–11,1 s w trzech pomiarach (próg Google dla dobrego wyniku to 2,5 s). Winne jest tło sekcji powitalnej: zdjęcie JPEG 2560×1707 px o wadze 853 KiB (S10, S11).
- **Wpisy przesuwają się podczas ładowania.** CLS na wpisie o małej kuchni wynosi 0,11–0,117 na telefonie i 0,163 na komputerze (próg: 0,1). Przyczyną jest leniwe ładowanie zdjęcia wyróżniającego przez wtyczkę LiteSpeed Cache (S10, S11).
- **Pozycja menu „Kalkulatory budowlane” prowadzi do pustej kategorii.** Strona pokazuje tylko komunikat „No results found.” (13 słów) i jest otwarta dla Google (S2, S13).
- **Brakuje opisów meta na 32 z 44 stron**, w tym na stronie głównej i na 19 z 31 wpisów (S2).
- **Mapa strony zawiera dwie zbędne strony:** testową stronę motywu `/styles/` z angielskim tekstem oraz archiwum autora `/author/admin/`, które zdradza login „admin” (S8).
- **Dane strukturalne (Yoast) działają, ale autor jest opisany słabo:** nazwa „kamil” małą literą, typ jednocześnie Person i Organization, Gravatar zamiast logo. Brak FAQ (S6).
- **Google pokazuje około 23 wyników dla `site:wnetrzakamila.pl`**, a w dwóch zapytaniach zobaczyłem 15 różnych adresów z 39 w mapie strony. Pełnego stanu indeksu nie da się ustalić bez Search Console (S12).

## Źródła

| Kod | Endpoint DataForSEO (18.10.2026) | Co z niego wziąłem |
|---|---|---|
| S1 | `/v3/on_page/task_post` + `/v3/on_page/summary/{id}` (crawl `10180825-2594-0216-0000-8124b2b6f17d`, max 500 stron, load_resources, validate_micromarkup) | liczba stron, serwer, SSL, testy domeny |
| S2 | `/v3/on_page/pages` (ten sam crawl) | kody, tytuły, opisy, H1, canonical, Open Graph, głębokość |
| S3 | `/v3/on_page/links` | linki wewnętrzne i zewnętrzne, nofollow, linki do przekierowań |
| S4 | `/v3/on_page/non_indexable` | strony oznaczone jako nieindeksowalne |
| S5 | `/v3/on_page/redirect_chains`, `/v3/on_page/duplicate_tags`, `/v3/on_page/pages` z filtrem `duplicate_content` | łańcuchy, duplikaty tytułów, opisów i treści |
| S6 | `/v3/on_page/microdata` (strona główna, /o-mnie/, wpis o małej kuchni) | dane strukturalne i ich walidacja |
| S7 | `/v3/on_page/resources` | skrypty, cache, wtyczki |
| S8 | `/v3/on_page/instant_pages` + `/v3/on_page/raw_html` | robots.txt, mapy strony, wersje http/www, adresy testowe |
| S9 | `/v3/on_page/raw_html` z crawla | kod HTML strony głównej i dwóch wpisów (CMS, motyw, wtyczki) |
| S10 | `/v3/on_page/lighthouse/live/json` (skrót wyników) | wyniki Lighthouse, mobile i desktop |
| S11 | `/v3/on_page/lighthouse/task_post` + `/task_get/json` (pełny raport) | element LCP, przyczyny CLS, obrazy, fonty |
| S12 | `/v3/serp/google/organic/live/advanced` (`site:wnetrzakamila.pl`, location 2616, pl, depth 100) | widoczność adresów w Google |
| S13 | `/v3/on_page/content_parsing/live` | treść strony „Kalkulatory budowlane” |

## 1. Technologia i hosting

| Element | Ustalenie | Źródło |
|---|---|---|
| CMS | WordPress 6.9.10 (meta generator) | S9 |
| Motyw | GeneratePress (`wp-content/themes/generatepress`), bloki GenerateBlocks (klasy `gb-*`) | S9 |
| Kreator stron | Elementor 4.3.5 jest aktywny (meta generator, `elementor-kit`). W zbadanym HTML treść zbudowana jest z bloków GenerateBlocks, więc nie wiem, czy Elementor jest jeszcze potrzebny | S2, S9 |
| Wtyczka SEO | Yoast SEO (komentarze w robots.txt i mapach, ścieżka `plugins/wordpress-seo`) | S8 |
| Cache i optymalizacja | LiteSpeed Cache (`wp-content/litespeed/js`, `litespeed-ccss`, leniwe ładowanie obrazów) | S7, S9 |
| Obrazy | ShortPixel Adaptive Images (CDN `sp-ao.shortpixel.ai`, konwersja do WebP) | S9 |
| Analityka | Site Kit by Google 1.189.0, tag `GT-5D9RK4ZX` | S7, S9 |
| Serwer | LiteSpeed, HTTP/2, kompresja Brotli, IP 185.208.164.198 | S1, S8 |
| Hosting | Certyfikat SSL wystawił cyber_Folks S.A., co wskazuje na hosting w cyber_Folks. Nie potwierdziłem tego w panelu ani u właściciela | S1 |
| Certyfikat SSL | ważny, CN=wnetrzakamila.pl, wygasa 17.11.2026 | S1 |

## 2. Crawl i indeksacja

### 2.1 Wynik crawla

Crawler DataForSEO zaczął od strony głównej i zakończył pracę, bo skończyły mu się adresy (`crawl_stop_reason: empty_queue`) (S1).

| Wskaźnik | Wartość | Źródło |
|---|---|---|
| Adresy znalezione | 49 | S1 |
| Strony HTML z kodem 200 | 44 | S2 |
| Przekierowania 301 | 5 | S2 |
| Błędy 4xx / 5xx | 0 | S1, S2 |
| Zepsute linki | 0 | S3 |
| Łańcuchy przekierowań | 0 | S5 |
| Wpisy blogowe | 31 | S2 |
| Linki wewnętrzne (wszystkie typy) | 981 | S1 |
| Linki zewnętrzne | 15, wszystkie dofollow, w 6 wpisach | S3 |
| Maksymalna głębokość kliknięć | 3 (7 stron), większość na poziomie 1–2 | S2 |
| Strona 404 | prawidłowo zwraca 404 | S1, S8 |

Podział 44 stron HTML: strona główna, O mnie, /blog/ z paginacją (4 strony), 4 kategorie z paginacją (7 stron), 31 wpisów (S2).

### 2.2 Przekierowania

Wszystkie 5 przekierowań to dopisanie ukośnika na końcu adresu: `/blog`, `/tematy/wnetrza`, `/tematy/remont`, `/tematy/ogrod`, `/tematy/kalkulatory-budowlane` (S2). Prowadzi do nich 6 linków wewnętrznych: 5 ze strony głównej (kafelki kategorii i przycisk bloga) i 1 z wpisu o umeblowaniu mieszkania (S3).

### 2.3 Wersje adresu (http, www)

| Adres wejściowy | Adres końcowy | Źródło |
|---|---|---|
| `http://wnetrzakamila.pl/` | `https://wnetrzakamila.pl/` (200) | S8 |
| `http://www.wnetrzakamila.pl/` | `https://wnetrzakamila.pl/` (200) | S8 |
| `https://www.wnetrzakamila.pl/` | `https://wnetrzakamila.pl/` (200) | S8 |
| `https://wnetrzakamila.pl/?p=1743` | adres przyjazny wpisu (200) | S8 |
| `https://wnetrzakamila.pl/home/` | `https://wnetrzakamila.pl/` (200) | S8 |

Wszystkie warianty kończą się na jednej wersji: https bez www. Test `test_https_redirect` w S1 wypadł pozytywnie. **Nie ustaliłem kodu przekierowania** (301 czy 302): `instant_pages` podaje tylko adres końcowy, a próbny crawl od wersji http i www też zapisał tylko stronę docelową.

### 2.4 Strony oznaczone jako nieindeksowalne

DataForSEO oznaczył 17 wpisów jako nieindeksowalne z powodu `attribute` (S4). Sprawdziłem kod HTML: te wpisy mają `index, follow` i własny canonical. Powodem flagi są **pingbacki między własnymi wpisami**, które WordPress pokazuje jako komentarze z linkiem `rel="ugc"`. Na przykład pod wpisem o remoncie kuchni wisi komentarz „Pingback: Ile kosztuje projekt ogrodu? – Wnętrza Kamila” (S9). Takich linków jest 22 (S3). Strony są indeksowalne, ale pod wpisami widać śmieciowe „komentarze”, a wpis o remoncie dachu pokazuje nagłówek „1 komentarz do…” (S2).

### 2.5 Strony poza crawlem

| Adres | Stan | Źródło |
|---|---|---|
| `/styles/` | 200, indeksowalna, w mapie strony, bez linków wewnętrznych. Strona wzorcowa motywu z tekstem „This text is here as a visual reference…” i dwoma nagłówkami H1 | S8 |
| `/author/admin/` | 200, indeksowalna, w mapie strony. Tytuł „kamil, Autor w serwisie Wnętrza Kamila”, H1 „kamil”, lista wpisów | S8 |
| `/?s=kuchnia` (wyszukiwarka) | 200, `noindex, follow`, poprawnie. Nagłówek po angielsku „Search results for:” | S8 |
| `/tag/...` | W crawlu nie ma ani jednego linku do tagów. Adresu `/tag/kuchnia/` nie udało się sprawdzić (błąd API „duplicate crawl host”) | S3, S8 |
| Strony załączników | nie sprawdziłem | — |
| Parametry (np. `?utm_source=`) | nie sprawdziłem bezpośrednio (ten sam błąd API). Canonical wpisów wskazuje czysty adres, więc parametry powinny się sklejać | S2 |

### 2.6 Indeks Google

| Wskaźnik | Wartość | Źródło |
|---|---|---|
| Szacunek Google dla `site:wnetrzakamila.pl` | około 23 wyniki | S12 |
| Różne adresy widoczne w dwóch zapytaniach `site:` | 15 | S12 |
| Adresy w mapie strony | 39 | S8 |

Widoczne w Google: strona główna, /blog/, /o-mnie/, kategorie Wnętrza i Ogród oraz 10 wpisów (wizualizacja mieszkania, założenie trawnika, malowanie salonu, malowanie sufitu, kolor ścian do szarych mebli, pokój dziecka, pokój młodzieżowy, mały balkon, mała kuchnia, mały salon w bloku) (S12). Operator `site:` jest niedokładny. Wyniki obu zapytań różniły się między sobą, a zapytanie `site:wnetrzakamila.pl ile kosztuje` zwróciło „No Search Results”, choć dwa wpisy „ile kosztuje” są widoczne w zwykłym `site:`. Dokładny stan indeksu pokaże tylko raport „Strony” w Search Console.

## 3. robots.txt i mapa strony

### 3.1 robots.txt

Plik zwraca 200, ma 174 bajty i w całości pochodzi z Yoast (S8):

```
User-agent: *
Disallow:

Sitemap: https://wnetrzakamila.pl/sitemap_index.xml
```

Nic nie jest zablokowane, a mapa strony jest podana. To poprawne ustawienie dla małego bloga.

### 3.2 Mapa strony

`/sitemap.xml` i `/wp-sitemap.xml` przekierowują na `/sitemap_index.xml` (S8). Indeks generuje Yoast i zawiera 4 mapy (S8):

| Mapa | Adresy | Ostatni lastmod | Uwagi |
|---|---|---|---|
| post-sitemap.xml | 32 (/blog/ + 31 wpisów) | 19.12.2025 | lastmod przy każdym adresie, zdjęcia w `image:image`. Wpis o pokoju młodzieżowym nie ma zdjęcia |
| page-sitemap.xml | 3 (/, /styles/, /o-mnie/) | 19.11.2025 | `/styles/` nie powinna tu być |
| category-sitemap.xml | 3 (ogród, remont, wnętrza) | 19.12.2025 | brak pustej kategorii kalkulatorów (Yoast pomija puste) |
| author-sitemap.xml | 1 (/author/admin/) | 19.12.2025 | archiwum autora przy jednym autorze dubluje /blog/ |

Wszystkie 31 wpisów z mapy zostały znalezione w crawlu, więc mapa jest pełna (S2, S8). Najnowszy lastmod to 19.12.2025: od 10 miesięcy na stronie nie pojawił się ani nie zmienił żaden wpis (S8). Data publikacji wpisów: 25 z listopada 2025 i 6 z grudnia 2025 (S2).

## 4. Canonical, duplikaty, meta

### 4.1 Canonical i dyrektywy

- Wszystkie 44 strony HTML mają canonical wskazujący na siebie (S2).
- Meta robots na wpisach: `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` (S9).
- Strony paginacji (`/blog/page/2/`–`/4/`, `/tematy/remont/page/2/`–`/3/`, `/tematy/wnetrza/page/2/`) są indeksowalne i mają własny canonical. To domyślne zachowanie Yoast i jest w porządku (S2).
- `html lang="pl-PL"`, brak hreflang (strona jest tylko po polsku, więc nie jest potrzebny) (S9, S11).

### 4.2 Duplikaty

| Sprawdzenie | Wynik | Źródło |
|---|---|---|
| Zduplikowane tytuły | 0 | S5 |
| Zduplikowane opisy meta | 0 | S5 |
| Strony z podobną treścią | 8: /blog/, /blog/page/2/ i /3/, kategorie Ogród, Remont (+ str. 2), Wnętrza (+ str. 2) | S5 |

Duplikaty treści to listy wpisów bez własnego tekstu wstępu. Kategorie mają tytuły w szablonie „Archiwa Remont – Wnętrza Kamila” (S2).

### 4.3 Tytuły, opisy, nagłówki

| Sprawdzenie | Wynik | Źródło |
|---|---|---|
| Brak opisu meta | 32 z 44 stron (strona główna, /blog/ z paginacją, wszystkie kategorie, O mnie, 19 z 31 wpisów) | S2 |
| Tytuł dłuższy niż 60 znaków | 9 wpisów, najdłuższy 90 znaków (remont kuchni) | S2 |
| Tytuł krótszy niż 25 znaków (wg DataForSEO) | 3: strona główna „Home – Wnętrza Kamila”, /blog/, /o-mnie/ | S1, S2 |
| Brak H1 | 5: /blog/ i jego 3 strony paginacji, /o-mnie/ | S2 |
| Dwa H1 | /styles/ (strona testowa) | S8 |

Opis meta ma 12 wpisów: wszystkie 6 z grudnia, 4 z 5 z 23.11 i 2 z 5 z 17.11. Nie ma go żaden z 15 wpisów z 18 i 19.11.2025, czyli głównie wpisy „ile kosztuje” (S2). W Google strona główna wyświetla się jako „Wnętrza Kamila: Home” (S12).

## 5. Wydajność i Core Web Vitals

### 5.1 Lighthouse (dane laboratoryjne)

Lighthouse 13.4.0. Mobile symuluje Moto G Power z 4-krotnie wolniejszym procesorem i łączem około 1,6 Mb/s (S10). Progi Google dla dobrego wyniku: LCP do 2,5 s, CLS do 0,1, INP do 200 ms (web.dev, „Web Vitals”). Wykonałem kilka pomiarów, bo wyniki się wahają.

| Strona | Urządzenie | Wydajność | SEO | LCP | CLS | TBT | Waga strony | Źródło |
|---|---|---|---|---|---|---|---|---|
| Strona główna | mobile, pomiar 1 | 75 | 92 | 11,1 s | 0,014 | 43 ms | 1,64 MB | S10 |
| Strona główna | mobile, pomiar 2 | 73 | n/d | 10,4 s | 0,014 | 169 ms | 1,64 MB | S10 |
| Strona główna | mobile, pomiar 3 | 71 | 92 | 10,9 s | 0,014 | 230 ms | 1 602 KiB | S11 |
| Strona główna | desktop | 88 | 92 | 2,3 s | 0,006 | brak w odpowiedzi | 3,0 MB | S10 |
| Wpis: mała kuchnia | mobile, pomiar 1 | 95 | 100 | 1,8 s | 0,117 | 41 ms | 602 KB | S10 |
| Wpis: mała kuchnia | mobile, pomiar 2 | 89 | 100 | 3,2 s | 0,11 | 40 ms | 588 KiB | S11 |
| Wpis: mała kuchnia | desktop, pomiar 1 | 88 | 100 | 1,4 s | 0,163 | brak w odpowiedzi | 632 KB | S10 |
| Wpis: mała kuchnia | desktop, pomiar 2 | 89 | 100 | 1,4 s | 0,163 | 0 ms | 618 KiB | S11 |
| Kalkulatory budowlane | mobile, pomiar 1 | 99 | 92 | 0,9 s | brak w odpowiedzi | 123 ms | 374 KB | S10 |
| Kalkulatory budowlane | mobile, pomiar 2 | 99 | 92 | 1,0 s | 0 | 140 ms | 365 KiB | S11 |
| Kalkulatory budowlane | desktop | 100 | 92 | 0,4 s | 0 | brak w odpowiedzi | 344 KB | S10 |

Dostępność: 95 (strona główna), 96–97 (wpis), 100 (kalkulatory). Dobre praktyki: 100 na każdej stronie (S10). Wynik SEO 92 obniża brak opisu meta. Inne audyty SEO Lighthouse (indeksowanie, robots.txt, canonical, alt obrazów, tytuł, kod HTTP) przechodzą (S11).

**Dane z prawdziwych wizyt (CrUX) nie są dostępne w użytych endpointach.** Przy obecnym ruchu Google najpewniej ich nie zbiera. INP mierzy się tylko u użytkowników, więc jako przybliżenie podaję TBT.

### 5.2 Strona główna: skąd LCP 11 s

Pełny raport Lighthouse (S11) wskazuje element LCP: sekcję powitalną „Piękne Wnętrza, Krok po Kroku” z tłem CSS `ogrod-scaled.jpg`.

- Plik ma 2560×1707 px i 853 KiB, a na telefonie wyświetla się w polu 412 px szerokości. Lighthouse szacuje oszczędność na 734 KiB (S11).
- Tło CSS omija ShortPixel: plik idzie jako JPEG z serwera, bez WebP i bez wersji dla mniejszych ekranów (S11).
- Lighthouse zgłasza też, że ten zasób nie ma `fetchpriority=high` (S11).
- Obrazy stanowią 1,22 MB z 1,63 MB pobieranych na telefonie (5 żądań). Fonty ważą 156 KB, skrypty 196 KB (S11).
- Kafelki kategorii też używają pełnych plików „scaled” 2560 px (`wnetrza-scaled.jpg` 2037×2560, `remont-scaled.jpg` 2560×1700) (S9). Na komputerze strona waży przez to 3,0 MB (S10).
- Logo w nagłówku (`wnetrze_kamila.svg`) ma `fetchpriority="high"`, a mimo to LiteSpeed ładuje je leniwie (atrybut `data-lazyloaded`) (S9).

### 5.3 Wpisy: skąd CLS 0,11–0,16

Lighthouse (S11) wskazuje jako źródło przesunięcia blok treści wpisu, a jako przyczynę zdjęcie wyróżniające nad nim. Zdjęcie ma `fetchpriority="high"` i wymiary w atrybutach, ale LiteSpeed Cache podmienia je na leniwe ładowanie z zastępczym obrazkiem GIF 1×1 px (S9). Najpewniej to ten zastępczy obrazek zajmuje najpierw złą wysokość, a po wczytaniu zdjęcia tekst przesuwa się w dół. Sprawdziłem jeden wpis. Pozostałe wpisy używają tego samego szablonu, więc problem najpewniej dotyczy wszystkich, ale tego nie zmierzyłem.

### 5.4 Inne ustalenia o wydajności

| Ustalenie | Szczegóły | Źródło |
|---|---|---|
| Czas odpowiedzi serwera | 38–108 ms (bardzo dobry, działa cache LiteSpeed) | S10 |
| Zasoby blokujące renderowanie | jQuery 3.7.1 i 8 małych skryptów LiteSpeed. Na telefonie szacowana strata 200 ms (wpis), na stronie głównej brak | S11 |
| Nieużywany JavaScript | 70–72 KiB. Na stronie głównej w całości z tagu Google (`gtag/js`, 180 KB) | S11 |
| Nieużywany CSS | 22–24 KiB z jednego pliku LiteSpeed | S11 |
| Fonty | Lato i Newsreader z Google Fonts w formacie .ttf, 122–224 KB zależnie od strony. Lighthouse zgłasza audyt „Font display” | S11 |
| Cache przeglądarki | zdjęcia, CSS i JS: 7 dni. Lighthouse sugeruje dłużej (oszczędność 124 KiB przy powtórnej wizycie na stronie głównej) | S11 |
| Rozmiar HTML | 94–120 KB przed kompresją, około 22–25 KB po kompresji Brotli | S2, S8 |

## 6. Dane strukturalne

Yoast generuje jeden graf JSON-LD na każdej stronie. Motyw GeneratePress dodaje osobno mikrodane `Blog`/`WebPage` (S6).

| Typ | Gdzie | Stan | Źródło |
|---|---|---|---|
| Article | wpisy | jest: headline, datePublished, dateModified, wordCount, articleSection, image, author. Autor nie ma `url` | S6 |
| WebPage | wszystkie strony | jest | S6 |
| BreadcrumbList | wszystkie strony | jest: Strona główna › Blog › wpis | S6 |
| WebSite + SearchAction | wszystkie strony | jest | S6 |
| Person / Organization | wszystkie strony | jeden obiekt z dwoma typami naraz. `name: "kamil"` (małą literą), `url` prowadzi do `/author/admin/`, `logo` i `image` to Gravatar 96 px, `sameAs` wskazuje na samą domenę. Wydawca artykułów to ta sama osoba | S6 |
| ImageObject | wszystkie strony | na wpisach poprawny (podpis po angielsku, np. „white and black gas range oven”). Na /o-mnie/ brak `url` i `contentUrl` | S6 |
| FAQPage, HowTo | — | brak | S6 |

Walidator DataForSEO zgłasza 2–3 błędy na stronę (S6):
- `license` w ImageObject. Google wymaga tego pola tylko do oznaczenia licencji zdjęcia w Grafice Google, więc ten błąd można pominąć.
- `query-input` w SearchAction zapisany jako obiekt. To format nowszych wersji Yoast. Google i tak wycofał pole wyszukiwania witryny w wynikach w listopadzie 2024.
- Na /o-mnie/ brak `contentUrl` obrazu głównego. To realny błąd.

## 7. Open Graph i media społecznościowe

| Sprawdzenie | Wynik | Źródło |
|---|---|---|
| og:title, og:url, og:site_name, og:locale (pl_PL), twitter:card | na wszystkich 44 stronach | S2 |
| og:image | brak na 13 stronach: strona główna, /blog/ z paginacją, wszystkie kategorie z paginacją i wpis o pokoju młodzieżowym | S2 |
| Rozmiar og:image | od 900×1200 do 2561×2000 px. 9 wpisów podaje pełne pliki o szerokości 2560 px | S2 |
| og:description strony głównej | sklejony tekst sekcji z dopiskiem „… Read more” | S2 |
| Autor w podglądzie (twitter:data1) | „kamil” | S2 |

## 8. Wersja mobilna

- Meta viewport jest ustawiony (`width=device-width, initial-scale=1`) (S9).
- Lighthouse mobile: dostępność 95–100, dobre praktyki 100, brak problemów z indeksowaniem (S10, S11).
- Strona używa tego samego HTML na telefonie i komputerze (motyw responsywny). Zrzutów ekranu nie robiłem, bo proxy blokuje przeglądarkę.
- Słabym punktem jest tylko szybkość strony głównej (rozdział 5.2).

## 9. Drobne ustalenia

- Teksty szablonu są częściowo po angielsku: „No results found.” (pusta kategoria), „Search results for:” (wyszukiwarka), „Read more” (opis OG strony głównej) (S2, S8, S13).
- Teksty alternatywne zdjęć są po angielsku, np. „2 brown wooden armchairs beside white wall” (S9). Nazwy plików (`pexels-gdtography-…`, `vgyn_cwxqvm.jpg`) wskazują na zdjęcia z banków Pexels i najpewniej Unsplash. Źródło i licencję zdjęć powinien potwierdzić właściciel.
- Pod każdym wpisem blok „Podobne wpisy” pokazuje te same trzy najnowsze wpisy. Na wpisie o małej kuchni jednym z nich jest sam ten wpis (S2).
- Wpis o małej kuchni ma śródtytuł „Trendy w urządzaniu małych kuchni w 2024 i 2025 roku” (S2). To sprawa treści, ale wpływa na świeżość.
- Strona podaje wersje oprogramowania w meta generator (WordPress, Site Kit, Elementor) (S9).
- HTML ma drobne błędy składni („closing tag does not match”), 1–10 na stronę (S2, S8). Przeglądarki i Google je tolerują.
- Wejście na stronę przez sam adres IP serwera zwraca 403, a listowanie katalogów jest wyłączone (403) (S1).

## 10. Lista problemów i rekomendacje

| # | Priorytet | Problem | Rekomendacja |
|---|---|---|---|
| 1 | wysoki | LCP strony głównej na telefonie 10,4–11,1 s. Tło sekcji powitalnej to JPEG 853 KiB, 2560 px | Zastąpić tło CSS zwykłym obrazem `<img>` z `fetchpriority="high"` i `srcset` (WebP, około 800 px dla telefonu). Wykluczyć je z leniwego ładowania w LiteSpeed. Zmniejszyć kafelki kategorii do rozmiaru wyświetlania |
| 2 | wysoki | CLS 0,11–0,163 na wpisie, przyczyną leniwe ładowanie zdjęcia wyróżniającego | W LiteSpeed Cache wykluczyć z lazy load zdjęcie wyróżniające (np. klasę `gb-media-01e58dbd` albo pierwsze obrazy na stronie). Potem zmierzyć kilka wpisów |
| 3 | wysoki | Kategoria „Kalkulatory budowlane” w menu jest pusta („No results found.”) i indeksowalna | Decyzja właściciela: opublikować kalkulatory albo do tego czasu zdjąć pozycję z menu i ustawić noindex |
| 4 | średni | Brak opisu meta na 32 z 44 stron, w tym strona główna i 19 wpisów | Uzupełnić w Yoast, zaczynając od strony głównej i wpisów „ile kosztuje” |
| 5 | średni | `/styles/` (strona testowa motywu, angielski tekst) w mapie strony i indeksowalna | Usunąć stronę albo ustawić noindex, żeby wypadła z mapy |
| 6 | średni | Archiwum `/author/admin/` zdradza login „admin”, dubluje /blog/ i jest w mapie | Przy jednym autorze wyłączyć archiwa autora w Yoast. Zmienić slug użytkownika. Zabezpieczenie logowania sprawdzić osobno |
| 7 | średni | Autor w danych strukturalnych: „kamil”, typ Person i Organization naraz, logo z Gravatara, url do /author/admin/ | Po decyzji właściciela, jak ma się przedstawiać (imię, zdjęcie, profile), ustawić w Yoast osobę albo markę z logo i powiązać autora ze stroną /o-mnie/ |
| 8 | średni | Pingbacki między własnymi wpisami wyświetlane jako komentarze (22 linki `ugc`) | Wyłączyć pingbacki w Ustawienia › Dyskusja, usunąć istniejące |
| 9 | średni | Listy wpisów (blog, kategorie) bez własnej treści, 8 stron z podobną treścią, tytuły „Archiwa X” | Dodać krótki wstęp do kategorii i zmienić szablon tytułu w Yoast. Przy przebudowie rozważyć huby tematyczne |
| 10 | średni | Brak H1 na /blog/ (z paginacją) i /o-mnie/ | Dodać H1 w szablonie lub w treści strony |
| 11 | średni | Teksty alternatywne zdjęć po angielsku, podpisy w ImageObject po angielsku | Przepisać alt na polski i opisowy. Potwierdzić źródło i licencję zdjęć |
| 12 | średni | Fonty .ttf z Google Fonts (122–224 KB), tag Google 180 KB z 70 KB nieużywanego kodu | Hostować fonty lokalnie w WOFF2 z ograniczonym zestawem znaków. Tag zostawić, ale ładować po interakcji, jeśli wtyczka na to pozwala |
| 13 | niski | 6 linków wewnętrznych bez końcowego ukośnika prowadzi do 301 | Poprawić adresy w kafelkach i przycisku na stronie głównej oraz w jednym wpisie |
| 14 | niski | 9 tytułów dłuższych niż 60 znaków | Skrócić w Yoast, zwłaszcza wpisy „praktyczny poradnik krok po kroku” |
| 15 | niski | og:image brak na 13 stronach, a w 9 wpisach to pełny plik 2560 px | Ustawić domyślny obraz OG w Yoast i zdjęcie wyróżniające we wpisie o pokoju młodzieżowym |
| 16 | niski | Angielskie teksty szablonu („No results found.”, „Search results for:”, „Read more”) | Sprawdzić język witryny i tłumaczenie GeneratePress |
| 17 | niski | Elementor 4.3.5 aktywny, a treść zbudowana z GenerateBlocks | Sprawdzić w panelu, czy Elementor jest używany. Jeśli nie, wyłączyć |
| 18 | niski | Certyfikat SSL wygasa 17.11.2026 | Sprawdzić, czy cyber_Folks odnawia go automatycznie |
| 19 | niski | Brak danych o indeksie i Core Web Vitals z prawdziwych wizyt | Dać dostęp do Search Console (Site Kit sugeruje, że konto Google jest podpięte) i sprawdzić raporty „Strony” i „Podstawowe wskaźniki internetowe” |

## Czego nie udało się ustalić

- Kodu przekierowań http→https i www→bez www (301 czy 302).
- Pełnego stanu indeksu Google i danych CrUX (wymaga Search Console).
- Zachowania tagów, stron załączników i adresów z parametrami (błąd API przy próbie).
- Tego, czy Elementor jest faktycznie używany na którejś stronie.
- Hostingu inaczej niż po wystawcy certyfikatu.

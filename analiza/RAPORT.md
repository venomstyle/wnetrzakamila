# Raport: analiza wnetrzakamila.pl

Stan na 18.10.2026. Wszystkie dane pochodzą z DataForSEO (On-Page, Lighthouse, Labs, Keywords Data, SERP, Backlinks, Business Data), bo proxy sesji blokuje bezpośredni dostęp do domeny. Szczegóły, endpointy i tabele są w plikach częściowych:

| Plik | Zakres |
|---|---|
| [seo-techniczne.md](seo-techniczne.md) | crawl, indeksacja, mapa strony, szybkość, dane strukturalne |
| [seo-tresci.md](seo-tresci.md) | 31 wpisów: metadane, treść, ceny, autor, linkowanie, obrazy |
| [frazy.md](frazy.md) + [dane/](dane/) | widoczność, popyt z 12 miesięcy (415 fraz), mapa fraz, SERP |
| [seo-lokalne.md](seo-lokalne.md) | Profil Firmy w Google, Mapy |
| [linki.md](linki.md) | profil linków, porównanie, pomysły na linki |
| [oferta.md](oferta.md) | oferta, kontakt, zarobek, analityka, zgody, zrzuty (tylko linki) |
| [konkurencja.md](konkurencja.md) | 10 domen, typy treści, zarobek, reklamy |

## Czym jest strona

- **Blog poradnikowy jednej osoby („Cześć, jestem Kamil”), a nie firma.** Nie ma oferty, usług, cennika, portfolio ani kontaktu [oferta.md §1–2].
- **31 wpisów** w działach Wnętrza, Remont i Ogród, z czego 20 to „Ile kosztuje…?”. Wszystkie opublikowano między 18.11 a 19.12.2025, później nic nie doszło [seo-tresci.md, mapa strony Yoast].
- **Technologia:** WordPress 6.9.10, GeneratePress, Yoast, LiteSpeed Cache, ShortPixel, Site Kit. Elementor jest aktywny, ale nic go nie używa. Hosting i SSL według certyfikatu: cyber_Folks [seo-techniczne.md §1].
- **Domena** zarejestrowana 17.11.2025, **wygasa 17.11.2026** (WHOIS). Certyfikat SSL też wygasa 17.11.2026 [linki.md, seo-techniczne.md §1].

## Ocena stanu

| Obszar | Ocena | Najważniejsze |
|---|---|---|
| SEO techniczne | dobra baza, słaba szybkość | 49 adresów, 0 błędów 404, canonical i mapa strony w porządku; strona główna na telefonie: LCP 10,4–11,1 s, Lighthouse 71–75 (`on_page/lighthouse`) |
| Treści | słabe | ceny bez źródeł i sprzeczne między wpisami, ślady masowego pisania, sprzeczne fakty o autorze, 19 z 31 wpisów bez opisu meta |
| Widoczność | prawie zero | 2 frazy w top 100 (poz. 37 i 73), ETV 0,75 (`dataforseo_labs/…/ranked_keywords`, `domain_rank_overview`) |
| Lokalne | nie dotyczy | brak Profilu Firmy w Google (`business_data/google/my_business_info`); ma sens tylko przy sprzedaży usług |
| Linki | brak | 14 linków z 14 domen, wszystkie ze spamowych list domen, spam score 59, żadnej domeny .pl (`backlinks/summary`, `referring_domains`) |
| Konwersja i zarobek | brak | brak kontaktu, newslettera, reklam i afiliacji; pusty dział „Kalkulatory budowlane” w menu |
| Analityka i zgody | częściowo | tag Google GT-5D9RK4ZX (Site Kit) ładowany od razu; brak banera zgód; polityka prywatności zwraca 404 (opis stanu, bez oceny prawnej) |

## Najważniejsze odkrycie: popyt jest w kalkulatorach

- **Kalkulatory budowlane mają 42 250 wyszukań miesięcznie** w badanej grupie, przez cały rok: od 33 170 w grudniu do 57 910 w marcu (`keywords_data/google_ads/search_volume`) [frazy.md §2].
- **W top 10 dla kalkulatorów są najsłabsze domeny w całej niszy.** Na „kalkulator płytek” wygrywają serwisy bez ruchu, a na „kalkulator paneli podłogowych” w top 10 jest kalkulator komory chłodniczej (`serp/google/organic/live/advanced`) [frazy.md §4, konkurencja.md].
- **Przykłady popytu:** beton 6 170/mies. (szczyt 9 210 w kwietniu), m²/m³ 4 920, płytki z klejem i fugą 2 830, murowanie 1 800, farba 1 550, wylewka i gładź 920 [frazy.md §5].
- **Ogólne poradniki aranżacyjne** („mała kuchnia”, „mały salon”) zajmują portale z ponad 1 300 domenami linkującymi (homebook, urzadzamy, dobrzemieszkaj) i sklepy. Na start ta droga jest zamknięta [linki.md, konkurencja.md].
- **AI Overview był w 13 z 14 sprawdzonych wyników.** Przy kalkulatorach Google cytuje w nim działające narzędzia, także małych serwisów [frazy.md §4].
- **CPC jest niskie:** około 0,6 USD przy kalkulatorach i remoncie, około 0,2 USD przy aranżacji. Same reklamy na blogu przyniosą mało; liczy się skala ruchu albo własny produkt [frazy.md §5].

## 10 najważniejszych problemów (wpływ × koszt)

| # | Problem | Wpływ | Koszt | Źródło |
|---|---|---|---|---|
| 1 | Domena i SSL wygasają 17.11.2026. Nie wiadomo, czy jest auto-odnawianie | krytyczny | minimalny | linki.md |
| 2 | Menu na każdej stronie prowadzi do pustego działu „Kalkulatory budowlane” („No results found.”), a wpisy zapowiadają „nasze kalkulatory” | wysoki | niski (ukrycie) / średni (budowa) | oferta.md §5 |
| 3 | 20 wpisów kosztowych: żadna kwota nie ma źródła ani daty, liczby różnią się między wpisami (sufit „12–25 zł/m²” i „20–30 zł/m²”), błędny rachunek w „ile kosztuje projekt domu”. To łamie zasadę projektu | wysoki | średni | seo-tresci.md §1–2 |
| 4 | Sprzeczne fakty o autorze: „pasjonat od kilku lat” na /o-mnie/ i „absolwent architektury wnętrz po latach w studio” w ramce pod wpisami, do tego niepotwierdzone historie o klientach | wysoki | niski (decyzja właściciela) | oferta.md §3, seo-tresci.md §4 |
| 5 | Brak kontaktu, danych administratora i polityki prywatności (404); tag Google ładuje się bez banera zgód | wysoki | niski | oferta.md §2, §7–8 |
| 6 | Ślady masowego generowania: 10 wpisów w 6 godzin, 5 wpisów w 10 minut, powtarzalne metafory i schematy, potem 10 miesięcy bez zmian | wysoki | średni | seo-tresci.md §3 |
| 7 | Strona główna na telefonie: LCP ~11 s przez tło 853 KiB JPEG 2560 px; wpisy: CLS 0,11–0,16 przez leniwie ładowane zdjęcie główne | średni | niski | seo-techniczne.md §5 |
| 8 | Metadane: brak opisu na 32 z 44 stron, 9 tytułów ponad 60 znaków, tytuł główny „Home - Wnętrza Kamila”, angielskie resztki szablonu („Read more”, „No results found.”) | średni | niski | seo-techniczne.md §4, seo-tresci.md §5 |
| 9 | Kanibalizacja i linkowanie: 3 wpisy o suficie, 3 o kolorze salonu, 3 o kosztach kuchni; „Podobne wpisy” zawsze te same 3; w mapie strony /styles/ i /author/admin/ (ujawnia login „admin”) | średni | niski | seo-tresci.md §7, §10; seo-techniczne.md §3 |
| 10 | Brak prawdziwych linków i powiązań z social media; brak dostępu do Search Console, więc nie wiemy, co Google faktycznie indeksuje | średni | średni | linki.md, seo-techniczne.md §2.6 |

## Szybkie poprawki (do tygodnia, po decyzjach)

Wszystkie wymagają dostępu do panelu WordPress albo decyzji o przeniesieniu strony (pytanie 4 niżej).

1. Włączyć auto-odnawianie domeny i SSL u cyber_Folks (robi właściciel).
2. Podpiąć Google Search Console i dać dostęp do GA4 (robi właściciel).
3. Ukryć pozycję „Kalkulatory budowlane” w menu i usunąć zapowiedzi kalkulatorów z wpisów, dopóki pierwsze kalkulatory nie są gotowe. Pustą kategorię oznaczyć noindex.
4. Ujednolicić „O mnie” i ramkę autora do faktów potwierdzonych przez właściciela. Niepotwierdzone historie usunąć z wpisów.
5. Dodać stronę kontaktu, dane administratora w stopce i politykę prywatności (treść do decyzji właściciela).
6. Tło sekcji powitalnej zamienić na WebP około 1200 px; zdjęcie główne wpisów ładować bez lazy loading.
7. Dopisać opisy meta, skrócić tytuły, zmienić „Home” na nazwę z frazą, przetłumaczyć teksty szablonu.
8. Usunąć z mapy strony /styles/ i /author/admin/; wyłączyć pingbacki; wyłączyć nieużywany Elementor.

## Plan na 3 miesiące

### Miesiąc 1 (listopad): porządek i decyzje
- **Szybkie poprawki z listy wyżej.**
- **Wpisy kosztowe:** każdą kwotę potwierdzić u źródła z datą albo zastąpić „sprawdź w cenniku” z linkiem. Zostaje jeden poradnik na temat:
  - 3 wpisy o suficie łączymy w jeden mocny poradnik „jak malować sufit” (temat ma 4 410 wyszukań miesięcznie, a obecny wpis celuje w frazę z 220);
  - nadmiarowe wpisy przekierowujemy 301 na poradnik.
- **Przegląd niezależny wszystkich 31 wpisów** (agent bez kontekstu: źródła, rachunki, uczciwość).

### Miesiąc 1–2: kalkulatory (główny kierunek, jeśli go zatwierdzisz)
- **Pierwsza piątka do stycznia** (szczyt sezonu to luty–kwiecień): płytki z klejem i fugą, beton, farba, m²/m³, murowanie. Każdy kalkulator ma:
  - wzór i przykład liczbowy;
  - zapas materiału;
  - FAQ z krótkich pytań („ile kleju na m² płytek” 480, „ile schnie grunt” 1 300).
- **Dział „Kalkulatory budowlane” jako hub** łączy kalkulatory z poradnikami o malowaniu i remoncie.
- **Kolejne:** wylewka i gładź, ogrodzenie, kostka brukowa, panele, tapeta.
- **Kalkulator kosztów remontu** (1 720 wyszukań) tylko z cenami ze źródła i datą, do Twojej decyzji.

### Miesiąc 2–3: treści (skill `klaster-tresci`)
- **Malowanie i kolory** (62 800 wyszukań miesięcznie, równo przez rok):
  - hub „jak malować ściany”;
  - hub „kolor ścian do mebli”;
  - poradnik „jak malować sufit”.
- **Brakujące pomieszczenia** (publikacja listopad–grudzień, szczyt w styczniu): mała łazienka (5 640), salon z aneksem (4 770), przedpokój (4 530), pokój dziewczynki (4 400) i chłopca (2 900), domowe biuro (2 300).
- **Ogród i balkon do lutego**, bo szczyt jest w marcu–maju. Robimy go tylko, jeśli ogród zostaje w zakresie bloga.
- **Rytm z niechcieznajda:**
  - cały klaster w poniedziałek, potem dogrywka;
  - przegląd niezależny po każdej serii;
  - data aktualizacji zmieniana tylko przy realnej zmianie.

### Wizytówka i opinie
- **Nie dotyczy, dopóki nie ma usług.** Jeśli zdecydujesz się sprzedawać projekty wnętrz w swoim mieście, plan profilu jest w [seo-lokalne.md](seo-lokalne.md).
- **Poziom do dogonienia:** profile w top 10 Map w Warszawie i Krakowie mają medianę 56–57 opinii i 64–75 zdjęć.

### Linki
- **Bez kupowania i bez zimnych maili.**
- **Kalkulatory z kodem do wstawienia na inne strony** i zgłoszenia do katalogów narzędzi. Na „kalkulator farby” kalkulatorxxl.pl jest 6. z zaledwie 10 domenami linkującymi.
- **Social media:** Pinterest i Instagram z linkiem do strony, jeśli prowadzisz takie profile.

### Reklamy
- **Nie teraz.** Nie ma produktu ani oferty, a reklamy w niszy kupują sklepy (buduj24.pl, ponad 40 kreacji) i sprzedawcy projektów online (`serp/google/ads_advertisers`).
- **Wrócimy do nich** po decyzji o modelu zarobku (`playbook/prompty/badanie-reklam.md`).

## Pytania do właściciela

1. **Cel strony:** ruch i reklamy (AdSense), afiliacja z oznaczeniem, własne usługi projektowe czy na razie bez zarabiania?
2. **Domena:** czy jest auto-odnawianie przed 17.11.2026? Czy domena była kupiona z rynku wtórnego?
3. **Autor:** kto pisze i jakie fakty są prawdziwe (wykształcenie, studio, klienci, „od kilku lat”)? Czy profil Instagram @wnetrzebezfiltra jest Twój? Jest pierwszym wynikiem na „wnetrzakamila.pl”.
4. **Technologia:** zostajemy na WordPressie (potrzebny dostęp: konto w panelu albo hasło aplikacji do API) czy przenosimy stronę do tego repozytorium na Astro, jak niechcieznajda (build w GitHub Actions, FTP na cyber_Folks)?
5. **Wpisy kosztowe (20):** poprawiamy ze źródłami, zamieniamy kwoty na „sprawdź w cenniku” czy część zdejmujemy?
6. **Kalkulatory:** czy mają być głównym kierunkiem? Czy robimy kalkulator kosztów remontu (wymaga źródła cen)?
7. **Zakres:** czy ogród zostaje?
8. **Treści prawne:** czy pozwolenia na budowę i ulgi podatkowe mogą się pojawiać, czy są zakazane jak w niechcieznajda?
9. **Dostęp:** Search Console i GA4.
10. **Zgody i administrator:** kto jest administratorem danych (osoba czy firma)? Czy wdrażamy baner zgód i politykę prywatności?
11. **Wygląd:** zostawiamy obecny czy projektujemy nowy (warianty na arkuszu opcji)?
12. **Budżet:** czy jest budżet na reklamy albo płatne narzędzia?

Po akceptacji raportu uzupełnię sekcję „O projekcie” w CLAUDE.md (osobny PR).

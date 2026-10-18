# Oferta, UX, konwersja i monetyzacja: wnetrzakamila.pl

Stan na 18.10.2026. Proxy sesji blokuje bezpośredni dostęp do domeny, więc wszystkie dane pochodzą z DataForSEO:

- crawl On-Page: `/v3/on_page/task_post` (id `10180825-2594-0216-0000-cd51ceaa1205`, 40 stron, JavaScript włączony, zapis surowego HTML), potem `summary`, `pages`, `links`, `resources`, `raw_html`;
- `/v3/on_page/content_parsing/live` (treść stron);
- `/v3/on_page/instant_pages` (pojedyncze adresy, także z mobilnym user-agentem iPhone);
- `/v3/serp/google/organic/live/advanced` (zapytanie `site:wnetrzakamila.pl`, Polska, język polski);
- `/v3/on_page/page_screenshot` (zrzuty).

Skrót „[crawl]” w tekście oznacza crawl i surowy HTML z tego zadania. Wszystkie odczyty są z 18.10.2026.

---

## Podsumowanie

1. **To blog poradnikowy jednej osoby („Kamil”).** Nie ma oferty, usług, cennika ani produktów. Jest 31 wpisów w kategoriach Wnętrza, Remont i Ogród. Większość tytułów to pytania „Ile kosztuje…?” i „Jak…?”.
2. **Nie da się skontaktować z autorem.** Nie ma strony kontakt, formularza, adresu e-mail, telefonu ani linków do mediów społecznościowych. Jedynym formularzem poza wyszukiwarką są komentarze pod wpisami.
3. **Nie ma polityki prywatności, regulaminu ani danych administratora.** Stopka to tylko „Copyright @2026 Wnętrza Kamila”. Adresy `/polityka-prywatnosci/`, `/privacy-policy/`, `/regulamin/` i `/kontakt/` zwracają 404.
4. **Nie ma kalkulatorów budowlanych.** Pozycja w menu, kafelek na stronie głównej i linki „sprawdź nasze kalkulatory budowlane” w artykułach prowadzą do pustej kategorii z napisem „No results found.”
5. **Strona na razie nie zarabia.** Nie ma AdSense, linków afiliacyjnych, `rel="sponsored"` ani newslettera. Wszystkie 15 linków zewnętrznych to zwykłe linki „dofollow” do stron głównych serwisów (IKEA, Westwing, Homebook, Murator i inne).
6. **Analityka:** jest tag Google `GT-5D9RK4ZX` wstawiany przez wtyczkę Site Kit by Google 1.189.0, razem ze zdarzeniami czytania treści. Nie ma Meta Pixel, Hotjar, Clarity ani Plausible. Celów nie widać w kodzie.
7. **Nie ma banera cookies ani CMP.** Tag Google ładuje się w `<head>` od razu przy wejściu, a w kodzie nie ma ustawień Consent Mode (`gtag('consent', …)`). To tylko opis stanu.
8. **Opis autora jest niespójny.** Strona „O mnie” mówi „pasjonat wnętrz”, a ramka w artykułach mówi „absolwent architektury wnętrz, który po latach pracy w studio projektowym…”. Właściciel musi potwierdzić, która wersja jest prawdziwa.

---

## 1. Co strona oferuje i komu

**Rodzaj strony:** blog z poradami o urządzaniu wnętrz, remoncie i ogrodzie. Odbiorca to osoba, która sama urządza mieszkanie albo planuje remont i sprawdza koszty.

- Nagłówek H1 strony głównej: „Piękne Wnętrza, Krok po Kroku”. Tekst pod nim: „Witaj w moim zakątku internetu, gdzie dzielę się praktycznymi pomysłami na aranżację wnętrz, inspiracjami na co dzień i prostymi trikami… Zaparz herbatę i poczuj się jak w domu.” (content_parsing, `https://wnetrzakamila.pl/`).
- Opis witryny w danych strukturalnych Yoast: `"description":"Praktyczne porady, piękne wnętrza"`. Wydawca to `"@type":["Person","Organization"], "name":"kamil"` [crawl, HTML strony głównej].
- **Brak oferty.** Na 40 przeskanowanych adresach nie ma strony usług, cennika, portfolio, realizacji, opinii klientów ani sklepu [crawl, `/v3/on_page/pages`].

**Treści.** Lista wpisów na `/blog/` i `/blog/page/2–4/` (content_parsing) liczy 31 wpisów. Kategorie z menu:

| Kategoria | Adres | Stan |
|---|---|---|
| Wnętrza | `/tematy/wnetrza/` | 2 strony listy |
| Remont | `/tematy/remont/` | 3 strony listy |
| Ogród | `/tematy/ogrod/` | 1 strona, 4 wpisy (taras, trawnik, założenie ogrodu, projekt ogrodu) |
| Kalkulatory budowlane | `/tematy/kalkulatory-budowlane/` | **pusta**, 13 słów, „No results found.” |

Przykłady tematów: „Ile kosztuje remont mieszkania 60m2?”, „Ile kosztuje remont łazienki?”, „Ile kosztuje projekt kuchni?”, „Ile kosztuje wymiana okna?”, „Jak pomalować sufit bez smug?”, „Jak urządzić mały balkon?”. Wpisy przeskanowane w crawlu mają od 1147 do 1882 słów [crawl, `pages`]. Wpisy powstały między listopadem a grudniem 2025: najstarsza widoczna data to 18.11.2025, najnowsza 19.12.2025 (SERP `site:`, daty w wynikach). Od 19.12.2025 do 18.10.2026 na liście bloga nie pojawił się żaden nowszy wpis (content_parsing `/blog/`).

**Technologia** [crawl, `summary` i HTML]: WordPress 6.9.10, motyw GeneratePress z blokami GenerateBlocks, wtyczka Elementor 4.3.5, Yoast SEO, LiteSpeed Cache, ShortPixel (obrazy WebP przez `sp-ao.shortpixel.ai`), Easy Table of Contents (spis treści w artykułach), Site Kit by Google. Serwer LiteSpeed, certyfikat SSL od cyber_Folks S.A. ważny do 17.11.2026.

## 2. Kontakt, strony prawne, stopka

- **Kontakt:** w HTML strony głównej, „O mnie”, kategorii i artykułu nie ma linków `mailto:` ani `tel:`, linków do Facebooka, Instagrama, Pinteresta, YouTube czy TikToka ani formularza kontaktowego. Jedyne formularze to wyszukiwarka (`<form role="search" …>`) i komentarze (`<form action="https://wnetrzakamila.pl/wp-comments-post.php" … id="commentform">`) [crawl, raw_html].
- `/kontakt/`: **404** (instant_pages).
- **Polityka prywatności:** `/polityka-prywatnosci/` i `/privacy-policy/` zwracają **404** (instant_pages). W stopce, menu i formularzu komentarzy nie ma linku do takiej strony [crawl].
- **Regulamin:** `/regulamin/` zwraca **404** (instant_pages). W menu i stopce nie ma takiego linku [crawl].
- **Stopka (cała treść):** „Copyright @2026 Wnętrza Kamila”. Nie ma tu nazwy firmy, imienia i nazwiska, adresu, NIP-u ani e-maila administratora [crawl, raw_html strony głównej i artykułu].
- **Formularz komentarzy:** pola „Komentarz”, „Nazwa *”, „E-mail *”, „Witryna internetowa” oraz checkbox „Zapamiętaj moje dane w tej przeglądarce podczas pisania kolejnych komentarzy.”. Przy formularzu nie ma informacji, kto przetwarza dane ani linku do polityki [crawl, raw_html artykułu „Ile kosztuje projekt domu?”]. To opis stanu, bez oceny prawnej.

## 3. „O mnie” i fakty o autorze

To tylko opis tego, co jest na stronie. Niczego tu nie dopisuję.

- `/o-mnie/` (content_parsing, raw_html): H2 „Cześć, jestem Kamil”. Treść: „Pasjonat wnętrz, który uwielbia przekształcać przestrzenie… **Od kilku lat dzielę się praktycznymi poradami** z zakresu aranżacji wnętrz i projektowania…”, „Na blogu znajdziesz zarówno proste triki DIY, jak i inspiracje najnowszymi trendami designu”. Strona ma 91 słów i nie ma H1 [crawl, `pages`]. Nie ma zdjęcia autora: obrazy to ozdobnik „Flower design” i okładki wpisów. Nie ma też nazwiska, kontaktu ani linków do profili.
- Ramka „Witaj na moim blogu!” w pasku bocznym artykułów (raw_html artykułu): „Poznaj Kamila, kreatywny umysł stojący za tym blogiem o wnętrzach i kolorach. **Kamil to absolwent architektury wnętrz, który po latach pracy w studio projektowym** postanowił podzielić się swoją wiedzą…”.
- **Niespójność:** „O mnie” mówi o pasji i „kilku latach” dzielenia się poradami. Ramka podaje wykształcenie (architektura wnętrz) i lata pracy w studiu. Według zasad projektu fakty o autorze muszą być potwierdzone przez właściciela. Do decyzji: czy te dane są prawdziwe.
- Autor w danych strukturalnych to `"name":"kamil"` z małej litery, z avatarem Gravatar [crawl, schema Yoast]. Strona autora `/author/kamil/` zwraca 404 (instant_pages). Na stronie głównej przy wpisie widnieje angielskie „By kamil / 19 grudnia, 2025” [crawl].

## 4. Model zarobku

| Źródło | Stan 18.10.2026 | Dowód |
|---|---|---|
| Google AdSense / sieci reklamowe | brak | w HTML nie ma `adsbygoogle`, `pagead2`, `ca-pub-` [crawl, raw_html 5 stron] |
| Linki afiliacyjne | brak | 15 linków zewnętrznych prowadzi do stron głównych lub kategorii bez parametrów partnerskich: archipelag.pl, extradom.pl, izbaarchitektow.pl, dobrzemieszkaj.pl, meble.pl, ikea.com (2 adresy), twojogrodek.pl, muratordom.pl, homebook.pl, westwing.pl [crawl, `/v3/on_page/links`, direction=external] |
| `rel="sponsored"` / `nofollow` przy linkach | brak | wszystkie 15 linków ma `"dofollow": true` [crawl, `links`] |
| Newsletter | brak | brak formularza zapisu i skryptów MailerLite, Mailchimp czy GetResponse [crawl] |
| Własne usługi / produkty | brak | brak stron ofertowych [crawl, `pages`] |
| Wpisy sponsorowane | nieoznaczone, nie widać ich | brak oznaczeń „współpraca”, „sponsorowany” [crawl] |

Strona nie ma dziś żadnego mechanizmu zarobku. Tematy „Ile kosztuje…?” przyciągają ludzi, którzy planują wydatek (remont, projekt, meble na wymiar). To ruch, który da się zamienić na leady dla wykonawców, afiliację albo reklamy. Wybór modelu należy do właściciela (pytania niżej).

## 5. Kalkulatory budowlane

- **Na stronie nie ma żadnego kalkulatora.** Kategoria `/tematy/kalkulatory-budowlane/` jest pusta: H1 „Kalkulatory budowlane”, potem „No results found.” (angielski tekst motywu), 13 słów [instant_pages, content_parsing, raw_html].
- Na przeskanowanych stronach nie ma elementów `<input>` poza komentarzami i wyszukiwarką. Nie ma też `<iframe>` ani skryptów kalkulatora [crawl, raw_html artykułu o tarasie].
- **Obietnica bez pokrycia.** Pustą kategorię linkują: menu (każda strona), kafelek na stronie głównej i treść artykułów. Przykład z „Ile kosztuje zrobienie tarasu?”: „A jeśli potrzebujesz pomocy w oszacowaniu kosztów innych prac budowlanych, sprawdź nasze `<a href="https://wnetrzakamila.pl/tematy/kalkulatory-budowlane/">kalkulatory budowlane</a>`, które pomogą Ci w precyzyjnym planowaniu budżetu.” [crawl, raw_html]. Wyszukiwarka strony dla słowa „kalkulator” zwraca 7 wpisów i stronę główną, na przykład „Ile kosztuje remont mieszkania 60m2?”, „Jak pomalować sufit bez smug?” i „Jak pomalować płytki w łazience?” (content_parsing `/?s=kalkulator`). Prawdopodobnie zawierają podobne odesłanie. Sprawdziłem to tylko na wpisie o tarasie.
- UX kalkulatorów na telefonie: nie ma czego ocenić. Czytelnik, który kliknie link z artykułu, trafia na pustą stronę.

## 6. Pierwsze wrażenie, nawigacja, CTA

Zrzuty nie zostały pobrane (szczegóły w sekcji 9), więc ten opis opiera się na HTML i treści.

**Strona główna** [crawl, raw_html; instant_pages z user-agentem iPhone]:
- Kolejność: menu, ilustracja SVG, H1 „Piękne Wnętrza, Krok po Kroku”, tekst powitalny, przycisk **„ODKRYJ BLOGA”** (`href="https://wnetrzakamila.pl/blog/"`), 3 najnowsze wpisy, 4 kafelki kategorii (Wnętrza, Remont, Ogród, Kalkulatory budowlane), sekcja „Najnowsze” z linkiem „Wszystkie wpisy”, sekcja „Na czasie”.
- To jedyny CTA na stronie. Prowadzi do listy wpisów. Na stronie nie ma żadnego działania, które coś daje właścicielowi (zapis, kontakt, klik partnerski).
- Strona główna ma 167 słów. Tytuł to „Home - Wnętrza Kamila”, brak meta description, wynik w Google „Wnętrza Kamila: Home” [instant_pages; SERP `site:`].
- Pozostałości szablonu w kodzie: `aria-label="Style &amp; Fashion"` na kafelku Remont, `aria-label="Travel &amp; Inspiration"` na kafelku Ogród, `aria-label="Read article"`, `<meta name="apple-mobile-web-app-title" content="MyWebSite">`, opis Open Graph kończy się „... Read more” [crawl, raw_html strony głównej]. Czytniki ekranu przeczytają te angielskie etykiety.
- Ilustracja na górze (`wnetrze_kamila.svg`) ma w wyrenderowanym DOM status leniwego ładowania `data-ll-status="error"`. To samo dotyczy ozdobnika na „O mnie” [crawl]. Mogło to wystąpić tylko w przeglądarce crawlera. Trzeba to sprawdzić na zrzucie albo na żywo.

**Nawigacja** [crawl, `<header>`]: menu ma 6 pozycji: Strona główna, O mnie, Wnętrza, Remont, Ogród, Kalkulatory budowlane. Do tego ikona wyszukiwania. Na telefonie motyw pokazuje przycisk „Menu” (hamburger) i ikonę lupy (`has-inline-mobile-toggle`, `mobile-header`), menu jest przyklejone (`sticky-menu-fade`). W menu brakuje „Blog”, „Kontakt” i „Polityka prywatności”.

**Artykuł** (na przykładzie „Ile kosztuje projekt domu?”) [content_parsing, raw_html]:
- Kategorie, H1, data („18 grudnia, 2025”), wstęp, spis treści (Easy Table of Contents), treść, „Powiązane wpisy”, „Podobne wpisy”, formularz komentarza, pasek boczny z ramką o autorze.
- W kodzie pasek boczny (`is-right-sidebar`) stoi za komentarzami. W jednokolumnowym układzie na telefonie ramka o autorze trafi więc na sam dół, pod formularz. Do potwierdzenia na zrzucie.
- Artykuł nie kończy się żadnym działaniem poza linkami do innych wpisów i komentarzem.

**Gdzie użytkownik się gubi:**
1. Klik „Kalkulatory budowlane” z menu, kafelka albo artykułu kończy się pustą stroną z angielskim „No results found.”
2. Czytelnik, który chce zapytać autora, zlecić projekt albo zgłosić błąd, nie ma jak tego zrobić.
3. Ceny w artykułach nie mają źródeł ani dat. Przykład z „Ile kosztuje projekt domu?”: „Ceny zaczynają się już od 2000 złotych i mogą sięgać nawet 6000-8000 złotych”, „Cena indywidualnego projektu domu zaczyna się od około 15 000 złotych”. Meta description tego wpisu brzmi „Ile kosztuje projekt domu **w 2025**?…” [content_parsing, raw_html]. Czytelnik nie wie, czy kwoty są aktualne. Według zasad projektu (CLAUDE.md) takie kwoty trzeba potwierdzić u źródła albo zastąpić odesłaniem do cennika.
4. Opisy alternatywne zdjęć są po angielsku, na przykład „2 brown wooden armchairs beside white wall”, „white and black gas range oven” [crawl, raw_html].
5. Literówka w treści: „Z odpowiednim planowaniem, rozsądnym budżetem i **trocią** cierpliwości” w „Ile kosztuje zrobienie tarasu?” [crawl, raw_html].

## 7. Analityka

Skrypty znalezione w wyrenderowanym HTML stron: główna, O mnie, kategoria i artykuł [crawl, raw_html; `/v3/on_page/resources`, resource_type=script]:

| Narzędzie | Stan | Cytat z kodu |
|---|---|---|
| Google tag (gtag.js) przez Site Kit | **jest** | `<script src="https://www.googletagmanager.com/gtag/js?id=GT-5D9RK4ZX" id="google_gtagjs-js" async="">`, `gtag("config", "GT-5D9RK4ZX");`, `<meta name="generator" content="Site Kit by Google 1.189.0">` |
| Zdarzenia czytania treści (Site Kit) | **jest** | `window._googlesitekit.contentEvents={…"readTimeThresholdPercent":85,"minimumReadTimeSeconds":5}` i funkcja `gtag( "event", name, { ...data, event_source: "site-kit" } )` |
| GA4 (identyfikator `G-…`) | niewidoczny w HTML | w HTML jest tylko `GT-5D9RK4ZX`; usługi docelowe (GA4, Google Ads) zapisane są w kontenerze tagu, którego proxy nie pozwoliło pobrać |
| Google Tag Manager (`GTM-…`) | brak | |
| Meta Pixel (`fbq`) | brak | |
| Hotjar, Microsoft Clarity, Plausible, Matomo | brak | |
| AdSense | brak | |

Jedyny zewnętrzny skrypt ładowany przez stronę to tag Google (179 404 bajtów po kompresji). Reszta to pliki z własnego serwera [crawl, `resources`].

**Cele i konwersje:** w kodzie nie widać zdarzeń konwersji (formularz, klik w link partnerski, zapis). Na stronie nie ma zresztą takich działań. Cele mogą być ustawione w panelu GA4, a tego bez dostępu do konta nie da się sprawdzić.

## 8. Cookies i zgody (tylko opis stanu)

- **Brak banera i CMP.** W wyrenderowanym HTML (crawl z włączonym JavaScriptem) nie ma śladów Cookiebot, CookieYes, Complianz, Borlabs, iubenda, OneTrust ani innego banera [crawl, raw_html 5 stron].
- **Tag Google ładuje się od razu.** `gtag.js` jest w `<head>` z atrybutem `async`. W kodzie nie ma wywołań `gtag('consent', 'default', …)` (Consent Mode) [crawl, raw_html strony głównej].
- Inne mechanizmy zapisujące dane w przeglądarce: checkbox zgody na zapamiętanie danych w komentarzach (`wp-comment-cookies-consent`) i skrypt `eztoc-js-cookie` wtyczki spisu treści [crawl].
- Nie ma polityki prywatności ani polityki cookies (sekcja 2).

## 9. Zrzuty ekranu

Zrzuty zrobiłem przez `/v3/on_page/page_screenshot` (pełna strona, presety `mobile` i `desktop`). Proxy sesji blokuje host `api.dataforseo.com` dla curla (CONNECT 403), więc plików PNG nie udało się pobrać. Lighthouse (`/v3/on_page/lighthouse/live/json`, który zwraca zrzut w base64) dwa razy zwrócił pusty wynik. Linki do zrzutów są w `analiza/zrzuty/linki.txt`:

- strona główna, telefon i komputer;
- artykuł „Ile kosztuje projekt domu?”, telefon i komputer;
- kategoria „Kalkulatory budowlane”, telefon;
- „O mnie”, telefon.

Wnioski o wyglądzie (sekcja 6) trzeba potwierdzić na tych zrzutach albo w Playwright, gdy domena będzie dostępna.

---

## Problemy i rekomendacje

Priorytet: **P1** = zrobić najpierw (szkodzi zaufaniu albo blokuje zarabianie), **P2** = ważne, **P3** = porządki.

| # | Problem | Priorytet | Rekomendacja |
|---|---|---|---|
| 1 | Pusta kategoria „Kalkulatory budowlane” jest w menu, na stronie głównej i w artykułach | P1 | Zbudować 2–3 pierwsze kalkulatory (na przykład koszt malowania m², remontu łazienki, ilość farby) albo do tego czasu usunąć pozycję z menu, kafelek i zdania „sprawdź nasze kalkulatory” |
| 2 | Brak kontaktu (strona, e-mail, formularz) | P1 | Dodać stronę „Kontakt” z adresem e-mail albo prostym formularzem, link w menu i stopce |
| 3 | Brak polityki prywatności i danych administratora w stopce | P1 | Decyzja właściciela. Treści prawne należą do niego (CLAUDE.md), my nie piszemy porad prawnych |
| 4 | Tag Google ładuje się bez banera zgód | P1 | Opis stanu. Decyzja o banerze, CMP i Consent Mode należy do właściciela |
| 5 | Sprzeczne fakty o autorze („pasjonat” na „O mnie”, „absolwent architektury wnętrz… lata pracy w studio” w ramce) | P1 | Właściciel potwierdza prawdziwe dane, potem ujednolicamy oba miejsca. Niepotwierdzone zdania usuwamy |
| 6 | Ceny w artykułach bez źródeł i dat, meta z „2025” | P2 | Przegląd kwot według zasad projektu: źródło i data albo „sprawdź w cenniku” z linkiem |
| 7 | Strona nie ma żadnego modelu zarobku ani działania dla czytelnika poza czytaniem | P2 | Po decyzji właściciela dodać jeden konkretny element na końcu artykułu: kalkulator, link partnerski z `rel="sponsored"` albo zapis na listę |
| 8 | Analityka mierzy tylko odsłony i czytanie, bez celów | P2 | Gdy pojawią się działania (kalkulator, kontakt, klik partnerski), dodać zdarzenia w GA4. Potrzebny dostęp do konta Google, żeby sprawdzić, gdzie trafia `GT-5D9RK4ZX` |
| 9 | Brak nowych wpisów od 19.12.2025 | P2 | Plan treści według skilla `klaster-tresci`, z harmonogramem |
| 10 | Angielskie resztki szablonu: „No results found.”, „By kamil”, „Read more”, aria-label „Style & Fashion”, „Travel & Inspiration”, „MyWebSite”, angielskie alt-y | P3 | Przetłumaczyć lub usunąć |
| 11 | Tytuł strony głównej „Home - Wnętrza Kamila”, brak meta description | P3 | Polski tytuł i opis (szczegóły w `seo-tresci.md`) |
| 12 | Strona autora `/author/kamil/` zwraca 404, „O mnie” bez H1 i zdjęcia | P3 | Po potwierdzeniu faktów: H1, zdjęcie (jeśli właściciel chce), link do kontaktu |
| 13 | Literówka „trocią cierpliwości” | P3 | Poprawić przy przeglądzie treści |
| 14 | `data-ll-status="error"` przy ilustracji na górze strony głównej | P3 | Sprawdzić na żywo, czy grafika się wyświetla |

---

## Pytania do właściciela

1. **Cel strony.** Co ma dawać blog: ruch i reklamy (AdSense lub inna sieć), afiliację (sklepy meblowe, materiały budowlane), leady dla wykonawców, czy promocję własnych usług (na przykład projektowania wnętrz)?
2. **Usługi.** Czy Ty albo Twoja firma sprzedajecie coś, co ma się pojawić na stronie? Jeśli tak: co, dla kogo, w jakim mieście i za ile?
3. **Autor.** Które fakty są prawdziwe: „absolwent architektury wnętrz”, „lata pracy w studio projektowym”, „od kilku lat dzielę się poradami”? Czy podajemy nazwisko i zdjęcie?
4. **Kalkulatory.** Czy budujemy kalkulatory, czy na razie usuwamy tę kategorię z menu? Jeśli budujemy, to które najpierw?
5. **Kontakt.** Jaki adres e-mail albo jaką formę kontaktu mamy podać? Czy chcesz formularz?
6. **Dane administratora i polityka prywatności.** Kto jest administratorem strony (osoba czy firma)? Czy przygotujesz politykę prywatności sam, czy z prawnikiem? Czy treści prawne (przepisy, RODO jako temat) mogą trafiać do poradników?
7. **Cookies.** Czy wdrażamy baner zgód (CMP) i Consent Mode? Wybór narzędzia należy do Ciebie.
8. **Analityka.** Czy dasz dostęp do Google Analytics i Search Console? Pod `GT-5D9RK4ZX` jest tylko GA4, czy też coś innego?
9. **Reklamy na stronie.** Jeśli AdSense: czy akceptujesz reklamy w treści artykułów? Remarketing zostaje wyłączony, chyba że zdecydujesz inaczej.
10. **Afiliacja.** Czy linki do IKEA, Westwing, Homebook i innych mają zostać zwykłymi linkami, czy zamieniamy część na partnerskie, oznaczone `rel="sponsored"`?
11. **Platforma.** Zostajemy przy WordPressie (GeneratePress, Elementor, hosting cyber_Folks), czy przenosimy stronę do repozytorium (na przykład Astro, jak w niechcieznajda)?
12. **Komentarze.** Czy komentarze mają zostać włączone pod wpisami?

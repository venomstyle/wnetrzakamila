# Brief: nowe klastry dla „Niech Cię znajdą” (17.10.2026)

## Najpierw przeczytaj
1. Skill: `/home/user/niechcieznajda/.claude/skills/klaster-tresci/SKILL.md` oraz `references/szablon-artykulu.md` i `references/styl.md`.
2. Zasady projektu: `/home/user/niechcieznajda/CLAUDE.md` (obowiązują bezwzględnie).
3. Plan: `/home/user/niechcieznajda/content-plan.md` (kontekst istniejących klastrów) oraz dane fraz: `research/frazy-marketing-fachowcow-2026-10-17.json`, `research/frazy-klientow-branze-2026-10-13.json`.
4. Wzór gotowego tekstu i huba (format, ton, długość): `src/content/poradniki/fixly-dla-wykonawcow.md`, `src/content/poradniki/zlecenia-budowlane.md`, hub `src/content/poradniki/zlecenia-i-klienci.md`.

## Projekt
- Marka „Niech Cię znajdą” (niechcieznajda.pl): poradniki dla fachowców (hydraulik, elektryk, stolarz, płytkarz, dekarz, ekipa remontowa). Lejek: poradnik → darmowy audyt strony i wizytówki → strona dla fachowca (od 2 900 zł jednorazowo) → opieka.
- ODBIORCA: właściciel 1–5-osobowej firmy usługowej, mało czasu, mało wiedzy technicznej, czyta na telefonie. Pisz prosto, bez żargonu; każdy termin (CPC, indeksowanie) wyjaśnij jednym zdaniem przy pierwszym użyciu.
- Autor: **Kamil**. Jedyny fakt o autorze: „7 lat projektuję strony i aplikacje”. Nigdy „10+ lat”, liczby klientów, case'ów, testów ani wyników, których nie było.
- Autor sprzedaje strony dla fachowców. Gdy tekst porównuje kanały albo ceny, dodaj jedno zdanie ujawnienia (jak w `ile-kosztuje-wizytowka-google.md`).
- **TRYB AUTOMATYCZNY:** tekst gotowy do publikacji bez udziału autora. Bez ramek `[!praktyka]`, bez `[DO UZUPEŁNIENIA]`. Twierdzenie, którego nie potwierdzisz u źródła, usuń.
- **BEZ TREŚCI PRAWNYCH (twarda zasada):** żadnych ustaw, artykułów, kodeksów, kar, UOKiK, RODO, PKE, DSA, VAT/podatków, umów, odsyłania do prawnika. Opisujemy zasady Google/Meta, cenniki, praktykę i dane. Nigdy nie zachęcamy do kupowania opinii.

## Styl (zasady projektu, ważniejsze niż ogólne)
- Do czytelnika na „Ty” (wielka litera w formach Ty/Twój), autor w 1. os. tylko przy rzeczach naprawdę zrobionych („sprawdziłem cennik 17 października 2026”).
- Najwyżej jeden myślnik na akapit; w tytułach i nagłówkach separator to dwukropek.
- Bez konstrukcji „nie X, tylko Y” / „to nie X, to Y”. Bez wyliczanek trójkowych dla efektu. Bez frazesów z `styl.md`.
- Konkretne liczby, akapity 2–4 zdania, nagłówki zdaniem (wielka litera tylko na początku). Liczby z twardą spacją tysięcy (2 900 zł), przecinek dziesiętny, cudzysłów „”.
- Ceny w treści: tylko rynkowe ze źródeł (URL + data). Cena marki tylko w `cta` we frontmatterze.

## Źródła i dostęp do internetu (WAŻNE)
- WebFetch i curl NIE działają w tej sesji (DNS). Do czytania stron używaj DataForSEO: załaduj narzędzie `ToolSearch` → `select:mcp__DataForSeo__api_request`, potem `POST /v3/on_page/content_parsing/live` z `data: [{"url":"<URL>"}]` → tekst strony jest w `page_content.main_topic[].primary_content[].text`. Duże odpowiedzi zapisują się do pliku: wtedy wyciągnij tekst Pythonem.
- Do znajdowania URL-i: WebSearch (wyniki z USA, więc dodawaj polskie słowa) albo SERP DataForSEO `POST /v3/serp/google/organic/live/regular` z `[{"keyword":"...","location_code":2616,"language_code":"pl","depth":10}]` (jedno zadanie na wywołanie).
- Każdy fakt, liczba, krok w interfejsie: źródło pierwotne (pomoc Google/Meta, oficjalne cenniki firm), sprawdzone dziś. Nie przepisuj blogów agencji jako źródła faktów. Nie potwierdzisz → usuń.
- Limit kosztów: najwyżej ~40 wywołań DataForSEO na agenta.

## Format pliku
- Plik: `/home/user/niechcieznajda/src/content/poradniki/<slug>.md`. Tylko Twoje pliki; nic innego w projekcie nie zmieniaj (wyjątek: plik danych w `research/`, jeśli zadanie go wymaga).
- Frontmatter jak w `fixly-dla-wykonawcow.md` (pola: title, seoTitle ≤ 60 znaków, description 120–160 znaków z liczbą, slug, type, category, kicker, cluster, hub, primaryKeyword, secondaryKeywords, intent, publishedAt, verifiedAt, updatedAt, author, readingTime, lead, tldr, cover, faq, sources, related, cta, draft).
  - `author: Kamil`, `publishedAt: 2026-10-17`, `verifiedAt: 2026-10-17`, `updatedAt: 2026-10-17`, `draft: true` (datę publikacji ustawi koordynator).
  - `cover:` bez `src/og`; `big` tylko prawdziwa, zweryfikowana liczba (krótka, np. „1,74 zł”), `sub` jej kontekst (≤ 90 znaków), `label` ≤ 45 znaków, `alt`.
  - hub (type: hub) ma: title, seoTitle, description, slug, type: hub, kicker, cluster, primaryKeyword, secondaryKeywords, intent, daty, author, lead, cover, cta, draft – bez faq/sources jest OK, ale lead z liczbą ze źródła.
- Treść: bez H1, 4–7 sekcji H2, lead we frontmatterze (pierwsze zdanie z liczbą), FAQ (4–6) i źródła tylko we frontmatterze.
- Ramki: `> [!uwaga]`, `> [!wzor] Tytuł`, `> [!liczba] wartość`. Kroki: `### Krok 1: …`. Tabele z podpisem kursywą: źródło i data.
- Linki wewnętrzne (≥ 3 w treści) TYLKO do: `/strona-dla-fachowca/`, `/audyt-strony/`, `/wizytowka-google/`, `/narzedzia/koszt-zlecenia/`, `/poradniki/` oraz poradników `/poradniki/<slug>/` z listy:
  istniejące: czy-wizytowka-google-jest-platna, darmowa-strona-internetowa, firmowy-email-i-domena, fixly-dla-wykonawcow, ile-kosztuje-strona-internetowa, ile-kosztuje-utrzymanie-strony, ile-kosztuje-wizytowka-google, ile-opinii-ma-konkurencja, jak-odpowiadac-na-opinie-google, jak-robic-zdjecia-realizacji, jak-sprawdzic-strone-internetowa, jak-usunac-opinie-z-google, jak-usunac-wizytowke-google, jak-wystawic-opinie-w-google, jak-zalozyc-wizytowke-google, kiedy-klienci-szukaja-fachowca, kupowanie-opinii-google, link-do-opinii-google, modernizacja-strony-internetowej, oferteo-dla-wykonawcow, pozycjonowanie-lokalne, pozycjonowanie-wizytowki-google, strona-czy-facebook, strona-dla-firmy-budowlanej, strona-firmowa (hub), strona-w-abonamencie-czy-jednorazowo, strona-wizytowka, tania-strona-internetowa, wizytowka-i-opinie (hub), zlecenia-budowlane, zlecenia-i-klienci (hub);
  nowe (powstają równolegle): reklama-dla-fachowca (hub), ile-kosztuje-reklama-w-google, reklama-na-samochodzie, ile-kosztuje-reklama-na-facebooku, czy-google-widzi-twoja-strone (hub), jak-dodac-strone-do-google, search-console-dla-firmy, jak-sprawdzic-pozycje-strony, zapytania-od-klientow (hub), whatsapp-business-dla-firmy, oferta-cenowa-wzor, jak-odpisac-na-zapytanie-klienta, chatgpt-dla-fachowca, telefon-w-firmie (hub), przekierowanie-polaczen, poczta-glosowa, drugi-numer-w-telefonie, platnosci-u-klienta (hub), terminal-w-telefonie, terminal-platniczy-cena, terminal-sumup, kod-qr-dla-firmy (hub), jak-zrobic-kod-qr, kod-qr-na-wizytowce-i-aucie, firma-w-innych-mapach (hub), apple-business, bing-places.
  Narzędzie (powstaje równolegle): `/narzedzia/kod-qr/` (generator kodów QR w przeglądarce).
- Kolejne klastry wychodzą w różnych tygodniach: linkuj do nowych slugów tylko tam, gdzie to naturalne (build sam zamieni linki do jeszcze nieopublikowanych tekstów na zwykły tekst).
  `related:` tylko slugi z tej listy (3).
- Długość: poradnik 1 200–2 000 słów treści; hub 250–500 słów.
- `cta.href`: klaster „Reklama dla fachowca” → `/strona-dla-fachowca/`; klaster „Strona w Google” → `/audyt-strony/`. Tekst CTA w stylu istniejących (darmowy audyt: wideo w 3 dni robocze; strona od 2 900 zł jednorazowo).

## Na koniec
QA na swoich plikach i popraw błędy (uwagi oceń; „publishedAt w przyszłości” nie wystąpi; „related nie istnieje” jest OK dla nowych slugów):
`cd /home/user/niechcieznajda && python3 .claude/skills/klaster-tresci/scripts/sprawdz.py <Twoje pliki> --lp /strona-dla-fachowca/ --known /audyt-strony/ /wizytowka-google/ /poradniki/ /narzedzia/koszt-zlecenia/ /narzedzia/kod-qr/`
Do `cta.href` i linków możesz też użyć `/narzedzia/kod-qr/`.
Potem usuń `.claude/skills/klaster-tresci/scripts/__pycache__`, jeśli powstał. Nie rób commitów.

Zwróć (krótko): ścieżki plików, liczbę słów, źródła z datą, frazę główną, okładkę (big/sub/label) każdego tekstu, wynik QA oraz twierdzenia usunięte z braku źródła.

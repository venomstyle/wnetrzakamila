---
name: klaster-tresci
description: Jedna powtarzalna metoda budowy bloga z treściami SEO (rynek polski) dla dowolnej marki - wokół landing page'a albo jako nowy serwis. Stała struktura i proces według sprawdzonego blueprintu (dane → typy stron → odpowiedź od pierwszego zdania → zaufanie → narzędzie → monetyzacja → świeżość) - mapa tematów, huby, poradniki, porównania, strony encji, gotowy szkielet Astro, linkowanie, QA, przegląd wizualny, audyt prawny, harmonogram. Wygląd projektowany od zera dla marki, a styl bloga, logo i okładki użytkownik wybiera z arkuszy opcji. Używaj zawsze, gdy użytkownik chce "pokryć tematy dookoła" LP, zrobić content pod SEO, blog firmowy, bazę wiedzy, hub tematyczny, topic cluster, content plan, programmatic SEO, napisać kilka/kilkadziesiąt artykułów lub poradników, albo mówi "zrób jak w paliwowni" / "jak w niechcieznajda", nawet jeśli nie pada słowo "klaster" ani "SEO".
---

# Blog z klastrem treści: jedna metoda dla każdej marki

Ten skill zamienia projekt (najczęściej landing page z jedną ofertą) w blog, który pokrywa najważniejsze tematy wokół oferty: huby, poradniki, porównania, strony encji i narzędzie, spięte linkowaniem i prowadzące do konwersji.

**Ta sama struktura, inny wygląd.** Struktura (typy stron, kolejność bloków, dane strukturalne, linkowanie, publikacja) i proces są zawsze te same. Wygląd projektujesz od zera dla marki, a jego kluczowe elementy **wybiera użytkownik z arkuszy opcji** w stałych punktach decyzji (niżej oznaczone **⏸ WYBÓR**).

**Blueprint, nie kopia.** Mechanizmy wyprowadziliśmy z analizy paliwownia.pl (wzorzec) i promptowy.com (kontrast), a wdrożenie przećwiczyliśmy na niechcieznajda (32 poradniki dla fachowców). Z tych serwisów nie bierzesz wyglądu, palety, motywów, nazw sekcji, metafory ani tekstów; z poprzednich projektów też nie (taśma miernicza należy do niechcieznajda). Test każdej decyzji: czy umiesz ją uzasadnić potrzebą odbiorcy tego projektu?

## Pliki referencyjne (czytaj, gdy dojdziesz do kroku)

| Plik | Kiedy |
|---|---|
| `references/blueprint.md` | 9 warstw mechanizmu; zawsze przed nowym serwisem, przy klastrze przy LP warstwy 2-5 |
| `references/planowanie-klastra.md` | architektura, intencje, tytuły, linkowanie, format planu |
| `references/szkielet.md` | szkielet Astro: co stałe i dlaczego, co z wyborów marki |
| `references/wybory.md` | **punkty decyzji: jak przygotować, pokazać i wdrożyć arkusz opcji** |
| `references/szablon-artykulu.md` | frontmatter i bloki każdego typu strony |
| `references/styl.md` | głos, zwroty do unikania, uczciwość, YMYL |
| `references/brief-agenta.md` | szablon briefu dla agentów piszących równolegle |
| `references/okladki.md` | hierarchia informacji na okładce i wymagania szablonu |
| `references/przeglad-wizualny.md` | zrzuty każdego typu strony i lista kontrolna |
| `references/przeglad-niezalezny.md` | po każdym klastrze: brief dla agenta, który nie zna sprawy |
| `references/audyt-prawny.md` | procedura audytu prawnego i aktualności, brief agenta, lista aktów PL |
| `references/integracja-stack.md` | Astro / Next / WordPress / statyczny HTML |
| `references/tryb-wydarzen.md` | seria 4-6 tekstów wokół zmiany w niszy |
| `references/wnioski-z-analizy.md` | fakty z analizy (do uzasadniania decyzji) |

Skrypty (`~/.claude/skills/klaster-tresci/scripts/`): `sprawdz.py` (QA), `okladka.py` (okładki z szablonu projektu), `arkusz.py` (arkusz opcji PNG), `logo.py` (logo w kontekście), `zrzuty.mjs` (zrzuty całych stron + kontrast), `harmonogram.py` (daty publikacji). Szkielet: `assets/szkielet-astro/`.

## Zasady stałe

**Każdy tekst musi coś dodawać.** Masowe treści bez wartości dodanej Google traktuje jako "scaled content abuse", a czytelnik je ignoruje (Promptowy: 3,6 tys. wpisów, ~3 tys. wizyt organicznych/mies.). Każdy temat w planie ma **element wartości dodanej**: własne wyliczenie, tabelę z danymi, gotowy wzór, checklistę, scenariusze "czy się opłaca", dane zebrane z rozproszonych źródeł. Bez niego temat wylatuje lub łączy się z innym.

**Uczciwość:**
- Nie wymyślaj doświadczeń, testów, liczby klientów ani lat praktyki. Tylko prawdziwe fakty o autorze z pamięci i plików projektu.
- **Tryb automatyczny (domyślny):** treść gotowa do publikacji bez udziału autora. Bez znaczników `[DO UZUPEŁNIENIA]` i ramek „z praktyki”; wartość dodana pochodzi ze źródeł, danych, wyliczeń, tabel i wzorów. Twierdzenie niepotwierdzone u źródła usuń. **Tryb z autorem** tylko na wyraźną prośbę: ramki `[!praktyka]` ze znacznikiem i `draft: true` do uzupełnienia.
- Każda liczba, kwota, termin i warunek ma źródło (URL + data sprawdzenia); bez źródła - usuń.
- `publishedAt` = dziś lub planowana data, nigdy wstecz. Afiliacja oznaczona, YMYL ze źródłami urzędowymi i zastrzeżeniem.

**Lokalnie:** pracuj i podglądaj lokalnie (`127.0.0.1`). Nie publikuj, nie wdrażaj i nie pushuj bez wyraźnej prośby; reguły projektu (AGENTS.md/CLAUDE.md) mają pierwszeństwo.

**Dwa tryby:** *klaster przy LP* (domyślny: istniejąca strona i oferta, 10-60 tekstów, huby, ewentualnie narzędzie; jeśli LP ma wygląd, wybór stylu dotyczy przedłużenia go na blog, a wybór logo zwykle odpada) albo *nowy serwis według blueprintu* (nowa nisza, dane encji, narzędzie, drabina monetyzacji, tożsamość marki; najpierw `blueprint.md` w całości).

## Przebieg pracy

Kolejność jest stała. Punkty **⏸ WYBÓR** to miejsca, w których **zatrzymujesz się, pokazujesz arkusz i czekasz na odpowiedź użytkownika** (szczegóły: `wybory.md`).

| # | Krok | Wynik |
|---|---|---|
| 1 | Badanie: projekt i tematy | notatka o projekcie, lista tematów z trendem |
| 2 | Plan | `content-plan.md` zaakceptowany przez użytkownika |
| 3 | Szkielet | blog działa lokalnie na neutralnych tokenach |
| 4 | **⏸ WYBÓR stylu** | tokeny i forma bloków marki |
| 5 | **⏸ WYBÓR logo** | logo, favikona |
| 6 | Pisanie | teksty (`draft: true`) |
| 7 | **⏸ WYBÓR okładek** | szablon okładki projektu |
| 8 | Okładki | PNG dla wszystkich tekstów |
| 9 | QA | raport `sprawdz.py` bez błędów |
| 9a | Przegląd niezależny | agent bez kontekstu sprawdza źródła, rachunki i uczciwość; raport + poprawki |
| 10 | Przegląd wizualny | zrzuty 1280/375, poprawki |
| 11 | Audyt prawny i aktualności | poprawki + „Do decyzji użytkownika” |
| 12 | Harmonogram | daty publikacji, codzienny rebuild |

Opcjonalny **⏸ WYBÓR wariantów sekcji** (np. CTA, spis, stopka) w dowolnym momencie po kroku 4, gdy użytkownik o to prosi.

### 1. Badanie

**Projekt.** Przeczytaj LP i pliki projektu. Zapisz w 5-8 punktach: ofertę i konwersję; odbiorcę i jego pytania przed zakupem; markę (nazwa, tokeny, fonty, logo, ton, idea marki); stack i miejsce na treści; autora i **prawdziwe** fakty o nim; reguły projektu. Braki zbierz w jedno pytanie do użytkownika, nie blokuj reszty pracy.

**Tematy.** Cel: 20-60 tematów w klastrach, pokrywających intencje z `planowanie-klastra.md`.
1. Narzędzie słów kluczowych, jeśli jest (np. OpenSEO `get_keyword_metrics`, `research_keywords`, `get_serp_results`): frazy grupuj w jednym wywołaniu, SERP-y tylko dla priorytetów (kredyty są skończone).
2. **Zawsze 12-miesięczny trend, nie średnia** ("ksef od kiedy": średnio 33 tys., ale spadek ze 110 tys. do 1,6 tys.).
3. Bez narzędzia: WebSearch, "Podobne pytania", fora, FAQ konkurencji, oficjalne dokumenty; zaznacz w planie, że wolumeny są nieznane.

### 2. Plan

`content-plan.md` w formacie z `planowanie-klastra.md`: jedna fraza główna = jeden URL, każdy tekst z hubem, CTA, wartością dodaną i listą linków. Wybierz z planu **kategorie (huby)**: od nich zależą kolory kategorii na okładkach i kartach. **Pokaż plan i poczekaj na akceptację** przed pisaniem więcej niż 2-3 tekstów.

### 3. Szkielet

Według `szkielet.md`: nowy projekt Astro = kopia `assets/szkielet-astro/`; istniejący projekt = przeniesienie brakujących części w jego konwencjach (inne stacki: `integracja-stack.md`). Wypełnij `marka.ts`, dodaj hub i 2-3 pierwsze teksty (choćby szkice), zastępcze okładki (`okladka.py --template src/okladki/zastepcza.html`), `npx astro build` i podgląd lokalny. Szkielet ma neutralne tokeny: to celowe, wygląd przyjdzie z wyboru.

### 4. ⏸ WYBÓR stylu bloga

2-3 kierunki uzasadnione marką, każdy z opisem i **tokenami** (kolory z kontrastem, kroje, skala, promienie, para kolorów na kategorię) oraz formą bloków. Pokaż je **na tym samym szkielecie i tych samych tekstach**: artykuł, hub, lista z kartami (1280 px) i artykuł na telefonie (375 px), złożone w arkusz (`zrzuty.mjs --wys 1700` + `arkusz.py --grupuj 4`). **Czekaj na wybór.** Iteruj. Wybór → `tokeny.css` + `marka.css`, zapis w `DECYZJE.md`.

### 5. ⏸ WYBÓR logo

Gdy marka nie ma logo: około 10 różnych opcji (pełne SVG + sam znak), każda w kontekście przez `logo.py`: nagłówek strony, karta przeglądarki z favikoną 18 px, znak 40 px, jasne i ciemne tło. W opisie wskaż, które opcje słabną w małym rozmiarze. **Czekaj na wybór.** Iteruj („kolejny zestaw”, „połącz 2 z 5”, „popraw 3”). Wybór → `Logo.astro`, `favicon.svg`, DECYZJE.md. Gdy logo jest: tylko kontrola kontekstu tym samym skryptem.

### 6. Pisanie

Przed pierwszym tekstem przeczytaj `szablon-artykulu.md` i `styl.md`. Dla każdego tekstu: fakty z pierwotnych źródeł (z datą) → tekst według bloków typu strony, lead z liczbą w pierwszym zdaniu → element wartości dodanej → frontmatter (`draft: true` do akceptacji użytkownika).

Partiami po 3-6. Przy >10 tekstach piszą równolegle agenci z briefem z `brief-agenta.md` (wypełnionym raz na projekt): każdy dostaje swoje wiersze planu, listę dozwolonych linków i slugów rodzeństwa; nigdy dwóch agentów na jednym pliku. Po powrocie: `sprawdz.py` na całości i przegląd kilku tekstów w całości.

### 7. ⏸ WYBÓR okładek i miniatur

Gdy są teksty z każdej kategorii i hub: około 5 szablonów HTML (hierarchia z `okladki.md`), każdy na **tych samych 5-6 prawdziwych tekstach** (po jednym z kategorii + hub bez liczby + długi tytuł), z innym kolorem tła lub ilustracją dla każdej kategorii. Render równoległy, arkusz `arkusz.py --grupuj 6` (wiersz = opcja). **Czekaj na wybór.** Iteruj. Wybór → `src/okladki/szablon.html`, kolory kategorii do tokenów, DECYZJE.md.

### 8. Okładki

```bash
python3 ~/.claude/skills/klaster-tresci/scripts/okladka.py --template src/okladki/szablon.html --from-dir src/content/poradniki --out public/okladki
```

Obejrzyj wszystkie miniatury jednym arkuszem (`arkusz.py public/okladki/*-og.png --cols 5 --cell 300`): długie tytuły, długie liczby, hub bez liczby.

### 9. QA

```bash
python3 ~/.claude/skills/klaster-tresci/scripts/sprawdz.py src/content/poradniki [--lp /oferta/] [--known /strona-spoza-src-pages/]
```

Sprawdza: title/description, lead z liczbą, H2, FAQ, źródła z datami, linki wewnętrzne (trasy z `src/pages/**` i `dist/` są znane automatycznie) i martwe `related`, kanibalizację fraz, frazesy, znaczniki, daty z przyszłości. Popraw błędy, oceń uwagi.

### 9a. Przegląd niezależny (po każdym klastrze)

Autor tekstów nie widzi własnych błędów: liczby „z pamięci”, źródła, które mówią co innego, wnioski podane jako fakty. Po napisaniu każdego klastra (rdzeń + dogrywka), przed PR z datami publikacji, uruchom **nowego agenta, który nie zna rozmowy ani procesu pisania**. Dostaje tylko `references/przeglad-niezalezny.md` i listę plików (6–10 na agenta). Sprawdza każde źródło dziś, przelicza rachunki, usuwa twierdzenia bez potwierdzenia, pilnuje uczciwości i zasad projektu. Ty po nim: okładki ze zmienionymi liczbami, spójność liczb między tekstami, sprawy do decyzji użytkownika w opisie PR.

### 10. Przegląd wizualny

Według `przeglad-wizualny.md`: `zrzuty.mjs --szer 1280,375 --kontrast` dla każdego typu strony, obejrzenie każdego zrzutu i lista kontrolna (kontrast tekstu na akcencie, makiety na ciemnym tle, hover, odstępy pod nagłówkami, linki sekcji na linii tytułu, kolumny stopki, długie tytuły na okładkach, nieaktualny CSS serwera deweloperskiego: restart procesu, nie cofanie kodu). Pokaż użytkownikowi pary przed/po.

### 11. Audyt prawny i aktualności

Według `audyt-prawny.md`: migawka treści → lista aktów sprawdzona u źródła → równolegli agenci na rozłącznych zestawach plików → diff z migawką → QA → raport z sekcją **„Do decyzji użytkownika”**. Nie ustawiaj publikacji, dopóki ta sekcja nie ma odpowiedzi.

### 12. Harmonogram

`scripts/harmonogram.py <katalog> --start RRRR-MM-DD --dni pn,sr,pt [--kolejnosc hub1,hub2] [--caly-klaster] [--zapisz] [--zatwierdz]` rozkłada teksty klastrami (hub razem z pierwszym tekstem klastra). Z `--caly-klaster` hub i wszystkie teksty klastra wychodzą jednego dnia, jeden klaster na dzień publikacji; sprawdź w regułach projektu, który tryb obowiązuje. Po publikacji klastra warto dać dogrywkę: przez 2–3 dni po jednym tekście na węższą frazę z badania (ustaw `publishedAt` ręcznie na kolejne dni). Data w przyszłości = wpis zaplanowany; szkielet pomija takie wpisy w buildzie, więc hosting musi robić codzienny rebuild (zaplanowany deploy hook). Gdy w niszy dzieje się coś ważnego: seria według `tryb-wydarzen.md`, źródła do obserwacji w `monitoring.md` projektu.

## Co oddajesz

- `content-plan.md` ze statusami i `DECYZJE.md` z wyborami (arkusze w `arkusze/`),
- działający lokalnie blog: szkielet + wygląd marki + teksty + okładki,
- raport QA, raport przeglądu wizualnego, raport audytu z sekcją „Do decyzji użytkownika”,
- listę twierdzeń usuniętych z braku źródła i krótką listę następnych kroków (np. narzędzie, rytm aktualizacji dat sprawdzenia, hosting z codziennym rebuildem).

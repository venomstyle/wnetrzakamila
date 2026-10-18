# Wnętrza Kamila (wnetrzakamila.pl): zasady projektu

> **Stan: przed analizą.** Sekcja „O projekcie” jest pusta. Pierwszy czat robi analizę według `START.md` i dopiero potem ją uzupełnia (po akceptacji właściciela).

## O projekcie

- Domena: wnetrzakamila.pl. Repozytorium: github.com/venomstyle/wnetrzakamila (na razie bez kodu strony).
- Czym się zajmuje firma, dla kogo, oferta i ceny, technologia i hosting obecnej strony: **do ustalenia w analizie**. Nie zgaduj; pytaj właściciela.

## Jak pracujemy (sprawdzone w projekcie niechcieznajda.pl)

- **Właściciel scala z telefonu.** Każda zmiana: gałąź → pull request do `main` → właściciel scala. Nie wypychaj prosto do `main` bez jego zgody.
- **Wybory wizualne należą do właściciela:** logo, styl, kolory, okładki, kreacje reklam. Pokazuj warianty na arkuszu opcji (np. `.claude/skills/klaster-tresci/scripts/arkusz.py`) i czekaj na decyzję.
- **Odpowiadaj po polsku, krótko, z linkami do PR.** Pytaj tylko o decyzje, które naprawdę należą do właściciela; resztę rób.
- **Duże zadania dziel na agentów** (pisanie klastra, badania), a po każdej serii tekstów rób **przegląd niezależny**: nowy agent bez kontekstu sprawdza źródła dziś, rachunki i uczciwość (`.claude/skills/klaster-tresci/references/przeglad-niezalezny.md`).

## Treści i uczciwość

- Treść w pełni automatyczna, bez znaczników `[DO UZUPEŁNIENIA]`. Twierdzenie bez źródła usuwamy. Każda liczba ma źródło i datę sprawdzenia.
- Ceny, których nie da się dziś potwierdzić u źródła, nie trafiają na stronę: zamiast kwoty „sprawdź w cenniku” z linkiem.
- Fakty o autorze i firmie tylko potwierdzone przez właściciela (bez dopisywania lat doświadczenia, liczby klientów, realizacji czy nagród).
- Bez kupowania opinii i bez zachęt za opinie. Prośba o opinię SMS-em albo mailem tylko do klientów, którzy zgodzili się na kontakt.
- Bez wzorów dokumentów do podpisu (umowy, protokoły) do pobrania.
- Treści prawne (przepisy, kary, RODO jako temat): **do decyzji właściciela**. W niechcieznajda zakazane w poradnikach; zapytaj, czy tu też.
- Źródła z licencją niekomercyjną odpadają.
- Styl: prosty polski, zdania oznajmujące, bez kalek, maks. jeden myślnik na akapit, bez „nie X, tylko Y” (`.claude/skills/klaster-tresci/references/styl.md`).

## Prywatność i dostęp

- **Nie korzystaj z poczty użytkownika (Outlook, żadna skrzynka) ani z Microsoft Teams.** Nie czytaj, nie szukaj, nie wysyłaj. Dotyczy też agentów.
- Bez zimnych maili, SMS-ów i telefonów do firm.
- Dane z Map Google w `research/` tylko zbiorczo, bez telefonów i adresów firm.
- Reklamy: bez remarketingu, chyba że właściciel zdecyduje inaczej.

## Narzędzia w sesji

- **DataForSEO** (MCP): wolumeny fraz (`/v3/keywords_data/google_ads/search_volume/live`), SERP (`/v3/serp/google/organic/live/advanced`), czytanie stron (`/v3/on_page/content_parsing/live`, `instant_pages` z `enable_javascript`), Google Ads Transparency. WebFetch/curl bywa blokowany przez proxy; wtedy czytaj strony przez DataForSEO.
- **Przeglądarka:** Playwright z `/opt/pw-browsers/chromium` (zrzuty, testy); Remotion renderuje z `/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell`.

## Dokumenty

- `START.md`: pierwsze zadanie (analiza obecnej strony).
- `playbook/`: co zbudowaliśmy w niechcieznajda i jak to przenieść (kod, prompty, lekcje).
- `.claude/skills/klaster-tresci`: metoda budowy treści SEO (plan, pisanie, okładki, QA, harmonogram).

# Pierwsze zadanie: analiza wnetrzakamila.pl

Wklej w nowym czacie (repozytorium venomstyle/wnetrzakamila):

> Przeczytaj CLAUDE.md, START.md i playbook/README.md. Zrób analizę obecnej strony wnetrzakamila.pl według START.md. Niczego jeszcze nie zmieniaj na stronie. Na koniec daj mi raport i plan w punktach i zapytaj o decyzje.

## Co zbadać (agenci równolegle, wyniki do `analiza/`)

1. **Strona i technika** (`analiza/strona.md`):
   - Wszystkie podstrony: crawl przez DataForSEO On-Page albo listę z mapy strony.
   - Technologia, hosting, czas ładowania i Core Web Vitals na telefonie, tytuły i opisy, nagłówki, dane strukturalne, mapa strony, robots.txt, przekierowania, błędy 404.
   - Zrzuty kluczowych stron (Playwright).
2. **Oferta i lejek** (`analiza/oferta.md`):
   - Co firma sprzedaje, komu, za ile, jak się zgłosić (formularz, telefon, WhatsApp).
   - Co jest dowodem: realizacje, opinie, portfolio.
   - Gdzie klient się gubi (ocena z perspektywy klienta na telefonie).
3. **Widoczność** (`analiza/widocznosc.md`):
   - Na jakie frazy strona się pokazuje (DataForSEO Labs: ranked keywords, domain overview).
   - Popyt na frazy z niszy (wolumeny z 12 miesięcy, sezonowość, CPC).
   - Profil Firmy w Google: jest, opinie, zdjęcia, kategorie.
   - Linki do strony.
4. **Konkurencja** (`analiza/konkurencja.md`):
   - 5–10 firm z Map Google i wyników wyszukiwania w tym samym mieście i niszy.
   - Ich strony, oferta, ceny, dowody, treści, reklamy (Google Ads Transparency).
   - Tylko dane zbiorcze, bez kontaktowania się z firmami.
5. **Synteza** (`analiza/RAPORT.md`):
   - 10 najważniejszych problemów z priorytetem (wpływ × koszt).
   - Szybkie poprawki (do tygodnia).
   - Plan na 3 miesiące: strona, treści (`klaster-tresci`), wizytówka, narzędzie, reklamy.
   - Lista pytań do właściciela.

Każde twierdzenie z danymi ma źródło (endpoint, URL, data). Raport kończy się pytaniami o decyzje: zakres, budżet, styl, czy przenosimy stronę do repozytorium (np. Astro, jak w niechcieznajda).

Po akceptacji raportu uzupełnij sekcję „O projekcie” w CLAUDE.md (pull request).

# Pierwsze zadanie: analiza wnetrzakamila.pl

Wklej w nowym czacie (repozytorium venomstyle/wnetrzakamila):

> Przeczytaj CLAUDE.md, START.md i playbook/README.md. Zrób analizę obecnej strony wnetrzakamila.pl według START.md. Niczego jeszcze nie zmieniaj na stronie. Na koniec daj mi raport i plan w punktach i zapytaj o decyzje.

## Co zbadać (agenci równolegle, wyniki do `analiza/`)

1. **SEO techniczne** (`analiza/seo-techniczne.md`):
   - **Crawl i indeksacja:** wszystkie podstrony przez DataForSEO On-Page (`/v3/on_page/task_post` + `summary`, `pages`, `duplicate_tags`, `links`, `non_indexable`, `redirect_chains`); kody odpowiedzi, błędy 404, przekierowania i łańcuchy.
   - **Pliki i nagłówki:** robots.txt, mapa strony (czy jest, czy pełna, `lastmod`), canonical, noindex, duplikaty treści i tytułów, parametry URL, wersje z www i bez, HTTP na HTTPS.
   - **Szybkość:** Core Web Vitals i Lighthouse na telefonie i komputerze (`/v3/on_page/lighthouse/live/json`) dla głównych typów stron: LCP, CLS, INP, waga obrazów, render-blocking.
   - **Telefon i dane:** wersja mobilna, dane strukturalne (LocalBusiness/HomeAndConstructionBusiness, Organization, BreadcrumbList, FAQ) i ich poprawność, Open Graph.
   - **Indeks Google:** `site:wnetrzakamila.pl` w SERP. Jeśli właściciel da dostęp do Search Console, także indeksacja i frazy z GSC.
2. **SEO on-page i treści** (`analiza/seo-tresci.md`):
   - **Metadane:** tytuły i opisy (długość, unikalność, fraza, zachęta do kliknięcia), H1 i struktura nagłówków.
   - **Treść:** długość i jakość, odpowiedź na intencję. Strony ofertowe: usługi × miasta.
   - **Linkowanie i obrazy:** linkowanie wewnętrzne, struktura URL, obrazy (alt, rozmiar, format WebP/AVIF, lazy loading).
   - **Treści cienkie i duplikaty:** strony z małą ilością treści albo powtórzoną treścią.
   - **Luki:** tematy, które klienci wyszukują, a strony nie ma.
3. **Słowa kluczowe i popyt** (`analiza/frazy.md`):
   - **Na co strona się pokazuje dziś:** DataForSEO Labs `ranked_keywords`, `domain_rank_overview`. Pozycje, ruch szacunkowy, strony, które go zbierają.
   - **Popyt w niszy:** wolumeny z 12 miesięcy (sezonowość, nie średnia) i CPC dla usług (np. projektowanie wnętrz, aranżacja, projekt kuchni lub łazienki), miast i pytań („ile kosztuje projekt wnętrza”).
   - **Mapa fraz:** frazy przypisane do istniejących albo brakujących stron, z oceną trudności.
   - **SERP:** jakie typy stron wygrywają, czy jest Local Pack, AI Overview, Grafika, wideo.
4. **SEO lokalne** (`analiza/seo-lokalne.md`):
   - **Profil Firmy w Google:** jest czy nie, kategorie, opisy, zdjęcia, opinie (liczba, ocena, odpowiedzi), posty, usługi.
   - **Pozycje w Mapach** dla fraz z miastem: DataForSEO `/v3/serp/google/maps/live/advanced` w kilku punktach miasta.
   - **Spójność danych NAP** (nazwa, adres, telefon) w katalogach i serwisach branżowych (np. Houzz, Oferteo, Fixly, Panorama Firm).
   - **Porównanie** z 3 firmami z najwyższymi pozycjami w Mapach.
5. **SEO zewnętrzne** (`analiza/linki.md`):
   - **Profil linków:** DataForSEO Backlinks (`summary`, `referring_domains`, `anchors`); liczba domen, jakość, toksyczne, utracone.
   - **Porównanie** z konkurencją i pomysły na linki: media branżowe, katalogi, partnerzy, realizacje u producentów.
6. **Oferta, UX i konwersja** (`analiza/oferta.md`):
   - **Oferta i kontakt:** co firma sprzedaje, komu, za ile, jak się zgłosić (formularz, telefon, WhatsApp).
   - **Dowody:** realizacje, opinie, portfolio.
   - **Ścieżka klienta na telefonie:** pierwsze wrażenie, gdzie się gubi, długość formularza.
   - **Analityka:** czy jest, co mierzy, czy są cele.
   - **Cookies i zgody:** baner, polityka prywatności. Tylko opis stanu, bez porad prawnych.
   - **Zrzuty** kluczowych stron (Playwright, telefon i komputer).
7. **Konkurencja** (`analiza/konkurencja.md`):
   - **Kogo badamy:** 5–10 firm z Map Google i wyników wyszukiwania w tym samym mieście i niszy.
   - **Co porównujemy:** strony, oferta, ceny, dowody, treści (blog, poradniki), widoczność SEO (Labs: domain overview), reklamy (Google Ads Transparency).
   - Tylko dane zbiorcze, bez kontaktowania się z firmami.
8. **Synteza** (`analiza/RAPORT.md`):
   - **Ocena stanu** w punktach: SEO techniczne, treści, lokalne, linki, konwersja.
   - **10 najważniejszych problemów** z priorytetem (wpływ × koszt).
   - **Szybkie poprawki** (do tygodnia).
   - **Plan na 3 miesiące:**
     - SEO techniczne;
     - strony usług i miast;
     - treści (skill `klaster-tresci`);
     - wizytówka i opinie;
     - linki;
     - narzędzie, np. kalkulator kosztu projektu;
     - reklamy (`playbook/prompty/badanie-reklam.md`).
   - **Lista pytań do właściciela.**

Każde twierdzenie z danymi ma źródło (endpoint, URL, data). Raport kończy się pytaniami o decyzje: zakres, budżet, styl, czy przenosimy stronę do repozytorium (np. Astro, jak w niechcieznajda).

Po akceptacji raportu uzupełnij sekcję „O projekcie” w CLAUDE.md (pull request).

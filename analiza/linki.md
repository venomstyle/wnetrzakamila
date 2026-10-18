# SEO zewnętrzne (linki): wnetrzakamila.pl

Stan na 18.10.2026. Wszystkie dane z DataForSEO (endpointy podane przy liczbach). Proxy blokuje bezpośredni dostęp do domeny i do archive.org, więc historii domeny w Wayback Machine nie sprawdziłem.

## W skrócie

- Strona **nie ma ani jednego wartościowego linku**. Wszystkie 14 aktywnych linków to automatyczne listy domen typu „Where to buy aged domains and backlinks”.
- Ranga domeny w DataForSEO wynosi **0**, a spam score profilu linków **59** (w skali 0–100).
- Domena została zarejestrowana 17.11.2025, a jej rejestracja **wygasa 17.11.2026**, czyli za miesiąc.
- Konkurencja w poradnikach (dobrzemieszkaj.pl, urzadzamy.pl, homebook.pl, weranda.pl) ma od 1 320 do 2 506 domen linkujących. W kalkulatorach próg jest dużo niższy: na „kalkulator farby” w top 10 są strony z 0 i 10 domenami linkującymi.
- Żadnych działań naprawczych (disavow) nie trzeba. Trzeba zacząć zdobywać pierwsze prawdziwe linki.

## 1. Profil linków dziś

Źródło: `/v3/backlinks/summary/live` (target wnetrzakamila.pl, include_subdomains true), 18.10.2026.

| Wskaźnik | Linki aktywne | Wszystkie (z utraconymi) |
|---|---|---|
| Linki (backlinks) | 14 | 20 |
| Domeny linkujące | 14 | 20 |
| Domeny główne | 11 | 16 |
| Różne adresy IP | 6 | 6 |
| Linki nofollow | 1 | 1 |
| Ranga domeny (rank) | 0 | brak |
| Spam score linków | 59 | 41 |
| Pierwszy link widziany | 08.02.2025 | 08.02.2025 |

Druga kolumna to ten sam endpoint z `backlinks_status_type: "all"`.

Rozkład domen (aktywne): .info 4, .com 3, .org 3, .net 1, .cv 1, .org.in 1, .link 1. Nie ma ani jednej domeny .pl. Każdy link prowadzi na stronę główną `https://wnetrzakamila.pl/`.

### Jakość: wszystkie linki to spam z list domen

Źródło: `/v3/backlinks/backlinks/live` (limit 100, status all), 18.10.2026. Pełna lista ma 20 pozycji:

- **Tytuły stron linkujących:** „Where to buy 🚀 aged domains and backlinks 🔥…” (14 aktywnych) albo „Best websites list in the word- we provide high quality backlinks” (1). Utracone strony pokazują dziś „One moment, please...” albo błąd 503.
- **Liczba linków wychodzących na stronie:** od 9 001 do 10 501, a na jednej 25 001. Taka strona nie przekazuje żadnej wartości.
- **Kontekst linku:** alfabetyczna lista nazw domen, np. „…wnetrzakamea.pl wnetrzakameleon.pl **wnetrzakamila.pl** wnetrzakaroliny.pl wnetrzakaszuby.pl…”. Strona jest tam tylko dlatego, że jej nazwa zaczyna się od „wnetrza”.
- **Serwery:** większość stron linkujących stoi na dwóch adresach IP (118.139.176.46 i 118.139.178.200). To jedna sieć generująca listy.
- **Spam score pojedynczych linków:** 50–80 (`/v3/backlinks/referring_domains/live`).

Spam score całej domeny: **59** (`/v3/backlinks/bulk_spam_score/live`).

### Anchory

Źródło: `/v3/backlinks/anchors/live`, 18.10.2026.

| Anchor | Linki | Domeny | Uwagi |
|---|---|---|---|
| „wnetrzakamila.pl” | 14 | 14 | aktywne, spam score 59 |
| (pusty) | 6 | 6 | wszystkie utracone, ostatni 10.08.2026 |

Nie ma anchorów tematycznych ani anchorów z innych branż.

### Utracone linki

Według `/v3/backlinks/referring_domains/live` 6 domen ma datę utraty: australianwebdirectory.shop (27.02.2026), tunca.org (02.05.2026), pagesearch.net (14.05.2026), websiterace.com (18.06.2026), way2check.cv bez www (18.06.2026), wallpapers.pro (10.08.2026). To też strony z listami domen, więc ich utrata nic nie zmienia.

### Historia (miesiąc po miesiącu)

Źródło: `/v3/backlinks/history/live` (od 01.01.2019 do 18.10.2026).

| Koniec miesiąca | Domeny linkujące | Nowe | Utracone |
|---|---|---|---|
| 01.2025 | 1 | 1 | 0 |
| 04.2025 | 10 | 4 | 0 |
| 08.2025 | 14 | 1 | 0 |
| 12.2025 | 18 | 3 | 0 |
| 03.2026 | 27 (szczyt) | 2 | 1 |
| 06.2026 | 21 | 1 | 4 |
| 09.2026 | 14 | 0 | 1 |

Ten endpoint liczy inaczej niż `summary` (np. widzi domeny .xyz, .click, .co.uk, których nie ma już w liście), dlatego liczby nie muszą się zgadzać 1:1.

## 2. Czy domena ma historię (wygasła domena)?

Fakty:

- **WHOIS:** domena utworzona 17.11.2025, rejestrator cyber_Folks S.A., wygaśnięcie 17.11.2026 (`/v3/domain_analytics/whois/overview/live`, 18.10.2026).
- **Pierwszy link:** 08.02.2025 (`summary`), a w historii już styczeń 2025 (`history`). To ponad 9 miesięcy przed obecną rejestracją.
- **Najstarsze daty wśród 10 wyników `site:` w Google:** 18.11.2025 („Ile kosztuje wizualizacja mieszkania?”), potem 23.11.2025 i 19.12.2025 (`/v3/serp/google/organic/live/advanced`, fraza `site:wnetrzakamila.pl`).
- **Anchory:** tylko nazwa domeny albo pusty anchor. Brak śladów innej tematyki (kasyna, pożyczki, obce języki).

Wniosek: linki sprzed rejestracji pochodzą z automatycznych list nazw domen, które wypisują też domeny wolne lub wygasające. Nie ma śladu po wcześniejszej stronie z prawdziwymi linkami. Możliwe, że ktoś miał tę domenę przed 2025 rokiem, ale bez Wayback Machine tego nie potwierdzę. Dla SEO to bez znaczenia: domena nie odziedziczyła żadnej siły.

Pytania do właściciela:

1. Czy domena wnetrzakamila.pl była kupiona z rynku wtórnego (giełda wygasłych domen), czy zarejestrowana jako nowa?
2. Czy jest włączone automatyczne odnowienie? **Rejestracja wygasa 17.11.2026.**
3. Strona „O mnie” mówi: „Od kilku lat dzielę się praktycznymi poradami”. Domena działa od listopada 2025. Jeśli autor pisał wcześniej gdzie indziej (Instagram, inny blog), warto to pokazać z linkiem. Jeśli nie, to zdanie trzeba poprawić (zasada z CLAUDE.md: fakty o autorze tylko potwierdzone).

### Czy trzeba coś usuwać (disavow)?

Nie. Linki z list domen są powszechne i wyszukiwarki zwykle je pomijają. Plik disavow ma sens dopiero przy ręcznym działaniu (karze) w Google Search Console. Warto podpiąć GSC i sprawdzić zakładkę „Ręczne działania”; w SERP dla `site:wnetrzakamila.pl` Google pokazuje reklamę „Sprawdź w Google Search Console”, co sugeruje, że właściciel jeszcze tego nie zrobił (to tylko poszlaka).

## 3. Porównanie z konkurencją

Konkurentów wybrałem z SERP Google (`/v3/serp/google/organic/live/advanced`, location_code 2616, language_code pl, 18.10.2026):

- **„jak urządzić mały salon”**: w top 20 są sklepy i marki (selsey.pl, komandor.pl, dulux.pl, ikea.com, westwing.pl) oraz serwisy wnętrzarskie (homebook.pl, dobrzemieszkaj.pl, urzadzamy.pl, weranda.pl, architecturaldigest.pl). Na górze są grafika, wideo z YouTube, „Podobne pytania” i AI Overview. wnetrzakamila.pl ma artykuł „Jak urządzić mały salon w bloku?”, ale nie ma go w top 20.
- **„kalkulator farby”**: leroymerlin.pl, farbud.pl, dulux.pl, buduj24.pl, flugger.pl, kalkulatorxxl.pl, ilenametr.pl, dekorlux.pl, oblicz.edu.pl. AI Overview cytuje buduj24.pl, flugger.pl, kalkulatorxxl.pl, leroymerlin.pl, dulux.pl i farbud.pl. wnetrzakamila.pl nie ma w top 20.

Pomijam w porównaniu sieci handlowe i producentów (Leroy Merlin, IKEA, Dulux), bo to inna liga i inny model.

Źródła: `/v3/backlinks/bulk_referring_domains/live`, `/v3/backlinks/bulk_ranks/live`, `/v3/backlinks/bulk_spam_score/live`, a dla wybranych `/v3/backlinks/summary/live` (include_subdomains true). Wszystko 18.10.2026.

| Serwis | Typ | Domeny linkujące | Ranga | Spam score | Pierwszy link |
|---|---|---|---|---|---|
| **wnetrzakamila.pl** | blog poradnikowy | **14** | **0** | **59** | 08.02.2025 |
| homebook.pl | serwis wnętrzarski | 2 506 | 540 | brak danych | – |
| urzadzamy.pl | media wnętrzarskie | 1 847 | 520 | 14 | – |
| weranda.pl | media wnętrzarskie | 1 460 | 512 | 6 | – |
| dobrzemieszkaj.pl | media wnętrzarskie | 1 320 | 428 | 7 | 16.01.2019 |
| e-wystroj-wnetrz.pl | blog projektanta | 235 | 219 | 27 | – |
| buduj24.pl | kalkulatory + sklep | 215 | 171 | 15 | 02.10.2021 |
| noiladnie.pl | magazyn sklepu meblowego | 60 | 191 | 14 | 13.06.2021 |
| kalkulatorremontu.pl | kalkulatory | 57 | 100 | 48 | – |
| naw.best | blog wnętrzarski | 42 | 56 | 48 | – |
| oblicz.edu.pl | kalkulatory | 33 | 112 | 5 | – |
| kalkulatorxxl.pl | kalkulatory | 10 | 71 | brak danych | 24.07.2026 |
| ilenametr.pl | kalkulatory | 0 (brak w bazie) | brak | brak | – |

Co z tego wynika:

- **Ogólne poradniki („jak urządzić…”)** wygrywają serwisy z ponad 1 000 domen linkujących i sklepy znanych marek. Mały blog nie dogoni ich linkami w rok. Szansą są frazy węższe i treści, których oni nie mają.
- **Kalkulatory** to inna sytuacja. kalkulatorxxl.pl ma 10 domen, pierwszy link z 24.07.2026, a już jest 6. wynikiem organicznym (8. element strony) na „kalkulator farby”. ilenametr.pl nie ma żadnych linków w bazie DataForSEO i jest 7. wynikiem organicznym (9. element strony). Tu wygrywa jakość narzędzia, linki są mniej ważne.
- **Skąd mają linki małe serwisy z kalkulatorami:** kalkulatorxxl.pl ma linki m.in. z kalkulatorydomogrod.pl, mate.tools (katalog narzędzi, nofollow), play.pl i kilku polskich blogów (`/v3/backlinks/referring_domains/live`). To wzór do naśladowania.
- noiladnie.pl ma 457 linków z agatameble.pl, czyli ze sklepu tej samej firmy. Tego nie da się skopiować.

## 4. Pomysły na linki (bez kupowania)

Kolejność według wpływu i kosztu. Wszystko bez płatnych artykułów sponsorowanych, bez farm linków i bez „pakietów SEO”.

### A. Kalkulatory jako magnes na linki (najwyższy priorytet)

- Dopracować kalkulatory (farba, panele, płytki, tapeta, fuga, klej, grunt) tak, żeby były lepsze od top 10: liczą opakowania, zapas, wiele pomieszczeń, mają wynik do skopiowania lub wydruku.
- Dodać **przycisk „Wstaw na swoją stronę”** (kod iframe z linkiem do źródła). Blogi remontowe i małe sklepy chętnie wstawiają gotowe narzędzia.
- Zgłosić kalkulatory do katalogów narzędzi i zestawień (jak mate.tools u kalkulatorxxl.pl). Linki nofollow też dają ruch i rozpoznawalność.
- Opisać wzór i źródła (karta techniczna farby, wydajność z etykiety). AI Overview na „kalkulator farby” cytuje strony, które wyjaśniają wzór krok po kroku (flugger.pl, kalkulatorxxl.pl).

### B. Producenci i sklepy: realizacje i materiały

- Jeśli autor w swoich realizacjach używa konkretnych farb, paneli czy mebli, część producentów prowadzi galerie realizacji klientów lub sekcje inspiracji. Zgłoszenie realizacji ze zdjęciami może dać link. Warunki trzeba sprawdzić u każdego producenta.
- Kalkulator dla konkretnych produktów (np. wydajność z kart technicznych) to powód, by producent albo sklep zalinkował narzędzie. Dane tylko z oficjalnych kart, z datą sprawdzenia.

### C. Media wnętrzarskie i lokalne

- Odpowiadać na zapytania dziennikarzy szukających ekspertów (komentarz, porada, zdjęcie realizacji). Media typu urzadzamy.pl czy dobrzemieszkaj.pl publikują porady architektów i projektantów (np. „10 pomysłów architektów” w SERP na „mały salon”).
- Przygotować materiał do cytowania: własne zdjęcia przed i po, zestawienia z danymi (np. zużycie farby według wydajności z kart producentów). Liczby tylko ze źródłem.

### D. Wymiana gościnna (z umiarem)

- Artykuły gościnne na blogach o pokrewnych tematach (ogród, DIY, rodzina, mieszkanie w bloku), pisane dla czytelników, z jednym naturalnym linkiem.
- Bez masowej wymiany „link za link”. Google uznaje nadmierną wymianę linków za naruszenie zasad.

### E. Katalogi branżowe i profile

- Profile w serwisach wnętrzarskich, gdzie autorzy i projektanci pokazują projekty (np. homebook.pl). Warunki i to, czy profil dopuszcza link do strony, trzeba sprawdzić.
- Unikać katalogów SEO i list „aged domains”. Obecne linki pokazują, jak wyglądają.

### F. Pinterest, Instagram, YouTube

- Linki z tych serwisów są nofollow, ale dają ruch i sygnały marki. Pinterest dobrze pasuje do wnętrz i ogrodu: każda grafika z artykułu jako pin z linkiem do wpisu.
- W SERP na frazę „wnetrzakamila.pl” pierwszy wynik to profil Instagram „Kamila | Wnętrza | Ogród | Inspiracje (@wnetrzebezfiltra)”, ponad 9,6 tys. obserwujących (`/v3/serp/google/organic/live/advanced`, 18.10.2026). **Do potwierdzenia przez właściciela, czy to profil autora strony.** Jeśli tak, link w bio i w opisach do strony jest pierwszym prostym krokiem.
- Na „jak urządzić mały salon” 3. element strony to blok z 3 filmami z YouTube. Krótkie wideo do artykułów może dać i ruch, i linki.

### Czego nie robić

- Nie kupować linków, artykułów sponsorowanych bez oznaczenia ani pakietów z katalogów.
- Nie zgłaszać strony do serwisów typu „aged domains / backlinks list”.
- Nie wysyłać zimnych maili do firm (zasada z CLAUDE.md). Kontakt z producentami i mediami tylko przez ich formularze zgłoszeń, platformy dla ekspertów albo gdy właściciel sam zdecyduje.

## 5. Cele na 3 miesiące (propozycja)

- Odnowić domenę przed 17.11.2026 i podpiąć Google Search Console.
- 10–20 nowych domen linkujących z Polski, z tematyką dom, remont, ogród, rodzina.
- Co najmniej 3 linki do kalkulatorów z innych stron (wstawki iframe, zestawienia narzędzi).
- Pinterest i Instagram z linkami do każdego nowego wpisu.

Mierzyć co miesiąc tym samym endpointem `/v3/backlinks/summary/live` i `history/live`.

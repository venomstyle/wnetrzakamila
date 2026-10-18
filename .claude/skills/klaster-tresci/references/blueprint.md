# Blueprint serwisu treści z intencją zakupową

Ten plik opisuje **mechanizmy**, nie wygląd. Wyprowadzone z analizy paliwownia.pl (i kontrastu z promptowy.com), ale stosuj je do projektu użytkownika jego językiem, marką i formą. "U nich" to tylko ilustracja, jak dany mechanizm może wyglądać - nie wzór do odtworzenia.

Test, czy stosujesz blueprint, a nie kopiujesz: czy każdą decyzję umiesz uzasadnić potrzebą odbiorcy tego projektu? Jeśli jedynym powodem jest "tak mają w Paliwowni" - zrób to inaczej albo wcale.

## Warstwy

### 1. Dane jako fundament (fosa)
**Mechanizm:** lista realnych encji niszy (programy, produkty, urzędy, usługi, narzędzia, miasta) z polami, źródłem i datą sprawdzenia. Strony powstają z danych, nie są pisane od zera.
**Dlaczego:** dane trudno skopiować, łatwo aktualizować, każda encja to fraza z nazwą. Tekst bez danych konkurencja przepisze w godzinę.
**Kiedy:** gdy nisza ma naturalną listę ≥ 20 rzeczy, o które ludzie pytają po nazwie. Dla LP z jedną usługą często wystarczą dane wewnątrz artykułów (tabele cen, terminów, warunków).
*U nich:* 130 programów z polami: kwota, warunki tak/nie, czas decyzji, status, data sprawdzenia.

### 2. Typy stron odpowiadające typom pytań
**Mechanizm:** każda intencja ma swój typ strony z przewidywalnym układem: hub ("wszystko o X"), poradnik (jedna intencja), porównanie, strona encji, narzędzie, zestawienie/kalendarz.
**Dlaczego:** przewidywalny układ = szybsze pisanie, spójna jakość, czytelnik wie, gdzie szukać, a Google dostaje jednoznaczne sygnały.
Bloki każdego typu: `szablon-artykulu.md`.

### 3. Odpowiedź od pierwszego zdania
**Mechanizm:** H1 obiecuje konkret (liczba, wynik), lead go dostarcza, blok "w skrócie" streszcza 3-5 faktów, reszta to dowody i szczegóły.
**Dlaczego:** czytelnik z wyszukiwarki chce odpowiedzi, a AI Overview cytuje strony, które ją podają wprost.

### 4. Warstwa zaufania
**Mechanizm:** prawdziwy autor, strona "jak sprawdzamy", data sprawdzenia przy treści, źródła pierwotne, zastrzeżenie przy tematach YMYL, łatwe zgłoszenie błędu, datowane notki o zmianach.
**Dlaczego:** w tematach o pieniądzach i przepisach zaufanie decyduje o kliknięciu w CTA i o ocenie jakości.

### 5. Narzędzie jako środek ciężkości
**Mechanizm:** jedno proste narzędzie (kalkulator, sprawdzarka "czy się łapiesz", generator, checklista) jest głównym CTA całego serwisu; artykuły do niego prowadzą, a ono do oferty.
**Dlaczego:** narzędzie daje powód do linkowania i powrotów, a wynik narzędzia to naturalny moment na ofertę.

### 6. Drabina monetyzacji
**Mechanizm:** darmowe (treść, narzędzie) → mała płatna próba → pełny dostęp → usługa "zrobimy za ciebie" → oferta dla firm/partnerów. Dla LP z jedną usługą drabina może mieć 2 szczeble: darmowa wartość (narzędzie/raport) → usługa.
**Dlaczego:** zarabia intencja ("chcę to załatwić"), nie odsłony; ruch z Google bez produktu jest kruchy (Promptowy: 3,6 tys. wpisów, ~3 tys. wizyt organicznych/mies.).

### 7. Pętla świeżości
**Mechanizm:** daty sprawdzenia, "ostatnio dodane", reakcja na zmiany w niszy w ciągu godzin (kilka tekstów pod różne intencje naraz), regularny newsletter z tym, co się zmieniło.
**Dlaczego:** świeżość jest przewagą tam, gdzie fakty się zmieniają; pierwszy kompletny wynik na nową frazę wygrywa, zanim przyjdą duzi.

### 8. Tożsamość marki jako system
**Mechanizm:** jedna metafora lub idea wynikająca z obietnicy marki, konsekwentnie użyta w nazwach sekcji, narzędzi, planów, newslettera i w motywie okładek.
**Dlaczego:** w niszy, w której wszyscy piszą to samo, rozpoznawalność robi różnicę w kliknięciach (Discover, social, SERP) i zapamiętaniu.
**Jak:** wyprowadź ją z oferty i odbiorcy tego projektu. Wypisz 3 kandydatki, sprawdź, czy dadzą się naturalnie rozpisać na: hasło, nazwę narzędzia, nazwę newslettera, motyw okładki. Wybierz z użytkownikiem. Nie zapożyczaj metafory ani motywów z analizowanych serwisów.
*U nich:* "stacja paliw dla firm" - to ich idea, nie część blueprintu.

### 9. Lekka technika
**Mechanizm:** treści i dane w plikach → build do statycznych stron; minimum JS; wyszukiwarka z indeksu JSON; własna lekka analityka zdarzeń; poprawne dane strukturalne (Article, BreadcrumbList, FAQPage); sitemap z prawdziwym `lastmod`; okładka per strona.
**Dlaczego:** szybkość, tani hosting, pełna kontrola nad szablonami, łatwa masowa aktualizacja.
**Test popytu (fake door):** przycisk funkcji, której jeszcze nie ma, mierzy kliknięcia i uczciwie mówi "wkrótce" - buduj to, w co ludzie klikają.

## Kolejność wdrożenia (dowolny projekt)

1. Obietnica, odbiorca, oferta → idea marki (warstwa 8) - jeśli budujesz nowy serwis.
2. Model danych i pierwsze rekordy ze źródłami (warstwa 1) - jeśli nisza ma listę encji.
3. Szablony typów stron i szablon okładki - zaprojektowane od zera z tokenów marki projektu.
4. Narzędzie (warstwa 5), choćby proste.
5. Plan i treści (ten skill).
6. Warstwa zaufania: autor, "jak sprawdzamy", zastrzeżenia.
7. Start z kompletem najważniejszych stron zamiast pojedynczych wpisów; potem pętla świeżości.

W projektach użytkownika obowiązują ich reguły (np. tylko lokalnie, bez deployu).

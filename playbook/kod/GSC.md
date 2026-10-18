# Search Console: automatyczne zgłaszanie

Po każdej publikacji (push do `main`, codziennie o 6:00, ręcznie) GitHub Actions uruchamia `scripts/gsc.mjs`:

1. Zgłasza mapę strony `https://niechcieznajda.pl/sitemap-index.xml` do Search Console. W mapie każdy poradnik ma datę ostatniej zmiany (`updatedAt`, a bez niej `publishedAt`).
2. Sprawdza przez API, czy poradniki z ostatnich 14 dni są w indeksie Google. Wynik jest w podsumowaniu przebiegu: GitHub, zakładka Actions, ostatni przebieg „Publikacja”.

Przycisku „Poproś o zindeksowanie” nie da się nacisnąć przez API. Indexing API Google służy tylko do ofert pracy i transmisji na żywo, więc go nie używamy. Ręcznie klikasz tylko adresy, które w raporcie wiszą poza indeksem dłużej niż tydzień.

## Jednorazowa konfiguracja (ok. 10 minut, najwygodniej na komputerze)

1. Wejdź na console.cloud.google.com i utwórz projekt, np. „niechcieznajda”.
2. W wyszukiwarce na górze wpisz „Google Search Console API” i kliknij „Włącz”.
3. Menu: „Administracja” → „Konta usługi” → „Utwórz konto usługi”. Nazwa np. „publikacja”. Role pomiń, kliknij „Gotowe”.
4. Kliknij utworzone konto → zakładka „Klucze” → „Dodaj klucz” → „Utwórz nowy klucz” → JSON. Pobierze się plik.
5. Skopiuj adres konta usługi (kończy się na `iam.gserviceaccount.com`).
6. W Search Console: „Ustawienia” → „Użytkownicy i uprawnienia” → „Dodaj użytkownika”. Wklej adres, uprawnienia „Pełne”.
7. Na GitHubie: repozytorium → Settings → Secrets and variables → Actions → New repository secret:
   - `GSC_KLUCZ`: cała zawartość pobranego pliku JSON.
   - `GSC_WLASCIWOSC`: tylko jeśli właściwość w Search Console to „Prefiks URL”; wtedy wpisz `https://niechcieznajda.pl/`. Dla właściwości „Domena” sekretu nie dodawaj.
8. Usuń pobrany plik JSON z komputera. Klucz jest już tylko w Secrets.

Bez sekretu `GSC_KLUCZ` krok jest pomijany, a publikacja działa jak wcześniej. Błąd w tym kroku nie zatrzymuje publikacji.

# Zaplanowane zadanie: kwartalny przegląd cen

Utwórz jako zaplanowane zadanie w claude.ai, uruchamiane co kwartał w nowej sesji. Dodaj konektory **DataForSEO i GitHub**, bo bez nich zadanie nie zadziała.

Treść zadania (podmień nazwę serwisu i repozytorium):

> Kwartalny przegląd cen w treściach serwisu [domena] (repozytorium [owner/repo]). Odpowiadaj po polsku.
> 1. Przeczytaj CLAUDE.md i .claude/skills/klaster-tresci/references/przeglad-niezalezny.md.
> 2. Znajdź opublikowane teksty z cenami, prowizjami, limitami planów albo wolumenami ze źródeł zewnętrznych.
> 3. Podziel je na grupy po 4–6 plików. Dla każdej grupy uruchom agenta bez kontekstu: niech dziś otworzy każde źródło z `sources` (DataForSEO content_parsing), porówna liczby, poprawi zmienione ceny, a niepotwierdzalne zamieni na „sprawdź w cenniku” z linkiem. `updatedAt` zmienia tylko przy realnej zmianie treści, `verifiedAt` i `checkedAt` zawsze. Okładkę wygeneruje od nowa, jeśli zmieni się liczba na okładce.
> 4. Uruchom QA (sprawdz.py) i build. Jeśli strona ma tabelę cen w danych (np. cennik.json), popraw ją razem z tekstami.
> 5. Utwórz gałąź `przeglad-cen-RRRR-MM` i pull request z listą zmian w formacie: tekst, stara wartość → nowa wartość, źródło.
> 6. Podsumuj właścicielowi, co się zmieniło.

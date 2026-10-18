# Tryb wydarzeń: seria tekstów wokół zmiany w niszy

Mechanizm z analizy promptowy.com: przy premierze modelu AI w 27 minut wyszło 6 tekstów pod różne intencje, a pierwszy był w top 1 na świeżą frazę po ~30 minutach, bo nie miał konkurencji. Bierzemy mechanizm (szybkość + kilka intencji naraz + powiązanie z evergreenami), nie skalę ani wygląd.

## Kiedy uruchamiać

Tylko przy wydarzeniu, które zmienia coś dla odbiorcy projektu i jest potwierdzone w źródle pierwotnym:
- zmiana zasad lub funkcji produktu, którego dotyczy nisza (np. zasady opinii Google, nowa funkcja Profilu Firmy),
- nowy przepis, wejście w życie ustawy, decyzja urzędu (Dziennik Ustaw, UOKiK, KAS),
- zmiana cen/limitów/programu, ogłoszony nabór, zamknięcie programu,
- potwierdzona aktualizacja algorytmu (Google Search Status Dashboard).

Nie uruchamiaj przy plotkach, przeciekach i artykułach innych serwisów bez potwierdzenia u źródła.

## Monitoring

Każdy projekt ma plik `monitoring.md` z listą źródeł (URL, co obserwujemy, jak często). Agent monitorujący (zaplanowane zadanie, np. codziennie rano):
1. pobiera źródła z `monitoring.md` i porównuje z zapisanym stanem (`monitoring-stan.json`: ostatnio widziane tytuły/daty),
2. ocenia, czy nowość spełnia kryteria z sekcji „Kiedy uruchamiać”,
3. jeśli tak, uruchamia serię; jeśli nie, tylko aktualizuje stan i kończy bez zmian w treściach.

## Seria: 4-6 tekstów pod różne intencje

Dobierz z tej listy to, co ma sens dla wydarzenia:
1. **Wiadomość** (`type: news`): co się zmieniło, od kiedy, kogo dotyczy, źródło. Sekcje „Co wiemy” i „Czego jeszcze nie wiemy”.
2. **Co to zmienia dla [odbiorcy]**: konsekwencje w praktyce, tabela przed/po.
3. **Co zrobić teraz**: kroki lub checklista.
4. **Pytania i odpowiedzi / mity** wokół zmiany.
5. **Aktualizacja istniejących evergreenów**: datowana notka na górze („Aktualizacja [data]: …”), poprawka treści, nowe `updatedAt`, link do wiadomości. To często daje więcej ruchu niż nowe teksty.
6. Jeśli temat jest duży: **przewodnik** lub **porównanie** (np. stare vs nowe zasady).

Wszystkie teksty serii linkują się nawzajem i do huba klastra. Okładki z szablonu projektu, QA skryptem `sprawdz.py`.

## Zasady

- Tylko fakty ze źródeł pierwotnych, z datą. Bez spekulacji; czego nie wiadomo, nazwij wprost.
- Tryb automatyczny (bez znaczników do uzupełnienia), chyba że użytkownik zdecydował inaczej.
- Publikacja natychmiast (`publishedAt` = dziś, `draft: false`) tylko jeśli użytkownik zgodził się na automatyczną publikację serii; inaczej szkice + powiadomienie.
- Szybkość wymaga szybkiego wdrożenia: build/deploy po zapisaniu plików (hook hostingu). W projektach z regułą „tylko lokalnie” kończ na plikach i powiadomieniu.
- News sitemap (Google News) ma sens tylko, gdy serwis regularnie publikuje prawdziwe wiadomości.

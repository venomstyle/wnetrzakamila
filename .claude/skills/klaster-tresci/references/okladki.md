# Okładki - co ma na nich być i jak zaprojektować własny szablon

Z blueprintu bierzemy **jakie informacje** niesie okładka i w jakiej hierarchii. Wygląd projektujesz od zera dla projektu - z jego kolorów, fontów, logo i idei marki. Nie odtwarzaj okładek analizowanych serwisów (ich układu, motywu ani palety).

## Hierarchia informacji

1. **Kluczowa liczba lub fakt** (`cover.big`) - najważniejszy, największy element. Powód do kliknięcia w Discover, social i na karcie huba ("14 dni", "do 55 tys. zł", "3 błędy").
2. **Kontekst liczby** (`cover.sub`) - kilka słów, bez których liczba nic nie znaczy ("od zgłoszenia do raportu").
3. **Hasło tematu** (`cover.label`) - 2-5 słów, czytelne w miniaturze ~300 px.
4. **Etykieta kategorii** (`kicker`) - nawigacja wizualna między klastrami.
5. **Znak marki** - mały, stały, w tym samym miejscu na każdej okładce.
6. **Motyw marki** - jeden element graficzny wynikający z idei marki projektu (opcjonalny), wspólny dla wszystkich okładek, zmieniający się najwyżej kolorem kategorii.

Gdy temat nie ma uczciwej liczby - nie wymyślaj jej. Wtedy największym elementem jest hasło, a liczba znika.

## Wymagania

- Czytelność w miniaturze ~300×170 px: maks. ~6 słów dużym tekstem, kontrast co najmniej 4.5:1.
- Bezpieczne marginesy ~5% (social przycina krawędzie).
- Dwa formaty z jednego szablonu: `og` 1200×630 i `hero` 1600×900 (inne proporcje - inny układ, nie rozciąganie).
- Jedna konwencja dla całego serwisu: zmieniają się dane i kolor kategorii, nie układ.
- Kształt na liczbę musi mieścić zmienną długość („7”, „278”, „do 10% obrotu”, „3 kliknięcia”). Koło i inne stałe kształty się nie sprawdzają; lepszy jest kontener rosnący w pionie. Dodaj w szablonie skrypt, który po `document.fonts.ready` zmniejsza liczbę do szerokości kontenera i tytuł do 3 linii (licz linie, nie porównuj scrollHeight, bo polskie znaki wystają poza wysokość linii).
- Podpis liczby (`sub`) stoi zawsze tuż przy liczbie, nigdy osobno przy tytule.
- **Motyw według klastra (seria):** każdy hub/klaster ma swój kolor tła i akcentu oraz ikonę tematu, układ zostaje ten sam. Dzięki temu na liście kart i w social widać, z jakiej serii jest tekst, a całość nie jest monotonna. Kolory bierz z palety marki (tło jasne/ciemne, akcent, drugi akcent); szablon wybiera motyw z `{{meta.hub}}` / `{{meta.cluster}}` / `{{meta.type}}` (np. `zestawienie` = motyw danych). Unikaj logo marek, o których piszesz (prawa do znaków); używaj własnych ikon. **Każda kategoria ma inny kolor tła**, nie tylko inny akcent: jeśli część kategorii dzieli to samo jasne tło, lista kart wygląda jak "kilka kolorowych i kilka białych", a nie jak seria. Ilustracja kategorii (np. rysunek w konwencji motywu marki: telefon, pinezka, wykres) mocniej odróżnia serie niż sama ikona.
- Bez zdjęć stockowych i generycznych ikon "żarówka/rakieta/wykres".

## Proces (raz na projekt): wybór z arkusza

Szablon okładki wybiera użytkownik z arkusza opcji (`wybory.md`, punkt 3). W skrócie:

1. Przeczytaj tokeny wybranego stylu, logo i ideę marki.
2. Zrób około 5 szablonów HTML (`{{big}} {{sub}} {{title}} {{kicker}} {{brand}}`, `{{meta.cluster}}`/`{{meta.hub}}` do motywu kategorii, `<body data-format="{{format}}">`), każdy z innym pomysłem i jednym zdaniem uzasadnienia z marki.
3. Wyrenderuj każdy na tych samych 5–6 prawdziwych tekstach (po jednym z kategorii + hub bez liczby + długi tytuł), złóż arkusz `scripts/arkusz.py --grupuj 6`, pokaż i **czekaj na wybór**.
4. Iteruj („kolejny zestaw”, „połącz 2 z 5”, „popraw X”), aż użytkownik zaakceptuje.
5. Wybrany szablon do `src/okladki/szablon.html`, kolory kategorii do tokenów, decyzja do DECYZJE.md. Dopiero potem okładki dla wszystkich tekstów.

## Renderowanie

```bash
python3 ~/.claude/skills/klaster-tresci/scripts/okladka.py --template src/okladki/szablon.html --from-dir src/content/poradniki --out public/okladki
```

Skrypt nie ma własnego wyglądu - podstawia dane z frontmattera do szablonu projektu i robi PNG przez headless Chrome/Edge/Brave (`--formats og,hero` lub własne, np. `kwadrat=1080x1080`). Względne ścieżki do fontów/logo w szablonie działają, bo plik tymczasowy powstaje obok szablonu. Alternatywa przy buildzie: satori + `@resvg/resvg-js` z tych samych pól `cover.*`.

Opcja: ilustracja zamiast typografii (narzędzie do generowania obrazów) - tylko jeśli pasuje do marki; jeden stały opis stylu dla wszystkich okładek, bez tekstu w obrazie, a liczbę i hasło nakłada szablon.

# Punkty decyzji: arkusze opcji do wyboru

Struktura bloga jest stała (szkielet), a wygląd powstaje od zera dla marki. Kluczowe elementy wyglądu wybiera **użytkownik**, nie Claude. W każdym punkcie decyzji Claude przygotowuje arkusz opcji, pokazuje go i **zatrzymuje się, aż użytkownik odpowie**. Nie wybiera „najlepszej” opcji sam i nie idzie dalej „na razie z jedną z nich”.

## Zasady wspólne dla wszystkich punktów

1. **Opcje są prawdziwe.** Pokazujesz je na prawdziwych treściach projektu (tytuły z planu, prawdziwe liczby, długi i krótki tytuł) i w prawdziwym kontekście (nagłówek, karta przeglądarki, lista kart). Lorem ipsum i „Tytuł artykułu” ukrywają problemy, które użytkownik zobaczy dopiero po wdrożeniu.
2. **Opcje są różne.** Każda opcja to inny pomysł: inny motyw, kompozycja, krój albo relacja kolorów. Pięć wariantów tej samej kompozycji w innych kolorach to jedna opcja.
3. **Każda opcja ma uzasadnienie z marki** w jednym zdaniu (np. „pryzmaty szkliwa są heksagonalne, więc znak to kryształ”). Bez cech analizowanych serwisów i bez cudzych znaków.
4. **Arkusz ma numery i nazwy.** `scripts/arkusz.py` (siatka) albo `scripts/logo.py` (logo w kontekście). Pod arkuszem: „Odpowiedz numerem albo: kolejny zestaw, połącz 2 z 5, popraw 3: …”.
5. **Pokaż arkusz** (SendUserFile z `display: render`, a w terminalu ścieżka PNG) i krótko opisz każdą opcję: numer, nazwa, pomysł, na co uważać (np. „6 rozpada się w 18 px”).
6. **Czekaj na odpowiedź.** W tym czasie możesz robić tylko pracę, która od wyboru nie zależy (np. pisanie tekstów po wyborze stylu i logo).
7. **Iteruj:**
   - „kolejny zestaw” → nowe opcje, numeracja dalej (`--start 11`), poprzednie numery zostają ważne;
   - „połącz 2 z 5” → nazwij, co bierzesz z każdej („kompozycja z 2, ilustracja z 5”), pokaż 2–3 wersje połączenia;
   - „popraw X: …” → tylko ta opcja, w 2–3 wariantach poprawki, obok wersji przed poprawką;
   - „żadna” → zapytaj jednym pytaniem, co nie pasuje (kolor, nastrój, krój, motyw), i zrób nowy zestaw.
8. **Wdrożenie wyboru:** wybrana opcja trafia do tokenów (`src/styles/tokeny.css`), komponentów (Logo, karty, ramki) i szablonów (okładka). Nie zostaje jako osobny plik „na boku”.
9. **Zapis decyzji** w dokumentacji projektu (np. `DECYZJE.md` w katalogu głównym albo istniejący README/plan): data, punkt decyzji, ścieżka arkusza, wybrany numer i nazwa, poprawki użytkownika dosłownie, pliki, w których decyzję wdrożono. Arkusze trzymaj w projekcie (np. `arkusze/`, poza `public/`), bo scratchpad jest tymczasowy.

```markdown
## 2026-10-13 · Okładki (runda 2)
- Arkusz: arkusze/okladki-runda2.png
- Wybór: 7 „Taśma” + z 4: ilustracje kategorii
- Poprawki użytkownika: „mniej pustego miejsca pod tytułem”
- Wdrożone w: src/okladki/szablon.html, tokeny --kat-* w src/styles/tokeny.css
```

## Punkt 1: styl bloga (po szkielecie, przed pisaniem)

**Kiedy:** szkielet działa z neutralnymi tokenami i 2–3 prawdziwymi tekstami (choćby szkicami) i jednym hubem.

**Co przygotowujesz:** 2–3 kierunki. Każdy to:
- nazwa i 2–3 zdania: nastrój, dla kogo, z czego w marce wynika (oferta, odbiorca, obawy odbiorcy, istniejące materiały),
- **tokeny**: tło, papier, tekst, akcent i kolor na akcencie (z kontrastem ≥ 4,5:1), linia, kroje (nagłówki, tekst ciągły, OFL hostowane lokalnie), skala, promienie, cienie, para kolorów na każdą kategorię (`--kat-bg`, `--kat-ink`),
- **forma bloków** w osobnym `marka.css`: nagłówek, karta, ramki, „W skrócie”, CTA, FAQ, źródła, spis, stopka, motyw marki.

Gdy projekt ma już wygląd (LP), kierunki to różne sposoby przedłużenia tej marki na blog, a nie nowe marki.

**Jak pokazać:** każdy kierunek nałożony na **ten sam szkielet i te same teksty**. Build, `scripts/zrzuty.mjs --wys 1700` dla artykułu, huba i listy w 1280 px i artykułu w 375 px, potem arkusz: jeden wiersz = jeden kierunek.

```bash
node ~/.claude/skills/klaster-tresci/scripts/zrzuty.mjs --base http://127.0.0.1:4321 --out arkusze/styl-a --szer 1280 --wys 1700 /poradniki/<tekst>/ /poradniki/<hub>/ /poradniki/
node ~/.claude/skills/klaster-tresci/scripts/zrzuty.mjs --base http://127.0.0.1:4321 --out arkusze/styl-a --szer 375 --wys 1700 --kontrast /poradniki/<tekst>/
python3 ~/.claude/skills/klaster-tresci/scripts/arkusz.py arkusze/styl-a/*.png arkusze/styl-b/*.png --grupuj 4 --size 1280x1700 --cell 330 \
  --nazwy "Kierunek A: …|Kierunek B: …" --title "Styl bloga: <marka>" --out arkusze/styl-runda1.png
```

Kierunki trzymaj w osobnych kopiach projektu w scratchpadzie (np. `test-a/`, `test-b/`) albo przełączaj pliki tokenów między buildami. Raport kontrastu (`--kontrast`) dołącz do opisu: „A: 0 problemów, B: 2 (stopka)”.

**Po wyborze:** tokeny do `src/styles/tokeny.css`, forma do `src/styles/marka.css` (import w Base), zapis w DECYZJE.md.

## Punkt 2: logo (po stylu)

**Kiedy:** po wyborze stylu, bo logo korzysta z jego krojów i kolorów. Gdy marka ma już logo, pomiń wybór i zrób tylko kontrolę kontekstu (`logo.py` z jedną opcją): favikona 18 px, ciemne tło.

**Co przygotowujesz:** około 10 opcji, każda jako dwa SVG: pełne logo (znak + nazwa) i sam znak (favikona, awatar). Różne pomysły: znak z idei marki, monogram, sam napis z detalem, emblemat, znak abstrakcyjny. Części, które mają zmieniać kolor z tłem, mają `fill="currentColor"`. Tekst zamień na krzywe albo dołącz kroje przez `--css` (inaczej podgląd użyje kroju zastępczego).

**Jak pokazać:** `scripts/logo.py` robi kartę każdej opcji: nagłówek strony w kolorach wybranego stylu, karta przeglądarki z favikoną 18 px, znak 40/34/24 px na tle i na kaflu akcentu, logo na jasnym i ciemnym tle.

```bash
python3 ~/.claude/skills/klaster-tresci/scripts/logo.py logo/01.svg,logo/01-znak.svg=Kryształ logo/02.svg,logo/02-znak.svg=Połysk … \
  --nazwa "<marka>" --domena <domena> --naglowek "<tło nagłówka>" --naglowek-tekst "<tekst>" --akcent "<akcent>" --ciemne "<ciemne tło>" \
  --cols 2 --cell 640 --title "Logo: <marka>, runda 1" --out arkusze/logo-runda1.png
```

W opisie zaznacz, które opcje mają problem w małym rozmiarze albo na ciemnym tle: to informacja dla użytkownika, nie powód do ukrycia opcji.

**Po wyborze:** SVG do `src/components/Logo.astro`, `public/favicon.svg` (sam znak), znak do szablonu okładki; zapis w DECYZJE.md.

## Punkt 3: okładki i miniatury (po pierwszych tekstach)

**Kiedy:** gdy są gotowe co najmniej teksty po jednym z każdej kategorii i hub, bo okładka pokazuje ich dane (`cover.big`, `cover.sub`, `cover.label`).

**Co przygotowujesz:** około 5 szablonów HTML (hierarchia informacji i wymagania z `okladki.md`), każdy:
- na tych samych **5–6 prawdziwych tekstach**: po jednym z każdej kategorii + **hub bez liczby** + przynajmniej jeden **długi tytuł**,
- z **innym kolorem tła albo ilustracją dla każdej kategorii** (seria), sterowanym przez `data-kat="{{meta.cluster}}"` albo `{{meta.hub}}` w `<body>`,
- ze skryptem dopasowania liczby i tytułu (po `document.fonts.ready` zmniejsza liczbę do szerokości kontenera, tytuł do N linii; licz linie, nie scrollHeight).

**Jak pokazać:** render wszystkich szablonów równolegle (każdy szablon do swojego katalogu), potem arkusz: wiersz = opcja, kolumny = te same teksty.

```bash
for t in szablony/*.html; do python3 ~/.claude/skills/klaster-tresci/scripts/okladka.py --template "$t" --from-dir probki/ --formats og --out "render/$(basename "$t" .html)" & done; wait
python3 ~/.claude/skills/klaster-tresci/scripts/arkusz.py render/1-*/*.png render/2-*/*.png … --grupuj 6 --cell 300 \
  --nazwy "Karta|Kryształ|…" --title "Okładki: <marka>, runda 1" --out arkusze/okladki-runda1.png
```

`probki/` to kopie frontmattera wybranych tekstów (albo ich ścieżki przez `--from`). Sprawdź na arkuszu: długi tytuł nie wchodzi na liczbę, hub bez liczby nie ma pustej dziury, kategorie są rozróżnialne w miniaturze ~300 px, każda kategoria ma inne tło.

**Po wyborze:** szablon do `src/okladki/szablon.html` (fonty i logo projektu przez ścieżki względne), kolory kategorii także do `tokeny.css` (karty na liście używają tych samych `--kat-*`), render wszystkich okładek (krok „Okładki” w SKILL.md), zapis w DECYZJE.md.

## Punkt 4 (opcjonalny): warianty sekcji

Tylko gdy użytkownik o to prosi albo gdy jedna sekcja budzi wątpliwości (np. CTA, spis treści, stopka, karta huba). 2–4 warianty tej jednej sekcji na prawdziwej treści, zrzut samej sekcji (np. strona testowa z wariantami jeden pod drugim albo osobne buildy), arkusz z numerami. Wybór wdrażasz w komponencie i zapisujesz w DECYZJE.md.

## Czego nie robić

- Nie pokazuj opcji jako listy opisów bez obrazu: użytkownik wybiera wzrokiem.
- Nie wybieraj za użytkownika i nie wdrażaj „tymczasowo” jednej opcji przed odpowiedzią.
- Nie kopiuj wyglądu analizowanych serwisów ani poprzednich projektów (np. taśmy mierniczej z innej marki). Proces jest ten sam, wygląd nie.
- Nie mieszaj rund: nowy zestaw ma nowe numery, a arkusze poprzednich rund zostają w `arkusze/`.

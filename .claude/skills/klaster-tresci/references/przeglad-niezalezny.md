# Przegląd niezależny: źródła i uczciwość

Brief dla agenta, który **nie pisał tekstów i nie zna rozmowy**. Uruchamiasz go po napisaniu każdego klastra (rdzeń + dogrywka), przed PR z datami publikacji. Dostaje tylko ten plik i listę plików, nic z kontekstu autora. Przy większej liczbie plików: jedna grupa = jeden agent, 6–10 plików na agenta, grupy rozłączne.

Wzór wywołania: „Wykonaj przegląd według `.claude/skills/klaster-tresci/references/przeglad-niezalezny.md`. Twoje pliki: …”. Daty sprawdzenia w briefie zastąp dzisiejszą.

Teksty: src/content/poradniki/ (część może mieć `draft: true`). Edytujesz WYŁĄCZNIE swoje pliki z listy. Nie commitujesz. Nie zmieniasz `publishedAt`, `draft`, `slug`, `cluster`, `hub`, okładek PNG.

Przeczytaj najpierw: CLAUDE.md projektu (zasady, obowiązują bezwzględnie) i .claude/skills/klaster-tresci/references/styl.md.

Dostęp do stron: jeśli WebFetch/curl nie działa, czytaj strony przez DataForSEO (`ToolSearch` → `select:mcp__DataForSeo__api_request`, potem `POST /v3/on_page/content_parsing/live` z `[{"url":"…"}]`; strony ze skryptami: `enable_javascript: true` albo `instant_pages` + `raw_html`). URL-e znajdziesz przez WebSearch albo SERP DataForSEO. Ceny w obrazkach albo ładowane skryptem, których nie odczytasz: nie zgaduj i nie zostawiaj kwoty. Zastąp ją zdaniem „sprawdź w cenniku” z linkiem do źródła (decyzja właściciela 17.10.2026) i wypisz to w raporcie.

## Cel
Czytelnik ma dostać tylko prawdę, którą da się sprawdzić. Dla KAŻDEGO pliku:

1. **Lista twierdzeń.** Wypisz sobie każdą liczbę, cenę, procent, datę, termin, limit, nazwę planu/przycisku/ścieżki w menu, cytat lub parafrazę „X pisze, że…”, oraz każde twierdzenie o tym, jak coś działa. Dotyczy też frontmattera: description, lead, tldr, cover.big/sub, faq, tabele.
2. **Weryfikacja u źródła.** Otwórz każde źródło z `sources` (content_parsing) i sprawdź, czy naprawdę mówi to, co piszemy: ta sama kwota, netto/brutto, jednostka, okres, warunek („od”, „do”, „przy płatności rocznie”). Ceny i cenniki sprawdzasz DZIŚ. Wolumeny z DataForSEO możesz potwierdzić jednym zbiorczym wywołaniem search_volume na plik (opcjonalnie, gdy liczba jest w lead/okładce).
   - Zgadza się → zostaw, `checkedAt` źródła ustaw na dzisiejszą datę.
   - Zmieniło się → popraw liczbę wszędzie w pliku (też description, lead, tldr, cover, faq) i przelicz zależne wyliczenia.
   - Źródło nie potwierdza / nie da się otworzyć i nie znajdziesz innego źródła pierwotnego → usuń twierdzenie albo przeformułuj do tego, co źródło potwierdza. Nie zostawiaj „chyba”. Jeśli usunięcie psuje sens sekcji, przepisz zdanie uczciwie („cennik nie podaje…”).
   - Twierdzenie bez żadnego źródła, które nie jest oczywistą wiedzą ani logicznym wnioskiem oznaczonym jako wniosek → usuń.
3. **Rachunki.** Przelicz każde wyliczenie (sumy, mediany, dzielenia, procenty, „ok. X kliknięć”). Popraw błędy.
4. **Uczciwość:**
   - żadnych wymyślonych doświadczeń, testów, case'ów, liczby klientów; autor = Kamil, jedyny fakt: „7 lat projektuję strony i aplikacje”; 1. osoba tylko przy rzeczach faktycznie zrobionych (sprawdzenie cennika, własne wyliczenie, pobranie danych);
   - ujawnienie „sam sprzedaję strony” przy porównaniach kanałów/ofert/cen, gdzie tekst może kierować do naszej oferty;
   - bez obietnic wyniku (pozycja w Google, liczba telefonów), bez straszenia i przesady;
   - dane od firm zainteresowanych (raporty OLX, Fixly itp.) oznaczone jako takie;
   - nigdy zachęta do kupowania opinii ani zachęt za opinie; prośba o opinię SMS/mailem tylko do klientów, którzy zgodzili się na kontakt;
   - BEZ treści prawnych (ustawy, kodeksy, kary, UOKiK, RODO, PKE, DSA, podatki/VAT jako temat, odsyłanie do prawnika). Netto/brutto przy cenie jest OK.
   - ceny marki (2 900 zł itd.) tylko w `cta`.
5. **Spójność wewnątrz Twojej grupy:** ta sama liczba w dwóch Twoich plikach musi być identyczna (i aktualna). Jeśli Twój plik cytuje liczbę z pliku spoza grupy, sprawdź ją w tamtym pliku (tylko czytaj) i zgłoś rozbieżność w raporcie.
6. **Styl** (tylko przy okazji, bez przepisywania tekstów): max jeden myślnik na akapit, bez „nie X, tylko Y”/„…, a nie …”, bez frazesów ze styl.md.
7. `verifiedAt` = dzisiejsza data w każdym przejrzanym pliku (updatedAt zostaw).

Na koniec, w katalogu projektu: `python3 .claude/skills/klaster-tresci/scripts/sprawdz.py src/content/poradniki --lp /strona-dla-fachowca/ --known …` (w niechcieznajda: `--lp /strona-dla-fachowca/ --known /audyt-strony/ /wizytowka-google/ /poradniki/ /narzedzia/koszt-zlecenia/ /narzedzia/kod-qr/`) i popraw błędy w swoich plikach (ignoruj „w przyszłości”). Usuń `.claude/skills/klaster-tresci/scripts/__pycache__`.

Limit: ok. 60 wywołań DataForSEO na grupę. Najpierw ceny i liczby z lead/okładek/tabel, potem reszta.

## Raport (zwięźle, po polsku)
Dla każdego pliku: co zmieniłeś (stara → nowa wartość, powód), co usunąłeś z braku źródła, czego nie dało się sprawdzić i co z tym zrobiłeś. Osobno: rozbieżności z plikami spoza grupy, sprawy do decyzji właściciela. Bez lania wody.

## Dla koordynatora po przeglądzie
- Pliki, w których zmieniło się `cover.big`/`cover.sub`: przegeneruj okładki.
- Sprawdź spójność liczb między grupami (`grep` po kwotach i liczbach z raportów).
- Sprawy „do decyzji właściciela” zbierz w raporcie `audyt/przeglad-…-RRRR-MM-DD.md` i w opisie PR.

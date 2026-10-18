# Brief dla agentów piszących teksty (szablon)

Przy więcej niż ~10 tekstach piszą równolegle agenci (Agent tool), po 2–6 tekstów na agenta, każdy plik u jednego agenta. Każdy dostaje ten sam brief (wypełniony raz na projekt) i swoją listę wierszy z `content-plan.md`. Brief jest samowystarczalny: agent nie widzi tej rozmowy.

Wypełnij nawiasy z plików projektu i pamięci. Nie dopisuj faktów o autorze ani marce, których nie ma w źródłach.

```markdown
# Brief: [nazwa serii] dla „[marka]” ([data])

## Najpierw przeczytaj
1. Skill: `~/.claude/skills/klaster-tresci/SKILL.md` oraz `references/szablon-artykulu.md` i `references/styl.md` (frontmatter, bloki, uczciwość).
2. Plan: `[ścieżka]/content-plan.md` (Twoje wiersze + kontekst klastrów).
3. Oferta i ton: `[plik z treścią LP / strategią]`.

## Projekt
- Marka „[marka]”: [co sprzedaje, komu]. Lejek: [wejście] → [oferta i cena, jeśli jest w plikach] → [dalszy krok].
- ODBIORCA tekstów: [kto czyta, jego poziom wiedzy, czego się boi]. Pisz [prosto / fachowo], [bez żargonu X].
- Autor: **[imię lub forma podpisu]**. Prawdziwe fakty: [lista z plików/pamięci]. **Nie wymyślaj** innych doświadczeń, liczby klientów, case'ów ani wyników. Nigdy: [zakazane twierdzenia, np. „10+ lat”].
- **TRYB AUTOMATYCZNY:** tekst gotowy do publikacji bez udziału autora. Bez ramek `[!praktyka]` i bez znaczników `[DO UZUPEŁNIENIA]`/`[NIEZWERYFIKOWANE]`. Twierdzenie, którego nie potwierdzisz u źródła, usuń. Wartość dodana = źródła, dane, wyliczenia, tabele, wzory, checklisty.
- Dane własne (prawdziwe, można cytować): [np. pomiar z datą i metodą] albo „brak”.

## Styl (zasady projektu, ważniejsze niż ogólne)
- [forma zwracania się: „Ty” wielką literą / „ty” / bezosobowo].
- Najwyżej jeden myślnik (–, —, „ - ”) na ekran tekstu; w tytułach i nagłówkach separator to [dwukropek].
- Bez konstrukcji „nie X, tylko Y” / „to nie X, to Y”.
- Bez wyliczanek trójkowych dla efektu (trzy przymiotniki pod rząd). Listy z treścią są OK.
- Konkretne liczby, krótkie akapity, nagłówki zdaniem (wielka litera tylko na początku). Bez frazesów z `styl.md`.
- Ceny w treści: tylko rynkowe ze źródeł (URL + data). Cena marki tylko w CTA we frontmatterze [i najwyżej jedno zdanie z linkiem do oferty].

## Źródła
- Każdy fakt, liczba, krok w interfejsie i przepis: źródło pierwotne ([domeny: urzędy, ISAP, EUR-Lex, pomoc producenta, towarzystwa naukowe]), sprawdzone dziś przez WebFetch. Nie przepisuj blogów konkurencji. Nie potwierdzisz → usuń.
- **Tematy YMYL** ([prawo / zdrowie / finanse]): pisz, na czym się opierasz („art. … ustawy … stanowi”, „wytyczne … zalecają”), z linkiem. Bez własnych opinii i interpretacji; gdy źródła czegoś nie rozstrzygają, napisz to i odeślij do [specjalisty]. `ymyl: true` i na końcu akapit: „Ten tekst opisuje [przepisy / zalecenia] na dzień [data]. Nie jest [poradą prawną / medyczną].”
- Akty prawne można cytować dosłownie. Inne źródła streszczaj własnymi słowami.

## Format pliku
- Plik: `[katalog treści]/<slug>.md`. Tylko Twoje pliki, nic innego w projekcie nie zmieniaj.
- Frontmatter wg `szablon-artykulu.md`, z ustaleniami:
  - `author: [autor]`, `publishedAt/verifiedAt/updatedAt: [data]`, `draft: true`;
  - `hub:` jeden z: [lista URL-i hubów];
  - `cover:` bez `src/og` (okładki robi koordynator); `big` tylko prawdziwa, zweryfikowana liczba (inaczej pomiń `big` i `sub`), `label` = krótki tytuł zdaniem (≤ 45 znaków), `alt`;
  - `kicker`: [przykłady etykiet kategorii];
  - `cta.href`: [mapowanie hub → adres oferty].
- Treść: bez H1, 4–7 sekcji H2, lead we frontmatterze (pierwsze zdanie z liczbą), FAQ i źródła tylko we frontmatterze.
- Ramki: `> [!uwaga]`, `> [!wzor] Tytuł`, `> [!liczba] wartość`. Kroki: `### Krok 1: …`.
- Linki wewnętrzne (≥ 3 w treści) **tylko** do: [lista stron projektu] oraz poradników `[baza]/<slug>/` z listy: [slugi całego planu, także tych pisanych równolegle]. Nigdy do [np. strony głównej]. `related:` tylko slugi z tej listy.
- Długość: [1200–2200] słów treści.

## Na koniec
QA na swoich plikach i poprawa błędów (uwagi oceń; „related nie istnieje” jest OK dla slugów z listy, które powstają równolegle):
`python3 ~/.claude/skills/klaster-tresci/scripts/sprawdz.py <Twoje pliki> --lp [adres oferty] --known [strony spoza src/pages, jeśli są]`
(trasy z `src/pages/**` są znane automatycznie).

Zwróć: ścieżki plików, liczbę słów, źródła z datą sprawdzenia, frazę główną i okładkę (big/sub/label) każdego tekstu oraz twierdzenia usunięte z braku źródła.
```

## Jak rozdzielić pracę

- Agent = 2–6 tekstów z jednego klastra (spójny ton i linkowanie wewnątrz klastra); huby pisze koordynator albo jeden agent na końcu, gdy wiadomo, co jest w klastrze.
- W jednym kroku uruchom wszystkich agentów (równolegle). Po powrocie: `sprawdz.py` na całości (kanibalizacja fraz i duplikaty slugów widać dopiero razem), przegląd 2–3 tekstów w całości, poprawki koordynatora.
- Raporty agentów to ich relacja, nie dowód: sprawdź pliki i wyniki QA, zanim powiesz użytkownikowi, że teksty są gotowe.

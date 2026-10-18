# Planowanie klastra

## Architektura

```
                  LP / strona oferty (konwersja)
                            ▲  CTA z każdego tekstu
        ┌───────────────────┼────────────────────┐
     HUB A ("Wszystko o X")  HUB B             NARZĘDZIE (kalkulator / sprawdzarka / kalendarz)
     ▲   ▲   ▲               ▲   ▲                  ▲ linkowane z tekstów, które liczą coś ręcznie
  poradniki, porównania,   strony encji (z danych)
  "czy się opłaca", krok po kroku
```

- **LP** - jedna oferta. Każdy tekst ma CTA prowadzące tutaj (albo do narzędzia, które prowadzi tutaj).
- **Hub (pillar)** - "Wszystko o X": 2-4 akapity wprowadzenia, karty wszystkich tekstów klastra pogrupowane w sekcje, krótkie FAQ. Celuje w najszerszą frazę klastra.
- **Poradnik** - jedna intencja, 1200-2500 słów. Główny typ treści.
- **Porównanie** - "X vs Y vs Z", tabela + rekomendacja per typ odbiorcy.
- **Strona encji** - z bazy danych, stałe pola (kwota, warunki tak/nie, termin, status, data sprawdzenia, źródło). Ma sens od ~20 encji.
- **Narzędzie** - kalkulator/sprawdzarka; strona narzędzia ma krótki opis metody i FAQ.
- **News/aktualizacja** - tylko gdy temat ma realne wydarzenia (zmiana przepisów, nowy nabór, premiera). Seria 3-6 tekstów pod różne intencje w ciągu kilku godzin, potem aktualizuj poradnik evergreen i linkuj z newsa.

Dla LP z jedną usługą (np. audyt SEO) zwykle wystarczy: 1-2 huby, 20-40 poradników/porównań, 1 narzędzie. Strony encji tylko, jeśli istnieje naturalna lista (miasta, branże, narzędzia, programy, urzędy).

## Rodzaje intencji do pokrycia wokół oferty

Dla każdej oferty przejdź tę listę i zapisz tematy:
1. **Co to jest / jak działa** (definicja, mechanizm) - najwyżej 1-2 teksty, reszta to szczegóły.
2. **Ile kosztuje / ile wynosi / ile można dostać** - zawsze z tabelą i datą.
3. **Kto może / warunki / czy mnie dotyczy** - lista warunków, wyjątki, "kto się łapie".
4. **Jak krok po kroku** - kroki z numerami, zrzuty, gotowe wzory.
5. **Czy się opłaca** - wyliczenie dla 3 scenariuszy (mały/średni/duży).
6. **X vs Y** - alternatywy, konkurencyjne rozwiązania, "zamiast".
7. **Błędy, pułapki, czego nie obejmuje**.
8. **Terminy, zmiany, nowości w roku X**.
9. **Dla kogo konkretnie** - wersje pod segment (JDG, spółka, branża, miasto).
10. **Narzędzia i wzory** - szablon, checklista, arkusz.

## Wzorce tytułów (H1)

H1 to obietnica z liczbą. `<title>` to krótsza wersja (≤ 60 znaków). Poniżej wzorce z przykładami z analizy - używaj **struktury**, a słowa, liczby i temat bierz z projektu; nie przepisuj przykładowych tytułów.

- `[Temat] [rok] - [konkretna liczba/obietnica] [kwalifikator]`
  → "Darmowe kredyty AWS 2026 - jak dostać 1000 USD z AWS Activate bez inwestora"
- `[Temat] [rok] - [N] [rzeczy], [wymiar], [wymiar] i [wymiar]`
  → "Darmowe kredyty AI dla startupów 2026 - 12 programów, kwoty, warunki i kolejność składania"
- `[A] vs [B] vs [C] - [kryterium porównania]`
  → "Kredyty chmurowe dla startupów 2026 - AWS vs Google vs Azure vs Cloudflare i chmury z UE"
- `Czy [X] się opłaca? Ile [zyskasz] przy [scenariusz 1], [2] i [3]`
  → "Czy IP Box się opłaca? Ile zaoszczędzi programista przy 15, 25 i 40 tys. zł miesięcznie"
- `[X] - co realnie daje, kto się kwalifikuje i jak [działać] ([rok])`
- `Jak [zrobić X] - [gotowe elementy] do [miejsca]`
  → "Jak wypełnić wniosek o kredyty startupowe - gotowe odpowiedzi do pól traction, team i funding"
- `[X] po [zmianie]: co dziś realnie dostaniesz i co wybrać zamiast ([rok])` - aktualizacja po wydarzeniu
- `[Zrobiłem X] - [wynik] (mój test)` - **tylko jeśli autor naprawdę to zrobił**

Rok w tytule tylko dla tematów, które się zmieniają (ceny, przepisy, programy). Przy zmianie roku aktualizuj treść, nie tylko tytuł.

## Slugi

Krótkie, po polsku, bez roku i bez stop-words: `darmowe-kredyty-aws`, `ip-box-ewidencja`, `czy-ip-box-sie-oplaca`. Bez roku, żeby URL przetrwał aktualizacje. Strony encji w podkatalogu (`/programy/slug/`), poradniki płasko w korzeniu.

## Linkowanie wewnętrzne

- Każdy tekst: link do huba w leadzie lub pierwszej sekcji, 2-4 linki do rodzeństwa w treści (tam, gdzie temat naturalnie się styka), CTA do LP/narzędzia w środku i na końcu, 3 powiązane teksty na końcu.
- Anchory opisowe, z nazwą rzeczy ("kalkulator ulgi B+R", "Google for Startups Cloud"), nie "kliknij tutaj".
- Hub linkuje do wszystkich tekstów klastra. Teksty klastra nie linkują masowo do innych klastrów - jedna, dwie wzmianki, gdy pasuje.
- Strona encji ↔ poradnik o tej encji: linkują się nawzajem, a jeśli encja ma też stronę z gotowym wzorem/narzędziem - wszystkie trzy tworzą trójkąt linków.
- Linkuj tylko do stron istniejących lub zaplanowanych w tym samym przebiegu - QA wyłapie martwe linki.

## Priorytetyzacja

Punktacja orientacyjna dla każdego tematu: `popyt (wolumen + trend) × dopasowanie do oferty × szansa (niska KD, słaby SERP) × możliwa wartość dodana`. Kolejność publikacji:
1. Huby (nawet jeśli krótkie) - szkielet linkowania.
2. 5-10 tekstów o najwyższej punktacji.
3. Narzędzie, jeśli jest proste do zrobienia.
4. Reszta partiami; po 4-8 tygodniach sprawdź Search Console i dopisz teksty pod frazy, które "prawie" łapią (pozycje 8-20).

## Format pliku planu (`content-plan.md`)

```markdown
# Plan treści - [projekt] (stan: RRRR-MM-DD)

Oferta: ... | Konwersja: ... | Odbiorca: ...
Źródło danych o frazach: OpenSEO / szacunek bez narzędzia

| # | status | slug | H1 | fraza główna (wol./KD/trend) | intencja | typ | hub | wartość dodana | CTA | linkuje do |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | plan | ile-kosztuje-audyt-seo | Ile kosztuje audyt SEO w 2026 - ... | ile kosztuje audyt seo (720/12/↗) | komercyjna | poradnik | /seo/ | tabela 14 ofert z cenami | formularz audytu | hub, co-zawiera-audyt-seo, ... |
```

Statusy: `plan → szkic → do uzupełnienia → gotowe → opublikowane`.

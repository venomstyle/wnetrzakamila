# Styl pisania

## Głos

- **1. osoba liczby pojedynczej autora, bezpośrednio do czytelnika na "ty"** ("Sprawdziłem", "Złóż najpierw te", "Jeśli masz JDG..."). 1. osoba tylko przy rzeczach, które autor naprawdę zrobił/sprawdził (np. „sprawdziłem u źródła”) - inaczej strona bezosobowa. W trybie automatycznym bez znaczników `[DO UZUPEŁNIENIA]`.
- **Konkret zamiast przymiotników:** kwoty, daty, terminy, liczba kroków, liczba dni. "Decyzja w 5-10 dni roboczych", nie "decyzja zapada szybko".
- **Źródło przy twierdzeniu:** "AWS pisze to wprost w FAQ", "według oficjalnej strony", "MF nie precyzuje, więc przyjmuję, że...". Wnioski własne oznaczaj jako wnioski.
- **Rekomendacje dla typu odbiorcy:** "Jeśli masz JDG bez inwestora - zacznij od X. Jeśli masz spółkę z VC - od Y."
- **Zdania średnie i krótkie,** listy tam, gdzie są wyliczenia. Akapit 2-4 zdania.
- **Pogrubienia** tylko dla kluczowych liczb i wniosków, najwyżej 1-2 na sekcję.
- Polskie zasady: cudzysłów „”, liczby z twardą spacją jako separatorem tysięcy (1 000 USD, 55 398,78 zł), przecinek dziesiętny, daty "12 października 2026" w tekście i "12.10.2026" w tabelach. Wybierz jeden separator w tytułach (" - ", " – " albo dwukropek) i trzymaj się go w całym serwisie.

## Zwroty do unikania (lista sprawdzana przez `sprawdz.py`)

Wypełniacze i kalki z AI, które obniżają zaufanie:
- "w dzisiejszych czasach", "w dobie", "w dynamicznie zmieniającym się świecie"
- "warto zauważyć, że", "warto podkreślić", "należy pamiętać, że" (zamiast tego po prostu podaj fakt)
- "kluczowy/kluczowe" (gdy nic nie odróżnia), "kompleksowy", "holistyczny", "innowacyjny"
- "nie ulega wątpliwości", "bez wątpienia", "jak sama nazwa wskazuje"
- "w tym artykule dowiesz się", "zapraszamy do lektury", "mamy nadzieję, że"
- "podsumowując", "reasumując", "w podsumowaniu" (sekcje-podsumowania powtarzające treść są zbędne)
- "odkryj", "zanurz się", "przenieś na wyższy poziom", "gra zmieniająca zasady"
- "idealny dla każdego", "dla każdego coś miłego"

## Uczciwość i YMYL

- Nie wymyślaj doświadczeń, liczby klientów, lat praktyki ani wyników testów. W trybie automatycznym pomiń takie fragmenty; w trybie z autorem zostaw `[DO UZUPEŁNIENIA: ...]`.
- Każda liczba ma źródło; nieweryfikowalne - usuń.
- Przy podatkach, prawie, finansach, zdrowiu: źródła urzędowe (ustawa, MF, ZUS, interpretacje, oficjalne regulaminy), ostrożne sformułowania, flaga `ymyl: true` (zastrzeżenie w layoucie).
- Linki partnerskie: `affiliate: true` + jedno zdanie informacji przy pierwszym takim linku.
- Gdy temat się zmienił (program wstrzymany, nowa stawka) - datowana notka na górze ("Aktualizacja 9.10.2026: ...") i aktualizacja `updatedAt`. Nie przepisuj historii po cichu.

## Długość

Tyle, ile trzeba, żeby wyczerpać intencję - zwykle 1200-2500 słów dla poradnika, 600-1200 dla porównania z tabelą, 400-900 opisu na stronie encji (resztę robią dane). Nie rozciągaj sekcjami "Historia X" czy "Podsumowanie".

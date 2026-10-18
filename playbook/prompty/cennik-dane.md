# Agent: tabela cen z opublikowanych treści

Zbuduj `src/data/cennik.json` wyłącznie z tekstów `draft: false`. Bierz tylko ceny, które tekst podaje w treści i które mają źródło w jego `sources`. Nie zbieraj nowych cen z internetu.

Pola każdej pozycji: `kategoria`, `co`, `firma`, `cena` (netto, brutto albo „cennik nie podaje”), `okres` ze stałego słownika (jednorazowo, miesięcznie, rocznie, od transakcji, za sztukę, bez opłat), `uwagi` (do 80 znaków, w tym promocje i progi ilościowe), `zrodlo`, `sprawdzono` (z `checkedAt`), `poradnik`.

Czego nie bierzesz:
- cen autora wyliczonych w tekście ani sum;
- własnych cen marki;
- duplikatów.

Każdą pozycję porównaj z treścią tekstu, potem zleć przegląd niezależny i otwórz u źródła próbkę co najmniej 30 pozycji. Strona `cennik.astro` pokazuje tylko pozycje z opublikowanych tekstów.

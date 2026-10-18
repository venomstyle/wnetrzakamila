# Szablon artykułu i bloki typów stron

To lista **bloków informacji** i ich celu, nie projekt graficzny. Wygląd, nazwy sekcji i kolejność dopasuj do marki projektu; pomiń blok, jeśli w danym temacie nic nie wnosi.

## Frontmatter

Wszystko, co da się wyrenderować z danych (skrót, FAQ, źródła, okładka, powiązane, CTA), trzymaj we frontmatterze. Layout wyświetla to w stałych miejscach i z tego samego źródła generuje JSON-LD, więc FAQ na stronie i FAQPage w danych strukturalnych są zawsze zgodne.

```yaml
---
title: "[H1: temat + rok, jeśli temat się zmienia + konkretna obietnica z liczbą]"
seoTitle: "[krótsza wersja do <title>, ≤ 60 znaków]"
description: "[120-160 znaków: odpowiedź z liczbą + co jeszcze jest w tekście]"
slug: krotki-slug-bez-roku
type: poradnik            # poradnik | hub | porownanie | encja | narzedzie | zestawienie | news
category: "[kategoria]"
kicker: "[KATEGORIA · PODKATEGORIA]"   # krótka etykieta nad H1 i na okładce
cluster: nazwa-klastra
hub: /hub-klastra/
primaryKeyword: "[jedna fraza główna, unikalna w całym serwisie]"
secondaryKeywords: ["[wariant]", "[wariant]"]
intent: informacyjna      # informacyjna | komercyjna | transakcyjna
publishedAt: RRRR-MM-DD   # prawdziwa data publikacji
verifiedAt: RRRR-MM-DD    # kiedy fakty sprawdzono u źródła
updatedAt: RRRR-MM-DD     # zmieniaj tylko przy realnej zmianie treści
author: autor-slug
readingTime: 8            # minuty, ~200 słów/min
lead: "[2-3 zdania: odpowiedź z liczbą, najważniejszy warunek, czas/koszt]"
tldr:                     # 3-5 faktów, każdy z liczbą lub konkretem
  - "[fakt]"
cover:                    # dane do okładki - patrz okladki.md
  src: /okladki/slug-hero.png
  og: /okladki/slug-og.png
  alt: "[opis treści okładki]"
  big: "[kluczowa liczba/fakt]"
  sub: "[kontekst liczby]"
  label: "[krótkie hasło tematu]"
faq:                      # 4-7 pytań; odpowiedź 1-3 zdania, samodzielna
  - q: "[pytanie tak, jak je wpisują ludzie]"
    a: "[odpowiedź]"
sources:                  # tylko źródła pierwotne
  - title: "[nazwa źródła]"
    url: https://...
    checkedAt: RRRR-MM-DD
related: [slug-a, slug-b, slug-c]
cta:
  title: "[pytanie, na które odpowiada narzędzie/oferta]"
  text: "[co dostanie czytelnik i ile mu to zajmie]"
  href: /narzedzie-albo-lp/
affiliate: false          # true → informacja o linkach partnerskich
ymyl: false               # true → zastrzeżenie "to nie jest porada"
draft: true               # false dopiero bez znaczników [DO UZUPEŁNIENIA]
---
```

## Poradnik (główny typ)

| Blok | Cel |
|---|---|
| Okruszki | kontekst i link w górę do huba; BreadcrumbList |
| Etykieta kategorii + H1 + lead | obietnica i natychmiastowa odpowiedź |
| Metadane: autor, opublikowano, **sprawdzono**, czas czytania | zaufanie i świeżość |
| Okładka | rozpoznawalność, og:image |
| "W skrócie" (3-5 faktów) | odpowiedź dla skanujących wzrokiem i AI Overview |
| Spis treści (od ~1200 słów; na dużym ekranie może być lepki obok treści) | nawigacja w długim tekście |
| 4-7 sekcji H2, każda = jedna podintencja | dowody i szczegóły |
| CTA w środku (gdy czytelnik ma już kontekst) i na końcu | przejście do narzędzia/oferty |
| FAQ | długi ogon pytań, FAQPage |
| Źródła z datami sprawdzenia | weryfikowalność |
| Autor (bio, link "jak sprawdzam") | E-E-A-T |
| 3 powiązane teksty | głębokość wizyty, linkowanie |

Elementy sekcji, dobierane do treści:
- **tabela** - gdy porównujesz ≥ 3 rzeczy w ≥ 2 wymiarach (z podpisem: źródło, data),
- **wyróżniona liczba** - jedna najważniejsza wartość tekstu,
- **lista warunków** + ramka **ostrzeżenia** - przy "kto może",
- **kroki z numerami** (H3 w każdym) + zrzuty z podpisem - przy "jak zrobić",
- **gotowy tekst do skopiowania** - wzór pisma, odpowiedzi do formularza, szablon,
- **ramka z praktyki** - tylko z prawdziwego doświadczenia autora (inaczej znacznik `[DO UZUPEŁNIENIA]`),
- **wyliczenie dla 3 scenariuszy** - przy "czy się opłaca".

## Strona encji (z danych)

| Blok | Cel |
|---|---|
| Nagłówek: nazwa, 3-4 najważniejsze fakty, "dla kogo" jednym zdaniem, link do oficjalnego źródła, data sprawdzenia | odpowiedź w 5 sekund |
| Wizytówka z kluczową wartością i 3 polami decyzyjnymi | szybkie porównanie z innymi encjami |
| Kafelki faktów (wartość, czas, ważność, główny warunek) | skanowanie |
| Notka o zmianie (datowana), jeśli encja się zmieniła | aktualność, uczciwość |
| Sprawdzarka "czy się łapiesz" (przełączniki + checklista z licznikiem) | interakcja, kwalifikacja leada |
| Co dokładnie zawiera / kroki / co po akceptacji | konkret |
| Na tle podobnych (ranking, bieżąca encja wyróżniona) | linkowanie między encjami, kontekst |
| Karta encji (lista wszystkich pól) | do skanowania i dla AI |
| Powiązane poradniki, FAQ, źródła, "zgłoś błąd" | domknięcie |

Pola encji trzymaj w pliku danych; każde pole ze źródłem i datą sprawdzenia.

## Hub

Okruszki → H1 → 1-2 zdania obietnicy (np. "każdy tekst ma datę sprawdzenia i źródła") → liczniki (ile tekstów/encji, kiedy sprawdzono) → grupy kart → krótkie FAQ → CTA. Karta tekstu: okładka, etykieta, tytuł, zajawka ~140 znaków, czas czytania, data sprawdzenia.

## Narzędzie

H1 jako pytanie, na które narzędzie odpowiada → lead (ile pytań, ile minut) → pytania z dużymi polami wyboru i paskiem postępu → wynik (liczba + "co zrobić najpierw") → metoda i założenia → informacja, że liczy lokalnie / co dzieje się z danymi → FAQ → CTA do oferty.

## Zestawienie / kalendarz

Etykieta z licznikiem i datą sprawdzenia → H1 → zasada doboru danych ("tylko potwierdzone u źródła, zapowiedzi osobno") → filtry → tabela (nazwa + opis, kto, status, termin + "ile dni zostało", kwota, link do źródła i do opisu).

## Bloki w treści - składnia

W MDX - komponenty projektu. W czystym Markdown - alerty w cytacie, zamieniane w layoucie na ramki:

```markdown
> [!uwaga]
> [ostrzeżenie z konkretem]

> [!praktyka]
> [DO UZUPEŁNIENIA: czego autor nauczył się, robiąc to sam? 2-3 zdania z konkretem]

> [!wzor] [Do czego jest ten tekst]
> [gotowy tekst z polami w nawiasach kwadratowych]

> [!liczba] [wartość]
> [kontekst]
```

Kroki: `### Krok 1: [czynność]`.

## Typografia tekstu ciągłego

Krój display marki (geometryczny, z małą wysokością liter) zostaw na nagłówki i UI. Do akapitów, leadu, FAQ i ramek użyj kroju do czytania na ekranie (np. Inter, z dużą wysokością liter i odróżnialnymi l/I/1), hostowanego lokalnie z podzbiorami latin i latin-ext dla polskich znaków. Rozmiar 18 px (17 px na telefonie), interlinia ok. 1,7, szerokość kolumny do ~68 znaków. Zanim wybierzesz, porównaj 3-4 kroje na prawdziwym akapicie z polskimi znakami.

## Lead - jak pisać

Pierwsze zdanie odpowiada na pytanie z H1 konkretną liczbą. Drugie i trzecie dodają najważniejszy warunek/wyjątek i czas/koszt. Bez "W tym artykule dowiesz się" i bez definicji oczywistości.

Źle: "Audyt SEO to ważny element strategii marketingowej. W tym poradniku przyjrzymy się jego kosztom."
Dobrze: "[Typ audytu] kosztuje w Polsce zwykle [od-do] zł netto, a [drugi typ] - [od-do] zł. Cena zależy głównie od [czynnik]. Na raport czeka się [czas]." (wartości z prawdziwych źródeł)

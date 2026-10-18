# Szkielet bloga (Astro): co jest stałe, a co pochodzi z wyborów marki

`assets/szkielet-astro/` to niestylowany szkielet wyciągnięty z niechcieznajda. Daje strukturę, dane i linkowanie. Nie daje wyglądu: CSS to tylko układ na tokenach o neutralnych wartościach, a okładka jest zastępcza.

## Pliki

| Plik | Co robi |
|---|---|
| `astro.config.mjs` | `trailingSlash: 'always'`, sitemap, wtyczka ramek |
| `src/content.config.ts` | kolekcja `poradniki` ze schematem frontmattera z `szablon-artykulu.md` |
| `src/lib/poradniki.ts` | lista bez szkiców i dat z przyszłości w buildzie, huby, `inHub`, okładki, daty, odmiana liczebników, `katOf` (klucz kategorii) |
| `src/lib/remark-ramki.mjs` | `> [!uwaga]`, `[!praktyka]`, `[!wzor]`, `[!liczba]` → `<aside class="ramka ramka--typ">` |
| `src/data/marka.ts` | nazwa, URL, baza bloga, autor (prawdziwe fakty), domyślne CTA, linki |
| `src/layouts/Base.astro` | meta, canonical, OG, `noindex` dla szkiców, slot na JSON-LD |
| `src/layouts/Article.astro` | artykuł: bloki w stałej kolejności + JSON-LD Article, BreadcrumbList, FAQPage |
| `src/pages/poradniki/[slug].astro` | artykuł albo hub (`type: hub`) z CollectionPage, BreadcrumbList, FAQPage |
| `src/pages/poradniki/index.astro` | lista wszystkich tekstów pogrupowana według hubów, CollectionPage |
| `src/components/PoradnikCard.astro` | karta: okładka, kategoria, tytuł, zajawka (duża karta), czas, data sprawdzenia, `data-kat` |
| `src/components/Footer.astro` | stopka: równe kolumny poradników (jedna na hub, ta sama liczba linków, „Wszystkie: N”) |
| `src/components/Header.astro`, `Logo.astro` | miejsce na logo z wyboru i CTA |
| `src/styles/tokeny.css` | neutralne tokeny (kolory, kroje, promienie, kategorie) do podmiany |
| `src/styles/szkielet.css` | tylko układ: siatki, odstępy, zachowanie na telefonie |
| `src/okladki/zastepcza.html` | neutralna okładka do podglądu przed wyborem okładek |
| `przyklad/poradniki/` | hub + 2 teksty testowe (marka zmyślona; nie publikować) |

## Jak użyć

**Nowy projekt:** skopiuj katalog, `npm install`, wypełnij `marka.ts` i `site` w `astro.config.mjs`, treści do `src/content/poradniki/`. Test: skopiuj `przyklad/poradniki/*.md`, wyrenderuj zastępcze okładki i zbuduj:

```bash
python3 ~/.claude/skills/klaster-tresci/scripts/okladka.py --template src/okladki/zastepcza.html --from-dir src/content/poradniki --out public/okladki
npx astro build
```

**Istniejący projekt Astro (np. LP):** nie nadpisuj jego plików. Przenieś brakujące części (kolekcja, `lib/poradniki.ts`, ramki, strony poradników, karta, kolumny poradników w stopce) i podłącz do jego Base, Header i tokenów. Klasy szkieletu (`.karta`, `.prose`, `.ramka`, `.kicker`…) przemianuj, jeśli kolidują.

**Testowy build poza projektem** (np. w scratchpadzie): `node_modules` skopiuj albo zainstaluj. Nie podpinaj symlinkiem `node_modules` innego projektu: Astro i Vite zapisują cache w `node_modules/.astro` i `node_modules/.vite`, czyli w tamtym projekcie.

## Co jest stałe i dlaczego

**Kolejność bloków artykułu:** okruszki → kategoria → H1 → lead → autor, data sprawdzenia, czas → okładka → spis sekcji → „W skrócie” → treść → CTA → FAQ → źródła, ramka „Widzisz zmianę? Daj znać” i zastrzeżenia → autor → powiązane. Odpowiedź i dowody zaufania są nad zgięciem; kto skanuje, dostaje skrót; CTA pojawia się, gdy czytelnik ma już kontekst; FAQ i źródła domykają długi ogon. Ramka pod źródłami (data sprawdzenia + mail z gotowym tematem do `marka.email`) to warstwa świeżości: czytelnik zgłasza zmianę u źródła, a my poprawiamy tekst i datę. Uzasadnienie bloków: `szablon-artykulu.md`.

**Dane strukturalne z frontmattera:** Article (z `datePublished`, `dateModified`, autorem, wydawcą, obrazem OG), BreadcrumbList, FAQPage (tylko gdy jest FAQ), CollectionPage na hubie i liście. FAQ na stronie i w JSON-LD mają jedno źródło, więc nie rozjeżdżają się.

**Publikacja:** `draft: true` i `publishedAt` w przyszłości widać tylko w `astro dev`; build je pomija (harmonogram), a szkice mają `noindex`. Plakietka „Szkic” albo „Zaplanowany na …” pokazuje się tylko lokalnie.

**Linkowanie:** okruszki do huba; hub z licznikiem i kartami swoich tekstów (pierwsza duża) i linkami do pozostałych hubów; artykuł z 3 powiązanymi (`related`); lista pogrupowana hubami z linkiem „Wszystko w temacie” na linii tytułu; stopka z kolumną na hub. Nowe teksty pojawiają się w hubie, liście i stopce bez ręcznej edycji.

**Stopka:** kolumny tej samej szerokości, ta sama liczba linków w każdej (`NA_KOLUMNE`), każdy link w jednej linii z wielokropkiem, na końcu „Wszystkie: N”. Dzięki temu kolumny kończą się na jednej wysokości niezależnie od długości tytułów.

**Adresy:** `trailingSlash: 'always'`, teksty pod `marka.blog.base` (domyślnie `/poradniki/`), hub to też wpis kolekcji (`/poradniki/<slug-huba>/`), pole `hub` w tekście = URL huba. Zmiana bazy: `marka.blog.base` + nazwa katalogu w `src/pages/`.

## Co pochodzi z wyborów marki (references/wybory.md)

| Element | Skąd | Gdzie trafia |
|---|---|---|
| Kolory, kroje, skala, promienie, cienie, kolory kategorii | wybór stylu | `src/styles/tokeny.css` |
| Forma bloków: nagłówek, karta, ramki, skrót, CTA, FAQ, źródła, spis (np. lepka kolumna, pasek postępu, „trasa”), stopka, motyw marki | wybór stylu | `src/styles/marka.css`, w razie potrzeby znaczniki w komponentach |
| Logo i favikona | wybór logo | `Logo.astro`, `public/favicon.svg`, szablon okładki |
| Okładki i miniatury | wybór okładek | `src/okladki/szablon.html` → `public/okladki/` |
| Teksty interfejsu (nazwy sekcji, etykiety ramek, przycisk CTA) | ton marki | `marka.ts`, `remark-ramki.mjs`, layouty |
| Warianty sekcji | opcjonalny wybór | komponenty |

Zmieniając formę, nie zmieniaj kolejności bloków, danych strukturalnych ani linkowania. Jeśli marka naprawdę potrzebuje innej kolejności (np. okładka nad H1), zapisz powód w DECYZJE.md.

## Kontrola po zmianach

- `npx astro build` bez błędów schematu; liczba stron = teksty + huby + lista.
- W `dist/` każdy artykuł ma Article i BreadcrumbList, a z FAQ także FAQPage; hub ma CollectionPage.
- `scripts/sprawdz.py` (trasy z `src/pages/**` i `dist/` są znane automatycznie).
- Przegląd wizualny: `przeglad-wizualny.md`.

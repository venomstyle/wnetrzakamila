# Przegląd wizualny

Po wdrożeniu stylu, logo i okładek (i po każdej większej zmianie CSS) obejrzyj **każdy typ strony** w całości, na dużym ekranie i na telefonie. Większość błędów z niechcieznajda była widoczna dopiero na pełnym zrzucie: ciemny tekst na akcencie, makiety znikające na ciemnym tle, link „Wszystko w temacie” na złej wysokości, nierówne kolumny stopki.

## Zrzuty

Uruchom podgląd lokalny (`npx astro dev --host 127.0.0.1` albo `npx astro preview --host 127.0.0.1` po buildzie), potem:

```bash
node ~/.claude/skills/klaster-tresci/scripts/zrzuty.mjs --base http://127.0.0.1:4321 --out przeglad --szer 1280,375 --kontrast \
  / /poradniki/ /poradniki/<hub>/ /poradniki/<poradnik-z-tabela-i-ramkami>/ /poradniki/<najdluzszy-tytul>/ /<lp-albo-narzedzie>/
```

- Typy stron: strona główna/LP, lista poradników, każdy hub (co najmniej jeden), poradnik z tabelą, ramkami, wzorem i FAQ, tekst z najdłuższym tytułem, narzędzie, strona encji, jeśli są.
- Szerokości: 1280 i 375 px (`--szer`); przy układach z punktem przełamania między nimi dodaj 900.
- `--kontrast` zapisuje `przeglad/kontrast.json`: elementy z kontrastem poniżej WCAG AA (4,5:1, duży tekst 3:1). Tekst na obrazie albo gradiencie trzeba ocenić wzrokiem.
- Bardzo długie strony skrypt tnie na części po 8000 px. Do obejrzenia w czacie możesz zrobić z nich arkusz (`arkusz.py … --cols 4`) albo czytać części po kolei.
- `--ciemny` emuluje tryb ciemny, jeśli projekt go obsługuje.

Każdy zrzut obejrzyj (Read na PNG). Nie wystarczy, że build przeszedł.

## Lista kontrolna

**Kontrast i kolor**
- [ ] Tekst na akcencie: przyciski, plakietki, CTA, aktywne elementy spisu. Kolor tekstu na akcencie to osobny token (`--on-accent`), nie „biały z przyzwyczajenia”. Żółty, miętowy, jasny turkus zwykle potrzebują ciemnego tekstu.
- [ ] Szare podpisy na ciemnym tle (stopka, CTA, hero): raport `kontrast.json` łapie je pierwsze.
- [ ] Linki w treści odróżnialne od tekstu nie tylko kolorem (podkreślenie).
- [ ] Kolory kategorii: czytelna etykieta na karcie i na okładce w każdej kategorii, nie tylko w pierwszej.

**Makiety, ilustracje, obrazy**
- [ ] Makiety telefonu/przeglądarki, zrzuty ekranu i ikony z ciemnym konturem na ciemnym tle: czy nie znikają? Dodaj jasną ramkę albo tło pod makietą.
- [ ] Logo na każdym tle, na którym występuje (nagłówek, stopka, okładka, CTA).
- [ ] Okładki na karcie nie są przycięte w złym miejscu (proporcja 16:9 karty = proporcja okładki hero).

**Stany interakcji**
- [ ] Hover na kartach, przyciskach, linkach w stopce, pozycjach spisu: widoczny i bez przesuwania sąsiednich elementów. Sprawdź przez najechanie (np. `computer` → `hover` w podglądzie) albo `:hover` wymuszony w DevTools.
- [ ] Fokus z klawiatury widoczny (Tab po stronie).
- [ ] FAQ: otwieranie i zamykanie, ikona zmienia stan.

**Odstępy i wyrównanie**
- [ ] Odstęp pod nagłówkami sekcji: H2 bliżej swojej treści niż poprzedniej sekcji; nagłówek sekcji nie „przykleja się” do kart.
- [ ] Link sekcji („Wszystko w temacie”, „Zobacz wszystkie”) na linii **ostatniej linii** tytułu (`align-items: last baseline`), także gdy tytuł łamie się na 2 linie; na telefonie przechodzi pod tytuł.
- [ ] Kolumna czytania ~60–70 znaków; tabela przewija się poziomo na telefonie zamiast rozpychać stronę.
- [ ] Brak poziomego przewijania całej strony w 375 px.

**Stopka**
- [ ] Kolumny poradników równej szerokości, ta sama liczba linków, każdy link w jednej linii (wielokropek), „Wszystkie: N” na tej samej wysokości we wszystkich kolumnach.
- [ ] Na telefonie kolumny jedna pod drugą, linki mogą się łamać.

**Okładki i karty**
- [ ] Najdłuższy tytuł mieści się w limicie linii i nie wchodzi na liczbę; najdłuższa liczba („do 10% obrotu”) mieści się w kontenerze.
- [ ] Hub bez liczby nie ma pustego miejsca po liczbie.
- [ ] Karty w jednym rzędzie mają równą wysokość, metadane na dole.

**Treść i stan**
- [ ] Plakietki „Szkic” / „Zaplanowany” tylko w `dev`; w `preview` po buildzie ich nie ma.
- [ ] Polskie znaki w krojach nagłówków i okładek (ą, ę, ł, ż, ź, ć, ń, ó, ś) bez kroju zastępczego.

**Nieaktualny CSS na serwerze deweloperskim**
- [ ] Po dużej przebudowie komponentów albo stylów Astro potrafi serwować stary, przetworzony CSS nawet po przeładowaniu strony. Jeśli zrzut nie zgadza się z kodem: zatrzymaj i uruchom ponownie proces `astro dev` (albo zrób build + `preview`) i porównaj jeszcze raz. **Nie cofaj zmian w kodzie**, żeby „naprawić” podgląd.
- [ ] Sprawdź, czy przeglądasz właściwy serwer: inna sesja może mieć swój `astro dev` na innym porcie w tym samym katalogu.

## Raport

Zapisz krótko: strona × szerokość → problem → poprawka (albo „do decyzji użytkownika”). Po poprawkach zrób zrzuty jeszcze raz tylko dla zmienionych stron i pokaż użytkownikowi pary przed/po (np. `arkusz.py przed.png=Przed po.png=Po --cols 2`).

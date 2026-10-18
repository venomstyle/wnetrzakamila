# Usługi druku 3D: popyt i gotowość do płacenia (18.10.2026)

Brief: `BRIEF-uslugi-druku.md`. Uzupełnia `druk3d.md` (tam frazy usługowe były wykluczone jako „zlecenie usługi”). Strona podaży (ile drukarni, kanały) jest w osobnym opracowaniu `uslugi-druku-podaz-*`.

**Oznaczenia źródeł (wszystko pobrane 18.10.2026):**
- **[W]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live` (2616, pl). Wolumen = średnia z 10.2025–09.2026 liczona przeze mnie z miesięcy. Trend r/r = VII–IX 2026 wobec VII–IX 2025. CPC i „stawka top (wysoka)” w USD.
- **[K]** odkrywanie fraz: `/v3/dataforseo_labs/google/keyword_suggestions/live` (ziarna: druk 3d na zamówienie, drukowanie 3d, skanowanie 3d, modelowanie 3d, projektowanie 3d, prototypowanie, wydruk 3d; plus `sug_druk3d` z poprzedniego badania) i lista ręczna (20 miast × 6 wzorców).
- **[S]** `/v3/serp/google/organic/live/advanced`, desktop, Polska, depth 10–100, `load_async_ai_overview`. Kontrola: 1 SERP mobilny z lokalizacją Warszawa.
- **[B]** `/v3/backlinks/bulk_referring_domains/live` dla 147 URL-i i 94 domen z top 10.
- **[A]** Google Ads Transparency: `/v3/serp/google/ads_advertisers/live/advanced` (szukanie reklamodawcy po nazwie) i `/v3/serp/google/ads_search/live/advanced` (reklamy wg domeny, region PL).
- **[C]** `/v3/on_page/content_parsing/live` (cenniki; WebFetch jest zablokowany przez proxy).
- Kurs USD: 3,8952 zł (średni NBP 15.10.2026) wg comparic.pl, odczyt przez WebSearch; API NBP zablokowane przez proxy. W rachunkach zaokrąglam do 3,90 zł.

Dane w `dane/`: `uslugi-druku-popyt-frazy.csv` (310 fraz), `-klastry.csv`, `-serp-top10.csv` (157 wyników), `-serp-podsumowanie.csv` (16 SERP-ów), `-reklamodawcy.csv`, `-ceny.csv`, `-rachunek.csv`, `-rachunek-podsumowanie.csv`. Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/uslugi-popyt/`.

---

## Wniosek w skrócie

Popyt na zlecenie wydruku jest, ale mały i rozproszony: **ok. 37 300 wyszukiwań/mies.** w rdzeniu usług, z czego ok. 25 100 to realna intencja zlecenia. Drukarnie płacą za klienta mało i nieregularnie: w 17 SERP-ach nie było żadnej reklamy, a w Ads Transparency stale reklamuje się garstka firm. Po 12 mies. serwis zbierający zapytania daje **ok. 10 zapytań/mies. i ok. 80 zł (ostrożnie)** albo **ok. 70 zapytań/mies. i ok. 3 400 zł (realnie)**. Prawie cały przychód realny daje B2B (prototypy, skan, CAD), bo zlecenie B2C to zwykle 30–150 zł.

---

## 1. Popyt na zlecenie wydruku [W][K]

- Pobrane: 310 fraz; 267 po zdjęciu bliskich wariantów (Google Ads łączy np. „druk 3d warszawa” i „drukowanie 3d warszawa” w jedną liczbę).
- **Rdzeń usług (B2C + B2B + mieszane B2C/B2B): 37 321/mies.** Trend r/r **+18%**. Sezon: najniżej 06.2026 (27 430), najwyżej 03.2026 (49 600). Szczyt przypada na marzec, inaczej niż w hobby (grudzień, `druk3d.md`).
- Frazy ogólne „druk 3d”, „drukowanie 3d”, „wydruk 3d”: 5 558/mies., intencja mieszana, poza rdzeniem.
- Uwaga do porównań: dziś „druk 3d” ma w [W] 2 900 (średnia 12 mies. grupy 3 067). W `druk3d.md` ta sama fraza ma 8 100. Google Ads inaczej grupuje warianty w różnych zapytaniach, więc pojedyncze liczby dla fraz-głów są niepewne.

| Segment / klaster [W] | Frazy | Wol./mies. | CPC ważony USD | Trend r/r | Sezon (min → max) |
|---|---|---|---|---|---|
| B2C/B2B: ceny i wycena | 15 | 12 109 | 0,25 | +64% | 06.2026: 8 980 → 09.2026: 15 630 |
| B2C/B2B: druk 3d + miasto | 78 | 7 002 | 1,12 | −14% | 08.2026: 4 770 → 03.2026: 11 270 |
| B2C/B2B: zlecenie ogólne | 11 | 4 843 | 1,37 | +12% | 06.2026: 3 960 → 03.2026: 6 170 |
| B2B: metal, SLS/MJF, prototypy, makiety, wielkoformat | 38 | 3 009 | 1,70 | −4% | 08.2026: 1 660 → 03.2026: 4 770 |
| B2B: skanowanie 3D i inżynieria odwrotna | 11 + 22 miejskich | 2 204 + 672 | 1,81 / 1,35 | −21% / −13% | 08.2026: 1 200 → 03.2026: 4 060 |
| B2C: figurki, części, gadżety | 28 | 1 895 | 0,47 | +36% | 06.2026: 1 420 → 01.2026: 2 310 |
| B2C/B2B: projektowanie i modelowanie do druku | 15 | 1 561 | 0,81 | +45% | 10.2025: 1 150 → 01.2026: 2 170 |
| B2C/B2B: żywica (SLA) | 5 | 1 450 | 1,03 | −22% | 08.2026: 950 → 01.2026: 1 860 |
| B2C: Allegro/OLX | 3 | 1 429 | 0,17 | +61% | 08.2026: 940 → 12.2025: 1 960 |
| B2B: platformy (nawigacyjne: xometry, protolabs, craftcloud, treatstock, 3d hubs) | 5 | 1 147 | 2,47 | +1% | |
| Podaż: „zlecenia na druk 3d”, „druk 3d zlecenia” | 2 | 248 | 0,63 | +26% | |
| **Sąsiad do porównania: laser i CNC** | 28 | 9 224 | 1,93 | −10% | 08.2026: 6 550 → 03.2026: 13 590 |

**Najważniejsze frazy [W]** (wol./mies., CPC USD, trend r/r):
- druk 3d ceny 5 333 (0,18; +55%), ile kosztuje druk 3d 4 292 (0,14; +118%), wydruk 3d cena 137, wycena druk 3d 274 (+129%), druk 3d online 305 (+75%).
- druk 3d na zamówienie 1 775 (1,44; +29%), drukarnia 3d 1 015 (1,45; 0%), wydruk 3d na zamówienie 540 (1,21; +50%), usługi druku 3d 525 (1,56; −41%).
- B2B: skanowanie 3d 925 (1,57; −18%), inżynieria odwrotna 411 (4,20), druk 3d z metalu 312 (1,08; +43%), druk 3d wielkoformatowy 258 (1,33; +52%), druk sls 244 (2,47), druk sla 232 (2,14), prototypowanie 222 (1,24; −41%), szybkie prototypowanie 152, makiety 3d 142 (2,60), druk 3d sla 140 (3,40), druk mjf 81 (2,48).
- B2C: figurka 3d ze zdjęcia 452 (0,27; +149%), druk 3d figurek 310 (0,30), figurki 3d na zamówienie 171 (+103%), druk 3d części samochodowych 118 (1,29). Cosplay po polsku prawie nie istnieje: „druk 3d cosplay” 0, „zbroja cosplay” 22. „druk 3d części zamiennych” 0.
- Projektowanie: projektowanie 3d do druku 1 122 (0,75; +66%), modelowanie 3d 651 (wieloznaczne, głównie nauka). „modelowanie/projektowanie 3d na zamówienie” 0.

**Miasta (20 największych) [W]:** suma „druk/drukowanie/wydruk 3d [miasto]” = **6 595/mies.** Warszawa 1 229, Kraków 975, Wrocław 705, Poznań 520, Łódź 387, Rzeszów 376, Lublin 345, Gdańsk 291, Katowice 291, Bydgoszcz 265, Szczecin 260, Białystok 192, Częstochowa 154, Sosnowiec 112, Kielce 103, Gdynia 92, Olsztyn 92, Gliwice 87, Toruń 65, Radom 54. **14 z 20 miast spada r/r** (Warszawa −23%, Lublin −33%, Łódź −29%). „druk 3d na zamówienie [miasto]” ma wolumen tylko w Warszawie (90) i Wrocławiu (10). Dla porównania „wycinanie laserowe [miasto]” w tych miastach: 694/mies., „skanowanie 3d [miasto]”: 587/mies.

**B2C a B2B:** B2C 3 324/mies. (figurki, gadżety, Allegro), B2B 7 032/mies., mieszane 26 965/mies. Mieszane to głównie pytania o cenę i frazy miejskie, gdzie po samym zapytaniu nie da się rozpoznać klienta.

**Wnioski z popytu:**
- Rośnie pytanie o cenę („ile kosztuje druk 3d” +118%), spadają frazy transakcyjne miejskie (−14%) i „usługi druku 3d” (−41%). Ludzie częściej porównują ceny i zamawiają online.
- CPC na frazach cenowych jest bardzo niski (0,14–0,18 USD). Reklamodawcy nie traktują ich jako zakupowych. W SERP „druk 3d ceny” 4 z 10 wyników to sklepy z drukarkami (Botland, Media Expert, x-kom, get3d), a Google podpowiada „Profesjonalna drukarka 3D cena” [S]. Część tej puli to ceny drukarek, więc w rachunku liczę tylko 50%.
- Laser i CNC mają 9 224/mies., czyli 78% tego, co frazy „zlecenie ogólne” i miejskie razem (11 845), przy wyższym CPC (1,93 USD). To naturalne rozszerzenie katalogu, jeśli produkt powstanie.

## 2. Szesnaście SERP-ów [S][B]

Dane: `dane/uslugi-druku-popyt-serp-top10.csv`, `-serp-podsumowanie.csv`.

| Fraza | Wol. [W] | Local Pack | AIO | Firmy usługowe w top 10 | Katalogi | Platformy / Allegro | URL-e <10 dom. link. | Mediana dom. link. domen |
|---|---|---|---|---|---|---|---|---|
| druk 3d ceny | 5 333 | nie | tak | 5 (+1 dystrybutor) | 0 | 0 | 9/10 | 362 |
| druk 3d na zamówienie | 1 775 | nie (na mobile w Warszawie: tak) | tak | 5 (+2) | 0 | Allegro 1 | 8/9 | 267 |
| drukarnia 3d | 1 015 | tak | tak | 6 | panoramafirm 1 | 0 | 6/9 | 140 |
| skanowanie 3d | 925 | nie | tak | 6 (+1) | 0 | ceneo 1 | 7/10 | 313 |
| druk 3d warszawa | 871 | tak | tak | 7 | robisz.to 1 | 0 | 8/10 | 42 |
| druk 3d wrocław | 555 | tak | nie | 7 | oferteo 1 | 0 | 9/10 | 194 |
| usługi druku 3d | 525 | tak | tak | 5 (+3) | 0 | Allegro 1 | 8/10 | 345 |
| druk 3d kraków | 504 | tak | nie | 6 (+2) | 0 | 0 | 4/10 | 237 |
| figurka 3d ze zdjęcia | 452 | nie | nie | 4 | 0 | Allegro 2 | 9/9 | 59 008* |
| druk 3d poznań | 410 | tak | tak | 6 (+2) | oferteo 1 | 0 | 9/10 | 127 |
| druk 3d łódź | 337 | tak | nie | 2 | automatyka.pl 1 | 0 | 9/10 | 628 |
| druk 3d lublin | 321 | tak | nie | 3 | oferteo, targeo, lento | 0 | 10/10 | 3 695* |
| druk 3d z metalu | 312 | nie | nie | 0 | 0 | 0 | 10/10 | 628 |
| druk 3d gdańsk | 246 | tak | nie | 4 (+2) | trojmiasto.pl 1 | 0 | 8/10 | 242 |
| druk sls | 244 | nie | tak | 2 (+2) | 0 | Xometry 1 | 9/10 | 1 389 |
| druk 3d katowice | 198 | tak | nie | 4 | targeo, naszemiasto | 0 | 8/10 | 76 |

\* mediana zawyżona przez Facebook, Allegro i strony uczelni.

**Wnioski z SERP:**
- **Local Pack w 10 z 16** SERP-ów: we wszystkich 8 miejskich oraz w „drukarnia 3d” i „usługi druku 3d”. Na mobile w Warszawie Local Pack (4 firmy) pojawia się też przy „druk 3d na zamówienie”. Pakiet zabiera kliknięcia z wyników organicznych, więc frazy miejskie są dla katalogu trudniejsze, niż wynika z linków.
- **AIO w 8 z 16.** Na „druk 3d ceny” AIO podaje gotowe widełki cen i cytuje cenniki małych pracowni (craft3d.pl, order3d.pl, elprodruk3d.pl, drukujemy3d.pl, geometryhustlers.pl, send3d.eu, v-slot.pl). Strona z cenami pracowni „z datą” ma więc szansę na cytowanie.
- **Wygrywają małe pracownie:** 72 ze 157 wyników to firmy usługowe, 15 to dystrybutorzy sprzętu z usługą (CadXpert, B3D, Center3DPrint). **131 ze 157 URL-i ma <10 domen linkujących [B].**
- **Programatyczne strony miejskie małych firm rankują:** druk3dkatowice.pl (15 domen linkujących do domeny [B]) ma strony „Druk 3D na zlecenie [miasto] i województwo” na 7. miejscu w Warszawie i 5. we Wrocławiu; drukarex.pl (56) jest 2. w Krakowie i 3. w Poznaniu; drukujemy3d.pl/lubelskie jest 1. w Lublinie.
- **Katalogi są słabe:** Oferteo 3 razy, i to adresami drugiej strony listingu („/druk-3d/poznan/2”, „/wroclaw/2”); Panorama Firm 1 raz; Fixly 0. Oferteo ma jednak kategorię „druk 3D”, czyli model zapytań już działa w Polsce. **Platformy zagraniczne prawie nieobecne:** Xometry 1 raz (SLS), Craftcloud, Treatstock, Protolabs, Hubs 0.
- **Facebook 13 razy** (strony pracowni, grupy „Druk 3D Polska”, „Druk 3D Trójmiasto”). Część zleceń idzie przez grupy, czego nie da się zmierzyć wolumenem.

## 3. Kto płaci za reklamy [A][S][W]

**W SERP:** w 16 SERP-ach desktop (Polska) i 1 mobilnym (Warszawa) **nie było ani jednej reklamy** [S]. To pojedynczy pomiar z 18.10.2026 ok. 13:50, więc nie wyklucza reklam o innej porze.

**Keyword Planner [W]:** konkurencja „HIGH” (0,99) na „druk 3d na zamówienie” i CPC 1,1–1,7 USD na frazach transakcyjnych. Ktoś więc licytuje, ale budżety są małe.

**Ads Transparency [A]** (reklamy w dowolnym formacie, nie tylko na te frazy):
- Szukanie reklamodawcy po nazwie: „druk 3d” → 2 reklamodawców i 6 domen; „wydruk 3d” → 1 (9 reklam); „drukarnia 3d” → 0.
- Sprawdzone domeny (pełna lista w `-reklamodawcy.csv`):

| Domena | Typ firmy | Reklam w PL | Od | Aktywna 10.2026 |
|---|---|---|---|---|
| xometry.eu | platforma (DE) | ok. 200 (≥37 widocznych) | 10.2021 | tak |
| lasertrade.pl | laser + druk 3D, sp. z o.o. | 93 | 12.2022 | tak |
| cadxpert.pl | dystrybutor z usługą | ≥40 | ≤06.2026 | tak |
| send3d.eu | drukarnia online, JDG | 12 | 06.2024 | tak |
| druk3dkrakow.pl | pracownia, JDG | 13 | 06.2025 | tak |
| pddruk3d.pl | pracownia, JDG | 4 | 05.2026 | tak |
| craft3d.pl | studio, JDG | 6 | 03.2025 | nie (do 09.2026) |
| b3d.com.pl | dystrybutor z usługą | 7 | 10.2025 | nie (X–XII 2025) |
| wydruk3dxxl.pl, protodruk3d.pl | pracownie | 1–2 | 2025–2026 | nie (krótkie kampanie) |
| drukarex.pl, drukujemy3d.pl, order3d.pl | pracownie z SERP | 0 | | |
| oferteo.pl | katalog zapytań (wszystkie branże) | ok. 5 000 | | tak |

**Wnioski:**
- W październiku 2026 reklamuje się 6 podmiotów z branży: platforma Xometry, dystrybutor CadXpert, firma laserowa LaserTrade i 3 jednoosobowe pracownie (send3d.eu, druk3dkrakow.pl, pddruk3d.pl). Reszta próbuje krótko (1–3 miesiące) i odpada. Typowa pracownia z top 10 nie reklamuje się wcale.
- **Górna granica wartości zapytania z Ads:** CPC 1,12–1,70 USD × 3,90 zł = 4,4–6,6 zł za kliknięcie. Przy konwersji strony drukarni 5–10% (założenie) zapytanie z Ads kosztuje **44–133 zł**. Tyle zapłaci firma, która liczy, że zapytanie jest warte więcej niż koszt. Dla B2C (zlecenie 30–150 zł, sekcja 4) to za drogo i to tłumaczy, czemu małe pracownie nie reklamują się długo.

## 4. Wartość zlecenia [C][S]

Próbka 10 firm z ceną (bez telefonów i adresów; pełna tabela w `-ceny.csv`). 4 kolejne firmy nie publikują cennika albo strona go nie oddała.

| Firma (URL) | Usługa | Cena | Minimum |
|---|---|---|---|
| craft3d.pl/ceni (Warszawa) | FDM PLA/PET-G | 1,7 zł/g (do 500 g), 1,4 zł/g (do 1 kg), 1 zł/g (pow. 1 kg) | 50 zł |
| craft3d.pl/ceni | SLA / nylon / modelowanie | od 5 zł/cm³ / od 4 zł/g / 120 zł/h | 200 / 100 / 60 zł |
| order3d.pl/druk-3d-poznan-cennik | FDM / mSLA | 2,1–2,5 / 3–6 zł netto/cm³ | 300 / 400 zł netto |
| order3d.pl | CAD / skan / projekt ze skanu | 250 zł netto/h / od 500 / od 1 200 zł netto | CAD + druk min. 400 zł netto |
| elprodruk3d.pl/cennik-p-15 (Łódź) | FDM, czas drukarki | 11,50 zł netto/h (z projektem 18 zł/h) | nie podano |
| drukujemy3d.pl (cennik) | FDM | ok. 13–15 zł/h; 6 h, 60 g PETG = 80 zł netto; mały detal od 30 zł | 50 zł netto |
| rudnik3d.pl/druk-3d-cena-warszawa | FDM | prosta część od 30 zł, średnia 60–300 zł, figurka PLA 40 g 40–90 zł | 30 zł |
| geometryhustlers.pl (artykuł z 25.03.2026) | ta sama część: FDM / SLA / MJF / SLM | 35 / 65 / 120 / 300 zł netto; SLM 1 150–1 400 zł/szt.; figurka 60–120 zł netto | zależne od technologii |
| send3d.eu/wycena-online | kalkulator FDM/SLA/SLS | cena po wgraniu pliku; rabat 5–30% od 2 szt. | koszt startowy |
| innovar.pl/cennik | skanowanie małych detali | 299–750 zł netto; modelowanie techniczne 1 000–2 000 zł netto | |
| 3duv.pl (cena z SERP) | skanowanie | 150 zł/h | |
| v-slot.pl (cena z SERP) | FDM „wydruk na zamówienie” | 22,11 zł brutto (jednostka nieopisana) | |

Bez cennika: hexagongroup.pl, strefadruku3d.pl, b3d.com.pl (liczby niewidoczne dla parsera), laboratoriumdruku3d.pl (blokada antybotowa).

**Typowe zlecenie (moje odczytanie próbki):**
- **B2C** (figurka, uchwyt, część do domu): **30–150 zł**. Minima 30–60 zł (rudnik3d, craft3d, drukujemy3d).
- **B2B** (projekt CAD + druk, skan, krótka seria, SLS/SLA): **400–1 500 zł**. CAD + druk min. 400 zł netto (order3d), skan 299–750 zł netto (innovar), seria 25 szt. FDM 545 zł, SLA/MJF ok. 1 050–1 060 zł netto (geometryhustlers). Metal to tysiące złotych za sztukę.

**Ile drukarnia mogłaby zapłacić za zapytanie (założenie: 5–10% wartości zlecenia, przy założeniu, że firma wygrywa część zapytań):**
- B2C: **2–15 zł** (w rachunku 5 zł ostrożnie, 10 zł realnie).
- B2B: **20–150 zł** (w rachunku 40 zł i 80 zł). To mieści się w koszcie zapytania z Ads (44–133 zł).

## 5. Rachunek po 12 miesiącach

Szczegóły per klaster: `dane/uslugi-druku-popyt-rachunek.csv`; parametry: `-rachunek-podsumowanie.csv`. Model jak w `druk3d.md`: wolumen × udział intencji × CTR pozycji × mnożnik SERP × pokrycie fraz × konwersja formularza „wyślij plik do wyceny”.

| Parametr | Ostrożny | Realny |
|---|---|---|
| Pula fraz w modelu (9 klastrów, bez Allegro, platform, lasera i fraz ogólnych) | 34 745/mies. | 34 745/mies. |
| Udział intencji usługowej | 50% ceny/projekt/żywica, 60% B2B tech i skan, 100% reszta | j.w. |
| Pokrycie fraz stronami | 60% | 85% |
| Pozycje | 6–8 | 3–5 |
| Mnożnik SERP | ×0,7 AIO, ×0,6 Local Pack, ×0,8 B2B | j.w. |
| **Sesje/mies.** | **366** | **1 325** |
| Konwersja formularza | 1–4% | 3–7% |
| **Zapytania/mies.** | **ok. 10** (7 B2C, 3 B2B) | **ok. 68** (48 B2C, 21 B2B) |
| Cena zapytania B2C / B2B | 5 / 40 zł | 10 / 80 zł |
| Zapytania, za które ktoś płaci | 50% | 80% |
| Ile firm dostaje to samo zapytanie | 1 | 2 |
| **Przychód: opłata za zapytanie** | **ok. 80 zł/mies.** | **ok. 3 400 zł/mies.** (78% z B2B) |
| Alternatywa: abonament za wpis | 3 firmy × 49 zł = 147 zł/mies. | 15 firm × 99 zł = 1 485 zł/mies. |

Wszystko poza wolumenem, CTR poz. 1/5/10 (SEO Inc. 2025, https://seoinc.com/?p=9742) i cenami z sekcji 4 to założenia. Ceny abonamentu nie mają odniesienia: stawek Oferteo i Fixly dla firm nie sprawdziłem (wymagają konta). Sezon: w marcu ruch ok. 1,3× średniej, w czerwcu–sierpniu ok. 0,75× [W].

**Co to znaczy:**
- Wariant ostrożny nie pokrywa nawet kosztu narzędzi. Realny daje kwotę rzędu afiliacji z `druk3d.md` (1 860 zł), ale tylko pod warunkiem, że kilkanaście firm sama się zgłosi i zapłaci.
- Model stoi na B2B: 21 zapytań B2B daje 2 660 z 3 430 zł. B2B szuka jednak głównie przez nazwy technologii i dystrybutorów (CadXpert, B3D) i w tym segmencie stale reklamuje się Xometry.
- Dla właściciela praktyczniejszy jest **wariant hybrydowy**: strona „cennik druku 3D w Polsce z datą” (12 109/mies. pytań o cenę, AIO cytuje małe pracownie) z formularzem wysyłającym plik do kilku pracowni. Ruch z tej strony wspiera też serwis hobbystyczny z `druk3d.md`.

## 6. Pokrycie z niechcieznajda.pl

Mechanizm jest ten sam: firma płaci za zapytanie od klienta. Branża jest inna i nie konkuruje z fachowcami budowlanymi. Część zleceń (projekt i druk części zamiennych, makiety) może trafiać do tych samych małych warsztatów. Ocena, czy da się użyć tego samego kodu formularza i rozliczeń, należy do właściciela: nie znam stosu technicznego niechcieznajda.

## 7. Ograniczenia i czego nie sprawdzono

- Reklamy w SERP: jeden pomiar (18.10.2026 ok. 13:50). Ads Transparency pokazuje reklamy wszystkich formatów, nie per fraza.
- Stawki dla firm w Oferteo i Fixly, liczba zapytań w kategorii „druk 3D” w Oferteo (strona listingu zwróciła pustą treść w [C]).
- Grupy na Facebooku („Druk 3D Polska”) jako kanał zleceń: niemierzalne bez logowania.
- Konwersje formularza i strony drukarni: brak danych, wszystko to założenia.
- Kurs USD z wtórnego źródła (comparic.pl), bo API NBP jest zablokowane.
- Frazy prawne (licencje modeli, CE, broń) pominięte zgodnie z zasadami.

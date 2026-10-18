# Druk 3D w Polsce (hobbyści i mała produkcja): badanie tak/nie (18.10.2026)

Brief: `research/nisze/finalisci/BRIEF.md`. Wcześniejsza ocena: `research/nisze/A-technologia.md` (wynik 3,45).

**Oznaczenia źródeł (wszystko pobrane 18.10.2026):**
- **[W]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live` (location 2616, pl): średnia z 12 mies. (10.2025–09.2026), CPC w USD; trend r/r = lipiec–wrzesień 2026 wobec lipiec–wrzesień 2025.
- **[K]** odkrywanie fraz: `/v3/dataforseo_labs/google/keyword_suggestions/live` (ziarna: druk 3d, drukarka 3d, drukarki 3d, filament, petg, bambu lab, prusa, creality, elegoo, anycubic, wydruk 3d) plus ręczna lista problemów i narzędzi. `keyword_ideas/live` zwrócił śmieci („squishy allegro”), więc go odrzuciłem.
- **[S]** `/v3/serp/google/organic/live/advanced`, depth 10, desktop, z `load_async_ai_overview`.
- **[B-URL]** `/v3/backlinks/bulk_referring_domains/live` dla 155 konkretnych URL-i z top 10. **[B-D]** to samo dla 75 domen.
- **[WWW]** WebSearch albo `/v3/on_page/content_parsing/live` (adres podany przy liczbie).

Dane: `dane/druk3d-mapa.csv` (1034 frazy), `dane/druk3d-serp-top10.csv` (156 wyników), `dane/druk3d-serp-podsumowanie.csv` (20 SERP-ów), `dane/druk3d-programy.csv`, `dane/druk3d-rachunek.csv`, `dane/druk3d-encje-zrodla.csv`.

---

## Werdykt w skrócie

**WARUNKOWO. Wynik 3,2 / 5** (wcześniej 3,45).

1. **SERP jest słaby i to się potwierdziło na poziomie URL.** 152 ze 156 adresów w top 10 ma mniej niż 10 domen linkujących [B-URL]. Polska wiki bambulab.get3d.pl (12 domen linkujących do całej domeny [B-D]) stoi trzy razy w top 10 na „bambu lab a1” (18 100 [W]). Programatyczne strony versus.com zajmują 4 miejsca na „ile prądu zużywa drukarka 3d” [S]. AI Overview jest w 6 z 20 SERP-ów [S].
2. **Zarobek jest niski i niepotwierdzony.** Programy partnerskie producentów istnieją (Bambu Lab w Awin, Creality w Impact i Awin, Elegoo, Anycubic), ale żaden nie potwierdza dziś stawki dla wydawcy z Polski [WWW]. Rachunek po 12 mies.: **ok. 120 zł/mies. (ostrożny) i ok. 1 900 zł/mies. (realny)**.
3. **Popyt jest duży, ale skupiony na markach i sprzęcie.** 732 frazy, 492 330 wyszukiwań/mies., trend +29% r/r [W]. 55% wolumenu (271 200) to 18 fraz-głów ≥5 000 (marki, „drukarki 3d”, „długopis 3d”). Cały klaster „problemy i ustawienia” (stringing, warping, pierwsza warstwa, retrakcja) to tylko 3 070/mies. [W]. SERP-y sugerują, że rozwiązań szukają po angielsku, na Reddit, YouTube i w grupie FB „Druk 3D Polska” (wniosek z wyników, nie z pomiaru).

**Warunek „tak”:** właściciel akceptuje model afiliacyjny z sufitem rzędu kilku tysięcy zł/mies. w sezonie i zaloguje się do Impact/Awin/x-kom SalesMasters, żeby potwierdzić stawki i kwalifikację dla PL (ja nie mogę się rejestrować).

---

## 1. Mapa fraz [W][K]

- Pobrane: 1034 frazy. Do serwisu: **732 unikalne frazy, 492 330 wyszukiwań/mies.**; 150 to bliskie warianty (te same liczby, liczone raz); 189 wykluczonych.
- Wykluczenia: 78 wieloznacznych lub szerszych niż nisza (Tinkercad 110 000, FreeCAD, Fusion 360, „warping” 5 400, „flexi”, „stl”, „petg”, „prusa”), 42 B2B i przemysł (metal, SLS, medycyna), 33 nawigacyjne (makerworld 40 500, thingiverse 40 500, printables 27 100, Bambu Studio), 19 skanery 3D, 17 usług druku na zlecenie (lokalne pracownie).
- Trend r/r: **+28,9%** (lip.–wrz. 2026 wobec 2025). Sezon: najsłabszy 07.2026 (358 370), najsilniejszy 12.2025 (737 440), czyli 2× różnicy [W].
- CPC ważony: **0,43 USD** [W]. Najwyższe: „druk 3d na zamówienie” 1,44, „orcaslicer” 1,29, „makerworld” 1,26 (obie nawigacyjne).

| Typ strony | Frazy | Wolumen/mies. | Przykłady [W] |
|---|---|---|---|
| Encja | 370 | 266 800 | bambu lab a1 18 100, a1 mini 12 100, p2s 9 900, p1s 8 100, elegoo centauri carbon 2 900, anycubic kobra s1 2 900, prusa core one 2 400, creality k1c 1 900, filament pla 2 400, filament petg 1 600, filament tpu 1 300 |
| Hub | 21 | 121 540 | drukarki 3d 90 500, druk 3d 8 100, filament 8 100, filament do drukarki 3d 6 600 |
| Porównanie / ranking | 90 | 52 780 | długopis 3d 27 100, drukarki 3d cena 5 400, druk 3d dla dzieci 3 600, suszarka do filamentu 2 400, drukarki 3d ranking 720, petg vs pla 480 |
| Poradnik | 205 | 38 510 | projekt do drukarki 3d 2 400, rzeczy z drukarki 3d 1 600, retrakcja 880 (wieloznaczna), co można wydrukować na drukarce 3d 480 |
| Narzędzie | 46 | 12 700 | druk 3d ceny 5 400, ile kosztuje druk 3d 4 400, kalkulator druku 3d 260, ile kosztuje filament do drukarki 3d 210, ile prądu zużywa drukarka 3d 110 |

**Ważne liczby dla decyzji:**
- Problemy po polsku są prawie zerowe: „stringing” 110, „nitkowanie druk 3d” 30, „pierwsza warstwa” 20, „wydruk odkleja się od stołu” 20, „warping druk 3d” 0, „zapchana dysza” 0 [W].
- Narzędzia są małe: „kalkulator druku 3d” 260, „ile prądu zużywa drukarka 3d” 110, „kalkulator filamentu” 20, „ile metrów filamentu w 1kg” 0 [W]. Duże „ile kosztuje druk 3d” (4 400) i „druk 3d ceny” (5 400) to w praktyce ludzie, którzy chcą zlecić wydruk.
- Encje mają popyt: modele drukarek i filamenty to 300 tys. wyszukiwań/mies. [W].

## 2. Dwadzieścia SERP-ów [S][B-URL][B-D]

Pełne dane: `dane/druk3d-serp-top10.csv`, podsumowanie: `dane/druk3d-serp-podsumowanie.csv`.

| Fraza | Wol. [W] | AIO | Mediana dom. link. (domena) | Wyniki z domen <300 dom. link. | Fora/social/wideo | Sprzed 2023 | Kto wygrywa |
|---|---|---|---|---|---|---|---|
| bambu lab a1 | 18 100 | nie | 161 | 5 | 0 | 0 | sklepy (edutech, 3dprima, x-kom, get3d), ceneo, wiki PL bambulab.get3d.pl ×3 |
| bambu lab p1s | 8 100 | nie | 1 783 | 3 | 1 | 0 | sklep Bambu EU, botland, x3dshop, neonet, reddit (2023), wiki PL, blog edutech „P1S vs P2S” (02.2026) |
| prusa core one | 2 400 | nie | 2 562 | 2 | 0 | 0 | prusa3d.com ×2, botland, global3d, blackfrog, help.prusa3d.com, rosa3d, ceneo |
| creality k1c | 1 900 | nie | 7 821 | 0 | 3 | 0 | center3dprint, ceneo, Media Expert, reddit ×2, 3dprima, creality.com, botland, PDF instrukcji |
| elegoo centauri carbon | 2 900 | nie | 5 130 | 2 | 2 | 0 | x-kom, drukmistrz, 3djake, Media Expert, reddit, ithardware (test 02.2025), grupa FB, botland |
| anycubic kobra s1 | 2 900 | nie | 92 | 3 | 0 | 0 | anycubicofficial.pl ×3, Media Expert (tylko 4 wyniki organiczne) |
| filament petg | 1 600 | nie | 727 | 5 | 0 | 2 | rosa3d, botland, spectrumfilaments, allegro, 3djake, marwiol, blog botland (2020), x3dshop, get3d (2020), forbot |
| filament tpu | 1 300 | nie | 96 | 5 | 0 | 1 | get3d, filament24, wiki PL, 3d-innowacje, zadar (2021), redraft3d |
| filament do drukarki 3d | 6 600 | nie | 745 | 4 | 1 | 1 | rosa3d, filament3d, botland, f3dfilament, 3djake, techlord, 3duv, dodrukarki (2022), YouTube |
| drukarka 3d dla dzieci | 3 600 | nie | 59 003 | 0 | 3 | 0 | botland, allegro, reddit, eisystem, FB ×2, meshy.ai |
| drukarka 3d dla początkujących | 720 | nie | 3 521 | 2 | 2 | 1 | 3djake, YouTube (2023), reddit, botland (2021), skapiec, xd3d.pl |
| drukarki 3d ranking | 720 | nie | 1 206 | 4 | 4 | 0 | drukarki.pl, forbot forum ×2, 3djake, YouTube, b3d, reddit, morele (04.2026), 3dwpraktyce (01.2026) |
| suszarka do filamentu | 2 400 | nie | 288 | 5 | 2 | 1 | global3d, zadar (2022), reddit ×2, pro3ds, blog botland, xam, 3dtuning, 3dwpraktyce |
| długopis 3d | 27 100 | nie | 2 503 | 2 | 2 | 0 | blog botland, morele, prorankingi.pl (ranking afiliacyjny, 10.2026), YouTube, Pinterest, 3drukarki, xam |
| ile kosztuje druk 3d | 4 400 | tak | 949 | 3 | 2 | 1 | v-slot (usługa), get3d, **pcmod.pl (kalkulator)**, peaklayer3d, YouTube (2021), reddit, allegro, duplicart3d, send3d |
| kalkulator druku 3d | 260 | tak | 1 617 535* | 2 | 4 | 0 | b3d (wycena usługi), reddit ×2, Google Play, FB, meshy.ai, v-slot, TikTok, soltech360.pl |
| ile prądu zużywa drukarka 3d | 110 | tak | 14 377 | 2 | 1 | 2 | blog botland (2022), reddit (2020), **versus.com ×4** (strony encji), global3d (EN), kosztpradu.pl |
| retrakcja | 880 | tak | 861 428* | 1 | 3 | 3 | SERP zdominowany przez fizjoterapię i matematykę; z druku 3D tylko reddit r/klippers |
| stringing | 110 | tak | 52 923 | 2 | 3 | 1 | reddit, snapmaker (EN), sunlu (EN), słownik Cambridge, 3dnatives (EN) |
| petg vs pla | 480 | tak | 79 | 4 | 2 | 1 | blog filament24, zaccord (węgierski!), YouTube, grupa FB, worknplay, ir.edu.pl, biobasefilm |

\* mediana zawyżona przez reddit/YouTube/Wikipedię w małej liczbie wyników.

**Wnioski:**
- **Kryterium briefu** (≥2 URL-e z <10 domenami linkującymi albo fora/PDF/stare treści) spełnia **20 z 20** SERP-ów. Kryterium na poziomie URL nie rozróżnia fraz: indeks DataForSEO widzi linki głównie do stron głównych, więc mediana dla URL-i to 0. Dlatego dodałem ścislejszy test na poziomie domeny (≥2 wyniki z domen <300 domen linkujących albo ≥2 fora/stare): też **20 z 20**.
- **Encje (drukarki):** wygrywają sklepy i producenci, a Google dokłada karuzelę produktów z cenami. Strona informacyjna wchodzi (bambulab.get3d.pl, blog edutech, ithardware), ale walczy z intencją zakupową. Wideo z YouTube jest w karuzeli w 5 z 6 SERP-ów modeli.
- **Encje (filamenty):** wygrywają polscy producenci i sklepy (Rosa3D, Spectrum, Botland), plus stare wpisy blogowe z 2020–2022. Brak dobrej strony „PETG: temperatury, suszenie, marki, ceny z datą”.
- **Problemy:** po polsku wygrywają fora (reddit) i anglojęzyczne strony producentów. „retrakcja” i „stringing” są wieloznaczne. Ten dział ma sens tylko jako wsparcie encji, nie jako źródło ruchu.
- **Narzędzia:** AIO na „kalkulator druku 3d” wymienia z nazwy darmowe kalkulatory: pcmod.pl, 3dprintingcostcalculator.com, blog.prusa3d.com, omnicalculator.com [S]. Mały serwis może tam trafić, ale rynek kalkulatorów jest zajęty i darmowy.
- **AIO** w 6 z 20 SERP-ów, wyłącznie na frazach informacyjnych (koszt, kalkulator, prąd, retrakcja, stringing, petg vs pla). Cytuje małe serwisy w 4 z 6 (pcmod.pl, 3dwpraktyce.pl z 2015, centrumdruku3d.pl, 3lian.pl, zadar.pl, techtutor.pl). Na encjach i rankingach AIO nie ma.
- **Ile fraz realnie weźmie nowa domena w 6–12 mies.:** wg kryterium wszystkie testowane typy. Po odjęciu 18 fraz-głów ≥5 000 (sklepy i producenci w top 3) zostaje **714 fraz i 221 130 wyszukiwań/mies.** To jest pula „do wzięcia” w wariancie ostrożnym. Wariant realny dolicza dalsze pozycje na głowach.

## 3. Zarobek (potwierdzony u źródła tam, gdzie się dało)

### Programy partnerskie (`dane/druk3d-programy.csv`)

| Program | Sieć | Prowizja | Cookie | PL | Źródło |
|---|---|---|---|---|---|
| Bambu Lab | Awin (profil 46345), umowa z Bambulab USA Inc | różne stawki na drukarki, filamenty, płyty; % nie podano | 15 dni | niepotwierdzone | https://ui.awin.com/merchant-profile/46345 [WWW] |
| Creality | Impact (zalecany) i Awin | na stronie bez %, „progi wydajności”, wypłaty miesięczne | brak na stronie | niepotwierdzone | https://www.creality.com/pages/affiliate-program [content_parsing] |
| Elegoo | ShareASale lub Impact | 5%+ (strona programu, wersja JP) | brak | niepotwierdzone | https://www.elegoo.com/en-jp/pages/elegoo-affiliate [WWW] |
| Anycubic | Impact / Awin ES / Webgains | od 5% (AU), Awin ES 5% | 30–60 dni | niepotwierdzone; istnieje sklep anycubicofficial.pl | https://anycubic.au/pages/affiliate-program [WWW] |
| Prusa Research | umowa bezpośrednia | nie znaleziono | — | niepotwierdzone | https://help.prusa3d.com/es/article/p2p-programa-de-recompensas-de-la-comunidad-de-prusa-a-prusa_670212 [WWW] |
| 3DJake | Awin | nie podano (affi.io: 7,5% DE, niepotwierdzone) | — | nie dla 3djake.pl | https://www.3djake.ch/en-CH/info/affiliate-program [WWW] |
| x-kom | SalesMasters (własny) / Admitad | „nawet kilkanaście procent” zależnie od kategorii | Admitad 1 dzień | tak | https://www.x-kom.pl/poradniki/4820-salesmasters-sposob-na-zarabianie-w-internecie.html [WWW] |
| Allegro | Allegro Share | 1,67% w punktach (źródło wtórne); Allegro Polecam zamknięty | 24 h | tak, status niepotwierdzony | https://antyweb.pl/allegro-share [WWW] |
| Amazon.pl | Partnerzy Amazon | wg kategorii, tabeli PL nie znaleziono | 24 h (wtórne) | tak | https://crevio.co/pl/blog/amazon-affiliate [WWW] |
| Botland, Spectrum, Fiberlogy, Devil Design, Rosa3D | — | programów nie znaleziono | — | — | WebSearch |

Ceneo, Media Expert, Morele: nie sprawdzono.

### Reklamy

RPM display dla PL: **brak wiarygodnego źródła**. W rachunku przyjmuję 5 i 10 zł na 1000 odsłon jako założenie. CPC ważony 0,43 USD [W] wskazuje na niską wartość reklam.

### Porównywarka cen filamentów

Da się ją zbudować technicznie (ceny ze źródłem i datą), ale:
- SERP „filament petg” ma już Allegro z karuzelą cen (30–61 zł za 1 kg [S]) i sklepy producentów;
- źródło cen z datą to np. DataForSEO Merchant (Google Shopping); **kosztu i pokrycia polskich sklepów nie sprawdziłem**;
- bez programu partnerskiego polskich producentów filamentów (nie znaleziono) porównywarka nie zarabia na kliknięciach.
Ocena: dodatek do encji filamentów („cena z dnia X w sklepie Y”), nie osobny produkt.

### Własny produkt

- Płatny kalkulator wyceny dla małych pracowni: słaby. Darmowe kalkulatory stoją w SERP i w AIO (pcmod.pl, Prusa, Omni, meshy.ai).
- Płatne profile druku: słaby. Profile są darmowe w MakerWorld i Printables, a Bambu i Prusa płacą twórcom za modele w swoich serwisach (punkty, vouchery) [WWW].
- PDF „pierwsze 30 dni z drukarką”: popytu nie sprawdziłem.
- Ogłoszenia płatne przez sklepy: wymaga kontaktu z firmami, czyli poza zasadami.

### Wybór modelu

- **Główny: afiliacja sprzętu i filamentów** przez Impact/Awin (Creality, Elegoo, Anycubic, Bambu Lab) i polski sklep (x-kom SalesMasters). Uzasadnienie: 54% wolumenu to encje (drukarki, akcesoria, filamenty) z intencją zakupową, a rankingi i porównania mają słaby SERP. Ryzyko: żaden program nie potwierdza dziś stawki dla PL.
- **Dodatkowy: reklamy display** od ok. 10 tys. sesji/mies., głównie w sezonie XI–I.

## 4. Rachunek po 12 miesiącach (`dane/druk3d-rachunek.csv`)

Ruch = wolumen fraz × CTR pozycji × pokrycie fraz stronami. Krzywa CTR: SEO Inc. 2025 (poz. 1 = 28,5%, poz. 5 = 6,1%, poz. 10 = 1,4%; https://seoinc.com/?p=9742); pozycje pośrednie to moja interpolacja (założenie). Na typach z AIO mnożnik ×0,7 (założenie wg GrowthSRC 2025: spadek CTR poz. 1 z 28% do 19%).

| Parametr | Ostrożny | Realny |
|---|---|---|
| Pokrycie fraz stronami | 60% | 85% |
| Pozycja: głowy ≥5 000 | poza top 10 | 8–10 |
| Pozycja: encje / rankingi / poradniki / narzędzia | 8 / 6 / 5 / 5 | 5 / 4 / 3 / 3 |
| **Sesje/mies.** | **4 110** | **17 157** |
| w tym encje | 2 202 | 10 162 |
| Klik do sklepu (encja 8%, ranking 12%, poradnik/narzędzie 2%, hub 3%) | 268 | 1 174 |
| Konwersja w sklepie | 2% | 3% |
| Średnie zamówienie | 600 zł | 900 zł |
| Prowizja | 3% | 5% |
| **Afiliacja** | **96 zł/mies.** | **1 585 zł/mies.** |
| Reklamy (RPM 5 / 10 zł, 1,3 / 1,6 odsłony na sesję) | 27 zł | 275 zł |
| **Razem** | **ok. 120 zł/mies.** | **ok. 1 860 zł/mies.** |

Wszystkie wiersze poza wolumenem i CTR poz. 1/5/10 to założenia. Ceny do średniego zamówienia (z SERP 18.10.2026): Bambu Lab P1S 1 655,72 zł (eu.store.bambulab.com), Elegoo Centauri Carbon 1 369 zł (x-kom.pl), Creality K1C 1 299,99 zł (mediaexpert.pl), filament PETG 30–61 zł (allegro.pl) [S]. W grudniu ruch będzie ok. 1,5× średniej, w lipcu ok. 0,75× [W].

## 5. Dane do stron encji (`dane/druk3d-encje-zrodla.csv`)

- **Drukarki:** brak otwartego zbioru. Specyfikacje trzeba zbierać z kart producentów (Bambu Lab, Prusa, Creality, Elegoo, Anycubic, Flashforge, Qidi, Snapmaker). Licencji na zbiór nie ma. Same fakty techniczne (pole robocze, temperatury, moc) zapisujemy własnymi słowami z linkiem do karty; masowe kopiowanie całych tabel to ryzyko prawne (prawo do bazy danych). To kwestia do decyzji właściciela, nie temat na stronę.
- **Liczba encji:** 25 drukarek na start, 60 po 6 mies.; 15 materiałów; 15 marek filamentów po 6 mies.; 5–8 slicerów.
- **Praca ręczna:** ok. 1–1,5 h na model drukarki (20–25 pól) → 30–40 h na start; ok. 2 h na materiał (zakresy z 3–5 kart TDS) → ok. 30 h.
- **Aktualizacja:** premiery 1–2 modeli/mies. (w 2025–2026 doszły m.in. P2S, H2C, X2D, Centauri Carbon 2, Kobra S1, Kobra X, Snapmaker U1 6 600/mies. [W]); ceny co tydzień, jeśli je pokazujemy.
- **Wikidata:** dane strukturalne na CC0 (https://www.wikidata.org/wiki/Wikidata:Licensing, przez WebSearch). **Nie sprawdziłem**, ile modeli drukarek ma tam elementy: SPARQL (query.wikidata.org) jest zablokowany przez proxy.
- **Sygnał z SERP:** versus.com rankuje stronami „zużycie energii | model” na 4 pozycjach [S]. Strona encji z mocą znamionową i kosztem prądu na model ma więc sens.

## 6. Szkic serwisu

**Działy i liczba stron:**

| Dział | Start | Po 6 mies. |
|---|---|---|
| Huby (drukarki, filamenty, koszty i prąd, problemy i ustawienia, slicery i pliki, pomysły na wydruki) | 6 | 6 |
| Encje: drukarki | 25 | 60 |
| Encje: filamenty (materiały, potem marki) | 15 | 30 |
| Porównania (A1 vs A1 mini, P1S vs P2S, A1 vs P1S, K1C vs A1, Centauri Carbon vs P1S, Core One vs P1S, PLA vs PETG, PETG vs ABS, ASA vs ABS, Orca vs Bambu Studio) | 10 | 30 |
| Rankingi (dla początkujących, do 1000/1500/2000 zł, dla dzieci, suszarki do filamentu, długopisy 3D) | 5 | 10 |
| Poradniki | 15 | 40 |
| Narzędzia | 4 | 5 |

**Narzędzia:**
1. Kalkulator kosztu wydruku (gramy filamentu, cena szpuli, czas, moc drukarki, cena prądu, amortyzacja, marża).
2. Koszt prądu dla wybranego modelu (moc z bazy encji).
3. Przelicznik długość ↔ waga filamentu (gęstość materiału z kart TDS).
4. Dobór temperatur dysza/stół dla materiału i marki (z kart producentów, z datą).
5. Po 6 mies.: porównywarka drukarek (pole robocze, obudowa, wielokolor, cena ze źródłem i datą).

**Pierwszy klaster i termin:** szczyt to XII (737 440), potem I (622 260) [W]. Nowa domena nie złapie sezonu 2026, więc:
- **10.2026–01.2027:** klaster „pierwsza drukarka i pierwszy filament” (rankingi dla początkujących i do kwoty, 10 encji Bambu/Creality/Elegoo/Anycubic, PLA/PETG/TPU, kalkulator kosztu). Styczeń 2027 łapie osoby, które dostały drukarkę na święta.
- **do 30.09.2027:** pełna baza encji i rankingi prezentowe na sezon XI–XII 2027.

**Pomysły na nazwę i domenę (dostępności nie sprawdzałem):** Pierwsza Warstwa (pierwszawarstwa.pl), Filamentownia (filamentownia.pl), Drukarnik (drukarnik.pl), Dysza i Stół (dyszaistol.pl).

## 7. Ryzyka

- **AIO:** 6 z 20 SERP-ów, tylko na frazach informacyjnych. Encje i rankingi bez AIO [S].
- **Sezonowość:** XII jest 2× mocniejszy od VII [W]. Przychód afiliacyjny skupi się w XI–I.
- **Zależność od programów:** frazy z „bambu” to 59% wolumenu klastra drukarek i akcesoriów (135 300 z 228 110/mies.; same bambu lab, a1, a1 mini, p2s, p1s, a1 combo to 38,5%) [W], a jego program w Awin nie podaje stawki i nie potwierdza PL. Creality i Elegoo zmieniają sieci (Impact, Awin, ShareASale).
- **Marki i premiery:** popyt szybko przechodzi na nowe modele („creality k1” spadł z 3 600 w 12.2024 do 880 w 09.2026; „prusa mk4” z 2 400 do 590 [W]). Baza encji wymaga stałej pracy.
- **Sklepy jako konkurencja:** Botland, x-kom, 3DJake, Media Expert, Ceneo mają własne blogi i rankingi.

### Omijamy (tematy prawne i pokrewne; autorzy ich nie ruszają)

- licencje modeli 3D (CC BY-NC, prawo do sprzedaży wydruków z cudzych projektów, prawa autorskie i znaki towarowe postaci na figurkach);
- broń i elementy broni z drukarki 3D (w danych są frazy „pistolet z drukarki 3d”, „karambit z drukarki 3d”, „nóż motylkowy z drukarki 3d”, „broń z drukarki 3d”: usunięte);
- podatki, działalność gospodarcza i rejestracja przy sprzedaży wydruków („zarabianie na druku 3d” tylko jako pomysły na wydruki, bez spraw formalnych);
- bezpieczeństwo produktów na sprzedaż: oznakowanie CE, zabawki dla dzieci, kontakt z żywnością (atesty);
- gwarancja, rękojmia, zwroty, cło i import z AliExpress/Temu;
- zdrowie: opary i cząstki z drukarki (YMYL) – do decyzji właściciela; jeśli tak, tylko fakty z badań z datą;
- druk 3D w medycynie i stomatologii;
- wzory umów na usługi druku.

## 8. Ocena wg `METODA.md`

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 4 | 492 330/mies., +29% r/r; minus: problemy i narzędzia po polsku małe |
| Słabość SERP | 25% | 4 | 20/20 SERP-ów spełnia kryterium; małe serwisy i fora w top 10; minus: karuzele produktów i YouTube na encjach |
| Zarobek | 25% | 2 | programy istnieją, stawki dla PL niepotwierdzone; 120–1 860 zł/mies. po 12 mies. |
| Fosa danych / narzędzia | 15% | 2 | bazę trzeba budować ręcznie (60–70 h na start); darmowe kalkulatory już są |
| Niskie ryzyko | 15% | 4 | mało treści prawnych, AIO 6/20; minus: sezon i zależność od Bambu Lab |
| **Wynik ważony** | | **3,2** | |

## Czego nie sprawdzono

- Stawek i kwalifikacji PL w panelach Awin/Impact/ShareASale/Admitad (wymaga rejestracji).
- Programów Ceneo, Media Expert, Morele, anycubicofficial.pl.
- Kosztu i pokrycia DataForSEO Merchant (ceny filamentów).
- Reklamodawców w Google Ads (`ads_advertisers`).
- Liczby modeli drukarek w Wikidata (proxy blokuje SPARQL).
- RPM dla PL (brak wiarygodnego źródła).

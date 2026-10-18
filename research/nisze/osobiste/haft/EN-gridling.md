# Haft krzyżykowy po angielsku: czy serwis treściowy zbuduje ruch do Gridlinga (badanie z 18.10.2026)

Metoda: `research/nisze/METODA.md`, z rynkami USA (`location_code` 2840), Wielka Brytania (2826), Kanada (2124) i Australia (2036), `language_code` "en". Punkt odniesienia: temat T3 w `research/nisze/osobiste/F-z-czatow.md` (Polska, 22 498 wyszukań/mies., wynik 3,75). Wszystkie liczby pobrano 18.10.2026.

**Skróty źródeł:**

- **[SV]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live`, 95 fraz × 4 rynki, X.2024–IX.2026. Średnia to X.2025–IX.2026. Trend r/r: suma VII–IX 2026 wobec VII–IX 2025. Google Ads łączy bliskie warianty (np. „photo to cross stitch pattern” = „cross stitch pattern from photo”), więc duplikaty o identycznym przebiegu liczę raz.
- **[KS]** DataForSEO `/v3/dataforseo_labs/google/keyword_suggestions/live` (seed „cross stitch”, US i UK, po 1 000 fraz) oraz `keyword_ideas/live` (5 seedów, US).
- **[SERP]** DataForSEO `/v3/serp/google/organic/live/advanced`, desktop, depth 10, z AI Overview, 14 fraz (12 US, 2 UK), 111 wyników organicznych.
- **[BL]** DataForSEO `/v3/backlinks/bulk_referring_domains/live` dla 104 URL-i i 63 domen; `/v3/backlinks/summary/live` dla stitchmate.app.
- **[TE]** DataForSEO `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (US, etv = szacowane wizyty organiczne/mies.) i `domain_rank_overview/live`.
- **[ADS]** DataForSEO `/v3/serp/google/ads_advertisers/live/advanced` i `ads_search/live/advanced` (Google Ads Transparency, US).
- **[CP]** DataForSEO `/v3/on_page/content_parsing/live` (strona odczytana). **[WS]** WebSearch (fragmenty wyników, strony nieodczytane; WebFetch i curl są blokowane przez proxy).
- **[TV]** TradingView `FX_IDC:EURUSD` = 1,12368.

Dane: `dane/EN-wolumeny.csv` (95 fraz × 4 rynki, 24 mies.), `dane/EN-popyt-podsumowanie.csv`, `dane/EN-sugestie.csv` (klastry z [KS]), `dane/EN-serp-top10.csv`, `dane/EN-serp-podsumowanie.csv`, `dane/EN-konkurencja.csv`, `dane/EN-reklamy.csv`, `dane/EN-rachunek.csv`. Skrypty i surowe odpowiedzi API: `/tmp/claude-0/-home-user/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/haft-2/`.

## Werdykt

**TAK, pod warunkiem że treści i narzędzia powstaną na domenie Gridlinga (podkatalog), a nie jako osobny serwis.** Rynek anglojęzyczny jest 12,7 razy większy od polskiego w porównywalnym koszyku fraz, a intencji „zrób mi wzór ze zdjęcia” jest w nim około 1 450 razy więcej (30 476 wobec ok. 21 wyszukań/mies.). Najmocniejszy dowód, że to działa, to **stitchmate.app**: jednoosobowe narzędzie z tym samym modelem co Gridling (7,99 USD za PDF), pierwszy raz zauważone w indeksie linków 2.01.2026, ma dziś 62 domeny linkujące, 1 922 frazy w Google US i ok. 2 108 wizyt organicznych/mies. [BL, TE, CP]. Jest w top 10 w 6 z 14 badanych SERP-ów. To jednocześnie najgroźniejszy konkurent Gridlinga.

Słabe strony: pojedynczy wzór za 4,99 EUR słabo zarabia, reklama w Google się nie zwraca (próg opłacalności ok. 28% konwersji kliknięcia), a AI Overview jest w 12 z 14 SERP-ów. Rachunek po 12 miesiącach: ok. 30 EUR/mies. w wariancie ostrożnym i ok. 450 EUR/mies. w realnym (sam EN, brutto, założenia niżej).

## Ocena (wagi z METODA.md)

| Kryterium | Waga | EN dla Gridlinga | PL T3 (z F) | Uzasadnienie EN |
|---|---|---|---|---|
| Popyt i trend | 20% | 5 | 4 | 488 608 wyszukań/mies. w rdzeniu (4 rynki, bez technik sąsiednich), intencja Gridlinga 30 476, trend r/r +3% do +25% zależnie od rynku [SV] |
| Słabość SERP | 25% | 3 | 4 | Generatory i sklepy mają po ok. 2 000 domen linkujących, ale 61 ze 104 URL-i ma 0 linków, a nowy stitchmate.app (62 domeny) wszedł w 9,5 mies. [SERP, BL] |
| Zarobek | 25% | 3 | 3 | Własny produkt z intencją zakupu; niska cena wzoru, CPC 0,38–2,51 USD, reklama nieopłacalna [SV, ADS] |
| Fosa danych / narzędzia | 15% | 3 | 4 | Kalkulatory i tabele DMC już robią stitchmate, thread-bare, 123stitch; brak danych na wyłączność |
| Niskie ryzyko | 15% | 4 | 4 | Bez YMYL; ryzyka: AIO 12/14, prawa autorskie do wzorów, szczyt w XI–I |
| **Wynik ważony** | | **3,55** | 3,75 | |

PL T3 ma wyższy wynik, ale tylko dlatego, że jego SERP jest słabszy. Zarobek w PL wymaga polskiej wersji Gridlinga, której nie ma, a popyt na samo „wzór ze zdjęcia” jest w PL bliski zera.

## 1. Popyt

### Grupy fraz, cztery rynki [SV]

Średnia miesięczna X.2025–IX.2026, po usunięciu duplikatów Google Ads. Trend r/r = VII–IX 2026 wobec VII–IX 2025.

| Grupa | US | UK | CA | AU | Trend r/r US | Szczyt / dołek US | CPC ważony US |
|---|---|---|---|---|---|---|---|
| 1. Zdjęcie → wzór, generatory, aplikacje (18 fraz) | 21 180 | 4 553 | 3 047 | 1 696 | +9,2% | I.2026 (26 280) / X.2025 (18 270) | 0,69 |
| 2. Wzory (darmowe, tematyczne) | 51 776 | 8 735 | 6 992 | 3 533 | −15,9% | I.2026 / VI.2026 | 0,47 |
| 3. Nauka, ściegi, zestawy | 89 404 | 25 748 | 9 153 | 12 955 | −17,8% | XI.2025 / V.2026 | 1,75 |
| 4. Materiały i kalkulatory (DMC, Anchor, aida) | 49 468 | 5 228 | 4 832 | 3 443 | −22,8% | XII.2025 / IX.2026 | 0,46 |
| 5. Marki narzędzi (Stitch Fiddle, FlossCross, Pattern Keeper…) | 59 758 | 12 259 | 8 010 | 4 738 | +22,9% | I.2026 / VI.2026 | 1,53 |
| 0. „cross stitch” | 66 833 | 18 917 | 9 725 | 6 625 | +14,4% | XII.2025 / VI.2026 | 0,44 |
| **Rdzeń razem (0–5)** | **338 419** | **75 440** | **41 759** | **32 990** | −4,7% | XII.2025 / VI.2026 | 1,00 |
| 6. Sąsiednie „photo to …” (diamond painting, paint by numbers, perler, pixel art, crochet, LEGO) | 168 409 | 20 872 | 22 982 | 7 859 | −2,1% | I.2026 / V.2026 | 1,27 |

Trend r/r w UK, CA i AU jest lepszy niż w USA: rdzeń UK +2,8%, CA +25,1%, AU +19,7%.

### Porównanie z Polską

| Miara | PL (F, T3) | EN: US | EN: US+UK+CA+AU | Krotność |
|---|---|---|---|---|
| Koszyk 13 odpowiedników fraz T3 (haft krzyżykowy→cross stitch, mulina→embroidery floss, kanwa→aida cloth, wzory, zestawy, dla początkujących, DMC, ze zdjęcia, program…) | 22 498 | 199 907 | 286 671 | ×8,9 / ×12,7 |
| Intencja Gridlinga: wzór ze zdjęcia, generator, aplikacja | ok. 21 („wzór haftu krzyżykowego ze zdjęcia” 11, „program do tworzenia wzorów…” 10) | 21 180 | 30 476 | ok. ×1 450 |
| W tym ściśle „ze zdjęcia / na zamówienie” (8 fraz) | ok. 11 | 2 882 | b.d. | ok. ×260 |

Wniosek: w Polsce serwis musiałby sprzedawać Gridlinga ludziom, którzy szukają muliny i kanwy. W krajach anglojęzycznych ludzie sami szukają generatora.

### Największe frazy pod Gridlinga (US, średnia/mies., CPC USD) [SV]

| Fraza | US | UK | CPC US | Trend r/r US (VII–IX) |
|---|---|---|---|---|
| cross stitch pattern maker (= creator, chart maker) | 11 817 | 2 400 | 0,58 | 34 100 → 36 300 |
| free cross stitch pattern maker | 1 575 | 328 | 0,13 | 3 300 → 4 500 |
| custom cross stitch pattern (= personalized) | 1 135 | 168 | 1,69 | 2 760 → 3 300 |
| cross stitch app | 1 013 | 114 | 1,25 | 1 770 → 2 320 |
| cross stitch generator / pattern generator | 897 / 892 | 172 / 164 | 0,53 / 0,38 | 2 480 → 2 640 / 2 160 → 2 760 |
| make your own cross stitch pattern | 658 | 168 | 0,68 | 1 770 → 2 030 |
| cross stitch pattern from photo (= photo to / picture to) | 573 | 188 | 1,01 | 1 260 → 1 660 |
| photo to cross stitch | 444 | 275 | 1,55 | 1 790 → 1 550 |
| custom cross stitch pattern from photo | 170 | 48 | 2,51 | 450 → 610 |

Sezon: „custom cross stitch pattern” ma szczyt w XI.2025 (1 900) i dołek w VI.2026 (880), czyli ×2,2. To sezon prezentowy z planu marketingu. Generatory mają szczyt w styczniu (14 800).

### Narzędzia i materiały (US / UK) [SV]

- „cross stitch calculator” 5 433 / 474, „cross stitch fabric calculator” 1 475 / 249, „cross stitch size calculator” 622 / 102 (CPC 0,04–0,05 USD). [KS] dodaje klaster „counted cross stitch calculator” 5 400 i „cross stitch material calculator” 1 600.
- „dmc color chart” 5 300 / 770; „dmc floss” 4 550; „aida cloth” 3 875 / 1 000; „14 / 16 / 18 count aida” 834 / 638 / 693; „aida count” 548.
- Konwersja nici: „dmc to anchor conversion” 137 / **492**, „anchor to dmc conversion chart” 335 / **429**. To temat brytyjski (Anchor to marka Coats, popularna w UK).
- „how much floss do i need” 0 i „cross stitch floss calculator” 64. Kalkulator ilości muliny nie ma osobnego popytu; lepiej działa jako funkcja w PDF Gridlinga i w kalkulatorze tkaniny.
- „pattern keeper” 3 467 (r/r 6 400 → 9 200), „pattern keeper app” 733 (CPC 5,54). Zgodność z Pattern Keeper to wyróżnik Gridlinga i rosnący temat.
- Ściegi: „backstitch” 16 000 (CPC 6,75 USD, prawdopodobnie część wyszukań dotyczy marki odzieżowej), „french knot” 7 008 (w AU 4 900, możliwe znaczenie fryzjerskie), „half stitch cross stitch” 1 035, „quarter stitch” 189.

### Marki narzędzi (US) [SV]

stitch fiddle 45 917 (r/r +22%), flosscross 5 833 (13 200 → 19 800), pic2pat 1 390 (4 800 → 3 180), winstitch 823, macstitch 621, kg chart 351, pcstitch 288, thread bare 48. Rośnie FlossCross i Pattern Keeper, maleją stare programy desktopowe.

### Sąsiednie techniki „photo to …” (US) [SV]

diamond painting 102 542, perler bead patterns 27 283, custom paint by numbers 7 625 (CPC 4,33), lego mosaic maker 7 283, pixel art generator 6 525 (CPC 4,27), custom diamond painting 5 308 (CPC 2,99), photo to pixel art 4 925 (CPC 4,91; r/r 38 100 → 11 600), crochet graph generator 1 850. Te tematy mają wyższe CPC niż haft. To kierunek rozwoju samego Gridlinga (silnik ten sam), na start poza serwisem.

### Spadki i anomalie

„cross stitch kits” 148 100 → 87 300 (−41%), „embroidery floss” 78 300 → 42 800 (−45%), „cross stitch patterns” −18% [SV]. Hobby jako całość w USA słabnie, a narzędzia rosną. „cross stitch patterns for beginners” spada z 15 600 do 3 000, co wygląda na zmianę grupowania wariantów w Google Ads.

### Tematy z rozszerzenia [KS]

Nowe klastry o sensownym wolumenie (US): „needlepoint vs cross stitch” 12 100, „embroidery vs cross stitch” 4 400, „cross stitch font / text generator” 1 300 (CPC 1,93), „qr code cross stitch” 3 600, „cross stitch graph paper” 1 300, „christmas stocking cross stitch” 2 400, „bookmark cross stitch pattern” 1 300, „wedding cross stitch patterns” 1 000, „pokemon cross stitch” 1 300 (odpada: cudza własność). Wolumeny w [KS] są klastrowane, więc ich nie sumuję.

## 2. SERP: kto wygrywa i gdzie wejdzie mała domena

14 SERP-ów, 111 wyników organicznych [SERP], linki [BL].

| Fraza (rynek) | Kto prowadzi | Mała domena (<100 domen) w top 10 | URL-e z 0 linków | AIO |
|---|---|---|---|---|
| cross stitch pattern maker (US) | FlossCross #1, Stitch Fiddle, Xstitchify, Stitchly, Reddit, cross-stitched, Pic2Pat | stitchmate.app (62) #8 | 4 z 9 | tak; cytuje FlossCross, Stitchmate, Xstitchify, Pic2Pat, Stitchly |
| photo to cross stitch (US) | Pixel-Stitch #1, FlossCross, Pic2Pat, Reddit (8 lat), Stitchly, DMC | stitchmate.app #7 | 2 z 8 | tak; cytuje m.in. photo2stitch.com |
| photo to cross stitch (UK) | Pic2Pat #1, Pixel-Stitch, FlossCross, DMC, Skye Stitching | photo-stitch.co.uk (48) #6, stitchmate.app #7 | 1 z 8 | tak |
| custom cross stitch pattern (US) | cross-stitched (blog 10.2025) #1, FlossCross, Stitch Fiddle, Facebook (5 lat), Etsy, sklepy | brak | 4 z 7 | tak; podaje cenę Stitchmate 7,99 USD i ceny z Etsy |
| cross stitch calculator (US) | Scarlet Quince #1 (3 linki do URL), Pinterest, Xstitchify, 2 posty z Facebooka (5 lat), cross-stitch.com, 123stitch | brak | 8 z 9 | tak; cytuje Yarn Tree, Crosstitch.com, 123stitch, Atom Heart |
| dmc color chart (US) | DMC #1, **stitchmate.app #2**, Thread-Bare, Lord Libidan, Reddit, Amazon, Pinterest | stitchmate.app #2 | 3 z 8 | tak |
| dmc to anchor conversion (UK) | Stitchtastic #1, Cyberstitchers, Willow Fabrics, PDF Yarn Tree, Lazy May, Hello Hooray, Stitchmate, Needle'nThread (2008) | lazymay.co.uk (85) #5, stitchmate.app #7 | 3 z 8 | tak |
| aida count (US) | Reddit, 3 strony „fb-answers” Facebooka, stitchcreator, spam, stitchthis.io | stitchthis.io (37) #7 | 7 z 7 | tak |
| pattern keeper (US) | YouTube, Reddit, recenzja 2022, Facebook, strona PK | stitchmate.app #8 | 7 z 8 | tak |
| free cross stitch patterns (US) | Pinterest #1, LoveCrafts, Daily Cross Stitch, Artecy, Cyberstitchers | crossstitchquest.net (87) #6 | 3 z 8 | tak; cytuje DMC (705 darmowych wzorów), Fat Quarter Shop, LoveCrafts |
| christmas cross stitch patterns (US) | DMC, sklepy, Pinterest | brak | 6 z 9 | nie |
| small cross stitch patterns (US) | DMC, sklepy, Reddit, Pinterest, Etsy, Amazon | brak | 7 z 9 | nie |
| cross stitch for beginners (US) | Stitched Modern (2017) #1, Reddit, YouTube, Cross Stitch Guild, DMC | brak | 3 z 7 | tak |
| half stitch cross stitch (US) | Craft Club, Reddit, Caterpillar, YouTube, Medium | brak | 3 z 6 | tak (asynchr.) |

Liczby zbiorcze:
- **AI Overview w 12 z 14 SERP-ów** (1 asynchroniczny). Brak AIO tylko przy listach wzorów (świąteczne, małe). AIO często cytuje małe narzędzia: Stitchmate, Xstitchify, Lazy May, Atom Heart, photo2stitch.
- **Reklamy w wynikach: 0 z 14 SERP-ów** w chwili pobrania.
- 33 ze 111 wyników to Reddit, Facebook, Pinterest, YouTube i Medium. 16 wyników jest sprzed 2023 roku.
- **61 ze 104 URL-i ma 0 domen linkujących do konkretnej strony**; mediana dla URL-i poza serwisami społecznościowymi to 1.
- Mediana domen linkujących do **całej domeny** (bez serwisów społecznościowych, Amazona, Etsy) to 2 072. Uwaga: 40 z 73 takich domen ma od 1 500 do 2 700 domen linkujących, nawet małe sklepy i strona ze spamem (cglosteopatia.com 1 831). To wygląda na wspólny szum ze spamerskich sieci linków w bazie DataForSEO, więc tej mediany nie traktuję dosłownie.

**Gdzie mała domena wejdzie w 6–12 mies.:**
1. **Kalkulatory (tkanina, rozmiar, aida):** SERP z postami z Facebooka sprzed 5 lat, Pinterestem i starymi stronami sklepów, 8 z 9 URL-i bez linków.
2. **Tabela kolorów DMC i konwerter DMC↔Anchor (UK):** stitchmate.app jest #2 i #7 po kilku miesiącach.
3. **Pattern Keeper i „aida count”:** SERP-y zdominowane przez UGC (Reddit, Facebook, YouTube).
4. **„photo to cross stitch”, „pattern maker”:** trudniej (FlossCross 1 944 domen do strony głównej, Stitch Fiddle 341), ale stitchmate.app jest w top 10 w obu krajach.
5. **Darmowe wzory i wzory świąteczne:** trudno (DMC, LoveCrafts, Pinterest, sklepy) i bez AIO, ale też bez bezpośredniej sprzedaży Gridlinga.

## 3. Konkurencja Gridlinga

Ruch organiczny US [TE], domeny linkujące do domeny [BL]. Ceny z podanego źródła, sprawdzone 18.10.2026 (pełna tabela z URL-ami w `dane/EN-konkurencja.csv`).

| Narzędzie | Model i cena | Źródło ceny | Ruch US/mies. | Fraz US | Domeny linkujące |
|---|---|---|---|---|---|
| Stitch Fiddle | edytor web, Premium 2,75 USD/mies. | fragment stitchfiddle.com/pricing w [WS]; strona wymaga JS | 27 443 | 1 745 | 2 667 |
| FlossCross | darmowy, bez rejestracji | opis w SERP i AIO | 7 324 | 321 | 2 122 |
| Pixel-Stitch | darmowy | opis w SERP | 3 290 | 163 | 597 |
| Thread-Bare | 10 USD (recenzja Lord Libidan) | [WS] | 2 699 | 1 064 | 2 072 |
| Stitchly | aplikacja, jednorazowo 39,99 USD (promocja) lub 75 USD (iOS) | tracker App Pricing Lab [WS] | 2 351 | 301 | 1 771 |
| **Stitchmate** | projekt za darmo; PDF 7,99 USD za wzór, 12 USD za 5, 20 USD za 10; passy 30 dni / rok / dożywotni (ceny passów nieodczytane) | stitchmate.app/pricing [CP] | 2 108 | 1 922 | 62 |
| Xstitchify | darmowy w opisie; AlternativeTo podaje subskrypcję 10–25 USD/mies. | [WS], niepotwierdzone | 1 223 | 698 | 1 737 |
| Pattern Keeper | czytnik PDF (Android), 9 USD jednorazowo | AIO cytuje patternkeeper.app | 1 188 | 130 | 303 |
| Pic2Pat | darmowy PDF | opis w SERP/AIO | 1 162 | 315 | 2 112 |
| WinStitch / MacStitch | desktop, Premium 47 USD przed podatkiem | sklep FastSpring [WS] | 468 | 111 | 1 999 |
| PCStitch | desktop, ok. 50 USD | Lord Libidan, III.2026 [WS] | 235 | 129 | 2 232 |
| DMC Stitch Your Photo | wzór lub zestaw, 10,99 USD | cena w wyniku SERP | (dmc.com 60 546) | 9 880 | 9 032 |
| Etsy (wzory na zamówienie) | 3–62 USD | zakres w SERP | | | |
| UK: Skye Stitching / photo-stitch.co.uk | zestaw 35,99 GBP / wzór od 21 GBP | SERP UK | | | |

Gridling za 4,99 EUR (5,61 USD przy kursie 1,12368 [TV]) jest tańszy od Stitchmate (7,99 USD) i od wzorów z Etsy, a droższy od darmowych FlossCross i Pic2Pat. Ceny KG-Chart i photo2stitch.com nie znalazłem.

**Stitchmate to wzorzec i główny rywal.** Według stopki robi go jedna osoba („made by one craft lover”, Dmitrii). Na jednej domenie ma generator, ok. 30 darmowych narzędzi (kalkulator tkaniny, czasu, nici, tabele DMC i Anchor, konwerter, generator tekstu, papier w kratkę), strony „photo to …” dla haftu, diamond painting, koralików i szydełka oraz poradniki. Pozycje US: 62 na 1. miejscu, 135 na 2–3, 638 na 4–10; 1 149 z 1 922 fraz to frazy nowe [TE]. Pierwsza obserwacja domeny w bazie linków: 2.01.2026 [BL].

**Reklamy [ADS]:** Stitchly (Subtlabs Ltd) emituje reklamy tekstowe i wideo od 4.11.2022 do dziś; cross-stitched.com (beegreeeen limited) reklamy tekstowe od 9.08.2025 do 12.09.2026; DMC ma ponad 40 kreacji. Stitchmate, Stitch Fiddle i photo2stitch nie mają reklam. Ads Transparency nie mówi, na jakie frazy kupują. W 14 SERP-ach reklam nie było.

**CPC:** photo to cross stitch 1,55 USD, custom cross stitch pattern 1,69, custom … from photo 2,51, cross stitch app 1,25, pattern maker 0,58 [SV]. Przy cenie 5,61 USD kampania wychodzi na zero dopiero przy ok. 28% konwersji kliknięcia w zakup (1,55 / 5,61). Płatna reklama na pojedynczy wzór się nie zwraca; ma sens dopiero przy dostępie rocznym lub koszyku kilku wzorów.

## 4. Rachunek po 12 miesiącach (założenia, nie dane)

| Wariant | Scenariusz | Wizyty/mies. | Konwersja wizyta → zakup | Przychód na kupującego | Kupujących/mies. | Przychód/mies. (brutto) | Tempo roczne |
|---|---|---|---|---|---|---|---|
| Sam PL | ostrożny | 1 000 | 0,2% | 4,99 EUR | 2 | ok. 10 EUR | ok. 120 EUR |
| Sam PL | realny | 3 000 | 0,5% | 7,00 EUR | 15 | ok. 105 EUR | ok. 1 260 EUR |
| Sam EN | ostrożny | 2 000 | 0,3% | 4,99 EUR | 6 | ok. 30 EUR | ok. 360 EUR |
| Sam EN | realny | 8 000 | 0,8% | 7,00 EUR | 64 | ok. 450 EUR | ok. 5 380 EUR |
| EN + PL | ostrożny | 3 000 | | | 8 | ok. 40 EUR | ok. 480 EUR |
| EN + PL | realny | 11 000 | | | 79 | ok. 550 EUR | ok. 6 640 EUR |

Założenia jawne:
- **Ruch EN:** ostrożnie tyle, ile ma dziś Stitchmate po ok. 9,5 mies. w samych USA (2 108 [TE]). Realnie ×4: cztery rynki (UK+CA+AU to ok. 43% koszyka US [SV]), narzędzia od pierwszego dnia i sezon IV kwartału. 8 000 wizyt to 2,8% koszyka EN (286 671).
- **Ruch PL:** w F przyjęto 3 000 / 10 000, co przy koszyku 22 498 oznacza 13–44% wszystkich wyszukań. Tu przyjmuję 1 000 / 3 000 (4–13% koszyka), bo SERP PL jest słabszy, ale popyt mały.
- **Konwersja:** w EN część ruchu ląduje na stronach z intencją „wzór ze zdjęcia”, więc przyjmuję 0,3% / 0,8% (jak w F). W PL takiej intencji prawie nie ma, więc 0,2% / 0,5%.
- **Przychód na kupującego:** 4,99 EUR to cena wzoru z sesji Gridling. 7,00 EUR zakłada, że część kupujących bierze więcej niż 1 wzór lub dostęp roczny; ceny dostępu rocznego nie znam.
- Kwoty brutto, przed VAT i prowizją operatora płatności. Grudzień może dać ok. 1,6–2,2× średniej (sezon „custom cross stitch pattern” [SV]).
- Wariant PL wymaga polskiej wersji Gridlinga i dodatkowego zestawu treści; wariant EN nie wymaga nic poza samym serwisem.

Wniosek z rachunku: nawet realny wariant to kieszonkowy przychód. Wartość serwisu leży w sufitach: EN ma 30 476 wyszukań z intencją Gridlinga, PL ok. 21. Rozbudowa Gridlinga o diamond painting i paint by numbers (CPC 3–5 USD, 168 409 wyszukań w USA) zwiększa sens tych samych narzędzi i treści.

## 5. Zalecenia

### Osobna domena czy blog na domenie Gridlinga

**Na domenie Gridlinga, w podkatalogach** (`/tools/`, `/guides/`, `/patterns/`; później `/pl/` z hreflang). Powody:
- Linki zdobyte przez darmowe narzędzia i poradniki wzmacniają tę samą domenę, na której jest generator i strony „photo to cross stitch”. Przy osobnej domenie autorytet zostaje w serwisie, a do Gridlinga płynie tylko ruch z kliknięć.
- Stitchmate robi dokładnie to i po 9,5 mies. jest w top 10 dla „pattern maker” i „photo to cross stitch” z 62 domenami linkującymi.
- Krótsza ścieżka zakupu: kalkulator tkaniny → „zrób wzór ze zdjęcia” w tym samym serwisie i tej samej sesji.
- Astro da się postawić jako część strony Gridlinga (statyczny build w podkatalogu lub przez reverse proxy). Osobna domena ma sens tylko wtedy, gdy hosting Gridlinga tego nie pozwala; wtedy subdomena jest gorsza od podkatalogu, ale lepsza od nowej domeny.

### Klastry na start (kolejność)

1. **Narzędzia (magnes na linki i AIO):** kalkulator tkaniny i rozmiaru (aida 11/14/16/18, płótno 28/32 „over 2”, zapas na ramę) dla „cross stitch calculator” 5 433 + „fabric calculator” 1 475 + „size calculator” 622 [SV]. W nim ilość muliny (osobno 0–64 wyszukań, ale to dobra funkcja). Konwerter DMC↔Anchor pod UK (921 wyszukań/mies. w UK). Generator tekstu i alfabetów (klaster 1 300, CPC 1,93 [KS]; „cross stitch alphabet” 2 125).
2. **Strony „photo to cross stitch” według tematu i zastosowania:** zwierzak, ślub, dom, dziecko, pamiątka, imię/tekst, QR („qr code cross stitch” 3 600 [KS]). Każda z przykładem wygenerowanym w Gridlingu z własnego zdjęcia lub zdjęcia z wolną licencją. Ostrożnie z objętością: „pet portrait cross stitch” ma 0 wyszukań, więc to podstrony jednego huba.
3. **Encje kolorów DMC:** tabela 489 kolorów + strona każdego koloru (odpowiednik Anchor, kolory sąsiednie, przykładowe wzory). „dmc color chart” 5 300, stitchmate #2. Do sprawdzenia przed startem: skąd brać wartości RGB i czy tabela zamienników ma licencję pozwalającą na użycie komercyjne (tego dziś nie sprawdziłem).
4. **Pattern Keeper i czytanie wzorów:** „pattern keeper” 3 467 (+44% r/r), poradniki „jak zrobić PDF zgodny z Pattern Keeper”, „Pattern Keeper na iPhone” (pytanie z PAA). Bezpośrednio sprzedaje wyróżnik Gridlinga.
5. **Poradniki podstaw (aida count, ściegi, porównania):** „needlepoint vs cross stitch” 12 100, „embroidery vs cross stitch” 4 400, „aida count” i 14/16/18 count ok. 2 700, half/quarter stitch ok. 1 200. SERP-y z Redditem i Facebookiem, AIO prawie wszędzie.
6. **Sezon prezentowy (start treści najpóźniej we wrześniu):** „custom cross stitch pattern” ×2,2 w listopadzie, „christmas cross stitch patterns” 1 853, „christmas stocking cross stitch” 2 400 [KS].

Na później lub wcale: duży katalog darmowych wzorów. SERP mają DMC (705 darmowych wzorów według AIO), LoveCrafts i Pinterest, a takie strony słabo sprzedają generator.

### Wzory jako strony encji: licencje

- Tylko **wzory własne** (zaprojektowane lub wygenerowane w Gridlingu z własnych zdjęć) oraz **dzieła w domenie publicznej** (stare obrazy, ryciny, hafty z muzeów udostępniających zbiory na licencji CC0 lub bez ograniczeń). Źródło i licencję każdej grafiki zapisujemy przy stronie. Konkretnych kolekcji muzealnych dziś nie sprawdzałem.
- Odpadają: postacie i marki (np. „pokemon cross stitch” 1 300 [KS]), kopie wzorów z Etsy, Pinteresta i sklepów, zdjęcia z licencją niekomercyjną (NC) i wzory z licencją NC.
- Wzór z domeny publicznej to też dobry pokaz Gridlinga („obraz X jako wzór: 14 count, 30 kolorów, PDF zgodny z Pattern Keeper”), bez ryzyka praw autorskich.

## Czego nie sprawdziłem

- Cen Stitch Fiddle, Xstitchify, Stitchly, Thread-Bare, WinStitch i PCStitch bezpośrednio na stronach producentów (WebFetch blokowany, strony z JS nieczytelne przez DataForSEO); podaję je z fragmentów WebSearch z adnotacją. Ceny passów Stitchmate. Ceny KG-Chart i photo2stitch.com.
- Na jakie frazy Stitchly, cross-stitched.com i DMC kupują reklamy (Ads Transparency tego nie podaje).
- Ruchu konkurentów w UK, CA i AU (`bulk_traffic_estimation` liczony tylko dla US).
- Licencji danych kolorów DMC/Anchor i kolekcji muzealnych w domenie publicznej.
- Ceny dostępu rocznego Gridlinga i rzeczywistej konwersji (rachunek opiera się na założeniach).
- Wiarygodności liczby domen linkujących w przedziale 1 500–2 700 (podejrzenie spamowych linków w bazie).

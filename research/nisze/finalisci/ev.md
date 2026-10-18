# Samochody elektryczne w Polsce (koszty ładowania, stacje i operatorzy, modele, ładowanie w domu): badanie tak/nie (18.10.2026)

Zakres: koszty ładowania, stacje i operatorzy, modele (zasięg, zużycie), ładowanie w domu. Bez dopłat, ulg, przepisów, leasingu i ubezpieczeń (lista w sekcji „Omijamy”). Metoda: `research/nisze/finalisci/BRIEF.md` i `research/nisze/METODA.md`. Punkt wyjścia: `research/nisze/A-technologia.md` (nisza 1).

**Oznaczenia źródeł (wszystko pobrane 18.10.2026):**
- **[W]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live` (location_code 2616, pl, `date_from` 2024-10-01): średni wolumen z 12 miesięcy (10.2025–09.2026) i CPC w USD. Trend r/r: suma VII–IX 2026 wobec VII–IX 2025.
- **[K]** DataForSEO `/v3/dataforseo_labs/google/keyword_suggestions/live` (11 nasion) i `keyword_ideas/live`: tylko do znalezienia fraz.
- **[S]** DataForSEO `/v3/serp/google/organic/live/advanced`, desktop, `load_async_ai_overview`. Pobierałem depth 40 (żeby wynik zapisał się do pliku), analizuję pierwsze 10 wyników organicznych.
- **[B-URL] / [B-D]** DataForSEO `/v3/backlinks/bulk_referring_domains/live` dla konkretnych URL-i / dla domen.
- **[T]** DataForSEO `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (szacowany ruch organiczny ETV).
- **[A]** DataForSEO `/v3/serp/google/ads_advertisers/live/advanced` (Google Ads Transparency).
- **[CP]** DataForSEO `/v3/on_page/content_parsing/live` (czytanie stron, bo WebFetch nie rozwiązuje domen przez proxy).
- **[WS]** WebSearch (podsumowanie wyników, bez otwierania źródła).

Pliki: `dane/ev-mapa.csv` (534 frazy), `dane/ev-serp-top10.csv` i `dane/ev-serp-podsumowanie.csv` (20 SERP-ów), `dane/ev-programy.csv`, `dane/ev-rachunek.csv`, `dane/ev-encje-zrodla.csv`, `dane/ev-omijamy.csv`.

## Werdykt w skrócie

**NIE (wynik 2,9 / 5).**

1. **Popyt jest duży, ale prawie cały nawigacyjny.** Mapa ma 492 frazy i 1 023 820 wyszukiwań/mies. [W]. Z tego 626 460 to nazwy marek i modeli (producent, dealerzy), a 268 180 to frazy typu „stacja ładowania greenway” z mapą Google nad wynikami [S]. Dla nowego serwisu realnie zostaje 386 fraz i 88 650 wyszukiwań/mies., z trendem −2,1% r/r [W].
2. **Nie ma na czym zarobić.** Nie znalazłem publicznego programu partnerskiego żadnego polskiego sklepu z wallboxami ani operatora ładowania. Ceneo płaci 0,20 zł za przejście do sklepu albo 1,05% w kategorii Motoryzacja, Allegro Share płaci kuponami (1,67%) [CP]. Leady na montaż wallboxa to „zlecenia dla fachowców”, które portfel wyklucza. Leasing to temat finansowo-prawny. Rachunek po 12 mies.: **ok. 27 zł/mies. (ostrożnie) i ok. 380 zł/mies. (realnie)**.
3. **Fosa EIPA jest zajęta i niepewna prawnie.** EIPA daje za darmo lokalizacje, ceny i dostępność punktów w JSON, ale na stronach rejestru nie ma licencji ani regulaminu ponownego użycia [CP]. Ten sam pomysł („paliwownia dla elektryków” na danych EIPA) realizuje już stacjeladowaniapojazdow.pl (ARINEA Sp. z o.o.), który ma cenniki operatorów, strony miast, katalog modeli i kalkulatory, a do tego cytuje go AI Overview [CP][S]. Podobne bazy prowadzą gdzieladowac.eu, stacje.com.pl i stacjomat.pl [S].

Plus: SERP-y są słabe na poziomie URL-i (20 z 20 spełnia kryterium briefu) i AIO cytuje małe serwisy w 11 z 20 zapytań [S][B-URL][B-D]. Ruch da się zdobyć, tylko nie przekłada się na pieniądze.

---

## 1. Mapa fraz [W][K] (`dane/ev-mapa.csv`)

Rozszerzenie: 11 wywołań `keyword_suggestions` i `keyword_ideas` (nasiona: „samochodu elektrycznego”, „samochody elektryczne”, „ładowania”, „ładowanie”, „ładowarka”, „wallbox”, „zasięg”, „elektryk”, „elektryka”, „greenway”, „cennik” z filtrem operatorów, „zużycie energii”), razem 4 181 fraz. Do tego wygenerowałem 769 kombinacji: 53 modele × (zasięg, zużycie energii, zasięg zimą, ładowanie, czas ładowania, bateria), 20 miast × 4 warianty „stacje ładowania [miasto]”, 25 operatorów × 6 dopisków (cennik, mapa, aplikacja, karta, ceny, abonament) oraz ok. 150 fraz poradnikowych. Wolumeny 1 227 fraz pobrałem z `search_volume/live`. Usunąłem frazy wieloznaczne (ładowarki do telefonów i elektronarzędzi, „elektryk” jako zawód i szkoła, zasięg sieci komórkowej, rowery i hulajnogi, „greenway” jako marka chlorelli) i prawne (`dane/ev-omijamy.csv`). W mapie zostały frazy z wolumenem ≥70 oraz narzędziowe i modelowe od 30 w górę.

| Typ strony | Fraz | Wolumen/mies. | W tym „do wzięcia: tak” (fraz / wolumen) | Przykłady (wolumen [W]) |
|---|---|---|---|---|
| Encja: model | 121 | 624 280 | 64 / 7 720 | „byd” 135 000, „byd seal” 33 100 (nawigacyjne); „dacia spring zasięg” 880, „renault zoe zasięg” 320, „toyota bz4x zasięg” 260 |
| Encja: operator | 53 | 219 650 | 18 / 4 440 | „stacja ładowania elocity” 33 100, „stacja ładowania greenway” 33 100, „orlen stacja ładowania” 27 100 (local pack); „greenway cennik” 1 300, „elocity cennik” 720, „powerdot cennik” 480 |
| Hub | 11 | 101 840 | 4 / 8 910 | „samochód elektryczny” 33 100, „stacje ładowania” 18 100, „wallbox” 5 400 |
| Porównanie / ranking | 110 | 34 660 | 110 / 34 660 | „ładowarka ev” 4 400, „wallbox 11kw” 2 400, „najtańszy samochód elektryczny” 1 600, „chińskie samochody elektryczne” 880 |
| Poradnik | 78 | 23 380 | 77 / 13 480 | „bateria do samochodu elektrycznego” 390, „wallbox co to jest” 260, „ładowanie samochodu elektrycznego w domu” 260 |
| Narzędzie | 93 | 15 840 | 93 / 15 840 | „ile kosztuje ładowanie samochodu elektrycznego” 1 300, „stacje ładowania samochodów elektrycznych mapa” 1 000, „tesla supercharger mapa” 1 000, „ile kosztuje ładowanie elektryka” 720 |
| Encja: wallbox | 20 | 3 600 | 20 / 3 600 | „tesla wall connector” 590, „green wallbox” 260, „wallbox pulsar plus” 260 |
| Encja: miasto | 6 | 570 | 0 / 0 | „stacja ładowania samochodów elektrycznych warszawa” 140, „… poznań” 140 |
| **Razem** | **492** | **1 023 820** | **386 / 88 650** | |

Dodatkowo 42 warianty pisowni (np. „stacja / stacje ładowania”) mają ten sam wolumen co fraza główna i nie wchodzą do sum.

**Trend i sezon [W].** Cała mapa: +15,7% r/r, najsłabszy luty 2026 (851 700), najmocniejszy marzec 2026 (1 093 600). Frazy „do wzięcia”: −2,1% r/r, czerwiec 2026 68 170, marzec 2026 115 670. Wzrost całej niszy ciągną marki operatorów: „stacja ładowania elocity” +235% r/r, „orlen stacja ładowania” +66% r/r [W].

**Frazy narzędziowe są małe [W]:** „kalkulator ładowania samochodu elektrycznego” 70, „kalkulator czasu ładowania samochodu elektrycznego” 40, „koszt przejechania 100 km samochodem elektrycznym” 140, „mapa stacji ładowania z cenami” 110, „planowanie trasy samochodem elektrycznym” 30. Planer trasy ma właściciela: „abrp” 1 900, „a better route planner” 210. Frazy „zasięg [model] zimą” mają 0–30 (np. „dacia spring zasięg zimą” 30, „nissan leaf zasięg zimą” 10).

**CPC [W]:** ważony całej mapy 0,43 USD, fraz „do wzięcia” 0,56 USD. Najwyżej: „karta greenway” 6,36 USD (70/mies.), „montaż stacji ładowania samochodów elektrycznych” 3,98 USD (90), „koszt instalacji wallboxa” 3,13 USD (10).

## 2. Dwadzieścia SERP-ów [S][B-URL][B-D] (`dane/ev-serp-podsumowanie.csv`, `dane/ev-serp-top10.csv`)

Kryterium briefu: w top 10 są ≥2 URL-e z <10 domenami linkującymi albo fora, PDF-y i stare treści (tu: sprzed 2024).

| Fraza [W] | Typ | URL-e <10 RD | Mediana RD domeny | Fora/social/PDF | Stare | AIO | Kto wygrywa |
|---|---|---|---|---|---|---|---|
| ile kosztuje ładowanie samochodu elektrycznego (1 300) | narzędzie | 10 | 209 | 1 | 2 | tak | cupra.com, beesafe.pl (2022), greenkick.com.pl (2022), sigmapolska.pl ×2 |
| ile kosztuje ładowanie … w domu (260) | narzędzie | 9 | 128 | 0 | 1 | tak | mazda.pl, volkswagen.pl (symulator, 16 RD), feyree.pl, xpeng.pl |
| greenway cennik (1 300) | operator | 9 | 1 945 | 2 | 0 | tak | greenwaynetwork.com ×4, elektromobilni.pl, PDF greenway.sk, stacjeladowaniapojazdow.pl |
| elocity cennik (720) | operator | 8 | 417 | 0 | 1 | tak | elo.city ×7, chinskisamochod.com, stacjeladowaniapojazdow.pl |
| powerdot cennik (480) | operator | 10 | 1 100 | 1 | 0 | tak | elo.city, powerdot.eu ×3, elektrowoz.pl, stacjeladowaniapojazdow.pl |
| ionity cennik (390) | operator | 10 | 1 414 | 1 | 0 | tak | ionity.eu ×3, elektrowoz.pl ×2, evklub.pl, otoev.pl |
| orlen charge cennik (390) | operator | 8 | 278 | 1 | 0 | tak | orlencharge.pl ×3, orlen.pl, energa.pl, arinea.pl |
| stacje ładowania … mapa (1 000) | narzędzie | 7 | 943 | 1 | 0 | nie | elektromobilni.pl (21 RD), chargefinder.com, stacjomat.pl, plugshare.com |
| dacia spring zasięg (880) | model | 9 | 1 193 | 3 | 3 | tak | e.autokult.pl (2022), Facebook, dacia.pl, elektrowoz.pl (2023) |
| tesla model 3 zasięg (210) | model | 9 | 1 868 | 4 | 1 | tak | tesla.com (18 RD), otoev.pl, YouTube, forum.elektrowoz.pl, reddit |
| toyota bz4x zasięg (260) | model | 10 | 169 | 2 | 1 | tak | dealerzy Toyoty ×5, otoev.pl, evkx.net |
| zasięg samochodu elektrycznego zimą (10) | poradnik | 10 | 843 | 0 | 1 | tak | automarket.pl, carleasepolska.pl, wysokienapiecie.pl (2023) |
| wallbox 11kw (2 400) | sprzęt | 10 | 147 | 0 | 0 | nie | sklepy: milivolt.pl, swiatbaterii.pl, greenkick, greenwallbox, ceneo |
| ładowarka do samochodu elektrycznego (2 400) | sprzęt | 9 | 274 | 0 | 0 | nie | wallbox.pl ×2, enzeit.com, elektromobilni.pl, evchargeplus.pl |
| najtańszy samochód elektryczny (1 600) | ranking aut | 9 | 548 | 2 | 2 | tak | elektromobilni.pl, forum.elektrowoz.pl, motofakty.pl (89 RD), superauto.pl |
| stacja ładowania … warszawa (140) | miasto | 8 | 1 414 | 2 | 0 | tak | local pack; Facebook, elektrowoz.pl, plugshare.com, chargefinder.com |
| ile trwa ładowanie samochodu elektrycznego (260) | narzędzie | 10 | 211 | 0 | 2 | tak | plugbox.eu (2023), jaguar.pl, kiawiarnia.pl, dealerzy |
| samochody elektryczne z największym zasięgiem (170) | ranking aut | 10 | 1 326 | 4 | 1 | tak | stacjomat.pl, Facebook, elektrowoz.pl, reddit ×2 |
| ładowanie samochodu elektrycznego w domu (260) | poradnik | 9 | 630 | 0 | 0 | tak | jaguar.pl, skoda.pl, strefaev.com, cupra.com, bmw.pl (59 RD) |
| kabel do ładowania samochodu elektrycznego (320) | sprzęt | 10 | 773 | 1 | 1 | nie | preis-zone.pl, swiatbaterii.pl, allegro.pl, tim.pl, ceneo.pl |

**Wnioski.**
- **20 z 20 SERP-ów spełnia kryterium.** URL-e prawie nie mają linków: mediana RD na URL to 0 w 17 z 20 SERP-ów [B-URL]. Kryterium jest więc łatwe do spełnienia w tej niszy. Siłę dają domeny: mediana RD domen w top 10 wynosi od 128 do 1 945 [B-D].
- **Kto wygrywa na poziomie URL-i.** „[operator] cennik”: strony operatora (3–7 URL-i w top 10) i portale branżowe (elektrowoz.pl, elektromobilni.pl, evklub.pl). „zasięg [model]”: producent, dealerzy, testy z 2022–2023, fora, YouTube i bazy modeli (otoev.pl, evkx.net). „koszt ładowania”: strony producentów aut (cupra, mazda, volkswagen, hyundai, jaguar) i sklepy z ładowarkami. „ładowarki / stacje [miasto]”: local pack, plugshare.com, chargefinder.com. Dodatkowe SERP-y (poza dwudziestką): „ile kosztuje ładowanie tesli” (140) wygrywają reddit (3 URL-e), interia.pl i elektrowoz.pl; „dacia spring zasięg zimą” (30) autokatalog.pl, motonews.pl, forum daciaklub.pl z 2020 r.; „ładowarki elektryczne warszawa” (50) local pack, equay.pl, plugbox.eu, plugshare.com [S].
- **AIO w 15 z 20 SERP-ów.** W 11 z nich AIO cytuje domenę z <300 RD (np. stacjeladowaniapojazdow.pl w 3 SERP-ach, lenergizee.pl, sigmapolska.pl, ampergo.pl, amperepoint.pl) [S][B-D]. Brak AIO na frazach sprzętowych i na mapie.
- **Local pack** stoi nad wynikami na „stacje ładowania”, „stacja ładowania greenway”, „ładowarki elektryczne warszawa” i frazach miejskich [S]. Dlatego frazy operatorów i miast liczę z mnożnikiem 0,3.
- **Konkurencja wprost [T][CP]:** stacjeladowaniapojazdow.pl (50 RD, ETV 2 482/mies.): „Niezależna baza 6079 publicznych stacji ładowania samochodów elektrycznych w Polsce. Dane z oficjalnego rejestru EIPA (UDT), aktualizowane codziennie. Porównania aut EV, kalkulatory, cenniki operatorów.” Należy do ARINEA Sp. z o.o. (arinea.pl, ETV 2 121), która sprzedaje budowę stacji i wallboxy. Inne bazy: gdzieladowac.eu (ETV 763), stacje.com.pl (927), stacjomat.pl (205 RD, ETV 625), mapaladowania.pl i evstar.pl (cytowane w AIO lub w top 10). Duże serwisy EV: elektromobilni.pl (ETV 31 440), elektrowoz.pl (20 186), otoev.pl (15 078), chinskisamochod.com (14 450).

**Ile fraz realnie wejdzie w 6–12 mies.:** 386 fraz (88 650/mies.) z kategorii „tak” oraz 44 frazy (268 180/mies.) z kategorii „częściowo”, gdzie organiczne wyniki są słabe, ale kliknięcia zabiera mapa Google. 58 fraz (626 460/mies.) z nazwami marek i modeli uznaję za niedostępne. Dla nich SERP-ów nie sprawdzałem (to analogia: wyniki producentów, dealerów i Shopping).

## 3. Zarobek (`dane/ev-programy.csv`)

### Programy partnerskie

| Program | Stawka | Cookie | PL | Status |
|---|---|---|---|---|
| Ceneo [CPC] (Admitad, Indoleads) | 0,20 zł za przejście z Ceneo do sklepu; kategoria „Samochody” bez prowizji | 90 dni | tak | z opisu w agregatorze affi.io [CP] |
| Ceneo CPS (BlueAff / Tradedoubler, ID 300324) | 0,53–2,63%; **Motoryzacja 1,05%**; tylko zakupy „KUP TERAZ” w Ceneo | — | tak | jw. |
| x-kom (Admitad) | stawki w arkuszu Google, nie otwierałem | 24 h | tak, akceptacja wybranych wydawców | zakaz linków na stronach „nastawionych głównie na marketing afiliacyjny”, wyjątek dla doradztwa [CP]; asortymentu wallboxów nie sprawdziłem |
| Allegro Share | 1 pkt za 1 zł, 60 pkt = 1 zł kuponu (ok. 1,67% w kuponach) | 24 h | tak | nagroda w kuponach Allegro, nie w gotówce [CP, tabletowo.pl; data artykułu nieznana] |
| Sklepy z wallboxami (wallbox.pl, greenwallbox.pl, Green Cell, evchargeplus.pl) | — | — | — | publicznego programu nie znalazłem [WS ×3] |
| Amazon.pl | tabeli stawek dla PL nie znalazłem | — | — | niesprawdzone [WS] |
| Leasing i wynajem EV (Vehis, Superauto, Masterlease, Carsmile) | — | — | — | publicznego programu nie znalazłem; Car Lease Polska ma polecenia za punkty [WS]; temat w „Omijamy” |
| Aplikacje i operatorzy (Elocity, Plugsurfing, Electromaps, Bonnet) | — | — | — | programu dla PL nie znalazłem [WS] |

Kto płaci za reklamy na „wallbox” [A]: GREEN WALLBOX SP Z O O (ok. 70 reklam), Wallbox Polska Sp. z o.o. (ok. 24), WallboxCenter GmbH (7). Sklepy kupują ruch w Google Ads, ale programu dla wydawców nie pokazują publicznie. Zapytanie o program to kontakt z firmą, czyli poza zasadami.

Ceny do rachunku [S, Google popular products 18.10.2026]: wallbox 11 kW od 988 zł (Ultimate Speed) do 2 413,14 zł; kabel typu 2 od 279,98 zł (Gembird) do 1 299 zł (Blaupunkt).

### Reklamy

RPM display dla PL: **brak wiarygodnego źródła** [WS]. Przyjmuję 5 i 10 zł na 1000 odsłon jako założenie, tak samo jak w `druk3d.md`.

### Leady

- **Montaż wallboxa:** to „zlecenia dla fachowców” (elektryk), wykluczone z portfela (`RANKING.md`: „Pominięte z góry: … zlecenia dla fachowców”). Popyt i tak jest mały: „montaż wallboxa” 140/mies., „wallbox cena z montażem” 50, „ile kosztuje montaż wallboxa” 30 [W]. Ci elektrycy mogą być za to klientami niechcieznajda.pl (strony dla fachowców); to decyzja właściciela.
- **Budowa stacji dla firm:** to model ARINEA. Wymaga sprzedaży B2B i kontaktu z firmami.
- **Leasing, wynajem, taryfy prądu:** treści finansowo-prawne; poza zakresem.

### Własny produkt

- **Planer trasy z kosztami:** EIPA daje stacje, ceny i dostępność, EEA zużycie na model, OSM drogi. Budowa jest ciężka (routing, model zużycia, krzywe ładowania). Rynek ma darmowego lidera: „abrp” 1 900/mies. [W]. Frazy „planer trasy samochód elektryczny” i „planer trasy ev” nie mają wolumenu [W]. Szansa na płatną wersję: niska.
- **Alert cen ładowania / raporty cen dla firm:** stacjeladowaniapojazdow.pl publikuje „Raporty cenowe” za darmo [CP]. Popytu nie sprawdziłem.
- **Ogłoszenia płatne przez operatorów lub sklepy:** wymagają kontaktu z firmami.

### Wybór modelu

- **Główny: reklamy display.** Ruch jest informacyjny i lokalny (koszty, mapy, cenniki), a afiliacji z sensowną stawką nie ma.
- **Dodatkowy: Ceneo na stronach wallboxów i kabli.** 0,20 zł za przejście albo 1,05% sprzedaży [CP]. Jedyny potwierdzony program, który działa dla PL i obejmuje ten asortyment.
- Oba źródła razem dają kwoty z rachunku niżej. To jest główny powód werdyktu.

## 4. Rachunek po 12 miesiącach (`dane/ev-rachunek.csv`)

Ruch = wolumen fraz × CTR pozycji × mnożnik (AIO 0,7; local pack 0,3) × pokrycie fraz stronami. Krzywa CTR: SEO Inc. 2025 (poz. 1 = 28,5%, poz. 5 = 6,1%, poz. 10 = 1,4%; https://seoinc.com/?p=9742), przejęta z `druk3d.md` bez ponownej weryfikacji. Pozycje pośrednie to interpolacja liniowa (założenie).

| Parametr | Ostrożny | Realny |
|---|---|---|
| Pokrycie fraz stronami | 60% | 85% |
| Pozycja: głowy / local pack / encje modeli / operatorzy / narzędzia / sprzęt / rankingi aut / poradniki | poza top 10 / 8 / 6 / 6 / 6 / 8 / 8 / 8 | 9 / 5 / 3 / 3 / 3 / 5 / 5 / 5 |
| Sesje: local pack (44 frazy, 268 180) | 1 593 | 4 172 |
| Sesje: sprzęt (91 fraz, 33 910) | 671 | 1 758 |
| Sesje: narzędzia (93 frazy, 15 840) | 351 | 1 652 |
| Sesje: encje modeli (64 frazy, 7 720) | 169 | 795 |
| Sesje: głowy (4 frazy, 40 530) | 0 | 792 |
| Sesje: rankingi aut (55 fraz, 13 680) | 190 | 497 |
| Sesje: poradniki (65 fraz, 13 060) | 181 | 474 |
| Sesje: operatorzy, cenniki (18 fraz, 4 440) | 97 | 457 |
| **Sesje/mies.** | **3 251** | **10 596** |
| Reklamy (RPM 5 / 10 zł; 1,3 / 1,6 odsłony na sesję) | 21 zł | 170 zł |
| Kliki do sklepu (sprzęt 8% / 12%, rankingi aut 3% / 5%) | 59 | 236 |
| Przychód na klik | 0,10 zł (Ceneo 0,20 zł × 50% przejść) | 0,90 zł (konwersja 2% × koszyk 1 500 zł × 3%) |
| Afiliacja | 6 zł | 212 zł |
| **Razem** | **ok. 27 zł/mies.** | **ok. 380 zł/mies.** |

Wszystkie wiersze poza wolumenem, stawką Ceneo i cenami wallboxów to założenia. Stawka 3% w wariancie realnym nie ma dziś potwierdzenia w żadnym programie. Szacunek ruchu zgadza się z rzędem wielkości konkurentów na EIPA: 625–2 482 ETV/mies. [T]. Nie liczyłem stron pojedynczych stacji (ok. 6 000 z EIPA), bo ich frazy mają wolumen poniżej progu DataForSEO.

## 5. Dane do stron encji (`dane/ev-encje-zrodla.csv`)

### EIPA (UDT): https://eipa.udt.gov.pl/

- **Co jest w danych** (strona „Udostępnianie danych EIPA”, https://eipa.udt.gov.pl/reader/docs [CP]): sześć plików JSON. `operator.json` (operatorzy i dostawcy usług), `pool.json` (bazy: adres, współrzędne, godziny otwarcia, zdjęcia), `station.json` (stacje, metody płatności i uwierzytelnienia, gmina, powiat, województwo), `point.json` (punkty: złącza, moc kW, kabel), `dynamic.json` („ceny paliw na stacjach ładowania i tankowania obowiązujących dla klientów niezwiązanych umową z operatorem” oraz `availability` i `status` punktu), `dictionary.json` (słowniki).
- **Dostęp:** „EIPA udostępnia dane o infrastrukturze paliw alternatywnych w formacie JSON. Dostęp do plików nadawany jest po zarejestrowaniu się. Przyznawany jest także limit pobrań plików na godzinę.” Rejestracja (https://eipa.udt.gov.pl/reader/register): „Dane zamieszczone w niniejszym rejestrze dostępne są dla każdego po zarejestrowaniu konta. Aby zarejestrować konto, wystarczy podać adres e-mail […]. Konta, z których nie pobrano danych przez okres 30 dni, będą automatycznie usuwane.” [CP]. Nie rejestrowałem się.
- **Licencja: nie znalazłem.** Strona główna mówi tylko o „możliwości pobrania i przetwarzania zgromadzonych w rejestrze danych w celu udostępnienia ich na mapie” oraz: „Urząd Dozoru Technicznego nie ponosi odpowiedzialności za aktualność danych przesyłanych przez operatorów infrastruktury do niniejszego rejestru” [CP]. Formularz rejestracji zawiera tylko zgodę RODO. Regulaminu, licencji ani zakazu użycia komercyjnego na stronach EIPA nie ma. Zbioru EIPA na dane.gov.pl nie znalazłem [WS].
- **Kontekst prawny (do decyzji, nie na stronę):** AFIR, rozporządzenie (UE) 2023/1804, art. 20 ust. 4: „państwa członkowskie zapewniają, aby dane, o których mowa w ust. 2 niniejszego artykułu, były udostępniane w sposób otwarty i niedyskryminujący wszystkim użytkownikom danych za pośrednictwem ich krajowych punktów dostępu”. Wśród danych dynamicznych jest „cena ad hoc” [CP, eur-lex.europa.eu, tekst PL]. Czy EIPA jest polskim punktem dostępu, nie sprawdziłem. Komercyjne serwisy już używają EIPA z podpisem „Dane stacji: EIPA UDT” (stacjeladowaniapojazdow.pl) [CP]. **Użycie komercyjne jest więc prawdopodobnie dozwolone, ale nie jest potwierdzone u źródła.** Potwierdzenie na piśmie wymaga pytania do UDT (eipa@udt.gov.pl); to decyzja właściciela.
- **Jakość danych:** według stacjeladowaniapojazdow.pl GreenWay Polska ma w EIPA 36 stacji i 31 punktów [CP], co wygląda na niepełne dane albo inne przypisanie operatora. Przed publikacją cen i liczb trzeba to porównać z danymi operatora.
- **Liczba encji:** wszystkie publiczne stacje (6 079 według stacjeladowaniapojazdow.pl; sam plików nie pobrałem). Operatorów z frazami w mapie jest ok. 25.
- **Aktualizacja:** `dynamic.json` na bieżąco (ceny i status od operatorów), pliki statyczne przy zmianach. Integracja: ok. 2–3 dni pracy, potem automat.

### Modele aut: EEA, CO2 emissions from new passenger cars

- Zbiór per pojazd z rozporządzenia (UE) 2019/631: https://www.eea.europa.eu/en/datahub/datahubitem-view/fa8b1229-3db6-495d-b18e-9c9b3267c02b (strona: „Last modified 25 Sept 2026”) [CP].
- **Licencja potwierdzona:** „Information, documents and material available on this website and for which the EEA holds the rights of use are public and may be re-used without prior permission, free of charge, for commercial or non-commercial purposes, provided that the EEA is always acknowledged as the original source of the material” (https://www.eea.europa.eu/en/legal-notice) [CP].
- **Zużycie energii:** według metadanych EEA 2024 zbiór zawiera pola „Electric energy consumption (Wh/km)” i „Electric range (km)” [WS]. PDF-u metadanych i eksportu nie otworzyłem: proxy blokuje sdi.eea.europa.eu i discodata.eea.europa.eu. Z tego samego zbioru da się policzyć rejestracje nowych aut w PL per model (pole kraju); tego też nie sprawdziłem w danych.
- **Liczba encji:** 50 modeli na start, 120 po 6 mies. Praca: mapowanie wariantów EEA na nazwy handlowe ok. 0,5–1 h na model, plus parametry ładowania (moc AC/DC, bateria netto) z kart producentów ok. 1 h na model. Razem ok. 75–100 h na start. Aktualizacja: raz w roku plus premiery.

### Alternatywy

- **OpenStreetMap (ODbL):** „Możesz swobodnie kopiować, rozpowszechniać, przekazywać innym i dostosowywać nasze dane, pod warunkiem podania OpenStreetMap i jego autorów jako źródła. Jeśli zmienisz, przekształcisz lub wykorzystasz nasze dane, wynik swojej pracy możesz rozpowszechniać tylko na podstawie tej samej licencji.” (https://www.openstreetmap.org/copyright/pl) [CP]. Komercyjnie wolno, z atrybucją i share-alike dla bazy pochodnej. Kafelki i API OSMF mają osobne zasady.
- **Open Charge Map:** „Data contributed to us by our users which we then redistribute is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0)”, ale „Data imported from 3rd party Data Providers is copyright the original Data Provider in each case and is not provided under the same terms” (https://openchargemap.org/about/terms) [CP]. Użyteczne tylko po filtrowaniu rekordów według dostawcy.
- **Cenniki z abonamentami:** EIPA ma tylko ceny ad hoc. Abonamenty trzeba zbierać ręcznie ze stron operatorów (ok. 1 h na operatora, zmiany kilka razy w roku; np. Ionity zmieniło cennik od 1.07.2026 według elektrowoz.pl [S]).

## 6. Szkic serwisu (gdyby właściciel jednak chciał wejść)

| Dział | Start | Po 6 mies. |
|---|---|---|
| Huby (koszt ładowania, stacje i operatorzy, ładowanie w domu, modele i zasięg, sprzęt) | 5 | 5 |
| Encje: operatorzy (cennik ad hoc z EIPA, abonamenty, liczba stacji, mapa) | 20 | 40 |
| Encje: modele (zasięg WLTP, Wh/km z EEA, koszt 100 km dom/AC/DC, czas ładowania) | 50 | 120 |
| Encje: miasta (stacje, najtańsze AC/DC, moc) | 20 | 100 |
| Rankingi sprzętu (wallbox 7/11/22 kW, kable typu 2, ładowarki przenośne) | 8 | 20 |
| Rankingi aut (najtańsze, największy zasięg, najszybsze ładowanie, auta miejskie) | 6 | 15 |
| Poradniki | 15 | 40 |
| Narzędzia | 3 | 5 |

**Narzędzia:**
1. Kalkulator kosztu ładowania i kosztu 100 km: model (Wh/km z EEA), cena prądu w domu wpisywana przez użytkownika, ceny operatorów z EIPA.
2. Najtańsze ładowanie dziś: ranking operatorów i stacji po cenie zł/kWh (AC, DC), z mapą i filtrem złącza i mocy.
3. Kalkulator czasu ładowania (bateria, moc AC/DC, zakres 10–80%).
4. Później: dobór wallboxa (faza, moc przyłącza, auto) i planer trasy z kosztem.

**Pierwszy klaster:** „Ile kosztuje ładowanie” (kalkulator, 20 stron operatorów, ładowanie w domu bez taryf i przepisów). Start publikacji w listopadzie 2026, żeby strony zdążyły się zaindeksować przed szczytem w marcu (fraza „ile kosztuje ładowanie samochodu elektrycznego”: 03.2026 1 900, 06.2026 880 [W]).

**Nazwa i domena (pomysły, dostępności nie sprawdzałem):** IleZaKWh (ilezakwh.pl), Ładuj Taniej (ladujtaniej.pl), Koszt Elektryka (kosztelektryka.pl), Prąd w Trasie (pradwtrasie.pl).

## 7. Ryzyka

- **AIO:** 15 z 20 SERP-ów [S]. Na „ile kosztuje ładowanie” AIO podaje gotowe widełki (dom 0,60–1,10 zł/kWh, stacje 1,50–3,50 zł/kWh, za moya-energia.pl) [S], więc proste strony z liczbami stracą kliknięcia.
- **Konkurent z tym samym pomysłem:** stacjeladowaniapojazdow.pl ma już cenniki operatorów, strony miast, katalog modeli i jest cytowany w AIO [CP][S]. Do tego 4 inne bazy na EIPA [S].
- **Zależność od jednego źródła danych:** EIPA bez licencji, z limitem pobrań, z kontem kasowanym po 30 dniach bez pobrań i z wątpliwą kompletnością (GreenWay) [CP].
- **Zarobek:** brak programu partnerskiego z sensowną stawką; leady wykluczone; reklamy przy RPM-ie nieznanym dla PL.
- **Nawigacja i aplikacje:** największe frazy to nazwy operatorów i marek; kierowcy korzystają z aplikacji operatorów i Map Google.
- **Sezonowość:** umiarkowana (marzec ok. +30% wobec czerwca dla fraz „do wzięcia” [W]).

### Omijamy (tematy prawne i pokrewne; autorzy ich nie ruszają) (`dane/ev-omijamy.csv`, 97 fraz)

- **Dopłaty i programy:** NaszEauto („naszeauto” 14 800/mies.), Mój Elektryk („mój elektryk” 2 400, „moj elektryk” 2 900), „dofinansowanie do samochodu elektrycznego” 4 400, „dopłaty do elektryków” 2 900, dotacje do stacji i wallboxów, warunki, wnioski [W].
- **Ulgi i podatki:** VAT, odliczenia, amortyzacja, akcyza, rozliczanie ładowania w firmie i w domu („jak rozliczyć ładowanie samochodu elektrycznego w domu” 110), samochód na firmę [W].
- **Leasing, wynajem długoterminowy, abonament na auto** („leasing elektryka” 170, „wynajem długoterminowy samochodu elektrycznego” 320) [W][K].
- **Ubezpieczenia** („ubezpieczenie samochodu elektrycznego” 140) [K].
- **Przepisy:** strefy czystego transportu, buspasy („czy samochody elektryczne mogą jeździć buspasem” 170), zielone tablice, darmowe parkowanie, przepisy o ładowaniu w garażach podziemnych i wspólnotach, odbiory UDT, obowiązki operatorów, AFIR jako temat [K].
- **Taryfy prądu jako porównywarka:** zmiany taryf, umowy, net-billing. W kalkulatorze tylko pole „cena prądu” wpisywane przez użytkownika.
- **Wzory dokumentów:** umowy, zgody wspólnoty, wnioski. Nie robimy.

## 8. Ocena wg `METODA.md`

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 3 | 1 023 820/mies., ale do wzięcia 88 650/mies. i −2,1% r/r [W] |
| Słabość SERP | 25% | 4 | 20 z 20 spełnia kryterium; AIO cytuje małe serwisy w 11 z 20; minus bezpośredni konkurent na EIPA [S][B] |
| Zarobek | 25% | 1 | brak programów ze stawką; Ceneo 0,20 zł / 1,05%; leady wykluczone; 27–380 zł/mies. |
| Fosa danych / narzędzia | 15% | 4 | EIPA (ceny, dostępność, lokalizacje; licencja niepotwierdzona), EEA CC BY, OSM ODbL; fosa niewyłączna |
| Niskie ryzyko | 15% | 3 | AIO 15 z 20, zależność od EIPA, konkurent; YMYL niski po wyłączeniu tematów prawnych |
| **Wynik ważony** | | **2,9** | 0,6 + 1,0 + 0,25 + 0,6 + 0,45 |

W `A-technologia.md` EV miało 3,35. Spadek wynika z dwóch rzeczy sprawdzonych dziś: braku programów partnerskich i istniejącego serwisu, który robi model paliwowni na danych EIPA.

## Czego nie sprawdzono

- Licencji EIPA na piśmie (wymaga pytania do UDT) i statusu EIPA jako krajowego punktu dostępu z AFIR.
- Zawartości plików EIPA (liczby stacji, operatorów, kompletności cen): wymaga rejestracji konta.
- Pól zbioru EEA per pojazd u źródła (PDF metadanych i API EEA blokowane przez proxy); tylko podsumowanie WebSearch.
- Stawek x-kom (arkusz Google), Amazon.pl, programów sklepów z wallboxami (brak publicznych stron; pytanie = kontakt z firmą).
- RPM display dla PL.
- SERP-ów nazw modeli („byd seal”, „tesla model y”) i stron pojedynczych stacji.
- Krzywej CTR SEO Inc. (przejęta z `druk3d.md`).
- Popytu na płatne produkty (alert cen, raporty).

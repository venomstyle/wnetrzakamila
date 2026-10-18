# Nisze B: natura i outdoor (18.10.2026)

Metoda: `research/nisze/METODA.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie dane pobrane 18.10.2026.

Skróty źródeł (każda liczba w tekście ma jeden z nich):

- **[SV]** `/v3/keywords_data/google_ads/search_volume/live`, okres 10.2024–09.2026, średni wolumen miesięczny z ostatnich 12 mies., CPC w USD.
- **[SERP]** `/v3/serp/google/organic/live/advanced`, depth 10, desktop.
- **[BL]** `/v3/backlinks/bulk_referring_domains/live` (domeny linkujące do całej domeny lub subdomeny z top 10).
- **[TR]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (szacowany ruch organiczny w PL, ETV/mies.).
- **[WS]** WebSearch 18.10.2026 (programy partnerskie, licencje danych). Źródła podane przy liczbie.

Dane surowe: `research/nisze/dane/B-*.csv` (wolumeny, miesiące, top 10 z domenami linkującymi, elementy SERP, ruch liderów).

## Tabela ocen

Skala 1–5, 5 = najlepiej. Wagi z METODA.md: popyt 20%, słabość SERP 25%, zarobek 25%, fosa 15%, niskie ryzyko 15%.

| Nisza | Popyt i trend | Słabość SERP | Zarobek | Fosa danych / narzędzia | Niskie ryzyko | **Wynik ważony** |
|---|---|---|---|---|---|---|
| 3. Kamping, kampery, vanlife | 3 | 4 | 4 | 3,5 | 4 | **3,7** |
| 2. Wędkarstwo | 3 | 4 | 2,5 | 3 | 3 | **3,1** |
| 4. Szlaki górskie i schroniska | 5 | 2 | 3 | 3 | 2 | **3,0** |
| 5. Ptaki Polski | 3 | 3 | 2 | 3 | 4 | **2,9** |
| 1. Grzybobranie | 3 | 2 | 1 | 3 | 1 | **2,0** |

Zestawienie liczbowe (rdzeń oczyszczony z fraz wieloznacznych, opis niżej):

| Nisza | Fraz w rdzeniu | Suma wolumenu [SV] | Trend lip–wrz 2026 vs 2025 [SV] | Max/min miesiąc [SV] | Ważony CPC [SV] | Mediana dom. linkujących top 10 [SERP+BL] | Wyniki <50 dom. [SERP+BL] | AIO w 5 SERP [SERP] |
|---|---|---|---|---|---|---|---|---|
| Grzybobranie | 53 | 444 350 | −6,4% | 09.2026: 1 845 620 / 02.2026: 72 600 (×25) | 0,09 | 1 745 | 1 z 40 | 3 z 5 |
| Wędkarstwo | 51 | 504 420 | −11,9% | 08.2026: 782 080 / 02.2026: 259 200 (×3,0) | 0,19 | 146 | 14 z 43 | 3 z 5 |
| Kamping | 44 | 321 950 | −1,9% | 07.2026: 811 300 / 12.2025: 101 510 (×8,0) | 0,23 | 204 | 4 z 45 | 3 z 5 |
| Szlaki | 46 | 1 162 820 | +4,1% | 08.2026: 2 357 500 / 03.2026: 744 800 (×3,2) | 0,57 | 1 708 | 5 z 40 | 5 z 5 |
| Ptaki | 42 | 479 690 | −13,4% (poza sezonem; 12 mies. r/r +3,3%) | 01.2026: 713 480 / 09.2026: 311 750 (×2,3) | 0,14 | 1 082 | 3 z 36 | 3 z 5 |

Uwagi do liczb:

- Rdzeń oczyszczony pomija frazy o innym głównym znaczeniu: „sum”, „karp” (matematyka, kuchnia), „kruk”, „bocian”, „sowa”, „kos” (marki i nazwiska), „śnieżka”, „rysy” (farby, rysy na lakierze), „camping” (głównie wyjazdy za granicę), sprzęt („namiot”, „śpiwór”, „lodówka turystyczna”), „zabudowa busa” (SERP pokazał zabudowy warsztatowe). Pełne sumy z tymi frazami: grzyby 495 550, wędkarstwo 570 620, kamping 653 950, szlaki 1 468 720, ptaki 915 790 [SV].
- 4 frazy nie miały danych w Google Ads: „muchomor czerwony”, „grzyby z nazwami”, „stacja serwisowa dla kamperów”, „czas przejścia szlaku” [SV].
- Domeny linkujące liczone są dla całej domeny lub subdomeny [BL]. Subdomeny kół PZW (np. kartuzy.pzw.pl) mają 0, choć stoi za nimi marka PZW. Platformy (Facebook, YouTube, Wikipedia) zawyżają mediany.
- Rozszerzania fraz przez `keyword_ideas` nie robiłem; rdzeń to 50–55 fraz na niszę ułożonych ręcznie.

---

## 1. Grzybobranie

### Popyt
- Rdzeń 53 frazy: 444 350 wyszukiwań/mies. średnio [SV]. Trend lip–wrz 2026 vs 2025: −6,4%; 12 mies. vs poprzednie 12 mies.: −26,9% [SV]. Spadek zależy od pogody: październik 2025 dał 1 810 700 wyszukiwań w całym koszyku, a luty 2026 tylko 101 400 [SV].
- Sezon skrajny: wrzesień 2026 to 25 razy więcej niż luty 2026 [SV]. Ruch skupia się w 6–8 tygodniach.
- Top frazy [SV]: grzybobranie 49 500 (CPC 0,18), grzyby 33 100, rydz 27 100, muchomor sromotnikowy 27 100, podgrzybek 22 200, mapa grzybów 22 200 (CPC 0,31), goryczak żółciowy 18 100, borowik ceglastopory 18 100, borowik szatański 18 100, gdzie na grzyby 14 800 (CPC 0,38), gdzie są grzyby 9 900 (CPC 0,48), atlas grzybów 5 400.
- Frazy „gatunek + rozpoznawanie” są duże, frazy narzędziowe małe: aplikacja do rozpoznawania grzybów 880, rozpoznawanie grzybów 320, kiedy zbierać grzyby 110 [SV].

### SERP
5 fraz: gdzie są grzyby (narzędzie), podgrzybek (encja), muchomor sromotnikowy (encja, YMYL), atlas grzybów, jak suszyć grzyby [SERP].
- Mediana domen linkujących w top 10: 1 745; tylko 1 wynik z 40 ma <50 domen (gdzienagrzyby.com.pl, 2 domeny) [SERP+BL].
- 8 z 40 wyników to PDF, wpisy sprzed 2023 lub stare strony (np. polskazachwyca.pl z 2017, podroze.onet.pl z 2021, PDF Lasów Państwowych) [SERP].
- Kto wygrywa: portale i serwisy medyczne. Przy muchomorze sromotnikowym są Wikipedia, medonet.pl (7 089 domen), mp.pl (10 164), polmed.pl, recepta.pl [SERP+BL]. Przy podgrzybku: panel wiedzy z Wikipedii, YouTube, melisa.pl, wylecz.to, ekologia.pl (4 282 domen) [SERP+BL].
- Narzędzia już istnieją: grzyboradar.pl (mapa prawdopodobieństwa, prognoza 5 dni), sezonnagrzyby.pl (mapa zgłoszeń, ETV 9 597), gdzienagrzyby.com.pl, grzyby.pl (raporty wg województw, ETV 69 693) [SERP, TR].
- AI Overview: 3 z 5 (gdzie są grzyby, atlas grzybów, jak suszyć grzyby). AIO przy „gdzie są grzyby” cytuje małe serwisy: grzyby.pl, grzyboradar.pl, sezonnagrzyby.pl [SERP]. Przy gatunkach AIO nie było, jest panel wiedzy.

### Zarobek
- Ważony CPC 0,09 USD, najwyższy 0,48 („gdzie są grzyby”) [SV]. Reklamodawcy prawie nie płacą.
- Możliwa afiliacja: suszarki do grzybów (w SERP „jak suszyć” są euro.com.pl i mediaexpert.pl), atlasy książkowe (empik, allegro w SERP „atlas grzybów”) [SERP]. Programów partnerskich nie sprawdzałem szczegółowo; przy tak niskim CPC i krótkim sezonie nie zmieniłyby oceny.
- Brak leadów, brak sensownego własnego produktu (płatny atlas przegrywa z darmowymi aplikacjami: „Atlas grzybów Classic”, 5 744 ocen w Google Play [SERP]).

### Fosa danych
- Lista grzybów dopuszczonych do obrotu: załącznik 1 do rozporządzenia Ministra Zdrowia, tekst jednolity Dz.U. 2023 poz. 2237, zmiana Dz.U. 2025 poz. 1797 [WS: api.sejm.gov.pl/eli/acts/DU/2023/2237, gov.pl/web/wsse-poznan/grzyby]. Akty normatywne nie są przedmiotem prawa autorskiego (art. 4 ustawy o prawie autorskim).
- GBIF (występowanie gatunków): większość zbiorów CC BY lub CC0, część CC BY-NC; licencję trzeba sprawdzać per zbiór, NC odpada [WS: gbif.org/terms, data-blog.gbif.org/post/gbif-occurrence-license-processing].
- Dane pogodowe do prognozy (IMGW): licencji na użycie komercyjne nie ustaliłem [WS].
- Ocena 3: gatunki da się zbudować z otwartych źródeł, ale mapa i prognoza już istnieją u konkurencji.

### Ryzyko
- **YMYL wysokie.** Strona encji gatunku to de facto porada „jeść / nie jeść”. W SERP „muchomor sromotnikowy” są serwisy medyczne, a polmed.pl podaje, że ten gatunek odpowiada za ponad 95% śmiertelnych zatruć grzybami w Polsce [SERP, snippet polmed.pl z 24.10.2025]. Błąd w opisie może kogoś zabić; Google premiuje tu źródła medyczne.
- AIO przy atlasie sam ostrzega, by nie decydować o zjedzeniu na podstawie atlasu w telefonie [SERP].
- Prawo: zbieranie w parkach narodowych i gatunki chronione to treść prawna (decyzja właściciela).
- Sezon ×25 i spadek r/r −26,9% zależny od pogody [SV].

### Pomysł na serwis (3 zdania)
Huby: grzyby jadalne, trujące, chronione oraz „sobowtóry” (pary do pomylenia), plus przetwory. Narzędzie: kalendarz sezonu gatunków z mapą zgłoszeń. Strony encji: gatunki z listy rozporządzenia i z GBIF, każda z blokiem „z czym możesz pomylić” i odesłaniem do klasyfikatora grzybów w sanepidzie.

### Werdykt
**Odrzucić jako główny serwis.** Zero zarobku (CPC 0,09), YMYL na stronach encji i gotowe narzędzia u konkurencji. Ewentualnie sezonowy moduł przetworów w innym serwisie kulinarnym.

---

## 2. Wędkarstwo

### Popyt
- Rdzeń 51 fraz: 504 420/mies. [SV]. Trend lip–wrz r/r −11,9%; 12 mies. r/r −12,0% [SV]. Wiele fraz gatunkowych spada o 11–18% [SV].
- Sezon umiarkowany: sierpień 2026 782 080, luty 2026 259 200 (×3,0) [SV].
- Top frazy [SV]: sklep wędkarski 135 000 (CPC 0,11), szczupak 27 100, sandacz 27 100, kalendarz brań 27 100 (CPC 0,54), łowisko 22 200 i łowiska 22 200 (obie +43% r/r), leszcz 18 100, pstrąg 18 100, wędkarstwo 14 800, spinning 14 800, łowiska komercyjne 12 100, pzw 12 100 (CPC 1,59), boleń 12 100 (CPC 0,58).
- Frazy prawne: karta wędkarska 8 100 (−33%), egzamin na kartę wędkarską 1 600, okresy ochronne ryb 880, wymiary ochronne ryb 590 [SV].

### SERP
5 fraz: kalendarz brań (narzędzie), sandacz (encja), łowiska (encja/katalog), okresy ochronne ryb (prawo), karta wędkarska [SERP].
- Mediana domen linkujących: 146; 14 z 43 wyników ma <50 domen [SERP+BL]. 8 z tych 14 to subdomeny pzw.pl (zastrzeżenie wyżej).
- Najsłabsze SERP-y: „karta wędkarska” (mediana 0; szablonowe strony kół PZW, stara strona old.pzwszczecin.com) i „okresy ochronne ryb” (mediana 29; PZW, decathlon.pl, małe stowarzyszenia, fishradar.pl z 35 domenami) [SERP+BL].
- „Kalendarz brań”: angloo.com (1 825 domen), sklep moonfin.pl, fishster.pl (207), łowienie.pl (74), gdybyryby.pl (57), blog insel.pl z 2018, dokument na scribd.com; mediana 207 [SERP+BL].
- „Łowiska”: znajdzlowisko.pl (132 domeny, a ETV 57 885), pojedyncze łowiska, 2 profile Facebook, forum spławikigrunt.pl z 2021 [SERP, BL, TR]. Katalog z małą liczbą linków zbiera duży ruch.
- „Sandacz”: Wikipedia, blog sklepu sklep-mietus.pl, ryby.wwf.pl, sklepy spożywcze i przepisy (intencja mieszana) [SERP].
- 6 z 43 wyników to fora, PDF lub wpisy sprzed 2023; 10 to sklepy [SERP].
- AI Overview: 3 z 5. Przy „okresy ochronne ryb” AIO podaje pełną tabelę wymiarów i okresów; przy „kalendarz brań” cytuje małe serwisy (amatorskie-wedkowanie.pl, fishster.pl, angloo.com, corona-fishing.pl); przy „łowiska” jest AIO ładowane asynchronicznie [SERP].

### Zarobek
- Ważony CPC 0,19 USD (bez „sum” i „karp”) [SV]. Wyżej: pzw 1,59, mapa łowisk 0,79, boleń 0,58, kalendarz brań 0,54 [SV].
- Sklepy wędkarskie piszą blogi pod te frazy (moonfin.pl, sklep-mietus.pl, sklep.ekagro.pl, sklep.insel.pl) [SERP], więc rynek sprzedaży istnieje. **Polskiego programu partnerskiego sklepu wędkarskiego nie potwierdziłem** (WebSearch zwrócił tylko programy zagraniczne) [WS].
- Model, który działa u konkurencji: katalog łowisk komercyjnych (znajdzlowisko.pl, fishster.pl). Płatne wyróżnienie łowiska to możliwy własny produkt; cen ani modelu konkurencji nie sprawdzałem.
- Ocena 2,5: popyt zakupowy jest (sklep wędkarski 135 000), ale bez potwierdzonej afiliacji.

### Fosa danych
- Wymiary i okresy ochronne: rozporządzenie Ministra Rolnictwa i Rozwoju Wsi (z 12.07.2023 według wedkarski.com) oraz regulaminy okręgów PZW [SERP, AIO]. Akt prawny jest wolny od praw autorskich; regulaminy PZW to fakty, ale treść prawna.
- Kalendarz brań: fazy Księżyca i wschody Słońca da się policzyć lokalnie, bez licencji. Dane pogodowe IMGW: licencji nie ustaliłem [WS].
- Łowiska i obwody rybackie: otwartego rejestru nie znalazłem (API dane.gov.pl blokowane przez proxy w tej sesji). OSM ma obiekty wędkarskie na licencji ODbL, użycie komercyjne dozwolone z atrybucją [WS: osmfoundation.org/wiki/Licence_and_Legal_FAQ]; kompletności nie sprawdzałem.
- Gatunki ryb: GBIF (CC BY/CC0 per zbiór) [WS].

### Ryzyko
- **Treść prawna w rdzeniu**: karta wędkarska, egzamin, wymiary, okresy ochronne, kary. Bez zgody właściciela na treści prawne odpada ok. 11 000 wyszukiwań/mies. i najsłabsze SERP-y [SV].
- AIO podaje gotową tabelę okresów ochronnych [SERP]; strona z tabelą straci kliknięcia.
- Spadek r/r −12% [SV].
- YMYL niski.

### Pomysł na serwis (3 zdania)
Huby: gatunki ryb, łowiska wg województw, metody i sprzęt. Narzędzie: kalendarz brań liczony dla lokalizacji (Księżyc, Słońce, ciśnienie) z oceną dnia, a w wersji z treścią prawną także „czy dziś mogę łowić ten gatunek w tym okręgu”. Strony encji: ok. 40 gatunków ryb oraz katalog łowisk komercyjnych z płatnym wyróżnieniem.

### Werdykt
**Warunkowo tak.** SERP najsłabszy z pięciu (mediana 146), ale zarobek zależy od własnego katalogu łowisk, a najlepsze frazy są prawne. Decyzja właściciela o treściach prawnych przesądza.

---

## 3. Kamping, kampery i vanlife w Polsce

### Popyt
- Rdzeń 44 frazy: 321 950/mies. [SV]. Trend lip–wrz r/r −1,9%; 12 mies. r/r −2,9% [SV]. Stabilnie.
- Sezon: lipiec 2026 811 300, grudzień 2025 101 510 (×8,0) [SV]. Planowanie zaczyna się od lutego–marca (luty 2026: 307 860 w pełnym koszyku) [SV].
- Top frazy [SV]: pole namiotowe 110 000, kemping 49 500 (+8%), kamper 33 100, przyczepa kempingowa 33 100, glamping 22 200, pole kempingowe 22 200 (+20%), wynajem kampera 8 100 (−26%), zanocuj w lesie 6 600 (+22%, CPC 2,32), wypożyczalnia kamperów 4 400, park4night 3 600 (CPC 1,90), biwak 2 900 (+18%), wynajem kampera cena 1 600, ile kosztuje wynajem kampera 880 (+19%).
- Frazy z „camping” (246 000) dotyczą głównie wyjazdów za granicę; liczę je osobno [SV].

### SERP
5 fraz: wynajem kampera (lead), ile kosztuje wynajem kampera (kalkulator), gdzie można stanąć kamperem (narzędzie/mapa), kemping mazury (encja), zabudowa busa [SERP].
- Mediana domen linkujących: 204; 4 z 45 wyników <50 domen [SERP+BL].
- **30 z 45 wyników to firmy** (wypożyczalnie, kempingi, producenci, ogłoszenia) [SERP]. W „wynajem kampera” cały top 10 to małe wypożyczalnie (43–168 domen) i OLX; mediana 79,5; nie ma porównywarki ani poradnika [SERP+BL].
- „Ile kosztuje wynajem kampera”: cenniki wypożyczalni, OLX, rankomat.pl (artykuł z 29.09.2026), camperdays.pl (68 domen); mediana 108 [SERP+BL].
- „Gdzie można stanąć kamperem”: camping.info, blog centrumcaravaningu.pl, stara strona pfcc.eu, wroclaw.pl z 2022, blogi wypożyczalni [SERP]. Wolumen tej frazy to tylko 10, ale temat ma park4night 3 600 i zanocuj w lesie 6 600 [SV].
- „Kemping mazury”: Local Pack, camprest.com (2 319 domen, ETV 21 289), polskicaravaning.pl, holidu.pl, strony kempingów [SERP, BL, TR].
- AI Overview: 3 z 5, wszystkie ładowane asynchronicznie (ile kosztuje, gdzie stanąć, zabudowa busa); przy „wynajem kampera” i „kemping mazury” AIO nie było [SERP].
- Uwaga: „zabudowa busa” (1 600) to zabudowy warsztatowe, intencja nie pasuje do vanlife [SERP, SV].

### Zarobek
- Wysoka wartość transakcji: wynajem kampera „od około 400 zł do 1000 zł za dobę” [SERP, snippet rankomat.pl z 29.09.2026]; cenniki 330–690 zł/doba w snippetach wypożyczalni [SERP].
- Reklamy: ważony CPC 0,23 USD, ale wyraźnie wyżej przy frazach zakupowych: ubezpieczenie kampera 3,08, zanocuj w lesie 2,32, park4night 1,90, kamping chorwacja 1,22, zabudowa busa 0,59 [SV]. Google Ads Transparency dla „wynajem kampera”: brak wyników [`/v3/serp/google/ads_advertisers/live/advanced`].
- Afiliacja: CamperDays ma program w Awin (UK: 3% od rezerwacji, średnio ok. 88 EUR, plus 8 EUR za lead) [WS: ui.awin.com/merchant-profile/52885]; **wersji polskiej nie potwierdziłem**. Booking.com: ok. 4% od noclegu przez CJ lub Awin według źródeł branżowych, oficjalnie niepotwierdzone [WS: skift.com 30.05.2025, marketplace.referly.so]. Yescapa: programy UK i ES oznaczone jako zamknięte, Polski brak [WS: affi.io/m/yescapa].
- Leady: dziesiątki małych wypożyczalni bez porównywarki w SERP [SERP]. Płatny wpis lub zapytanie ofertowe do wypożyczalni wg miasta to realny model (bez zimnych maili; tylko firmy, które same się zgłoszą).
- Ocena 4.

### Fosa danych
- OSM: kempingi i camper parki (tourism=camp_site, caravan_site), ODbL, komercyjnie dozwolone z atrybucją; własne uzupełnienia bazy trzeba udostępniać na tej samej licencji [WS: osmfoundation.org/wiki/Licence_and_Legal_FAQ, wiki.openstreetmap.org/wiki/License/Use_Cases].
- Program „Zanocuj w lesie” Lasów Państwowych: 425 obszarów, 600 ha [SERP, snippet caravanya.com; dane z 01.05.2021, liczba mogła się zmienić]. Formatu i licencji danych (BDL) nie ustaliłem [WS].
- Centralny Wykaz Obiektów Hotelarskich na dane.gov.pl: według gov.pl obejmuje głównie hotele (ok. 3 500); czy ma kempingi, nie potwierdziłem [WS: gov.pl/web/cyfryzacja/przydatne-wakacyjne-porady-z-danegovpl].
- Camping.info pokazuje 349 kempingów w Polsce [SERP, snippet] (dane prywatne, nie do kopiowania; tylko orientacyjna skala).
- Narzędzia bez licencji: kalkulator kosztu wyjazdu kamperem (doby, kaucja, paliwo, opłaty), sprawdzarka „czy kamper mieści się w kat. B (3,5 t)”.

### Ryzyko
- YMYL niskie. Treść prawna w małej skali: dopuszczalna masa i prawo jazdy, biwakowanie w lesie, postój na parkingu (decyzja właściciela).
- AIO 3 z 5, ale tylko asynchroniczne; frazy lokalne i zakupowe mają Local Pack zamiast AIO [SERP].
- Sezon ×8 [SV]. Część zarobku zależy od programów, których polskiej wersji nie potwierdziłem.

### Pomysł na serwis (3 zdania)
Huby: wynajem kampera (koszty, wymogi, wypożyczalnie wg miast), noclegi kamperem i z namiotem (kempingi, camper parki, „Zanocuj w lesie”), trasy po regionach. Narzędzie: kalkulator kosztu wyjazdu kamperem i mapa miejsc noclegowych z OSM z filtrem (prąd, zrzut nieczystości, psy). Strony encji: kempingi i pola namiotowe z OSM oraz strony „wynajem kampera [miasto]” z listą wypożyczalni i formularzem zapytania.

### Werdykt
**Najlepszy kandydat z pięciu.** Słaby, firmowy SERP przy frazach z pieniędzmi, wysoka wartość transakcji i otwarte dane OSM. Przed startem trzeba potwierdzić polskie programy partnerskie (CamperDays, Booking, ubezpieczenia).

---

## 4. Szlaki górskie i schroniska

### Popyt
- Rdzeń 46 fraz: 1 162 820/mies., największy w grupie [SV]. Trend lip–wrz r/r +4,1%; 12 mies. r/r −2,8% [SV].
- Sezon umiarkowany: sierpień 2026 2 357 500, marzec 2026 744 800 (×3,2) [SV].
- Top frazy [SV]: morskie oko 246 000, kasprowy wierch 135 000 (CPC 1,06), babia góra 90 500 (CPC 1,22), mapa turystyczna 90 500 (CPC 0,74), giewont 74 000, korona gór polski 60 500, hala gąsienicowa 60 500 (+78%), ślęża 49 500, schronisko samotnia 33 100, orla perć 33 100 (+69%), schronisko 27 100, czerwone wierchy 27 100 (+34%), tpn bilety 8 100 (+29%), schronisko murowaniec 6 600 (−52%).

### SERP
5 fraz: szlak na rysy (encja trasy), schronisko murowaniec (encja), czas przejścia szlaku (narzędzie), szlaki dla początkujących, warunki w tatrach [SERP].
- Mediana domen linkujących: 1 708; 5 z 40 wyników <50 domen [SERP+BL]. 10 z 40 to Facebook, YouTube, Instagram lub Reddit [SERP].
- Najsłabszy: „czas przejścia szlaku” (mediana 134; blog mapa-turystyczna.pl, kalkulatorxxl.pl z 10 domenami, stary kalkulator szlaki.net.pl, Reddit) [SERP+BL].
- Silni liderzy: hasajacezajace.com (ETV 606 781, 2 503 domen), mapa-turystyczna.pl (ETV 328 434), gorydlaciebie.pl (ETV 109 726), portaltatrzanski.pl (ETV 37 311) [TR, BL].
- „Schronisko murowaniec”: strona oficjalna, Facebook, Wikipedia, mapy.com, Instagram, pttk.pl; panel wiedzy z 10 550 opiniami Google [SERP].
- AI Overview: **5 z 5**. Przy „szlak na rysy” AIO podaje długość, czas, przewyższenie i sezon; przy „warunki w tatrach” streszcza bieżący komunikat TPN; przy Murowańcu podaje miejsca, płatności i telefony [SERP]. AIO cytuje blogi (hasajacezajace.com, mynaszlaku.pl, gorydlaciebie.pl, climb2change.pl) [SERP].

### Zarobek
- Ważony CPC 0,57 USD, najwyższy w grupie [SV]. Schroniska: murowaniec 1,56, na turbaczu 1,48, morskie oko 1,26, w tatrach 1,20; szlaki górskie 1,27; kasprowy wierch kolejka 1,10 [SV]. Płacą obiekty noclegowe i atrakcje.
- Afiliacja: noclegi (Booking ok. 4% przez CJ/Awin, niepotwierdzone oficjalnie [WS]); sklepy outdoorowe piszą poradniki (decathlon.pl, sportano.pl, e-horyzont.pl, triverna.pl w SERP) [SERP], ale ich programów partnerskich nie potwierdziłem [WS].
- Ocena 3: pieniądze są, ale trafiają do liderów z dużym ruchem.

### Fosa danych
- OSM: szlaki (route=hiking, operator PTTK), schroniska (tourism=alpine_hut), szczyty; ODbL [WS: wiki.openstreetmap.org/wiki/WikiProject_Poland/Tutoriale/Szlaki, osmfoundation.org].
- Geoportal PTTK: warunki korzystania nieustalone [WS].
- Komunikaty TPN i TOPR: fakty wolno streszczać, licencji na przedruk nie sprawdzałem.
- Narzędzia: kalkulator czasu przejścia i punktów GOT. Ten sam model ma już szlaki.net.pl i kalkulatorxxl.pl [SERP]; mapa-turystyczna.pl liczy trasy z danych szlaków [SERP].
- Ocena 3: dane są otwarte, ale lider robi z nich to samo.

### Ryzyko
- AIO 5 z 5 i wyczerpujące odpowiedzi [SERP]; największe ryzyko utraty kliknięć w grupie.
- Bezpieczeństwo w górach (lawiny, oblodzenie) to treść zbliżona do YMYL; błędne „warunki” mogą zaszkodzić.
- Przepisy TPN (bilety, zakazy) to treść prawna w małej skali.

### Pomysł na serwis (3 zdania)
Huby: pasma górskie, schroniska, Korona Gór Polski. Narzędzie: kalkulator czasu przejścia i GOT z planem powrotu przed zmrokiem. Strony encji: szczyty, trasy i schroniska z OSM, z dojazdem i parkingiem.

### Werdykt
**Nie jako nowy serwis.** Największy popyt, ale silni liderzy (mapa-turystyczna.pl, hasajacezajace.com) i AIO w każdym SERP. Ma sens tylko jako dodatek do niszy kampingowej (np. „kamperem pod szlak”).

---

## 5. Obserwacja przyrody, ptaki Polski

### Popyt
- Rdzeń 42 frazy: 479 690/mies. [SV]. Trend lip–wrz r/r −13,4%, ale to poza sezonem; 12 mies. r/r +3,3% [SV].
- Sezon zimowy: styczeń 2026 713 480, wrzesień 2026 311 750 (×2,3) [SV].
- Top frazy [SV]: sójka 40 500, sikorka 33 100, szpak 33 100 (−35%), karmnik dla ptaków 27 100 (+12%), wróbel 27 100, rudzik 27 100, żuraw 27 100, dudek 27 100, jastrząb 27 100, dzięcioł 22 200, zimorodek 22 200 (−38%), pustułka 22 200 (CPC 0,92), bielik 22 200.
- Frazy narzędziowe są małe: śpiew ptaków 2 900, budka dla ptaków 2 900, głosy ptaków 1 600, lornetka do obserwacji ptaków 1 600 (CPC 0,68), birdwatching 1 300 (CPC 1,62), atlas ptaków 1 000, aplikacja do rozpoznawania ptaków 720, czym karmić ptaki zimą 480, rozpoznawanie ptaków 210 [SV].

### SERP
5 fraz: rozpoznawanie ptaków (narzędzie), jemiołuszka (encja), karmnik dla ptaków, czym karmić ptaki zimą, głosy ptaków (narzędzie) [SERP].
- Mediana domen linkujących: 1 082; 3 z 36 wyników <50 domen [SERP+BL]. 9 z 36 to wpisy sprzed 2023, stare strony lub http (np. ptaki.info, benchmark.pl i mobirank.pl z 2021) [SERP].
- Strona encji „jemiołuszka”: panel wiedzy, posty Facebook, iStock, ptaki.info (stary atlas na php, 432 domen, a ETV 27 427), iNaturalist, blog sklepu furgo.pl [SERP, BL, TR]. Treści słabe, ale domeny mocne (mediana 46 077 przez platformy).
- „Głosy ptaków”: glosy-ptakow.pl (346 domen, ETV 37 977, narzędzie BirdID), YouTube, avesnature.com.pl [SERP, BL, TR].
- „Karmnik dla ptaków”: sklepy (mediana 195) [SERP+BL].
- AI Overview: 3 z 5 (rozpoznawanie asynchronicznie, czym karmić, głosy). AIO przy „głosy ptaków” cytuje małe serwisy glosy-ptakow.pl i avesnature.com.pl [SERP].

### Zarobek
- Ważony CPC 0,14 USD [SV]. Wyżej tylko niszowe frazy: birdwatching 1,62, pustułka 0,92, czym karmić ptaki zimą 0,76, lornetka do obserwacji ptaków 0,68 [SV]. „Bocian” 3,66 to marka finansowa, nie ptak [SV].
- Afiliacja: karmniki, karma, budki, lornetki; sklepy w SERP (legutko, 4iq, fabrykaform, kropkasklep) [SERP]. Programów nie potwierdzałem.
- Ocena 2: niskie koszyki i niska intencja zakupowa.

### Fosa danych
- GBIF: występowanie gatunków, większość zbiorów CC BY lub CC0 [WS: gbif.org/terms].
- **Nagrania głosów z xeno-canto odpadają**: większość na licencjach CC BY-NC (w tym NC-SA, NC-ND), licencja per nagranie [WS: xeno-canto.org/about/terms, en.wikipedia.org/wiki/Xeno-canto].
- Ochrona gatunkowa: rozporządzenie (akt prawny, wolny od praw autorskich).
- Zdjęcia: Wikimedia Commons (CC BY/BY-SA per plik), licencji per plik nie sprawdzałem.
- Narzędzie bez danych NC: klucz „jaki to ptak” po cechach (wielkość, kolor, miejsce, pora roku) i kalendarz przylotów. glosy-ptakow.pl ma 291 gatunków [SERP, snippet], więc skala encji to ok. 300 stron.

### Ryzyko
- YMYL niskie, prawo w małej skali (ochrona gatunkowa, zasady dokarmiania).
- AIO 3 z 5 [SERP]. Wiele nazw gatunków jest wieloznacznych (kruk, kos, sowa, bocian), co zawyża popyt [SV].
- Nagrania głosów, najbardziej angażujący format, nie mają łatwego otwartego źródła na licencji komercyjnej.

### Pomysł na serwis (3 zdania)
Huby: ptaki w ogrodzie i przy karmniku, gatunki Polski, rozpoznawanie. Narzędzie: klucz „jaki to ptak” po cechach i kalendarz „kto teraz przylatuje”. Strony encji: ok. 300 gatunków z GBIF (CC BY/CC0) i zdjęciami z Wikimedia Commons.

### Werdykt
**Nie jako główny serwis.** Słabe treści konkurencji, ale niski zarobek i brak otwartych nagrań. Może wesprzeć inny serwis sezonowo (karmniki zimą).

---

## Czego nie sprawdziłem

- Polskich programów partnerskich: CamperDays PL, Booking PL, sklepy wędkarskie, 8a.pl, Decathlon (WebSearch nie dał polskich stron) [WS].
- Licencji: IMGW, Bank Danych o Lasach, Geoserwis GDOŚ, geoportal PTTK, rejestry obwodów rybackich (dane.gov.pl niedostępne przez proxy w tej sesji).
- Rozszerzenia fraz (`keyword_ideas`) i danych z Map Google.

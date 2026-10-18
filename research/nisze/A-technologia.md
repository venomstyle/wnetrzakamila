# Nisze A: technologia (18.10.2026)

Metoda: `research/nisze/METODA.md`. Rynek: Polska (location_code 2616, język pl).

**Oznaczenia źródeł (wszystkie pobrane 18.10.2026):**
- **[W]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live`, średni wolumen z 12 miesięcy (10.2025–09.2026), CPC w USD. Trend r/r: suma lipiec–wrzesień 2026 wobec lipiec–wrzesień 2025 (zapytanie z `date_from` 2024-10-01).
- **[S]** DataForSEO `/v3/serp/google/organic/live/advanced`, depth 10, desktop.
- **[B]** DataForSEO `/v3/backlinks/bulk_referring_domains/live` (domeny linkujące do całej domeny, nie do podstrony).
- **[WWW]** WebSearch albo `/v3/on_page/content_parsing/live` (adres podany przy liczbie).

Surowe dane: `dane/A-wolumeny-*.csv` (246 fraz), `dane/A-wolumeny-24m.json` (24 miesiące), `dane/A-serp-top10.csv` i `dane/A-serp-notatki.txt` (31 SERP-ów), `dane/A-backlinki.csv` (163 domeny).

## Tabela ocen (1–5, 5 = najlepiej)

| Nisza | Popyt i trend (20%) | Słabość SERP (25%) | Zarobek (25%) | Fosa danych / narzędzia (15%) | Niskie ryzyko (15%) | **Wynik ważony** |
|---|---|---|---|---|---|---|
| 4. Druk 3D | 4 | 4 | 3 | 2 | 4 | **3,45** |
| 1. Samochody elektryczne | 4 | 3 | 3 | 4 | 3 | **3,35** |
| 3. Energia w domu (PV, magazyny, taryfy, pompy) | 3 | 3 | 4 | 4 | 2 | **3,25** |
| 5a. Drony | 2 | 3 | 3 | 3 | 2 | **2,65** |
| 5b. Rowery i hulajnogi elektryczne | 3 | 3 | 2 | 2 | 3 | **2,60** |
| 2. Smart home / Home Assistant | 2 | 3 | 2 | 2 | 4 | **2,55** |

Nisza 5: oceniłem drony i e-rowery osobno. Do porównania biorę drony (2,65), bo mają obowiązkowe OC z najwyższym CPC w grupie i publiczne dane stref lotów. Różnica jest jednak minimalna i obie odpadają w porównaniu z trzema pierwszymi niszami.

Trzy pierwsze wyniki dzieli 0,2 punktu. To mieści się w granicach błędu tej metody, więc decyzja zależy od tego, co właściciel woli: rosnący hobbystyczny rynek bez danych (druk 3D) albo rynek z mocną bazą danych publicznych i większym ryzykiem prawnym (EV, energia).

## Zestawienie liczb

| Nisza | Fraz | Suma wolumenu [W] | Trend r/r [W] | Najsłabszy / najmocniejszy miesiąc [W] | CPC ważony / max [W] | AIO w SERP [S] | Mediana domen linkujących top 10 (bez YouTube, Reddit, FB, GitHub, TikTok, dev.to) [S][B] | Wyniki <50 domen [B] | Wyniki sprzed 2023 [S] | Fora i social [S] |
|---|---|---|---|---|---|---|---|---|---|---|
| EV | 50 | 526 390 | +16% (+11% bez fraz o dopłatach i „greenway”) | 06.2026: 414 530 / 11.2025: 597 690 | 0,49 / 1,47 | 3 z 5 | 782 | 4 pozycje | 1 | 3 |
| Smart home | 40 | 132 080 | −3% | 06.2026: 102 010 / 01.2026: 171 960 | 0,42 / 1,77 | 2 z 5 | 862 | 3 | 2 | 4 |
| Energia | 44 | 293 990 | −15% (−12% bez „mój prąd”) | 07.2026: 203 370 / 01.2026: 419 970 | 1,36 / 3,96 | 4 z 5 | 626 | 2 | 1 | 0 |
| Druk 3D | 45 | 392 720 | +20% | 07.2026: 297 240 / 12.2025: 556 380 | 0,61 / 1,44 | 2 z 6 | 721 | 2 | 6 | 7 |
| Drony | 34 | 233 730 | −52% (−37% bez „dron”, „drony”) | 02.2026: 168 490 / 11.2025: 438 230 | 0,43 / 1,82 | 3 z 5 | 425 | 2 | 2 | 6 |
| E-rowery i hulajnogi | 33 | 438 550 | +1% | 01.2026: 161 250 / 05.2026: 704 340 | 0,29 / 0,51 | 1 z 5 | 315 | 5 | 2 | 3 |

Uwagi do liczb:
- „Suma wolumenu” to suma średnich miesięcznych wolumenów fraz rdzenia. W EV 421 000 z 526 390 to nazwy marek i modeli, w druku 3D 231 850 z 392 720 to marki, drukarki i serwisy z modelami [W]. Ruch z takich fraz trafia głównie do producentów i sklepów.
- Fraza „drony” miała skok do 301 000 we wrześniu 2025 i 201 000 w listopadzie 2025 [W]. To wygląda na ruch newsowy, dlatego podaję też trend bez niej.
- AIO „async” (Google dociąga AI Overview po załadowaniu strony) liczę jako obecne.
- W SERP-ach jest mniej niż 10 wyników organicznych, bo resztę miejsc zajmują wideo, Shopping i PAA. Dlatego w tabeli jest od 31 do 44 pozycji na niszę, a nie 50.

---

## 1. Samochody elektryczne w Polsce

**Popyt [W].** 50 fraz, suma 526 390, trend +16% r/r. Szczyt w listopadzie 2025 (597 690), dołek w czerwcu 2026 (414 530). Top frazy: „byd” 135 000, „leapmotor” 40 500, „samochód elektryczny” 33 100 (+39% r/r), „byd seal” 33 100, „greenway” 33 100 (+261% r/r), „tesla model 3” 27 100, „dacia spring” 27 100, „stacje ładowania” 18 100 (+31%), „naszeauto” 14 800 (−76%), „skoda elroq” 14 800. Frazy pod narzędzie są małe: „ile kosztuje ładowanie samochodu elektrycznego” 1 300, „koszt ładowania samochodu elektrycznego” 590, „kalkulator ładowania samochodu elektrycznego” 70, „zasięg samochodu elektrycznego zimą” 10. Popyt na dopłaty gaśnie: „naszeauto” spadło z 33 100 w styczniu 2026 do 2 400 we wrześniu 2026.

**SERP [S][B].** Frazy: „ile kosztuje ładowanie samochodu elektrycznego” (narzędzie), „naszeauto”, „najtańszy samochód elektryczny”, „skoda elroq zasięg” (encja), „ładowarka do samochodu elektrycznego”. Wygrywają: elektromobilni.pl (787 domen linkujących, w 4 z 5 SERP-ów), sklepy i producenci (wallbox.pl 158, skoda.pl 1 237, cupra.com 5 155, volkswagen.pl 1 495), portale moto (superauto.pl 1 977, moto.rp.pl 1 160, natemat.pl 20 368). Słabe wyniki: amperepoint.pl (41), forum.elektrowoz.pl (37), ingreen360.pl (37), omoda.margo.pl (31), greenkick.com.pl (64, wpis z 09.2022), otoev.pl (forum, 07.2023). AIO w 3 z 5. Cytuje małe serwisy: moya-energia.pl, amperepoint.pl, elektromobilni.pl. W SERP „ile kosztuje ładowanie” stoi kalkulator volkswagen.pl, ale nikt nie pokazuje cen operatorów na żywo.

**Zarobek.** CPC ważony 0,49 USD; najwyżej „naszeauto” 1,47, „leasing samochodu elektrycznego” 1,43, „dopłata do samochodu elektrycznego” 1,43, „greenway” 1,14 [W]. Kto płaci za reklamy: nie sprawdzono (`ads_advertisers` pominięty). Możliwe źródła: leasing i wynajem długoterminowy (w SERP są masterlease.pl, mauto.pl, superauto.pl [S]), sklepy z wallboxami, ubezpieczenia. Konkretnych polskich programów partnerskich dla leasingu EV nie sprawdziłem. Własny produkt: płatny alert cen ładowania albo raport „ile naprawdę kosztuje mój elektryk” (pomysł, nie sprawdzony popyt).

**Fosa danych.**
- EIPA (Ewidencja Infrastruktury Paliw Alternatywnych, UDT): https://eipa.udt.gov.pl/. Strona mówi, że to rejestr publiczny z lokalizacjami stacji, „aktualnymi cenami paliw alternatywnych” i dostępnością punktów, z „możliwością pobrania i przetwarzania zgromadzonych w rejestrze danych w celu udostępnienia ich na mapie” [WWW, content_parsing 18.10.2026]. Licencji nie znalazłem. Warunki dostępu do API dla użytkownika końcowego trzeba sprawdzić (nie rejestrowałem się).
- EEA, dane CO2 nowych aut (zużycie energii na model): nota prawna EEA mówi o licencji CC BY i ponownym użyciu „for commercial or non-commercial purposes” z podaniem źródła: https://www.eea.europa.eu/en/legal-notice [WWW, 18.10.2026].
- CEPiK, statystyki rejestracji: według wartowiedziec.pl rozporządzenie (§ 21) udostępnia dane statystyczne CEPiK do ponownego wykorzystywania. Samego API i licencji nie sprawdziłem.
- NaszEauto: https://naszeauto.gov.pl (regulamin, kalkulator wsparcia) jako źródło faktów, nie zbiór danych.

**Ryzyko.** Średnie. Dopłaty, leasing i ulgi to treści finansowo-prawne (właściciel jeszcze nie zdecydował, czy dozwolone). Zależność od programów rządowych pokazuje „naszeauto”: −76% r/r [W]. AIO w 3 z 5 SERP-ów. Plus: EIPA daje dane, których konkurencja w SERP nie pokazuje.

**Pomysł na serwis.** Huby: koszt ładowania (dom, stacje, taryfy), ładowarki domowe, zasięg i zima, używane elektryki, modele. Narzędzie: kalkulator kosztu 100 km z cenami operatorów z EIPA i taryfami G11/G12/dynamiczną, plus porównanie z autem spalinowym. Strony encji: każdy model (zasięg WLTP, zużycie z EEA, liczba rejestracji z CEPiK, koszt 100 km) i każdy operator stacji (ceny i liczba punktów z EIPA).

**Werdykt:** mocny kandydat, jeśli licencja i dostęp do API EIPA potwierdzą się na piśmie. Bez EIPA zostaje portal moto z dużą konkurencją.

---

## 2. Smart home / Home Assistant po polsku

**Popyt [W].** 40 fraz, suma 132 080, trend −3% r/r. Szczyt w styczniu 2026 (171 960), dołek w czerwcu 2026 (102 010). Top frazy: „home assistant” 18 100, „philips hue” 12 100, „google home” 12 100, „tuya”, „shelly”, „supla”, „tapo” po 8 100, „smart home” 6 600, „zigbee” 5 400, „sonoff” 5 400. Frazy poradnikowe po polsku są prawie zerowe: „home assistant automatyzacje” 20, „home assistant integracje” 20, „home assistant instalacja” 110. Rośnie „home assistant green” 1 900 (+167%).

**SERP [S][B].** Frazy: „home assistant instalacja”, „zigbee2mqtt”, „shelly plus 2pm” (encja), „czujnik temperatury zigbee” (encja/produkt), „inteligentny dom”. Wygrywają: YouTube (5 wyników w jednym SERP), github.com, zigbee2mqtt.io (2 710), reddit, sklepy (botland.com.pl 2 503, psmart.pl 128, rtx24.pl 121, ceneo.pl 21 063, amazon.pl 8 817), duże RTV (x-kom.pl 6 849, mediaexpert.pl 9 203). Słabe wyniki: hejsmart.pl (20, wpis 11.2024), zgranydom.pl (0 domen, a jest na 10. miejscu „home assistant instalacja”), 2 PDF-y instrukcji. Wiele wyników po angielsku. AIO w 2 z 5; cytuje hejdom.pl, techwish.pl, boneio.eu, elektrykpruszkow.pl.

**Zarobek.** CPC ważony 0,42 USD; max „frigate” 1,77, „node red” 1,70, „smart home” 1,02 [W]. Produkty tanie (czujnik Zigbee 35–80 zł w Shopping [S]). Amazon.pl ma program partnerski (stawki 1–20% zależnie od kategorii według źródeł wtórnych, np. shopify.com/pl; tabeli Amazon.pl nie sprawdziłem). Programów Botland, x-kom, Media Expert nie potwierdziłem [WWW]. Własny produkt: gotowe pakiety automatyzacji / konfiguracje (pomysł, popyt niesprawdzony).

**Fosa danych.** Słaba. Dokumentacja Home Assistant ma licencję CC BY-NC-SA 4.0 (plik LICENSE.md w repozytorium home-assistant/home-assistant.io [WWW, 18.10.2026]), więc odpada. Brak polskiego rejestru publicznego. Licencji bazy urządzeń Zigbee2MQTT i listy produktów Matter (CSA) nie sprawdziłem. Dane trzeba by budować testami własnymi.

**Ryzyko.** Niskie YMYL i niski udział AIO (2 z 5). Ryzyko praktyczne: poradniki podłączania przekaźników 230 V (bezpieczeństwo).

**Pomysł na serwis.** Huby: Home Assistant od zera, Zigbee i Matter, Shelly i Tuya, automatyzacje, oszczędzanie energii. Narzędzie: sprawdzarka „czy to urządzenie działa z HA / Zigbee2MQTT / Matter lokalnie” i generator prostych automatyzacji. Strony encji: każde urządzenie (protokół, kompatybilność, cena), ale bazę trzeba zbudować samemu.

**Werdykt:** odpada. Mały polski popyt na poradniki, tanie produkty, brak otwartych danych.

---

## 3. Energia w domu: fotowoltaika, magazyny, taryfy dynamiczne, pompy ciepła

**Popyt [W].** 44 frazy, suma 293 990, trend −15% r/r (−12% bez „mój prąd”). Szczyt w styczniu 2026 (419 970), dołek w lipcu 2026 (203 370). Top frazy: „fotowoltaika” 74 000, „pompa ciepła” 60 500, „magazyn energii” 33 100, „panele fotowoltaiczne” 27 100, „czyste powietrze” 18 100, „prosument” 12 100 (+33%), „mój prąd” 9 900 (−72%), „taryfa g11” 5 400, „pompa ciepła cena” 5 400, „falownik hybrydowy” 5 400. Rosną: „taryfa g12w” 4 400 (+42%), „tge ceny energii” 1 600 (+31%), „magazyn energii dofinansowanie” 1 000 (+84%). Frazy narzędziowe: „kalkulator zużycia prądu” 2 400, „rcem” 1 900, „kalkulator fotowoltaiki” 720, „taryfa dynamiczna” 720, „kalkulator pompy ciepła” 590, „net billing kalkulator” 140.

**SERP [S][B].** Frazy: „kalkulator fotowoltaiki” (narzędzie), „magazyn energii cena”, „taryfa dynamiczna”, „pompa ciepła koszt”, „rcem” (dane/encja). Wygrywają: koncerny energetyczne (gkpge.pl 2 831, tauron.pl 3 150, enea.pl 2 765), PSE (2 185), instalatorzy i hurtownie z kalkulatorami (columbusenergy.pl 1 016, enerad.pl 1 309, corab.pl 553, fega.pl 526), producenci (bosch-homecomfort.com 9 838, kaisai.com 2 529), obi.pl 3 155. Słabe: pvindex.pl (35 domen, 2. miejsce na „rcem”), sklep.voltforce.pl (13), ecolinker.pl (54), polska-energia.com (kalkulator z 05.2022). Forów brak. AIO w 4 z 5; cytuje także małe serwisy (pvindex.pl, kalkulatormocy.pl, enerad.pl, energetycznyprojekt.pl). Na „rcem” AIO wypisuje wartości miesięczne z PSE, więc sama tabela liczb traci kliknięcia.

**Zarobek.** Najwyższe CPC w grupie: ważony 1,36 USD; „depozyt prosumencki” 3,96, „fotowoltaika” 3,24, „prosument” 2,56, „rynkowa cena energii” 2,28 [W]. Rynek leadów istnieje: ogłoszenia na gramwzielone.pl oferują leady PV i pomp ciepła, np. 50 zł za lead albo 25 sztuk za 500 zł (ogłoszenia sprzedawców, ceny niezweryfikowane) [WWW]. Programów poleceń sprzedawców prądu z taryfą dynamiczną nie sprawdziłem. Uwaga: sprzedaż leadów instalatorom to model „zlecenia dla fachowców”, który jest na liście wykluczeń portfela.

**Fosa danych.**
- PSE, RCE i RCEm: https://www.pse.pl/oire/rcem-rynkowa-miesieczna-cena-energii-elektrycznej oraz API https://api.raporty.pse.pl/ (strona API działa [WWW, content_parsing 18.10.2026]). Licencji i warunków ponownego użycia nie znalazłem. Do potwierdzenia.
- PVGIS (JRC, Komisja Europejska): API z limitem 30 zapytań na sekundę na IP (strona JRC „API non-interactive service” [WWW, content_parsing 18.10.2026]). Noty prawnej JRC nie sprawdziłem; katalog danych JRC dla innego zbioru mówi, że ponowne użycie jest dozwolone z podaniem źródła.
- URE: taryfy OSD i sprzedawców z urzędu to dokumenty urzędowe (art. 4 ustawy o prawie autorskim wyłącza je spod ochrony). Formatu i dostępności zbiorów nie sprawdzałem.
- TGE (ceny RDN): warunków nie sprawdziłem.

**Ryzyko.** Wysokie. Opłacalność inwestycji za 20–60 tys. zł to YMYL finansowy; net-billing, taryfy i dotacje (Mój Prąd, Czyste Powietrze) to treści prawne. AIO w 4 z 5. Pompy ciepła i PV zahaczają o wykluczoną budowlankę i remont oraz o leady dla fachowców. Popyt spada (−15% r/r) i zależy od programów dotacji („mój prąd” −72%).

**Pomysł na serwis.** Huby: net-billing i ceny RCE, magazyny energii, taryfy dynamiczne, pompa ciepła w liczbach, zużycie prądu w domu. Narzędzie: kalkulator opłacalności PV z magazynem w net-billingu na godzinowych cenach RCE (PSE) i produkcji z PVGIS dla adresu, plus symulator taryfy dynamicznej dla profilu zużycia. Strony encji: miesięczne i dzienne strony RCE/RCEm, taryfy sprzedawców i OSD, strony miast z produkcją PV z PVGIS.

**Werdykt:** najlepszy zarobek i dobre dane, ale najwyższe ryzyko i konflikt z wykluczeniami. Tylko jeśli właściciel zgodzi się na treści prawno-finansowe i wyłączy model leadów dla instalatorów.

---

## 4. Druk 3D

**Popyt [W].** 45 fraz, suma 392 720, trend +20% r/r. Szczyt w grudniu 2025 (556 380), dołek w lipcu 2026 (297 240), czyli sezon prezentów. Top frazy: „drukarka 3d” 90 500 (+49%), „thingiverse” 40 500 (−29%), „makerworld” 40 500 (+109%), „bambu lab” 33 100 (+32%), „printables” 27 100, „długopis 3d” 27 100, „bambu lab a1” 18 100, „prusa” 14 800, „bambu lab a1 mini” 12 100, „druk 3d” 8 100. Frazy pod narzędzie i poradnik: „ile kosztuje druk 3d” 4 400 (+118%), „kalkulator druku 3d” 260 (+189%), „suszarka do filamentu” 2 400 (+41%), „filament petg” 1 600 (+48%), „pla czy petg” 110.

**SERP [S][B].** Frazy: „jaka drukarka 3d”, „bambu lab a1 mini” (encja), „ile kosztuje druk 3d” (narzędzie), „pla czy petg”, „drukarka 3d ranking”. Wygrywają: sklepy (botland.com.pl 2 503, x-kom.pl 6 849, morele.net 9 709, ceneo.pl, x3dshop.com 1 773, eu.store.bambulab.com 1 084), allegro.pl, reddit i YouTube. Słabości: najwięcej starych i forumowych wyników w grupie (6 sprzed 2023, 7 forów i social). „drukarka 3d ranking” ma na 8. miejscu ranking z 05.2014 (businesstraveller.pl, 352 domeny), są wątki forbot.pl (06.2024) i astropolis.pl (01.2024). „jaka drukarka 3d” ma tylko 6 wyników organicznych, w tym 3don.pl z 06.2020 i elektroda.pl z 05.2023. Małe serwisy w top 10: bambulab.get3d.pl (12), 3done.tech (42), pcmod.pl (kalkulator, 509), 3dwpraktyce.pl (244). AIO w 2 z 6; cytuje 3lian.pl, centrumdruku3d.pl, craft3d.pl, geometryhustlers.pl.

**Zarobek.** CPC ważony 0,61 USD; max „druk 3d na zamówienie” 1,44, „orcaslicer” 1,29, „makerworld” 1,26, „thingiverse” 1,19, „druk 3d” 1,11 [W]. Bambu Lab ma program partnerski w sieci Awin (profil https://ui.awin.com/merchant-profile/46345: prowizja od sprzedaży, okno 15 dni, różne stawki na drukarki, filamenty i płyty; procentów nie podano) [WWW]. Ceny drukarek: Bambu Lab A1 mini od 825,67 zł w sklepie Bambu Lab, 845 zł w Botland [S]. Inne programy (3DJake, polscy producenci filamentów) nie sprawdzone. Własny produkt: płatna wersja kalkulatora kosztu wydruku dla małych pracowni, profile druku (pomysł).

**Fosa danych.** Słaba. Brak rejestru publicznego. Specyfikacje drukarek i filamentów trzeba zbierać od producentów (fakty, ale bez gotowego zbioru). Repozytoria modeli mają mieszane licencje, w tym niekomercyjne; nie sprawdzałem szczegółowo. Narzędzia (kalkulator kosztu, dobór filamentu, temperatury) da się zrobić bez danych zewnętrznych.

**Ryzyko.** Niskie. Brak YMYL i treści prawnych (poza ewentualnym prawem autorskim do modeli). AIO w 2 z 6. Rynek mniejszy i hobbystyczny, sezon grudniowy.

**Pomysł na serwis.** Huby: wybór drukarki, filamenty, problemy z drukiem, slicery i ustawienia, druk 3D jako dodatkowy zarobek. Narzędzie: kalkulator kosztu wydruku (filament, prąd, amortyzacja, marża) i dobór filamentu do zastosowania. Strony encji: każda drukarka (specyfikacja, cena, porównania), każdy filament (temperatury, suszenie, marki polskie) i każdy problem (warping, stringing) jako osobna strona.

**Werdykt:** najwyższy wynik ważony. Rosnący popyt i najsłabszy SERP w grupie, ale zarobek zależy od afiliacji sprzętu, a fosę danych trzeba zbudować samemu.

---

## 5a. Drony

**Popyt [W].** 34 frazy, suma 233 730, trend −52% r/r (−37% bez „dron” i „drony”, które mają newsowy skok z września 2025). Szczyt w listopadzie 2025 (438 230), dołek w lutym 2026 (168 490). Top frazy: „dron” 40 500, „drony” 33 100, „dron z kamerą” 18 100, „dji mini 4 pro” 18 100 (−63%), „dji mini 5 pro” 18 100, „dji neo” 14 800, „drony.gov.pl” 14 800 (+60%), „dji mini 4k” 12 100, „dji flip” 9 900, „dji fly” 9 900. Rosną frazy formalne: „ubezpieczenie drona” 1 900 (+50%), „oc drona” 1 900 (+37%).

**SERP [S][B].** Frazy: „dron dla początkujących”, „gdzie można latać dronem” (narzędzie), „dji mini 4 pro” (encja), „ubezpieczenie drona”, „egzamin na drona”. Wygrywają: urzędy (ulc.gov.pl 2 269, drony.gov.pl 258, pansa), ubezpieczyciele (warta.pl 3 106, pzu.pl 6 127, cuk.pl 2 925, beesafe.pl 1 817), sklepy DJI (dji-ars.pl 451, mediaexpert.pl). Słabości: swiatdronow.pl z 09.2015 na „gdzie można latać dronem”, droneclub.pl (forum, 154), „dron dla początkujących” ma tylko 5 wyników organicznych (ironsky.pl z 05.2023, Facebook, TikTok, reddit). AIO w 3 z 5; cytuje megadron.pl, aeropolisa.pl, ironsky.pl.

**Zarobek.** CPC ważony 0,43 USD; „oc drona” 1,82, „ubezpieczenie drona” 1,79, „egzamin na drona” 1,12 [W]. OC operatora drona 250 g–20 kg jest obowiązkowe od 13.11.2025 (rf.gov.pl, cytowane w AIO [S]). DJI ma programy w Tradedoubler dla ES, PT, SK, HU; listing podaje 2% na drony i 5% na gimbale (directory.tradedoubler.com) [WWW]. Programu DJI dla Polski nie znalazłem. Programów partnerskich ubezpieczycieli nie sprawdziłem.

**Fosa danych.** Średnia. PANSA DroneMap udostępnia strefy przez interfejs api.dronemap.pansa.pl (według wtyczki QGIS „PANSA DroneMap Downloader”, plugins.qgis.org) [WWW]; licencji nie sprawdziłem. Przepisy ULC to dokumenty urzędowe.

**Ryzyko.** Wysokie. Rdzeń niszy to przepisy, uprawnienia i obowiązkowe OC (treści prawne do decyzji właściciela). Urzędy wygrywają frazy formalne. Popyt spada, a newsy o dronach wojskowych zaburzają wolumeny.

**Pomysł na serwis.** Huby: uprawnienia A1/A3/A2, OC i ubezpieczenia, wybór drona, gdzie latać, FPV. Narzędzie: sprawdzarka „jakie wymagania ma mój dron” (waga i klasa C0–C2 → kategoria, egzamin, OC) i mapa stref z PANSA. Strony encji: każdy model (waga, klasa, wymagania, cena) i strony miast ze strefami.

**Werdykt:** odpada. Spadek popytu, przewaga urzędów i ciężar treści prawnych.

## 5b. Rowery i hulajnogi elektryczne

**Popyt [W].** 33 frazy, suma 438 550, trend +1% r/r. Najsilniejsza sezonowość w grupie: maj 2026 704 340, styczeń 2026 161 250. Top frazy: „rower elektryczny” 135 000, „hulajnoga elektryczna” 135 000, „rowery elektryczne” 33 100, „rower elektryczny damski” 22 200 (+39%), „hulajnogi elektryczne” 22 200, „skuter elektryczny” 22 200, „e bike” 18 100 (+50%). „dopłata do roweru elektrycznego” spadła do 590 we wrześniu 2026 z 18 100 w kwietniu 2025.

**SERP [S][B].** Frazy: „rower elektryczny ranking”, „hulajnoga elektryczna przepisy”, „rower elektryczny zasięg” (narzędzie), „hulajnoga elektryczna dla dorosłych”, „segway ninebot” (encja). Wygrywają porównywarki i sklepy: skapiec.pl (4 539, 4 pozycje w jednym SERP), ceneo.pl, euro.com.pl, neonet.pl, mediamarkt.pl, producent pl-pl.segway.com (19 domen, ale to strona marki). Na „rower elektryczny zasięg” pierwszy jest kalkulator erider.pl (112 domen). Na „przepisy” wygrywają policja i gov.pl. AIO w 1 z 5 (tylko przepisy; zmiana 3.03.2026: wiek 13+, według stron cytowanych w AIO).

**Zarobek.** Najniższe CPC w grupie: ważony 0,29 USD, max 0,51 [W]. Wappalyzer wymienia decathlon.pl wśród stron z Convertiser [WWW]; programu nie potwierdziłem. Sprzedaż idzie przez sklepy i porównywarki, które same mają rankingi.

**Fosa danych.** Słaba. OpenStreetMap (trasy) ma licencję ODbL, której dziś nie sprawdzałem. Brak rejestru modeli.

**Ryzyko.** Średnie: przepisy o hulajnogach, mocna sezonowość, porównywarki z własnymi rankingami.

**Pomysł na serwis.** Huby: wybór e-roweru, hulajnogi dla dorosłych, baterie i zasięg, przepisy, serwis. Narzędzie: kalkulator zasięgu i kosztu ładowania. Strony encji: modele z parametrami.

**Werdykt:** odpada. Niski CPC, rankingi porównywarek i brak danych.

---

## Czego nie sprawdzono (do uzupełnienia, jeśli nisza przejdzie dalej)

- Reklamodawcy (`/v3/serp/google/ads_advertisers/live/advanced`): pominięte.
- Rozszerzenie fraz (`keyword_ideas`, `related_keywords`): nie robiłem; rdzeń to 33–50 fraz na niszę.
- Licencje i warunki: API EIPA, API PSE, nota prawna PVGIS, API CEPiK, DroneMap PANSA, baza Zigbee2MQTT, lista Matter (CSA), TGE. Kilka domen rządowych nie odpowiada przez WebFetch (blokada DNS), część czytałem przez `content_parsing`.
- Stawki programów partnerskich: tylko istnienie (Amazon.pl, Bambu Lab w Awin, DJI w Tradedoubler poza PL). Nie rejestrowałem się nigdzie.
- Domeny linkujące liczone dla całej domeny, nie dla podstrony z wyniku. Słaba podstrona na silnej domenie wygląda tu na silną.

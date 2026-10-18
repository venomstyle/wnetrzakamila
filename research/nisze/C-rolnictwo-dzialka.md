# Nisze C: rolnictwo, działka, zwierzęta przydomowe i akwarystyka (18.10.2026)

Metoda: `research/nisze/METODA.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie dane pobrano 18.10.2026.

**Oznaczenia źródeł** (każda liczba w tekście ma jeden z tych znaczników):

- **[V]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live`: średni wolumen miesięczny z 12 miesięcy (10.2025–09.2026), CPC w USD, miesiące od 07.2025 do 09.2026. Surowe dane: `dane/C-wolumeny.csv` (228 fraz rdzenia) i `dane/C-wolumeny-encje.csv` (109 fraz encji i narzędzi).
- **[S]** DataForSEO `/v3/serp/google/organic/live/advanced`, depth 10, z `load_async_ai_overview` (wyjątek: „cena pszenicy” bez tej opcji).
- **[B]** DataForSEO `/v3/backlinks/bulk_referring_domains/live`, domeny linkujące do domeny głównej. Surowe dane: `dane/C-serp-top10.csv`.
- **[A]** DataForSEO `/v3/serp/google/ads_advertisers/live/advanced`.
- **[P]** DataForSEO `/v3/on_page/content_parsing/live` (strony gov.pl, bo WebFetch nie rozwiązuje domen gov.pl).
- **[W]** WebSearch (programy partnerskie, licencje).

**Jak liczono:** trend r/r to suma wolumenów z 07–09.2026 wobec 07–09.2025. Sezon to najsłabszy i najmocniejszy miesiąc sumy rdzenia w okresie 10.2025–09.2026. Z sum usunięto frazy nawigacyjne lub wieloznaczne: „arimr” (246 000, nawigacja do agencji), „kurnik” (1 500 000, najpewniej serwis gier kurnik.pl; nie weryfikowano), „ptasia grypa” (12 100, temat newsowy), „ul” (27 100, myli się ze skrótem „ulica”), „mieczyki” (12 100, także kwiat) i „kameleon” (22 200, wieloznaczne) [V]. Mediana domen linkujących liczona jest dla wyników organicznych z top 10 pięciu fraz na niszę [S][B]. Wersja „bez platform” pomija YouTube, Facebook, Wikipedię, Allegro, OLX, Google Play i Ceneo.

## Tabela ocen

Skala 1–5, 5 = najlepiej. Wagi z METODA.md.

| Nisza | Popyt i trend (20%) | Słabość SERP (25%) | Zarobek (25%) | Fosa danych / narzędzia (15%) | Niskie ryzyko (15%) | **Wynik ważony** |
|---|---|---|---|---|---|---|
| 5. Akwarystyka i terrarystyka | 4 | 4 | 3 | 3 | 4 | **3,60** |
| 1. Rolnictwo (dopłaty, nawożenie, ceny, ŚOR) | 4 | 3 | 3 | 4 | 2 | **3,20** |
| 3. Kury i drób przydomowy | 3 | 4 | 2 | 2 | 3 | **2,85** |
| 2. Warzywnik i ogródek działkowy | 3 | 3 | 2 | 3 | 3 | **2,75** |
| 4. Pszczelarstwo | 2 | 3 | 2 | 2 | 3 | **2,40** |

Zestawienie liczb, na których oparto oceny:

| Nisza | Suma rdzenia [V] | Trend r/r [V] | Sezon min / max [V] | Mediana dom. link. top 10 (bez platform) [B] | Wyniki < 50 dom. [B] | Stare / fora / PDF [S] | AIO [S] | Średni CPC rdzenia [V] |
|---|---|---|---|---|---|---|---|---|
| Rolnictwo | 147 290 (47 fraz) | +9,5% | 06.2026: 92 900 / 03.2026: 192 090 | 442 (359) | 4 z 42 | 6 | 4 z 5 | 0,66 USD |
| Warzywnik | 117 180 (46 fraz) | −16,3% | 12.2025: 34 470 / 03.2026: 237 950 | 700 (636) | 0 z 40 | 11 | 4 z 5 | 0,15 USD |
| Kury | 90 560 (38 fraz) | +5,6% | 12.2025: 62 570 / 03.2026: 140 090 | 3 674 (826) | 2 z 42 | 7 | 3 z 5 | 0,26 USD |
| Pszczelarstwo | 113 020 (44 frazy) | −14,4% | 08.2026: 99 780 / 10.2025: 156 400 | 452 (452) | 0 z 43 | 6 | 3 z 5 | 0,34 USD |
| Akwarystyka | 328 250 (47 fraz) | −9,1% | 06.2026: 277 660 / 01.2026: 379 370 | 367 (195) | 4 z 43 | 6 | 2 z 5 | 0,29 USD |

---

## 1. Rolnictwo: dopłaty i ekoschematy, nawożenie, ceny skupu, środki ochrony roślin

### Popyt
- Suma rdzenia: **147 290** wyszukiwań miesięcznie w 47 frazach, bez „arimr” [V]. Trend r/r **+9,5%** (452 240 wobec 413 170 w 07–09) [V].
- Podgrupy [V]: ceny skupu i nawozów 73 470 (r/r +8%), dopłaty i ekoschematy 42 810 (r/r +22%), środki ochrony roślin 24 880 (r/r +10%), nawożenie, wysiew i odmiany 6 130 (r/r −24%).
- Sezon: najsłabszy czerwiec 2026 (92 900), najmocniejszy marzec 2026 (192 090) [V]. Dopłaty mają dwa szczyty: wnioski w maju („dopłaty bezpośrednie 2026”: 33 100 w 05.2026) i wypłaty jesienią („dopłaty bezpośrednie”: 22 200 w 11.2025) [V].
- Top frazy [V]: cena pszenicy 33 100, płatności bezpośrednie 22 200, cena rzepaku 14 800, glifosat 12 100, ceny nawozów 8 100, dopłaty bezpośrednie 6 600, dopłaty bezpośrednie 2026 6 600, cena kukurydzy 6 600, środki ochrony roślin 5 400, dopłaty do nawozów 5 400.
- Narzędzia [V]: kalkulator wysiewu 1 000, kalkulator nawożenia 40, kalkulator dopłat 10, kalkulator ekoschematów 10. Popyt na kalkulatory jest mały, poza wysiewem.
- Encje [V]: nazwy handlowe ŚOR mają duży wolumen (roundup 18 100, mospilan 14 800, chwastox 9 900, decis 3 600, karate zeon 2 900, amistar 2 400). Część nazw jest wieloznaczna (biathlon 22 200, pivot 8 100, atlantis 6 600), więc ich nie liczono.

### SERP
- Mediana domen linkujących w top 10: **442**, bez platform 359 [B]. Wyniki poniżej 50 domen: 4 z 42 (farmhub.pl 32, agrokontrola.pl 18, kalkulatorxxl.pl 10, akademiarzepaku.pl 49) [B].
- Stare wpisy, fora i PDF: 6 (cdr.gov.pl z 2021, dionp.pl z 2020, polcalc.pl i polifoska.pl z 2022, akademiarzepaku.pl z 2020, post na Facebooku) [S].
- Kto wygrywa [S]: przy dopłatach gov.pl, KRUS, ośrodki doradztwa (dodr.pl, cdr.gov.pl) i portale rolnicze (farmer.pl 4 447 domen, topagrar.pl 2 028) [B]. Przy cenach topagrar.pl, rolpetrol.com.pl, stat.gov.pl, izby rolnicze i notowania KPODR. Przy nawożeniu blogi producentów nawozów i ŚOR. Przy „kalkulator wysiewu” hodowcy nasion (IGP Polska 80 domen) i drobne strony [B].
- Nowe małe serwisy już weszły w niszę: farmhub.pl (32 domeny) jest w top 10 „ekoschematy 2026”, agrokontrola.pl (18 domen) w top 10 i w AIO dla wyszukiwarki ŚOR, terrafarm.pl jest cytowany w AIO [S][B].
- AI Overview: 4 z 5 SERP-ów (ekoschematy 2026, kalkulator wysiewu, wyszukiwarka ŚOR, nawożenie rzepaku). „Cena pszenicy” sprawdzona bez ładowania AIO: brak bloku, jest wykres giełdowy CBOT [S]. AIO cytuje głównie gov.pl, CDR i producentów, ale też małe serwisy (terrafarm.pl, agrokontrola.pl, agraves.pl) [S].

### Zarobek
- CPC [V]: płatności bezpośrednie 5,15 USD, arimr 3,06 USD, wyszukiwarka środków ochrony roślin 2,22 USD, kalkulator nawożenia 1,28 USD, plan nawożenia 0,97 USD. Reszta zwykle 0,1–0,6 USD.
- Reklamodawcy dla „płatności bezpośrednie”: brak wyników (status „No Search Results”) [A].
- Programy partnerskie: nie znaleziono polskich programów sklepów rolniczych (Agrosimex, Sklep Farmera, Agrotom, Rolnet) [W]. Allegro Polecam zamknięto, a Allegro Share daje punkty zamiast gotówki (według wyników wyszukiwania, bez daty zmiany) [W].
- Możliwy własny produkt: płatne narzędzie dla gospodarstw (plan nawożenia, kalendarz zabiegów z karencją, alerty cen). AIO podaje, że „plan nawożenia” daje 1–3 pkt w ekoschemacie „rolnictwo węglowe” (cytat z gov.pl/web/arimr) [S]. Czy rolnik może sam sporządzić taki plan i czy narzędzie mogłoby go generować: **nie sprawdzono**.

### Fosa danych
- **Rejestr ŚOR MRiRW**: https://www.gov.pl/web/rolnictwo/rejestr-rodkow-ochrony-roslin. Pliki XLSX, wersja 276 z 16.10.2026, aktualizacja co 1–3 tygodnie [P]. Stopka gov.pl: „Treści tekstowe publikowane w serwisie (z wyłączeniem treści audiowizualnych), są udostępniane na licencji typu Creative Commons: uznanie autorstwa - na tych samych warunkach 4.0 (CC BY-SA 4.0)” [P]. Osobnej licencji dla plików XLSX nie znaleziono; przed użyciem trzeba to potwierdzić. Z rejestru da się zrobić strony encji: środek → substancja czynna → uprawy → agrofagi → karencja → status.
- **Ceny skupu**: ZSRIR MRiRW publikuje co tydzień biuletyny cenowe na gov.pl [W]; licencja jak wyżej (stopka gov.pl). GUS (stat.gov.pl/copyright): kopiowanie i własne opracowania dozwolone z podaniem źródła [W]. Obwieszczenia GUS o cenie skupu pszenicy są w top 10 „cena pszenicy” [S].
- **Odmiany**: COBORU publikuje Krajowy rejestr i listy odmian jako PDF (np. https://coboru.gov.pl/Publikacje_COBORU/Listy_odmian/LORS_2026.pdf) i wersję elektroniczną [W]. Licencji COBORU **nie sprawdzono**.
- **Stawki dopłat**: strony ARiMR na gov.pl (np. „stawki-platnosci-rsk-2026” w top 10) [S], licencja jak wyżej.
- Ocena: najmocniejsza fosa z pięciu nisz (rejestr aktualizowany kilka razy w miesiącu, ceny tygodniowe), ale część licencji do potwierdzenia.

### Ryzyko (czy to „za bardzo prawne”)
- **Dopłaty i ekoschematy: tak, to treść prawna.** Terminy wniosków, limity (np. 300 ha, maks. 2 ekoschematy na powierzchni), punkty i stawki zmieniają się co roku i wynikają z rozporządzeń [S]. Błąd kosztuje rolnika pieniądze. Właściciel jeszcze nie zdecydował, czy treści prawne są dozwolone.
- **ŚOR: częściowo prawne i bezpieczeństwo.** Dopuszczenie, dawki i karencja wynikają z etykiety (dokument urzędowy). Bezpieczna forma to lustro rejestru z linkiem do etykiety, bez własnych zaleceń dawek.
- **Ceny skupu i nawożenie: niskie ryzyko prawne.** Nawożenie to agronomia (bez przepisów, poza programem azotanowym i ekoschematami).
- AIO w 4 z 5 SERP-ów, czyli wysoka presja na kliknięcia [S].

### Pomysł na serwis
Huby: ceny skupu (zboża, rzepak, tuczniki, mleko, nawozy), nawożenie i wysiew, środki ochrony roślin, dopłaty jako osobny hub tylko po zgodzie właściciela na treści prawne. Narzędzie: tygodniowy monitor cen z wykresem i alertem e-mail oraz kalkulator wysiewu i dawki NPK (wzór MTZ × obsada / siła kiełkowania podaje AIO za Syngentą i Danko [S]). Strony encji: każdy środek z rejestru MRiRW (substancja, uprawy, karencja, status, link do etykiety) i każda odmiana z COBORU.

### Werdykt
**Warto rozważyć, w wersji bez dopłat.** Popyt rośnie i są dane do stron encji, ale pieniądze nie są oczywiste (brak programów partnerskich, niski CPC poza kilkoma frazami). Najlepszy kąt: dane cenowe i rejestr ŚOR jako „paliwownia dla rolnika”. Dopłaty dopiero po decyzji właściciela o treściach prawnych.

---

## 2. Warzywnik i ogródek działkowy

### Popyt
- Suma rdzenia: **117 180** w 46 frazach [V]. Trend r/r **−16,3%** (258 500 wobec 308 800 w 07–09) [V].
- Sezon bardzo silny: grudzień 2025: 34 470, marzec 2026: 237 950, czyli prawie 7 razy więcej [V].
- Top frazy [V]: szklarnia ogrodowa 22 200, kompostownik 18 100, tunel foliowy 14 800, mszyce 8 100, kalendarz księżycowy ogrodnika 6 600, kiedy sadzić czosnek 4 400, nawóz do pomidorów 4 400, kiedy siać pomidory 3 600, kiedy sadzić ziemniaki 3 600, kiedy siać ogórki 3 600. Trzy pierwsze to frazy zakupowe.
- Dodatkowo [V]: zimni ogrodnicy 9 900.
- Narzędzia [V]: kalendarz siewu 320, kalendarz siewu warzyw 210, kiedy ostatnie przymrozki 20. Popyt jest w pytaniach „kiedy siać X”; samo słowo „kalendarz” ma mały wolumen.
- Encje (odmiany) [V]: pomidor bawole serce 4 400, pomidor koktajlowy 3 600, czosnek harnaś 1 600, pomidor malinowy ożarowski 1 300, pomidor san marzano 1 300, ogórek śremski 1 300, odmiany pomidorów 1 600.

### SERP
- Mediana domen w top 10: **700**, bez platform 636 [B]. Wyniki poniżej 50 domen: 0 z 40 [B].
- Stare wpisy i fora: 11, najwięcej z pięciu nisz [S]. Przykłady: „kalendarz księżycowy ogrodnika” ma w top 10 wpisy z 2015 (bezogrodek.com, mojpieknyogrod.pl, YouTube) i kalendarze na miesiące z 2021 i 2024 [S]. „Choroby pomidorów” ma dwa wątki forum (forumogrodniczeoaza.pl) [S].
- Kto wygrywa [S][B]: portale ogrodnicze i wnętrzarskie (zielonyogrodek.pl 1 769 domen, urzadzamy.pl 1 847, dom.wprost.pl), sklepy z nasionami (swiatkwiatow.pl 1 658, legutko.com.pl 493), markety (castorama.pl 5 286, obi.pl 3 155). „Tunel foliowy” to w całości sklepy i Google Shopping.
- AI Overview: 4 z 5 (bez AIO tylko „tunel foliowy”) [S]. AIO cytuje małe serwisy: gardenowo.pl, dziendobryogrod.pl, rytmnatury.pl, spa4garden.pl, mojepomidory.pl [S].

### Zarobek
- CPC niski: średnio 0,15 USD [V]. Najwyżej: ślimaki w ogrodzie 0,84, szklarnia poliwęglanowa 0,51, podwyższone grządki 0,36, szklarnia ogrodowa 0,33 USD [V].
- Programy partnerskie: nie znaleziono polskich programów sklepów z nasionami. Jedyny ślad to sklepdlaogrodu.pl na Affilitizer (wpis z 2016, sieć nieznana) [W]. Programów Leroy Merlin, Castorama, OBI w Polsce nie potwierdzono [W].
- Produkty o wysokiej cenie (szklarnie, tunele: od 48 do 2 539 zł w Google Shopping) [S] sprzedają Allegro i sklepy, bez potwierdzonej prowizji.

### Fosa danych
- COBORU: Krajowy rejestr odmian warzyw (PDF 2026: https://coboru.gov.pl/Publikacje_COBORU/Listy_odmian/LORW_2026.pdf) [W]. Licencji **nie sprawdzono**. AIO dla „odmiany pomidorów” cytuje już stronę rejestru COBORU [S].
- Terminy przymrozków: dane klimatyczne IMGW-PIB. Aktualnych warunków komercyjnego użycia **nie potwierdzono**; jeden projekt IMGW (PMAXTP) wymaga podania źródła [W].
- Kalendarz księżycowy da się policzyć z efemeryd bez zewnętrznych danych, ale to temat bez podstaw naukowych (ryzyko uczciwości).

### Ryzyko
- Niskie YMYL. Opryski na działce dotykają rejestru ŚOR (środki dla amatorów), czyli tematu prawnego [S].
- Silna sezonowość (×7) i spadek r/r −16% [V].
- Blisko wykluczonego „ogrodu dekoracyjnego”; trzeba trzymać się warzyw.
- AIO w 4 z 5 SERP-ów [S].

### Pomysł na serwis
Huby: kalendarz prac (miesiąc po miesiącu), warzywa (siew, rozsada, choroby, szkodniki), uprawa pod osłonami. Narzędzie: planer siewu liczący daty siewu, pikowania i wysadzenia wstecz od lokalnej daty ostatniego przymrozku (po potwierdzeniu licencji IMGW). Strony encji: odmiany z rejestru COBORU z grupą, przeznaczeniem i linkiem do rejestru.

### Werdykt
**Raczej nie.** Dużo starych treści w SERP, ale domeny są średnio silne, zarobek słaby, a sezon bardzo krótki. Mogłoby to być sezonowe skrzydło serwisu rolniczego.

---

## 3. Kury i drób przydomowy

### Popyt
- Suma rdzenia: **90 560** w 38 frazach (bez „kurnik” i „ptasia grypa”) [V]. Trend r/r **+5,6%** (239 660 wobec 226 950 w 07–09) [V].
- Sezon: grudzień 2025: 62 570, marzec 2026: 140 090 [V].
- Top frazy [V]: inkubator do jaj 12 100, kury ozdobne 8 100, poidło dla kur 8 100, kury nioski 6 600, przepiórki 6 600, perliczki 6 600, ptaszyniec 6 600, pasza dla kur niosek 4 400, karmnik dla kur 4 400, rasy kur 3 600, pasza dla kur 3 600.
- Encje (rasy) [V]: kury silki 8 100, leghorn 4 400, kury zielononóżki 3 600, kury jedwabiste 2 900, kury australorp 1 900, zielononóżka kuropatwiana 1 300, kury sussex 1 000, kury brahma 880, rhode island red 880, kury marans 880.
- Narzędzia [V]: kurnik dla 10 kur 720, ile kur na m2 390, ile jaj znosi kura 260, ile paszy dla kury dziennie 0.
- Przepisy [V]: czy trzeba rejestrować kury 170, rejestracja drobiu 40, rejestracja kur w arimr 10.

### SERP
- Mediana domen w top 10: **3 674**, ale zawyżają ją platformy (16 z 42 wyników to YouTube, OLX, Allegro, Facebook) [S][B]. Bez platform: **826** [B].
- Wyniki poniżej 50 domen: 2 z 42 (twojafarma.pl 13, piw-malbork.lo.pl 6) [B]. Stare, fora i PDF: 7 (m.in. PDF-y Wiadomości Zootechnicznych z 2018, YouTube z 2021–2022) [S].
- Strony encji są słabo obsadzone: „kury australorp” ma w top 10 trzy filmy YouTube, trzy listingi OLX, grupę na Facebooku i nowy blog twojafarma.pl (13 domen, wpis z 24.09.2026) [S][B]. „Rasy kur”: agrofortel.pl (74 domeny), trzy filmy YouTube, PDF instytutu [S][B].
- AI Overview: 3 z 5 (rasy kur, kokcydioza, rejestracja kur) [S]. „Kury australorp” i „kurnik dla 10 kur” bez AIO [S]. AIO cytuje małe serwisy: twojkurnik.pl, wieluszki.pl, mojekurczaki.pl, agrokurier.pl, tinyhousedesign.pl [S].

### Zarobek
- CPC niski: średnio 0,26 USD [V]. Najwyżej: choroby kur 0,61, budowa kurnika 0,45, pasza dla kur 0,36, inkubator do jaj 0,35 USD [V].
- Programy partnerskie: nie znaleziono programów sklepów z akcesoriami dla drobiu (fermo.pl, rolnet.pl nie sprawdzone pod tym kątem) [W].
- Produkty drogie: kurniki od 618,99 do 5 075 zł w Google Shopping dla „kurnik dla 10 kur” [S]. W grafice Google jest płatny plan kurnika na Etsy [S]; własny PDF z planami kurnika to możliwy produkt (to nie jest wzór dokumentu prawnego).

### Fosa danych
- Brak otwartego rejestru ras z licencją sprawdzoną dziś. Możliwe źródła: Wikidata i Wikipedia (licencje projektów **nie sprawdzano dziś**), programy ochrony zasobów genetycznych IZ PIB (**nie sprawdzono**).
- Narzędzia (powierzchnia kurnika, zużycie paszy, koszt jajka) nie wymagają zewnętrznych danych, ale i nie dają fosy.

### Ryzyko
- Zdrowie zwierząt: choroby, leki weterynaryjne, odrobaczanie (umiarkowane YMYL).
- **Treść prawna (oznaczona):** zgłoszenie miejsca utrzymywania drobiu do powiatowego lekarza weterynarii i progi rejestracji w ARiMR (AIO podaje progi 350 niosek i 500 brojlerów za PIW Malbork) [S]. To wymaga decyzji właściciela.
- Ptasia grypa może nagle zmienić przepisy (np. nakaz trzymania drobiu w zamknięciu); nie sprawdzano bieżących komunikatów.

### Pomysł na serwis
Huby: start z kurami (kurnik, wybieg, pasza), rasy, zdrowie (opisowo, z odesłaniem do weterynarza), inne drób (przepiórki, perliczki, kaczki). Narzędzie: kalkulator kurnika (m² kurnika i wybiegu, liczba grzęd i gniazd, zużycie paszy i koszt jajka). Strony encji: rasy z typem użytkowym, nieśnością, masą, kolorem jaj, odpornością, każda ze źródłem.

### Werdykt
**Słaby SERP, słaby zarobek.** Najlepsza okazja na strony encji z pięciu nisz (YouTube i OLX zamiast artykułów), ale bez programów partnerskich i z niskim CPC. Sens tylko z własnym produktem (plany kurnika) albo jako część większego serwisu „gospodarstwo przydomowe”.

---

## 4. Pszczelarstwo

### Popyt
- Suma rdzenia: **113 020** w 44 frazach (bez „ul”) [V]. Trend r/r **−14,4%** (319 200 wobec 372 940 w 07–09) [V].
- Uwaga: 73 370 z tej sumy to frazy konsumenckie o miodzie, propolisie i pierzdze (r/r −16%) [V]. Samo pszczelarstwo (ule, choroby, karmienie, sprzęt) to tylko **39 650** (r/r −11%) [V].
- Sezon słaby: sierpień 2026: 99 780, październik 2025: 156 400 [V].
- Top frazy [V]: propolis 22 200, pierzga 18 100, miód spadziowy 12 100, pasieka 12 100, miód gryczany 8 100, miód rzepakowy 6 600, miód lipowy 5 400, ule 2 900, pszczelarstwo 2 400, ul warszawski 2 400, matki pszczele 2 400, węza pszczela 2 400.
- Początkujący i dotacje [V]: pszczelarstwo dla początkujących 50, jak zacząć pszczelarstwo 20, dofinansowanie dla pszczelarzy 50, rejestracja pasieki 170.
- Encje [V]: miód manuka 18 100, miód faceliowy 14 800, miód akacjowy 6 600, miód nawłociowy 6 600, apiwarol 1 300.
- Narzędzia [V]: kalkulator syropu dla pszczół 50, proporcje syropu dla pszczół 40.

### SERP
- Mediana domen w top 10: **452** (z platformami i bez nich tyle samo) [B]. Wyniki poniżej 50 domen: 0 z 43 [B].
- Stare i fora: 6 (forum Ambrozja z 2016, topagrar z 2015, filmy z 2016 i 2018) [S].
- Kto wygrywa [S][B]: sklepy i portale pszczelarskie (pasieka24.pl 591 domen, lyson.com.pl 452, pszczelnictwo.com.pl 444), pasieki sprzedające miód (pasiekisadowskich.pl 724, skarbyroztocza.com 1 819), Wikipedia.
- AI Overview: 3 z 5 (pszczelarstwo, ul wielkopolski, warroza) [S]. Bez AIO: „syrop dla pszczół”, „miód spadziowy” [S]. AIO cytuje pasieka24.pl, pasiekasmakulskich.pl, pasiekasciegienny.pl [S].

### Zarobek
- CPC [V]: pasieka 2,42 USD, miód lipowy 0,77, syrop dla pszczół 0,72, sprzęt pszczelarski 0,70, ul 0,69 USD; średnio 0,34 USD.
- Programy partnerskie sklepów pszczelarskich: nie znaleziono [W].
- Frazy o miodzie prowadzą do sklepów pasiek z twierdzeniami zdrowotnymi w opisach (np. o działaniu na serce i ciśnienie) [S].

### Fosa danych
- Brak otwartego zbioru danych sprawdzonego dziś. Lista leków na warrozę jest w rejestrze produktów leczniczych weterynaryjnych (URPL), licencji **nie sprawdzono**. Dane o rynku miodu i dotacjach (krajowy program pszczelarski) **nie sprawdzono**.

### Ryzyko
- Leczenie warrozy to leki weterynaryjne (tylko dopuszczone preparaty) [S].
- Rejestracja pasieki w PIW i dotacje to treści prawne [S].
- Miód i propolis jako zdrowie to YMYL.
- Spadek r/r −14% [V].

### Pomysł na serwis
Huby: pierwszy rok w pasiece, ule (typy i wymiary ramek), zdrowie rodzin, miody. Narzędzie: kalkulator syropu i zapasów zimowych (proporcje cukru i wody, kg na rodzinę). Strony encji: gatunki miodu (skład, krystalizacja, pochodzenie roślin) i typy uli (wymiary ramek, np. wielkopolski 360 × 260 mm według AIO [S]).

### Werdykt
**Nie.** Mały i malejący rdzeń, brak danych do encji, brak programów partnerskich, a większość wolumenu to zdrowotne frazy o miodzie.

---

## 5. Akwarystyka i terrarystyka

### Popyt
- Suma rdzenia: **328 250** w 47 frazach (bez „mieczyki” i „kameleon”) [V]. Trend r/r **−9,1%** (884 760 wobec 973 800 w 07–09) [V].
- Podgrupy [V]: terrarystyka 194 530 (r/r −3%), akwarystyka 133 720 (r/r −19%).
- Sezon słaby: czerwiec 2026: 277 660, styczeń 2026: 379 370 [V].
- Top frazy [V]: aksolotl 60 500, akwarium 27 100, glonojad 27 100, gekon lamparci 27 100, agama brodata 27 100, wąż zbożowy 22 200, bojownik 18 100, pyton królewski 14 800, ptasznik 12 100, gupiki 9 900, terrarium 9 900, patyczaki 9 900.
- Encje (dodatkowe) [V]: gekon orzęsiony 22 200, złota rybka 14 800, legwan 12 100, żółw grecki 6 600, molinezja 6 600, boa dusiciel 5 400, aksolotl cena 5 400, otoski 4 400, gurami 4 400. To największa przestrzeń encji z pięciu nisz.
- Narzędzia [V]: kalkulator akwarium 590, kalkulator pojemności akwarium 170, ile litrów ma akwarium 50, ile ryb w akwarium 60l 40, obsada akwarium 10. Popyt na kalkulatory jest mały.

### SERP
- Mediana domen w top 10: **367**, bez platform **195**, najniższa z pięciu nisz [B]. Wyniki poniżej 200 domen: 17 z 43; poniżej 50: 4 z 43 [B].
- „Kalkulator akwarium” ma najsłabszy SERP w całym badaniu: mediana 43 domeny, w top 10 cztery cienkie strony aquariumvolume.com (30 domen, tłumaczenia z angielskiego) i strona-załącznik mn-tech.pl (56 domen) [S][B].
- Strony encji: „gekon lamparci” i „bojownik” to Wikipedia, OLX, Allegro i małe sklepy zoologiczne (vantisterra.pl 72 domeny, turkusowezoo.pl 64, gadzisklep.pl 152) [S][B]. Brak AIO, za to panel wiedzy z Wikipedii [S].
- Stare i fora: 6 (aquaforum.pl z 2015, forum.tropheus.com.pl z 2009, pupilek.pl z 2022, gadzisklep.pl z 2021) [S].
- „Akwarium 60l” to w całości sklepy i Google Shopping (zestawy 139,99–535 zł) [S].
- AI Overview: 2 z 5 (kalkulator akwarium, glony w akwarium) [S]. AIO cytuje małe serwisy: podwodnekrolestwo.pl, omnicalculator.com i sklepy [S].

### Zarobek
- CPC [V]: rasbora 1,49 USD, kalkulator akwarium 1,00, danio pręgowany 0,92, molinezje 0,76, bojownik syjamski 0,69, skalary 0,61 USD; średnio 0,29 USD.
- Reklamodawcy dla „akwarium”: jeden, AKWARIUM24 (akwarium24.pl), około 300 reklam [A].
- Program partnerski: zooplus.pl istnieje w Awin (3% za pierwsze 3 zamówienia klienta, potem 1%) i w Tradedoubler (cookie 30 dni, okres oczekiwania 60 dni); inne źródła podają 0,8% i „do 7%”, więc stawki trzeba sprawdzić [W]. Zooart, Krakvet, Kakadu: programu nie znaleziono [W]. Prowizje są niskie.
- Możliwy własny produkt: planer akwarium lub terrarium (lista zakupów, obsada, start cyklu azotowego) jako płatny PDF lub darmowe narzędzie z linkami do sklepu.

### Fosa danych
- FishBase: licencja CC BY-NC, czyli **odpada** (tylko niekomercyjne) [W].
- Reptile Database: w katalogach danych opisana jako CC BY 4.0; to źródło wtórne, trzeba sprawdzić na stronie projektu [W].
- Wikidata i GBIF: licencji **nie sprawdzano dziś**.
- Parametry hodowli (temperatura, pH, litraż, wielkość) nie są w tych bazach w gotowej formie. Strony encji wymagałyby ręcznego zbierania ze źródeł z otwartą licencją.
- Narzędzia (litraż dla różnych kształtów, waga, podłoże, obsada, CO2, nawozy) liczy się wzorami, bez danych zewnętrznych.

### Ryzyko
- Niskie YMYL. AIO tylko w 2 z 5 SERP-ów [S].
- **Treść prawna (oznaczona):** część gadów i żółwi podlega CITES i rejestracji, a niektóre gatunki inwazyjne mają zakaz hodowli i sprzedaży. Nie sprawdzano dziś listy gatunków ani przepisów.
- Dobrostan zwierząt: porady o obsadzie i wielkości zbiornika muszą mieć źródła.
- Akwarystyka spada r/r −19% [V].

### Pomysł na serwis
Huby: akwarium od zera (zakładanie, cykl azotowy, glony, choroby), terrarium od zera (gekon, agama, węże), sprzęt (filtry, grzałki, lampy UVB). Narzędzie: kalkulator akwarium (litraż dla 7 kształtów, waga z podłożem, obsada i zgodność ryb, ilość podłoża) jako lepsza wersja słabego SERP-u „kalkulator akwarium”. Strony encji: gatunki ryb, gadów i bezkręgowców z kartą parametrów (temperatura, pH, min. litraż lub wymiar terrarium, długość życia, zgodność), każda liczba ze źródłem.

### Werdykt
**Najlepsza z pięciu, ale z zastrzeżeniem zarobku.** Duży i stabilny popyt na encje (szczególnie terrarystyka), najsłabsze SERP-y, mało AIO i niskie ryzyko prawne. Słabe strony: niskie prowizje zoo, spadek akwarystyki i brak gotowej bazy danych z otwartą licencją.

---

## Czego nie sprawdzono (wprost)

- Licencji plików XLSX rejestru ŚOR (sprawdzono tylko stopkę gov.pl), licencji COBORU, IMGW, Wikidata, GBIF, URPL i IZ PIB.
- Programów partnerskich sklepów rolniczych, pszczelarskich i drobiarskich poza wyszukiwaniem WebSearch; nie rejestrowano się nigdzie.
- Czy „kurnik” (1 500 000) to rzeczywiście serwis gier [V].
- Czy rolnik może sam sporządzić plan nawożenia do ekoschematu.
- Bieżących przepisów dla drobiu (ptasia grypa) i gadów (CITES, gatunki inwazyjne).
- Reklamodawców sprawdzono tylko dla dwóch fraz [A].

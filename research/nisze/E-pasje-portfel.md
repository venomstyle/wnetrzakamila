# Nisze grupy E: pasje i portfel (badanie z 18.10.2026)

Metoda: `research/nisze/METODA.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie liczby pobrane 18.10.2026.

**Skróty źródeł** (każda liczba w tekście ma przy sobie jeden z nich):

- **[SV]** DataForSEO `/v3/keywords_data/google_ads/search_volume/live`, okres 10.2024–09.2026, pobrane 18.10.2026. Wolumen = średnia miesięczna z ostatnich 12 mies. CPC w USD.
- **[KS]** DataForSEO `/v3/dataforseo_labs/google/keyword_suggestions/live`, 300 fraz o największym wolumenie, pobrane 18.10.2026.
- **[SERP]** DataForSEO `/v3/serp/google/organic/live/advanced`, desktop, depth 10, z AI Overview, pobrane 18.10.2026.
- **[BL]** DataForSEO `/v3/backlinks/bulk_referring_domains/live`, liczba domen linkujących do **całej domeny** (nie do podstrony), pobrane 18.10.2026.
- **[WS]** wyszukiwanie w sieci 18.10.2026 (adresy podane przy faktach).

Surowe dane: `dane/E-wolumeny.csv` (237 fraz, 24 miesiące), `dane/E-sugestie.csv` (1 500 fraz z [KS]), `dane/E-serp-top10.csv` (25 SERP-ów, 207 wyników z domenami linkującymi).

## Tabela ocen

Skala 1–5, 5 = najlepiej. Wagi z METODA.md: popyt 20%, słabość SERP 25%, zarobek 25%, fosa 15%, niskie ryzyko 15%.

| Nisza | Popyt i trend (20%) | Słabość SERP (25%) | Zarobek (25%) | Fosa danych / narzędzia (15%) | Niskie ryzyko (15%) | **Wynik ważony** |
|---|---|---|---|---|---|---|
| E4 Bieganie i sport amatorski (YMYL-zdrowie) | 4 | 3,5 | 3 | 3 | 3 | **3,33** |
| E1 Rachunki domowe: prąd i gaz (YMYL-finanse) | 3 | 4 | 2 | 4 | 2 | **3,00** |
| E2 Numizmatyka | 2 | 3 | 3 | 4 | 3 | **2,95** |
| E3 Gry planszowe | 4 | 3 | 2 | 2 | 4 | **2,95** |
| E5 Kawa w domu | 4 | 2 | 3 | 2 | 4 | **2,95** |

Zbiorcze liczby z badania:

| Nisza | Fraz w rdzeniu | Suma wolumenu rdzenia [SV] | Trend r/r (VII–IX 2026 vs VII–IX 2025) [SV] | Mediana CPC / CPC ważone wolumenem [SV] | Mediana domen linkujących w top 10 [BL] | Wyniki <300 domen [BL] | „Słabe” wyniki* | AI Overview [SERP] |
|---|---|---|---|---|---|---|---|---|
| E1 Rachunki | 54 | 70 000 | −15,6% | 0,45 / 0,57 USD | 360 | 20 z 42 | 12 z 42 | 5 z 5 |
| E2 Numizmatyka | 46 | 27 300 | +2,4% | 0,21 / 0,30 USD | 827 | 14 z 41 | 5 z 41 | 3 z 5 |
| E3 Planszówki | 45 | 346 400 | −6,3% | 0,15 / 0,15 USD | 721 | 6 z 41 | 10 z 41 | 1 z 5 |
| E4 Bieganie | 46 | 189 490 | −6,8% | 0,37 / 0,60 USD | 968 | 11 z 40 | 8 z 40 | 4 z 5 |
| E5 Kawa | 46 | 496 420 | −9,9% | 0,41 / 0,50 USD | 1 587 | 9 z 43 | 5 z 43 | 1 z 5 |

\* „Słaby” wynik = domena z <50 domenami linkującymi albo forum/serwis społecznościowy/wideo (Facebook, YouTube, Reddit, TikTok, Instagram, Elektroda, fora) albo wpis sprzed 2023 r. lub PDF [SERP, BL].

---

## E1. Rachunki domowe: taryfy prądu i gazu, sprzedawcy, zużycie urządzeń (YMYL-finanse)

### Popyt
- Rdzeń: 54 frazy, suma 70 000 wyszukiwań/mies. [SV].
- Trend r/r: −15,6% (126 030 w VII–IX 2026 wobec 149 370 w VII–IX 2025) [SV]. Bez fraz z rokiem w nazwie: −16,8% [SV]. Spada temat „mrożenia” i dopłat: „bon energetyczny” 18 500 → 4 090 w tych samych 3 miesiącach, „opłata mocowa” 10 100 → 3 600 [SV]. Rosną taryfy wielostrefowe: „taryfa g12w” 8 400 → 11 900, „taryfa g12” 7 700 → 9 700, „ile prądu zużywa klimatyzacja” 1 240 → 2 410 [SV].
- Sezon: szczyt XII 2025 (106 880 w miesiącu), dołek VIII 2026 (35 090) [SV]. Popyt skacze przy decyzjach URE i zmianach cen (grudzień, styczeń, marzec).
- Top frazy [SV]: „cena gazu” 14 800 (CPC 1,18), „ile kosztuje 1 kwh” 8 100 (0,45), „ceny prądu 2026” 6 600 (0,67), „taryfa g11” 5 400, „taryfa g12” 4 400, „taryfa g12w” 4 400, „taryfa g13” 4 400, „bon energetyczny” 4 400, „kalkulator zużycia prądu” 2 400, „opłata mocowa” 2 400.
- Długi ogon „ile prądu…”: 300 fraz = 35 580/mies., łącznie 1 009 fraz w bazie [KS]. Przykłady: „ile kosztuje kilowat prądu” 4 400, „ile prądu zużywa lodówka” 720, „…airfryer” 480, „…płyta indukcyjna” 320, „…zmywarka” 260 [KS]. Każde urządzenie to osobna strona encji.
- Słabo: zmiana sprzedawcy. „zmiana sprzedawcy prądu” 140, „porównanie cen prądu” 50, „najtańszy prąd” 70 [SV]. Polacy rzadko szukają zmiany sprzedawcy.

### SERP
- Frazy: „taryfa g12w”, „ile kosztuje 1 kwh”, „kalkulator zużycia prądu” (narzędzie), „ile prądu zużywa lodówka” (encja: urządzenie), „zmiana sprzedawcy prądu” [SERP].
- Kto wygrywa: sprzedawcy i OSD (eon.pl 1 166 domen linkujących, gkpge.pl 2 831, tauron-dystrybucja.pl 1 518, energa.pl 2 319) oraz porównywarki i portale (rankomat.pl 4 803, biznes.interia.pl 5 416) [SERP, BL].
- Słabe miejsca: mediana 360 domen linkujących, najniższa z piątki; 20 z 42 wyników ma <300 domen [BL]. „ile prądu zużywa lodówka”: na 1. miejscu wątek z elektroda.pl z 2017 r., dalej wpisy z 2022 r. (elektrykapradnietyka.com, pamimeble.pl 58 domen, paniagd.pl, sprawdzonewpraktyce.pl), Reddit i YouTube [SERP, BL]. „kalkulator zużycia prądu”: kalkulatorxxl.pl ma 10 domen linkujących i jest w top 10 [BL]. „zmiana sprzedawcy prądu”: mtmenergygroup.pl 14 domen, estimenergy.pl 44 [BL].
- AI Overview: 5 z 5 SERP-ów [SERP]. Cytuje małe serwisy: rachuneo.pl, enerad.pl, kalkulatorxxl.pl, calculat.org, naukowiec.org, akademia-fotowoltaiki.pl (64 domeny) [SERP, BL]. AIO podaje gotowe stawki (np. 0,96–1,10 zł/kWh brutto) [SERP], więc odpowiedź „ile kosztuje 1 kWh” kończy się w Google.

### Zarobek
- CPC niskie: mediana 0,45 USD, ważone 0,57 USD [SV]. Wyjątki: „sprzedawcy prądu” 2,80, „energa operator taryfa” 2,76, „ceny prądu 2027” 1,77, „zmiana sprzedawcy gazu” 1,73, „jak obniżyć rachunki za prąd” 1,36 [SV].
- Programy partnerskie: **nie znalazłem** programu, w którym sprzedawca prądu płaci prowizję za umowę gospodarstwa domowego [WS]. Tauron ma program bonusów dla klientów, nie dla pośredników (tauron.pl, regulamin z 2022 r.) [WS]. Brokerzy (np. ogłoszenie Energomix na gramwzielone.pl) płacą za klientów biznesowych [WS].
- Konkurencja z państwem: Prezes URE prowadzi bezpłatną porównywarkę ofert dla gospodarstw domowych (art. 31g Prawa energetycznego, start 24.08.2024 według podatki.biz i bankier.pl) [WS].
- Możliwy zarobek: reklama kontekstowa, afiliacja AGD (energooszczędne urządzenia, watomierze) przez sklepy, leady fotowoltaika/pompy ciepła. Uwaga: leady PV i pomp zahaczają o wykluczoną „budowlankę i remont”.

### Fosa danych
- Taryfy OSD na 2026 r. zatwierdził Prezes URE 17.12.2025 (money.pl, infor.pl) [WS]. OSD publikują stawki w PDF, np. Energa-Operator: https://www.energa.pl/dam/jcr:e936004d-b99d-443b-aafd-310482d5e8fe/2026_01_01_informacja_o_stawkach_brutto_taryfa_eop_2026.pdf [WS]. Decyzje URE i taryfy to dokumenty urzędowe. Według art. 4 ustawy o prawie autorskim dokumenty urzędowe nie są chronione. Formalnej licencji zbioru na dane.gov.pl nie znalazłem [WS].
- Porównywarka URE (tabele ofert sprzedawców, pierwsza wersja w Excelu według gramwzielone.pl) [WS]: źródło danych o ofertach. Warunków ponownego użycia nie sprawdziłem.
- **EPREL** (unijna baza etykiet energetycznych, https://eprel.ec.europa.eu): zużycie kWh/rok dla modeli lodówek, pralek, zmywarek, telewizorów. Rozporządzenie wykonawcze (UE) 2024/994 mówi o bezpłatnym dostępie do informacji publicznych o modelach [WS]. Jest publiczne API na klucz. **Licencji komercyjnego użycia nie potwierdziłem**; strona EPREL nie otworzyła się z tej sesji [WS].
- Narzędzia oczywiste: kalkulator zużycia, „G11 czy G12/G12w” na stawkach OSD, koszt pracy urządzenia z modelu EPREL.

### Ryzyko
- YMYL-finanse (rachunki, oferty). Treści prawne (Prawo energetyczne, bony, mrożenie cen) wymagają decyzji właściciela.
- Ceny zmieniają się często (taryfy, opłata mocowa). Zasada projektu „ceny niepotwierdzone u źródła nie trafiają na stronę” oznacza stałą aktualizację.
- AIO na 5 z 5 SERP-ów [SERP]. Bezpłatna porównywarka URE [WS]. Popyt spada r/r [SV].

### Pomysł na serwis
Huby: taryfy (G11, G12, G12w, G13, dynamiczna) z rozbiciem na OSD, „ile prądu zużywa” (urządzenia), „rachunek za prąd” (składniki opłat). Narzędzie: kalkulator „która taryfa się opłaca” na oficjalnych stawkach OSD oraz kalkulator kosztu pracy urządzenia. Strony encji: każdy model AGD z EPREL (zużycie roczne → koszt w zł na stawkach każdego OSD) i każdy OSD z aktualną tabelą stawek.

### Werdykt
**Warunkowo, jako projekt rezerwowy.** SERP-y są słabe, a dane mocne (URE, OSD, EPREL), ale brakuje płatnika: nie ma potwierdzonej afiliacji dla gospodarstw domowych, CPC jest niskie, a URE daje darmową porównywarkę. Ma sens tylko wtedy, gdy licencja EPREL pozwala na użycie komercyjne i gdy właściciel zgodzi się na treści YMYL-finanse.

---

## E2. Numizmatyka: monety kolekcjonerskie NBP, monety obiegowe, banknoty, skup

### Popyt
- Rdzeń: 46 fraz, suma 27 300/mies. [SV]. Najmniejszy rdzeń w grupie.
- Trend r/r: +2,4% (65 840 vs 64 290) [SV]. Stabilnie. Rosną: „numizmatyka” 22 800 → 28 600, „destrukty monet” 1 100 → 2 170 [SV]. Spadają: „złote monety” 16 900 → 13 400, „monety kolekcjonerskie nbp” 2 480 → 1 770 [SV].
- Sezon: szczyt I 2026 (37 020), dołek VII 2026 (17 850) [SV].
- Top frazy [SV]: „numizmatyka” 9 900 (CPC 0,17), „złote monety” 6 600 (0,54), „skup monet” 1 300 (0,42), „numizmatyk” 1 300, „monety kolekcjonerskie nbp” 880, „nbp monety kolekcjonerskie” 880, „plan emisji monet 2026” 720 (0,64), „banknoty kolekcjonerskie nbp” 720, „katalog monet polskich” 590, „2 zł okolicznościowe” 590.
- Długi ogon encji [KS]: „moneta” = 300 fraz i 226 060/mies. (4 428 fraz w bazie), ale z dużym szumem (krzyżówki „dawna moneta…”, monety bulionowe). „2 zł” = 300 fraz i 47 830/mies., w tym encje: „najbardziej poszukiwane monety 2 zł” 1 300, „katalog monet 2 zł cennik” 1 000, „2 zł 1994” 720, „2 zł 1958” 480, „2 zł 1994 duża korona” 480, „2 zł zygmunt august” 390, „2 zł 1995” 390, „2 zł jeż” 260 [KS]. Frazy typu „1 zł 1990 wartość” mają 0 w [SV]: ludzie szukają rocznika bez słowa „wartość”.

### SERP
- Frazy: „monety kolekcjonerskie nbp”, „plan emisji monet 2026”, „2 zł 1994” (encja), „najbardziej poszukiwane monety 2 zł”, „wycena monet” (lead) [SERP].
- Kto wygrywa: nbp.pl (5 z 9 wyników na „monety kolekcjonerskie nbp”, 10 816 domen) i sklepy numizmatyczne: numizmatyczny.com 2 203, goldenmark.com 3 083, coin24.pl 75, alegan.pl 134, swiat-monet.pl 218 [SERP, BL]. Mediana 827 domen zawyżona przez nbp.pl; 14 z 41 wyników ma <300 domen [BL].
- Słabe miejsca: „2 zł 1994”: dwa wideo TikTok, OLX, pl.ucoin.net (92 domeny), sklep enumizmatyczny.pl (326) [SERP, BL]. „plan emisji monet 2026”: stary PDF planu z 2019 r. na numizmatyczny.com, forum monetyforum.pl (76 domen), Facebook, news.notafilia.pl (50) [SERP, BL]. Nikt nie ma porządnej bazy emisji NBP poza samym NBP i sklepami.
- AI Overview: 3 z 5 [SERP]. Cytuje sklepy (coin24.pl, swiat-monet.pl, alegan.pl), pankolekcjoner.pl, cndukat.pl, Wikipedię i monetyforum.pl [SERP]. Na „wycena monet” zamiast AIO jest mapka z lokalnymi skupami [SERP].

### Zarobek
- CPC niskie: mediana 0,21, ważone 0,30 USD [SV]. Wyżej: „złota moneta 1 uncja” 0,67, „złota moneta 1 oz” 0,64 [KS], „plan emisji monet 2026” 0,64 [SV].
- Programy partnerskie: AZ Aurum (złote i srebrne monety) w sieci Tradedoubler, 12,5% od sprzedaży, cookie 45 dni (https://directory.tradedoubler.com/en/programs/361608-AZ-Aurum-zlote-i-srebrne-monety-kolekcje-numizmatyczne) [WS]. Programu Goldenmark i Mennicy Polskiej nie znalazłem [WS].
- Inne źródła: abonament i alerty emisji (newsletter, później płatny PDF „katalog emisji z nakładami”), leady do skupów (tylko z formularza na stronie, bez zimnych kontaktów).

### Fosa danych
- NBP: plan emisji 2026 (https://static.nbp.pl/publikacje/numizmatyka/plan-2026-pl.pdf) i 2027 (https://static.nbp.pl/publikacje/numizmatyka/plan-2027-pl.pdf) z tematami, nominałami, próbą, masą, nakładem i terminem [WS]. Katalog NBP monet okolicznościowych: https://nbp.pl/banknoty-i-monety/monety-okolicznosciowe/katalog/ (link w SERP opisany jako „Monety okolicznościowe (560)”) [SERP].
- Licencja: warunków ponownego wykorzystania treści nbp.pl **nie znalazłem** [WS]. Plany emisji to dokumenty urzędowe banku centralnego (art. 4 pr. aut.). Zdjęcia i wizerunki monet trzeba sprawdzić osobno, zanim trafią na stronę.
- Wikipedia (CC BY-SA) ma strony pojedynczych monet, np. „2 złote wzór 1994”, cytowane przez AIO [SERP]. Użycie komercyjne dozwolone z tą samą licencją.
- Wartość rynkowa monet nie ma otwartego źródła. Zasada projektu („ceny niepotwierdzone u źródła nie trafiają na stronę”) wyklucza własne „cenniki”. Zostaje link do aukcji lub sklepu.

### Ryzyko
- Niskie YMYL (wyjątek: złoto inwestycyjne, to finanse). AIO 3 z 5 [SERP].
- Główna intencja („ile warta moneta”) wymaga cen, a tych nie da się uczciwie podać bez źródła.
- Mały rynek: 27 300 wyszukiwań/mies. w rdzeniu [SV].

### Pomysł na serwis
Huby: emisje NBP według lat, serii i nominałów, monety obiegowe według roczników, banknoty kolekcjonerskie. Narzędzie: kalendarz emisji NBP z przypomnieniem e-mail i „sprawdź swoją monetę” (rok + nominał → nakład, odmiany, destrukty, link do aukcji). Strony encji: każda emisja NBP (data, nakład, cena emisyjna z planu NBP, projektant) i każdy rocznik monet obiegowych.

### Werdykt
**Nie jako główny serwis.** Dane NBP dają czystą bazę encji, a SERP na długim ogonie jest słaby. Popyt jest jednak mały, a najbardziej dochodowa intencja (wycena) zderza się z zasadą źródeł. Nadaje się na mały serwis poboczny z newsletterem emisji.

---

## E3. Gry planszowe: gry jako encje, rankingi, ceny, liczba graczy, wiek

### Popyt
- Rdzeń: 45 fraz, suma 346 400/mies. [SV]. Część to nawigacja do marek: „monopoly” 40 500, „rummikub” 40 500, „gry logiczne” 40 500 (głównie gry online) [SV].
- Trend r/r: −6,3% (782 230 vs 834 440) [SV]. Spadają hity: „monopoly” 95 800 → 82 400, „dixit” 31 900 → 24 300 [SV]. Rosną: „catan” 26 100 → 29 700, „sagrada” 5 100 → 6 700 [SV].
- Sezon: szczyt XII 2025 (735 300), dołek VI 2026 (251 590), czyli prawie 3 razy mniej [SV]. Silna zależność od prezentów świątecznych.
- Top frazy [SV]: „gry planszowe” 33 100 (CPC 0,15), „7 cudów świata” 18 100, „carcassonne” 14 800, „dixit” 14 800, „catan” 12 100, „wsiąść do pociągu” 12 100, „splendor” 12 100, „everdell” 8 100.
- Długi ogon [KS]: „gra planszowa” = 300 fraz i 223 750/mies. (6 809 fraz w bazie). Ważne filtry wiekowe: „gra planszowa dla 5 latka” 2 900, „…dla 7 latka” 2 400, „…dla 6 latka” 2 400, „…dla 4 latka” 1 900 [KS].

### SERP
- Frazy: „gry planszowe dla 2 osób”, „gra planszowa dla 7 latka” (filtr jako narzędzie), „ranking gier planszowych”, „splendor” i „everdell” (encje) [SERP].
- Kto wygrywa: sklepy (rebel.pl 3 130, grybezpradu.eu 637, gryplanszowe.pl 808, empik.com 23 585, smyk.com 6 443) i karuzele Google Shopping z porównywarkami (taniomania, skąpiec, cenojad) [SERP, BL].
- Bezpośredni konkurent naszego modelu: **planszeo.pl** (721 domen) ma ranking, strony gier i porównanie ofert; zajmuje 1. miejsce na „ranking gier planszowych” i pojawia się na „dla 2 osób” [SERP, BL].
- Słabe miejsca: forum gry-planszowe.pl, recenzja z 2015 r. na angryboardgamer.pl, wideo YouTube z 2020 i 2021 r., PDF instrukcji na files.rebel.pl [SERP]. Tylko 6 z 41 wyników ma <300 domen [BL].
- AI Overview: 1 z 5 (tylko „everdell”) [SERP].

### Zarobek
- CPC najniższe w grupie: mediana i średnia ważona 0,15 USD [SV].
- Programy partnerskie: programu Rebel.pl nie znalazłem [WS]. Allegro Share: według tabletowo.pl i antyweb.pl 1,67% ceny produktu wypłacane w punktach; aktualność w 2026 r. niepotwierdzona [WS]. Integracja webePartners istnieje dla sklepów na Shoperze, ale konkretnego sklepu z grami w tej sieci nie potwierdziłem [WS].
- Koszyk 100–200 zł (np. Splendor 169,95 zł w rebel.pl według wyniku [SERP]) przy niskiej prowizji daje mało.

### Fosa danych
- BoardGameGeek XML API: domyślna licencja tylko niekomercyjna, licencja komercyjna przyznawana indywidualnie, a aplikacje konkurujące z BGG mogą dostać odmowę (https://boardgamegeek.com/wiki/page/XML_API_Terms_of_Use, https://boardgamegeek.com/wiki/page/BGG_XML_API_Commercial_Use) [WS]. Według zasad projektu źródło niekomercyjne **odpada**.
- Wikidata (CC0) ma część gier; pokrycia nie sprawdzałem. Pozostaje ręczne zbieranie danych od wydawców.

### Ryzyko
- Niskie YMYL, AIO 1 z 5 [SERP]. Ryzyko biznesowe: sezon IV kwartału [SV], gotowy konkurent planszeo.pl [SERP], brak licencji na główną bazę danych [WS].

### Pomysł na serwis
Huby: gry według liczby graczy, wieku dziecka i okazji (impreza, rodzina, para). Narzędzie: „dobierz grę” (liczba osób, wiek, czas, budżet). Strony encji: każda gra z parametrami od wydawcy, porównaniem cen i wariantami (dodatki, edycje).

### Werdykt
**Nie.** Duży, ale nawigacyjny i sezonowy popyt, bardzo niskie CPC, brak licencji na dane (BGG), a dokładnie ten model prowadzi już planszeo.pl.

---

## E4. Bieganie i sport amatorski: kalkulatory, kalendarz biegów, plany, sprzęt (YMYL-zdrowie)

### Popyt
- Rdzeń: 46 fraz, suma 189 490/mies. [SV].
- Trend r/r: −6,8% (555 720 vs 596 360); bez fraz z rokiem −7,7% [SV]. Spadają: „buty do biegania” 181 500 → 159 500, „kalkulator tempa biegu” 21 900 → 14 600, „jak zacząć biegać” 12 400 → 8 200 [SV]. Rosną: „półmaraton gdańsk” 13 900 → 32 000, „garmin forerunner” 54 300 → 62 500, „buty do biegania damskie” 76 400 → 81 300 [SV].
- Sezon: szczyt III 2026 (288 680), dołek XII 2025 (131 050) [SV]. Drugi pik wrzesień (228 000) [SV].
- Top frazy [SV]: „buty do biegania” 60 500 (CPC 0,39), „buty do biegania damskie” 27 100, „garmin forerunner” 18 100, „maraton warszawski” 12 100 (1,44), „półmaraton warszawski” 8 100, „maraton poznań” 6 600, „kalkulator tempa biegu” 5 400, „vo2max” 5 400, „parkrun” 4 400, „półmaraton gdańsk” 4 400, „kalendarz biegów” 2 900 (0,65), „kalendarz biegów 2026” 2 400 (8,13).
- Długi ogon encji (biegi) [KS]: sam „półmaraton” = 300 fraz i 193 240/mies. (4 567 fraz w bazie). Przykłady: „półmaraton warszawski 2026” 12 100, „półmaraton praski” 5 400 (CPC 1,16), „półmaraton poznań 2026” 5 400, „półmaraton gdynia 2026” 3 600, „półmaraton wrocław 2026” 2 900 (2,78), „półmaraton szczecin” 2 400 (6,39) [KS]. Do tego maratony, „dychy” i biegi górskie (nie liczone).

### SERP
- Frazy: „kalkulator tempa biegu” (narzędzie), „kalendarz biegów 2026”, „półmaraton gdynia 2026” (encja), „buty do biegania ranking”, „vo2max” [SERP].
- Kto wygrywa: narzędzia na małych stronach. Na „kalkulator tempa biegu” w top 10: patathlete.pl (0 domen), kalkulatorxxl.pl (10), kalkulatorbiegu.pl (24), mistrzowski-trening.pl (38), silesiarunner.pl (105), matnerrunning.pl (112) [SERP, BL]. Kalendarz: maratonypolskie.pl (1 615), kalendarzbiegowy.pl (191), biegigorskie.pl (394), treningbiegacza.pl (968), elektronicznezapisy.pl (2 451), running.life (3 171) [SERP, BL]. Encja biegu: strona organizatora, Facebook, Instagram, wyniki b4sport [SERP]. Sprzęt i VO2max: duże marki i sklepy (garmin.com 132 352, decathlon.pl 6 356, runningxpert.com 4 211) [BL].
- Liczby: mediana 968 domen, 11 z 40 wyników <300, 5 wyników <50 [BL]. Mediana zawyżona przez marki na „vo2max” i „buty”; na frazach narzędziowych i kalendarzowych konkurencja jest słaba.
- AI Overview: 4 z 5 (brak tylko na „buty do biegania ranking”) [SERP]. AIO cytuje małe serwisy: kalkulatorbiegu.pl (24 domeny), biegnijmy.pl, fitanka.pl, treningbiegacza.pl, kalendarzbiegowy.pl [SERP, BL]. Przy kalendarzu AIO wylicza konkretne biegi z datami, więc dobra baza wydarzeń ma szansę być cytowana.

### Zarobek
- CPC: mediana 0,37, ważone 0,60 USD [SV]. Wysokie na encjach i kalendarzu: „kalendarz biegów 2026” 8,13, „półmaraton szczecin” 6,39, „półmaraton polska 2026” 3,23, „półmaraton wrocław 2026” 2,78, „rozgrzewka przed bieganiem” 2,41 [SV, KS]. Ktoś płaci za ruch na biegi (organizatorzy, zapisy).
- Programy partnerskie: programów Decathlon Polska i sklepów biegowych **nie potwierdziłem** [WS]. Allegro Share 1,67% w punktach, aktualność niepotwierdzona [WS].
- Inne źródła (do sprawdzenia, bez kontaktu z firmami na tym etapie): płatne wyróżnienia biegów w kalendarzu, plany treningowe jako własny produkt (PDF lub subskrypcja, z zastrzeżeniem YMYL), afiliacja zegarków i butów.

### Fosa danych
- Otwartego zbioru danych o polskich biegach z licencją **nie znalazłem** [WS]. PZLA prowadzi kalendarz zawodów z atestem, bez API [WS]. Wyniki prowadzą firmy pomiaru czasu (np. wyniki.b4sport.pl, elektronicznezapisy.pl); ich regulaminów nie sprawdzałem.
- Fosą byłaby własna baza budowana z regulaminów organizatorów (data, dystanse, limit, wpisowe, atest, trasa), aktualizowana co roku. To praca, którą trudno skopiować; tak działa paliwownia.
- Narzędzia proste do zrobienia: kalkulator tempa, przelicznik km/h ↔ min/km, prognoza czasu na dystans (wzór Riegela), strefy tętna.

### Ryzyko
- YMYL-zdrowie: plany treningowe, VO2max, tętno. Bez porad medycznych; normy tylko ze źródłem.
- AIO 4 z 5 [SERP].
- Świeżość: daty biegów zmieniają się co roku, więc baza wymaga stałej aktualizacji.
- Popyt spada r/r o 6,8% [SV]; sezon wiosna i wrzesień.

### Pomysł na serwis
Huby: kalendarz biegów według miasta, województwa, dystansu i miesiąca oraz poradniki „pierwszy półmaraton/maraton”. Narzędzie: kalkulator tempa z prognozą czasu i opaską z międzyczasami dla konkretnego biegu (trasa z bazy). Strony encji: każdy bieg i każda edycja (data, dystanse, limit, wpisowe, link do zapisów, czasy zwycięzców ze źródłem).

### Werdykt
**Najlepsza z piątki, warto pogłębić.** Duży długi ogon encji (biegi) przy słabych SERP-ach narzędziowych i kalendarzowych, a wysokie CPC na frazach biegów pokazuje, że ktoś płaci za ten ruch. Przed decyzją trzeba potwierdzić płatnika: programy partnerskie sklepów biegowych i gotowość organizatorów do płacenia za wyróżnienie. Właściciel musi też zdecydować o treściach YMYL-zdrowie.

---

## E5. Kawa w domu: ekspresy, ziarna i palarnie, metody parzenia, proporcje

### Popyt
- Rdzeń: 46 fraz, suma 496 420/mies. [SV]. Największy w grupie.
- Trend r/r: −9,9% (1 365 600 vs 1 516 000) [SV]. Spadają: „kawa ziarnista” 114 100 → 66 600, „lavazza” 63 300 → 39 000, „cappuccino” 62 500 → 44 400 [SV]. Rosną: „ekspres do kawy z młynkiem” 11 600 → 18 600, „ekspres kolbowy” 62 500 → 72 300, „kawiarka” 71 500 → 81 300 [SV].
- Sezon: szczyt XII 2025 (739 070), dołek VI 2026 (365 110) [SV].
- Top frazy [SV]: „ekspres do kawy” 165 000 (CPC 0,60), „młynek do kawy” 33 100, „kawa ziarnista” 33 100 (1,03), „kawiarka” 27 100, „ekspres kolbowy” 22 200, „ekspres przelewowy” 18 100, „flat white” 18 100, „delonghi magnifica” 14 800, „aeropress” 14 800, „specialty coffee” 14 800, „palarnia kawy” 12 100 (1,38).

### SERP
- Frazy: „ranking ekspresów do kawy”, „proporcje kawy do wody” (narzędzie), „palarnia kawy” (encja), „delonghi magnifica” (encja: model), „kawa ziarnista ranking” [SERP].
- Kto wygrywa: sklepy, marki i porównywarki. „delonghi magnifica”: delonghi.com 5 z 7 wyników, reszta mediaexpert.pl [SERP]. Rankingi: coffeedesk.pl (2 003 domeny), neonet.pl (4 037), mediaexpert.pl (9 203), skapiec.pl (4 539), allegro.pl (59 005) [SERP, BL]. „palarnia kawy”: mapka z lokalnymi palarniami, potem sklepy palarni [SERP].
- Liczby: mediana 1 587 domen, najwyższa z piątki; 9 z 43 wyników <300 [BL].
- Słabe miejsca: „proporcje kawy do wody” (2 wątki Reddit sprzed 8–9 lat, cmsale.com, aquick.pl 170 domen); w rankingach kaw theintro.pl (35) i monkocoffee.pl (146) [SERP, BL].
- AI Overview: 1 z 5 („proporcje kawy do wody”) [SERP]. Cytuje sklepy i blogi kawowe (craftbe.pl, coffeelove.pl, kaffinity.pl) [SERP].

### Zarobek
- CPC: mediana 0,41, ważone 0,50 USD [SV]. Najwyżej: „palarnia kawy” 1,38, „kawa ziarnista” 1,03 [SV].
- Programy partnerskie: Coffeedesk widnieje w katalogu affi.io (status „Opened”, cookie 30 dni), ale w Admitad jako „Closed”; stawka nieznana; reklama w Google na marki zabroniona (https://affi.io/m/coffeedesk-pl) [WS]. Allegro Share 1,67% w punktach, aktualność niepotwierdzona [WS]. Programów Media Expert, Konesso i Morele nie znalazłem [WS].
- Plus: wysoka wartość koszyka (ekspres automatyczny 900–2 800 zł w karuzeli Allegro [SERP]).

### Fosa danych
- Otwartego źródła o ekspresach nie znalazłem. Ekspresy do kawy, według mojej wiedzy, nie mają unijnej etykiety energetycznej, więc nie ma ich w EPREL (do potwierdzenia).
- Open Food Facts (licencja ODbL, użycie komercyjne dozwolone z tą samą licencją) ma produkty kawowe; pokrycia polskich palarni nie sprawdzałem.
- Palarnie jako encje: tylko ręczne zbieranie. Dane z Map Google wolno używać wyłącznie zbiorczo (zasada projektu).
- Narzędzia (kalkulator proporcji, czas parzenia) łatwo skopiować.

### Ryzyko
- Niskie YMYL (kofeina to drobny wątek zdrowotny), AIO 1 z 5 [SERP].
- Ryzyko konkurencyjne: SERP zajęty przez sklepy z tysiącami domen linkujących [BL]. Popyt spada r/r o 9,9% [SV].

### Pomysł na serwis
Huby: ekspresy według typu (automatyczne, kolbowe, przelewowe, kapsułkowe), metody parzenia, ziarna i palarnie. Narzędzie: kalkulator proporcji i „dobierz ekspres” (budżet, mleko, liczba kaw dziennie). Strony encji: każdy model ekspresu z parametrami od producenta i każda polska palarnia z ofertą ziaren.

### Werdykt
**Nie.** Duży popyt, ale SERP należy do sklepów i marek, brak otwartych danych i potwierdzonej afiliacji ze stawką. Nasz model (encje z danych) nie daje tu przewagi.

---

## Czego nie sprawdzono

- Reklamodawców w Google Ads (`/v3/serp/google/ads_advertisers/live/advanced`) nie pobierałem; o płatnikach świadczy tylko CPC.
- Licencji EPREL i warunków ponownego użycia treści nbp.pl nie udało się potwierdzić u źródła (strona EPREL nie otworzyła się z tej sesji).
- Stawek programów partnerskich (poza AZ Aurum: 12,5%) nie potwierdziłem. Nie rejestrowałem się nigdzie i nie kontaktowałem z firmami.
- Domeny linkujące liczone dla całych domen, nie dla konkretnych podstron [BL].
- Wiek wyników znany tylko tam, gdzie Google pokazał datę [SERP].

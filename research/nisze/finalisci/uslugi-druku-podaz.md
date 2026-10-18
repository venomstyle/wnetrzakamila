# Usługi druku 3D jako produkt: podaż, konkurencja, model (18.10.2026)

Brief: `BRIEF-uslugi-druku.md`. Serwis treściowy: `druk3d.md`. Popyt i reklamy bada osobny agent.

**Oznaczenia źródeł (wszystko pobrane 18.10.2026):**
- **[M]** DataForSEO `/v3/serp/google/maps/live/advanced`, fraza „druk 3d {miasto}”, location 2616, pl, depth 100. W plikach tylko liczby zbiorcze.
- **[L]** DataForSEO Labs: `bulk_traffic_estimation/live` (ruch organiczny w PL, etv), `ranked_keywords/live`, `serp_competitors/live` (14 fraz usługowych).
- **[V]** `/v3/keywords_data/google_ads/search_volume/live`, średnia 10.2025–09.2026.
- **[P]** `/v3/on_page/content_parsing/live` (adres przy liczbie).
- **[WWW]** WebSearch (źródło wtórne albo opis strony, adres przy liczbie).

Dane: `dane/uslugi-druku-podaz-mapy.csv`, `-mapy-kategorie.csv`, `-posrednicy.csv`, `-kanaly.csv`, `-serp-konkurenci.csv`, `-frazy-podazy.csv`, `-rachunek.csv`. Skrypty: scratchpad `uslugi-podaz/` (`maps_agg.py`, `rachunek.py` i inne).

---

## Werdykt w skrócie

**WARUNKOWO, tylko model b w lekkiej wersji:** formularz „wyślij zapytanie do 3 drukarni” jako moduł serwisu z `druk3d.md`, najpierw jako test „wkrótce”, potem płatny od drukarni za zapytanie. **NIE** dla osobnego katalogu, wyceny STL jako głównego produktu i marketplace’u z prowizją.

1. **Podaż jest, ale rozproszona i mała.** W 10 największych miastach Mapy Google pokazują 286 profili druku 3D [M]; poza Warszawą Google wyczerpuje listę na 19–59 wynikach. Oferteo podaje 1 496 firm w kategorii [P]. Mediana profilu w Mapach to 8 opinii [M]. To setki małych pracowni.
2. **Miejsce „wgraj STL i poznaj cenę” jest zajęte przez drukarnie.** Drukarex (jedna drukarnia z Wrocławia z konfiguratorem) jest na poz. 2 dla „druk 3d” (8 100/mies.) i na poz. 1 dla „druk 3d na zamówienie”, „wydruk 3d”, „usługi druku 3d” i „druk 3d warszawa” [L]. Pośrednicy międzynarodowi (Craftcloud, Treatstock) mają w PL ruch bliski zeru: etv 2,4 i 4,6 [L].
3. **Zarobek z pośrednictwa jest mały i zależy od zimnego startu.** Rachunek po 12 mies.: model b daje ok. **280 zł/mies. (ostrożny)** i najwyżej **ok. 6 300 zł/mies. (realny)**, a realny wymaga ok. 20 płacących drukarni i poz. 4 na frazach usługowych [rachunek, większość parametrów to założenia]. Drukarnie same szukają „zlecenia druk 3d” (170 + 140 + 110 = 420 wyszukiwań/mies. [V]), więc da się je przyciągnąć bez kontaktu, ale powoli.

**Warunek „tak”:** test „wkrótce” na serwisie z `druk3d.md` pokaże co najmniej 30 kliknięć „wyślij zapytanie” miesięcznie przez 2 miesiące, a strona „Dla drukarni” zbierze co najmniej 10 zgłoszeń bez żadnego kontaktu z naszej strony. Progi to moja propozycja do decyzji właściciela.

---

## 1. Ilu jest usługodawców [M][P]

### Mapy Google, 10 miast (`dane/uslugi-druku-podaz-mapy.csv`)

Profil liczę jako „druk 3D”, gdy ma kategorię „Usługi drukowania 3D” (główną lub dodatkową) albo „3D” w nazwie. Odpadły punkty ksero, drukarnie poligraficzne i agencje reklamowe (132 z 418 wyników).

| Miasto | Wyniki | Profile 3D | W granicach miasta | Z własną www | Mediana opinii | Mediana oceny |
|---|---|---|---|---|---|---|
| Warszawa | 100 | 76 | 69 | 59 | 8 | 4,9 |
| Kraków | 46 | 35 | 28 | 32 | 11 | 4,9 |
| Wrocław | 59 | 38 | 30 | 34 | 9,5 | 5,0 |
| Łódź | 42 | 27 | 22 | 21 | 5 | 5,0 |
| Poznań | 55 | 30 | 26 | 26 | 5,5 | 5,0 |
| Gdańsk | 20 | 18 | 16 | 14 | 6 | 5,0 |
| Szczecin | 19 | 19 | 17 | 14 | 11 | 5,0 |
| Bydgoszcz | 25 | 12 | 10 | 8 | 2 | 5,0 |
| Lublin | 22 | 17 | 16 | 14 | 10 | 4,7 |
| Białystok | 30 | 16 | 7 | 12 | 17,5 | 5,0 |
| **Razem (unikalne)** | **418** | **286** | | **232 (81%)** | **8** | **5,0** |

- Kategoria główna „Usługi drukowania 3D”: 120 z 286 profili. Reszta to drukarnie poligraficzne (32), doradztwo inżynieryjne (17), druk cyfrowy (11), producenci (9) [M, `-mapy-kategorie.csv`].
- 38 profili bez strony, 16 tylko z Facebookiem lub Instagramem. Razem 54 (19%) [M].
- 257 profili (90%) jest przejętych przez właściciela. 63 (22%) nie ma opinii, 28 (10%) ma ponad 50 [M].
- Tylko Warszawa dała pełne 100 wyników. W 9 miastach Google pokazał wszystko, co ma, czyli 19–59 wyników. Liczby są więc bliskie pełnej podaży w Mapach dla tych miast.

### Inne źródła podaży

- **Oferteo, kategoria „Druk 3D”:** 1 496 firm w Polsce, 187 opinii, średnia ocena 4,76, „średni koszt” usługi 368–928 zł netto (https://www.oferteo.pl/druk-3d [P]).
- **OLX, Usługi, „druk 3d”:** 295 ogłoszeń. Najwięcej w mazowieckim (60), śląskim (46) i małopolskim (38) (https://www.olx.pl/uslugi/q-druk-3d/ [P]; suma liczników województw).
- **Allegro:** nie udało się odczytać. `content_parsing` zwrócił pustą odpowiedź albo przekroczył czas, a WebFetch nie znalazł adresu. W `serp_competitors` Allegro stoi na poz. 3 dla „druk 3d na zamówienie” i poz. 6 dla „wydruk 3d na zamówienie”, a Allegro Lokalnie na poz. 9 [L].

**Wniosek:** podaż to kilkaset firm i pracowni z mapy plus kilkaset ogłoszeń hobbystów. Druk wysyła się kurierem, więc jedna drukarnia obsługuje cały kraj. To ułatwia zimny start (wystarczy kilkanaście drukarni), ale też pozwala jednej dużej drukarni z dobrym SEO zebrać ruch bez pośrednika.

## 2. Konkurenci i pośrednicy [L][P][WWW]

Pełna tabela: `dane/uslugi-druku-podaz-posrednicy.csv`. Zamiast `domain_rank_overview` dla każdej domeny użyłem jednego zapytania `bulk_traffic_estimation` (ta sama miara: szacowany ruch organiczny w PL) i `ranked_keywords` dla domen z ruchem.

| Pośrednik | Działa w PL | Model zarobku i stawki | Ruch org. w PL (etv / frazy) | Co robi słabo |
|---|---|---|---|---|
| Craftcloud (All3DP) | wysyłka tak, treści PL brak | marketplace; partnerzy ustalają ceny, Craftcloud bierze „stały procent” od zamówienia, % nie podany (all3dp.com/1/craftcloud-cheaper-without-compromising-quality/ [WWW]); partner musi być firmą (craftcloud3d.com/en/become-a-partner [P]) | 2,4 / 2 | po angielsku, brak widoczności w PL; programu dla wydawców nie znalazłem |
| Treatstock | globalnie | escrow; opłata min. 2,99 USD, maks. 25% (treatstock.com/help/article/140-selling-fee [P]), doliczana do ceny i potrącana z wypłaty (…/100-manufacturing-fee [P]) | 4,6 / 3 | po angielsku, marginalny w PL; programu afiliacyjnego nie znalazłem |
| Xometry Europe | tak, wersja /pl/ | marża; dla partnera bez opłat i prowizji, 2 000+ partnerów w Europie (xometry.eu/en/?p=41920 [WWW]) | 377,9 / 21 | B2B przemysłowe (CNC, MJF, metal); ruch głównie z marki („xometry” 720/mies. [V]) |
| Protolabs Network (Hubs) | sprzedaż do UE | marża; 250+ partnerów (en.wikipedia.org/wiki/Protolabs_Network [WWW]) | 84,6 / 19 | tylko B2B, brak treści PL |
| JLC3DP | wysyłka z Chin | własne fabryki; afiliacja 5 USD gotówką albo kupon 8 USD za klienta z zamówieniem (jlc3dp.com/help/article/affiliate-program [WWW]; parser nie odczytał strony) | 165,9 / 20 | dostawa z Chin, brak w top 60 fraz usługowych |
| PCBWay | wysyłka z Chin | 10% od zamówień z udostępnionych projektów; stawka afiliacyjna niepodana (strona z 2018) [WWW] | 1 584,8 / 13 | druk 3D poboczny wobec PCB |
| Oferteo | tak | wykonawca płaci punktami za kontakt; 25 pkt = 259 zł netto (10,36 zł/pkt) do 1 200 pkt = 7 199 zł (6,00 zł/pkt), ważne 12 mies.; koszt zapytania w pkt zależy od branży, nie podany dla druku 3D (oferteo.pl/cennik [P]) | 340 570 / 52 897 (cały serwis) | w druku 3D: 21 fraz, etv 14,5; najlepiej poz. 11–12 (Lublin, Poznań), Warszawa poz. 36 |
| Fixly | tak | punkty: oferta 0–50 pkt, numer 0–10 pkt; pakiety 30 pkt 99 zł do 700 pkt 999 zł brutto (kydi.pl/baza-wiedzy/fixly-dla-wykonawcow-cennik/, stan 09.2026, wtórne) | 54 810 / 5 494 (cały serwis) | **brak kategorii druku 3D**; 0 fraz o druku 3D |
| Zlecenia Przez Net | nie potwierdzono | cennika nie znalazłem | brak danych | nie da się ocenić |
| Polskie katalogi druku 3D | — | **nie znalazłem żadnego** katalogu ani porównywarki drukarni 3D z wpisem dla firm (WebSearch, `serp_competitors`) | — | luka |

**Kto naprawdę zbiera ruch usługowy** (`serp_competitors`, 14 fraz: „druk 3d na zamówienie”, „usługi druku 3d”, 6 miast, „wycena druku 3d” i inne; `dane/uslugi-druku-podaz-serp-konkurenci.csv`):

- **drukarex.pl** (drukarnia z konfiguratorem STL): etv 1 856, 44 frazy. Poz. 2 „druk 3d” (8 100), poz. 1 „wydruk 3d” (2 400), poz. 1 „druk 3d na zamówienie” (1 600), poz. 1 „usługi druku 3d”, poz. 1 „druk 3d warszawa” (880), osobne strony miast. Marka „drukarex” ma 210 wyszukiwań/mies. [L][V].
- **send3d.eu**: druga drukarnia z automatyczną wyceną online (send3d.eu [P]); słaba widoczność (etv 34,7).
- OLX poz. 1 dla „wydruk 3d na zamówienie” i „druk 3d poznań”; Facebook poz. 5 w Krakowie, Wrocławiu i Poznaniu; katalogi ogólne (Panorama Firm, Baza Firm, Cylex) poz. 3–8 w Poznaniu [L].
- Reszta top 10 to strony pojedynczych drukarni (cadxpert.pl, protoplastic.pl, solid3d.pl, 3d-innowacje.pl, ajmaker.pl i inne).

**Wniosek:** pośrednika w polskim Google nie ma. Oferteo jest daleko, Fixly nie ma kategorii, zagraniczne platformy nie istnieją po polsku. Luka jest prawdziwa, ale ruch usługowy już dziś odbierają drukarnie z własnymi stronami miast i konfiguratorem.

## 3. Jak drukarnie zdobywają klientów

- **Mapy Google i własna strona:** 81% profili ma stronę, 90% przejętych wizytówek [M]. To główny kanał.
- **Oferteo:** 1 496 firm w kategorii [P]. Ilu z nich kupuje punkty, nie wiadomo. Oferteo nie ujawnia, ile punktów kosztuje zapytanie o druk 3D.
- **Fixly:** brak kategorii, więc nie [P][L].
- **OLX:** 295 ogłoszeń usługowych [P], głównie mniejsi wykonawcy.
- **Allegro:** obecne w SERP dla „druk 3d na zamówienie” (poz. 3) [L], liczby ofert nie odczytałem.
- **Google Ads:** CPC „druk 3d na zamówienie” 1,44 USD (`druk3d.md` [W]); szczegóły reklamodawców bada drugi agent.
- **Same szukają zleceń:** „zlecenia druk 3d” 170, „zlecenia na druk 3d” 140, „druk 3d zlecenia” 110, „farma drukarek 3d” 90, „jak zarabiać na drukarce 3d” 70 wyszukiwań/mies. [V]. To kanał pozyskania drukarni bez kontaktu z nimi.

## 4. Modele dla nas

Rachunek: `dane/uslugi-druku-podaz-rachunek.csv`. Ruch liczony z 12 fraz usługowych i cenowych (15 610/mies.) i 5 głów (18 700/mies.) [L][W]. Ostrożny: poz. 8 na frazach usługowych, głowy poza top 10. Realny: poz. 4 i głowy na poz. 8. Konwersja sesji na zapytanie 3% / 6%. Wszystko poza wolumenami i krzywą CTR (SEO Inc. 2025, jak w `druk3d.md`) to założenia.

| | Ostrożny | Realny |
|---|---|---|
| Sesje usługowe/mies. | 416 | 1 754 |
| Zapytania/mies. | 12,5 | 105 |

| Model | Przychód/mies. po 12 mies. (ostr. / real.) | Koszt budowy | Ryzyko | Bez zimnego kontaktu? | Ocena |
|---|---|---|---|---|---|
| **a) katalog, darmowy wpis + wyróżnienie 49 zł/mies.** | 147 zł / 735 zł (3 / 15 płacących) | niski: formularz zgłoszenia, moderacja, strony miast | pusty katalog na starcie; wpisy z Map bez zgody (patrz niżej) | tak, jeśli wpisy tylko ze zgłoszeń | **NIE jako produkt.** Przychód za mały. Katalog ma sens tylko jako zaplecze dla b. |
| **b) zapytanie do 3 drukarni, opłata za zapytanie** | 281 zł / 6 313 zł (15 / 25 zł netto za zapytanie, 50% / 80% miejsc wykupionych) | niski–średni: formularz z plikiem, routing po materiale i terminie, panel lub e-mail dla drukarni, rozliczenia | zimny start; spory o jakość zapytań; realny wariant wymaga ok. 21 drukarni po ok. 12 zapytań | tak | **WARUNKOWO.** Jedyny model z sensownym górnym pułapem. Stawka 15–25 zł to ok. 2–7% średniego zlecenia 368–928 zł netto [P]. |
| **c) wycena natychmiastowa (STL → szacunek) + przekazanie** | 421 zł / 9 470 zł (b × 1,5 zapytań, założenie) | średni–wysoki: parser STL (objętość, gabaryt), cenniki drukarni, utrzymanie | drukarex.pl i send3d.eu już to robią i stoją wyżej; szacunek „z kalkulatora” różni się od ceny drukarni | tak | **NIE jako start.** Dodać później do b jako „szacunek” (objętość i orientacyjny przedział), bez obietnicy ceny. |
| **d) marketplace z prowizją** | 224 zł / 3 078 zł przed kosztami płatności (12–15% od zamówienia 500–650 zł, 30% akceptacji) | wysoki: płatności dzielone, escrow, reklamacje, obsługa | odpowiedzialność za jakość i terminy cudzych wydruków; Treatstock potrzebuje do 25% prowizji i globalnej skali | tak | **NIE.** Nierealny dla małego zespołu bez obsługi klienta. |
| **e) afiliacja do platform** | ok. 10 USD / 44 USD (JLC3DP 5 USD za klienta, 10% klik, 5% zamówień) | bardzo niski | Craftcloud i Treatstock nie mają programu (nie znalazłem); JLC3DP wysyła z Chin | tak | **Tylko dodatek** w poradnikach („tanio z Chin”), bez znaczenia dla przychodu. |

Dla porównania serwis treściowy z `druk3d.md` daje 120–1 860 zł/mies. z afiliacji sprzętu. Model b może go uzupełnić. Zastąpić go nie da rady.

### Zimny start: skąd pierwsze drukarnie bez kontaktu z nimi

| Sposób | Ocena |
|---|---|
| **Wpisy z danych publicznych (Mapy, strony firm) bez zgody** | **Odradzam.** Część drukarni to jednoosobowe działalności, więc ich dane firmowe to dane osobowe. UODO ukarał Bisnode w 2019 r. kwotą 943 470 zł za brak informacji dla przedsiębiorców z rejestrów publicznych; WSA uchylił część decyzji z karą (pro.rp.pl/abc-firmy/art39132691 [WWW]). Do tego wpis, za którego wyróżnienie potem prosimy o pieniądze, wygląda jak model, którego firmy nie lubią. To ryzyko do decyzji właściciela, nie treść na stronę. |
| **Przekazywanie zapytań klientów drukarniom, które się nie zapisały** | **Odradzam.** Formalnie to prośba klienta, ale w praktyce my inicjujemy kontakt z firmą. Narusza zasadę „drukarnie przychodzą same”. |
| **Strona „Zlecenia na druk 3D: odbieraj zapytania”** (SEO pod 420 wyszukiwań/mies. [V]) | **Tak.** To ten sam mechanizm co w niechcieznajda („fachowcy szukają zleceń”). Na starcie pokazuje licznik zebranych zapytań i darmowy okres. |
| **Ogłoszenie w społecznościach** (grupa FB „Druk 3D Polska”, forum, reddit) | **Tak, jeśli właściciel się zgodzi.** Post właściciela jako członka grupy nie jest zimnym kontaktem. Regulaminy grup często zakazują jednak reklam. Do sprawdzenia przy publikacji. |
| **Darmowe zapytania przez pierwsze 3 mies.** | **Tak.** Drukarnia zapisuje się sama, dostaje zapytania za darmo, a opłata rusza po ogłoszonej z góry dacie. |

**Czy to wystarczy?** Na start w skali kilkunastu drukarni prawdopodobnie tak, bo druk wysyła się w całej Polsce i nie trzeba pokrywać każdego miasta. Na wariant realny (ok. 21 płacących) potrzeba 6–12 mies. i ruchu z serwisu treściowego. Tego nie da się dziś zmierzyć; to ocena.

**Kolejność:** najpierw popyt, potem podaż. Serwis z `druk3d.md` ma frazy „ile kosztuje druk 3d” (4 400) i „druk 3d ceny” (5 400) [W]. Na tych stronach przycisk „wyślij zapytanie do 3 drukarni” jako „wkrótce” (jak `Newsletter.astro` w playbooku: liczy kliknięcia, nie zbiera danych). Dopiero przy progu z werdyktu otwieramy stronę „Dla drukarni”.

## 5. Pokrycie z niechcieznajda.pl

niechcieznajda.pl to poradniki dla fachowców (głównie budowlanka) i strona lub audyt dla fachowca (`playbook/README.md`).

- **Odbiorcy się nie pokrywają.** Drukarnie 3D to pracownie techniczne i hobbyści z drukarkami. niechcieznajda trafia do hydraulików i ekip remontowych. Brak kanibalizacji fraz: niechcieznajda celuje w „zlecenia budowlane” (2 400/mies., playbook), druk 3D w „zlecenia druk 3d” (170/mies.) [V].
- **Model się uzupełnia.** Ta sama logika: wykonawca szuka zleceń. Formularz, test „wkrótce”, cele w Plausible i strona „Dla wykonawców” przenoszą się 1:1.
- **Mała sprzedaż krzyżowa:** 54 z 286 profili (19%) nie ma własnej strony [M]. Ofertę „strona dla wykonawcy” z niechcieznajda można pokazać na stronie „Dla drukarni” (tylko przychodzący, bez kontaktu).
- **Ryzyko:** dwa produkty lead-gen dla wykonawców dzielą czas właściciela, a marki nie wolno mieszać (niechcieznajda to budowlanka).

## 6. Werdykt

**Model b (zapytanie do 3 drukarni) jako moduł serwisu z `druk3d.md`: WARUNKOWO.** Katalog (a), wycena STL jako osobny produkt (c) i marketplace (d): NIE. Afiliacja platform (e): tylko dodatek.

1. **Luka jest prawdziwa:** w polskim Google nie ma pośrednika druku 3D. Oferteo stoi na poz. 11–36, Fixly nie ma kategorii, Craftcloud i Treatstock mają etv poniżej 5 [L]. Podaż istnieje (286 profili w 10 miastach, 1 496 firm w Oferteo) [M][P].
2. **Pułap jest niski i trudny:** frazy usługowe to ok. 15 600 wyszukiwań/mies. [L][W], a ich górę trzyma drukarnia z konfiguratorem (drukarex.pl). Rachunek: 280 zł/mies. ostrożnie, do ok. 6 300 zł/mies. przy poz. 4 i ok. 21 płacących drukarniach.
3. **Zasady właściciela da się zachować:** drukarnie mogą przyjść same (420 wyszukiwań „zlecenia druk 3d”/mies. [V], społeczności, darmowy okres), a test „wkrótce” sprawdza popyt bez kosztów. Wpisy z Map bez zgody odpadają.

## Czego nie sprawdzono

- Liczby ofert „druk 3d na zamówienie” na Allegro (strona nieczytelna dla parsera).
- Ile punktów Oferteo kosztuje zapytanie o druk 3D (nie podano publicznie; wymaga konta).
- Prowizji Craftcloud dla partnerów (wymaga zgłoszenia jako firma) i stawek Hubs.
- Oficjalnej strony cennika Fixly (dane z kydi.pl, stan 09.2026, wtórne) i treści strony afiliacyjnej JLC3DP (parser zwrócił pusty szablon; stawka ze streszczenia WebSearch).
- Zlecenia Przez Net: domeny i cennika nie ustaliłem.
- Ostatecznego wyroku NSA w sprawie Bisnode.
- Reklamodawców Google Ads na frazy usługowe (zakres drugiego agenta).

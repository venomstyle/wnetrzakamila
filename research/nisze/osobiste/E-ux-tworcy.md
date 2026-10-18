# Nisze osobiste E: UX/UI po polsku oraz twórcy wideo w Polsce (18.10.2026)

Brief: `osobiste/BRIEF.md`, metoda: `../METODA.md`. Rynek: Polska (location_code 2616, język pl). Wszystkie dane pobrano 18.10.2026. Obie nisze oceniono osobno.

**Znaczniki źródeł:**

- **[V]** `/v3/keywords_data/google_ads/search_volume/live`, 24 mies. (10.2024–09.2026). Wolumen = średnia z 10.2025–09.2026, trend r/r = suma 07–09.2026 do 07–09.2025, CPC w USD. Dane: `dane/E-ux-popyt.csv`, `dane/E-tworcy-popyt.csv`, `dane/E-popyt-podsumowanie.csv`.
- **[L]** `/v3/dataforseo_labs/google/keyword_suggestions/live` (ziarna: „ux”, „figma”, „youtube”, „ile zarabia”), tylko do rozszerzenia listy.
- **[S]** `/v3/serp/google/organic/live/advanced`, desktop, depth 10, `load_async_ai_overview`. Dane: `dane/E-ux-serp-top10.csv`, `dane/E-tworcy-serp-top10.csv`, `dane/E-serp-podsumowanie.csv`.
- **[B]** `/v3/backlinks/bulk_referring_domains/live` dla 94 URL-i i 73 domen z top 10.
- **[T]** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` (ETV w PL). Dane: `dane/E-konkurencja.csv`.
- **[A]** `/v3/serp/google/ads_advertisers/live/advanced`.
- **[P]** `/v3/on_page/content_parsing/live` (strony programów partnerskich i regulaminów, bo WebFetch był blokowany przez proxy).
- **[W]** WebSearch (tylko wskazanie adresu albo informacja oznaczona jako niepotwierdzona).

Programy partnerskie: `dane/E-programy-partnerskie.csv`. Ceny kursów: `dane/E-ux-kursy-ceny.csv`. Źródła danych i licencje: `dane/E-zrodla-danych.csv`. Rachunek: `dane/E-rachunek.csv`. Skrypty: `/tmp/claude-0/-home-user-wnetrzakamila/1ba86930-7213-5036-9c2e-f13d81b0db89/scratchpad/os-E/` (`vol24.py`, `nav.py`, `serp.py`, `serp_an.py`, `tabele.py`).

---

## Werdykt w skrócie

| | UX/UI po polsku | Twórcy wideo w Polsce |
|---|---|---|
| **Werdykt** | **NIE** (jako osobny serwis) | **NIE** |
| **Wynik ważony** | **2,40 / 5** | **2,25 / 5** |
| Dopasowanie do profilu (poza wagą) | 4 / 5 | 3 / 5 |
| Popyt informacyjny (bez zapytań o marki) | 82 582 / mies., r/r −5,4% | 92 693 / mies., r/r −4,9% |
| Rdzeń, na którym da się zarobić | kursy 1 996 / mies. (r/r −54%) | zarobki twórców 8 861 (r/r −34%), narzędzia 853 |
| AI Overview w SERP | 5 z 6 | 5 z 6 |
| Główny model zarobku | afiliacja kursów (strefakursów 50% pierwszego zamówienia, Coursera 15–45%) | afiliacja narzędzi w USD (vidIQ 15–25%, ElevenLabs 22%, Riverside do 20%) |
| Rachunek, 12. miesiąc (ostrożny / realny) | ok. 80 zł / ok. 1 060 zł miesięcznie | ok. 65 zł / ok. 440 zł miesięcznie |

**UX/UI.** Właściciel zna temat, ale popyt, który płaci, jest mały i spada. Frazy o kursach dają 1 996 wyszukiwań miesięcznie i spadły r/r o 54%, frazy o zawodzie i zarobkach o 46% [V]. Bootcampy nie mają publicznych programów za lead, a na „kurs ux” nikt nie kupuje reklam [A]. Słownik UX ma ruch, ale 5 z 6 SERP-ów ma AI Overview, które odpowiada na definicje w całości [S].

**Twórcy wideo.** Duża liczba w popycie to marki (Canva, CapCut, ElevenLabs), których serwis nie przejmie. Zostaje ok. 20 tys. zapytań o zarobki, kanały i start, plus sprzęt, gdzie wygrywają sklepy (8 z 9 wyników) [S]. Strony encji kanałów blokuje regulamin YouTube API: statystyk kanału bez zgody właściciela nie wolno trzymać dłużej niż 30 dni ani liczyć z nich własnych metryk czy rankingów, chyba że Google zaakceptuje audyt [P]. CapCut nie płaci za polskich klientów [P].

---

## 1. UX/UI po polsku

### 1.1 Popyt [V]

**Jak zbudowano:** 78 fraz rdzeniowych w 6 grupach plus 17 fraz z [L] (np. „ux ui design”, „figma make”, „ux tester”). Razem 95 fraz, 94 bez duplikatu („ux research” i „ux researcher” Google łączy w jeden wolumen). Frazy, które są nazwą produktu (Figma, Miro, Behance, Dribbble, Webflow, Framer, Adobe XD, Axure), oznaczono jako nawigacyjne. Serwis ich nie przejmie, bo wygrywa strona producenta.

| Grupa | Fraz | Wolumen / mies. | Trend r/r | Uwagi |
|---|---|---|---|---|
| Wszystko (bez duplikatu) | 94 | 229 083 | −10,9% | 146 501 to nazwy marek (figma 59 250, miro 44 600, behance 16 067) |
| **Informacyjne i komercyjne** | 83 | **82 582** | **−5,4%** | najsłabszy 08.2026: 63 220, najmocniejszy 03.2026: 98 830; ważony CPC 1,42 USD |
| Wzorce UI i narzędzia online | 6 | 43 718 | −14,1% | „lorem ipsum” 27 308, „paleta kolorów” 13 225 (wieloznaczna: farby, makijaż), „kontrast kolorów” 165 |
| Słownik i metody | 24 | 24 662 | +4,4% | „ux ui design” 5 117 (skok: 12 600 w 07–09.2026 vs 1 460 rok wcześniej), „ux” 2 983, „wireframe” 1 390, „heurystyki nielsena” 562 |
| Zawód i zarobki | 22 | 6 746 | **−46,2%** | „ux designer” 1 683 (r/r −51%), „ux designer zarobki” 195, „ile zarabia ux designer” 49 |
| Narzędzia (bez marek) | 9 | 5 374 | +310,7% | skok to jedna fraza: „figma tutorial” 21 100 vs 550 w 07–09; „figma cena” 94, „figma vs framer” 10 |
| **Kursy i bootcampy** | 18 | **1 996** | **−54,0%** | „kurs ux” 281, „kurs ux designer” 239, „kurs ux design” 222, „kurs figma” 203, „bootcamp ux” 12 |
| Portfolio i rekrutacja | 4 | 86 | −43,2% | „portfolio ux designer” 63; „zadanie rekrutacyjne ux” 0 |

**Wniosek:** rdzeń zawodowy i kursowy (zawód, kursy, portfolio) to 8 828 wyszukiwań miesięcznie i spada o ok. połowę r/r. Kursy mają szczyt w 03.2026 (3 440), dołek w 09.2026 (680).

**CPC [V]:** „kurs ux” 2,18 USD, „kurs ux designer” 2,12, „kurs ux design” 2,41, „kurs figma” 2,67, „ux studia” 3,62, „google ux design certificate” 3,55, „audyt ux” 6,21, „testy użyteczności” 6,67, „wireframe” 4,05. Kursy mają wyższe CPC niż reszta, ale przy tym wolumenie to małe pieniądze. **Kto płaci za reklamy:** dla „kurs ux” Ads Transparency nie zwraca reklamodawców (status 40102 „No Search Results”) [A], a SERP z 18.10 nie ma bloku reklam [S].

### 1.2 Kto wygrywa i słabość SERP [S][B][T]

Sprawdzono 6 fraz: „kurs ux” (komercyjna), „ux designer zarobki” (zarobki), „ux ui design” (hub słownika), „figma cena” (encja narzędzia), „kontrast kolorów” (narzędzie), „heurystyki nielsena” (słownik).

| Fraza | Wol. | AIO | Mediana dom. link. domeny (bez platform) | Domeny <50 | Sprzed 2023 | Kto wygrywa |
|---|---|---|---|---|---|---|
| kurs ux | 281 | tak | 500 | 2 | 0 | 9 z 9: kursodawcy (grow.google, strefakursow.pl, learndesign.pl, Udemy, Future Collars, Comarch, Alx) |
| ux designer zarobki | 195 | tak | 1 213 | 0 | 2 | portale pracy i płac (bulldogjob, jooble ×3, randstad, zarobky) i 2 blogi agencji |
| ux ui design | 5 117 | tak | 187 | 0 | 1 | blogi agencji i software house'ów (designpractice 187, damianrams 54, devstock 82, blurify 90) |
| figma cena | 94 | nie | 24 | 1 | 0 | 5 × figma.com, sklepy z kontami „edukacyjnymi” (G2A, pixystore.eu), Allegro, Reddit |
| kontrast kolorów | 165 | tak | 33 | 3 | 1 | słabe domeny: Politechnika Rzeszowska (0), tworze.com (4), lepszyweb.pl (33), imagecolorpicker.com |
| heurystyki nielsena | 562 | tak | 681 | 1 | **5 z 7** | nr 1 uxchojrak.pl (3 domeny linkujące), stare wpisy agencji (widzialni 2020, thestory 2019, 2022) |

**Liczby zbiorcze:** 47 wyników organicznych. 46 z 47 URL-i ma mniej niż 10 domen linkujących, więc liczy się domena i treść. Mediana domen linkujących domeny: 1 136, bez platform (figma.com, Google, Udemy, Allegro, G2A, Reddit, YouTube) 500; 7 z 35 domen bez platform ma mniej niż 50. 9 z 11 wyników z datą jest sprzed 2023 r. [S][B].

**Kto wygrywa w niszy [T] (ETV w PL):** płace i praca: wynagrodzenia.pl 267 847, nofluffjobs.com 74 522, justjoin.it 36 734, theprotocol.it 16 071, bulldogjob.pl 14 285. Szkoły: coderslab.pl 46 921, learndesign.pl 11 390, itmedia.pl 10 760, strefakursow.pl 7 175, futurecollars.com 2 560. Blogi eksperckie są małe: ux.marszalkowski.org 529, damianrams.pl 404, ux-man.pl 101. **uxdesign.pl ma ETV 10**, więc nie jest konkurentem. Słabe miejsca są w słowniku (stare wpisy agencji, mały blog na 1. miejscu), ale to frazy, które AIO zjada.

**AI Overview:** 5 z 6 SERP-ów (bez „figma cena”). AIO dla „kurs ux” sam porównuje kursy z cenami (Google Certificate, strefakursów 914 zł, Future Collars 6 700 zł, IT Media 5 400 zł netto, Alx 3 790 zł). AIO dla „heurystyki nielsena” wypisuje wszystkie 10 heurystyk. AIO cytuje małe serwisy: damianrams.pl (54 domeny linkujące), learndesign.pl (28), testy.lepszyweb.pl (33), artnova.com.pl, webmetric.com [S][B].

### 1.3 Zarobek

**Kursy i bootcampy: czy płacą za leady?** Publicznie nie. Nie znaleziono programów partnerskich ani płatności za lead u Future Collars, Coders Lab, Alx i IT Media [W]. Potwierdzone u źródła [P]:

| Program | Warunki | Status |
|---|---|---|
| strefakursów.pl | 50% wartości netto **pierwszego** zamówienia, 30 dni od kliknięcia, wypłata na fakturę lub rachunek po 31 dniach (regulamin z 15.02.2022) | potwierdzone |
| Coursera (Impact) | 15–45% od zakupów w 30 dni; przy subskrypcji tylko 1. miesiąc; przypis: „Degrees and Certificate purchases excluded” | potwierdzone, zakres dla certyfikatu Google niejasny |
| Framer | 50% płatności przez 12 mies., cookie 90 dni, wypłata od 200 USD, zakaz kuponów | potwierdzone |
| Figma | program zamknięty 16.08.2024 | potwierdzone (zamknięty) |
| Webflow, Udemy | nie sprawdzono | — |

**Porównanie kursów z cenami (odczyt 18.10.2026 z SERP i AIO, `dane/E-ux-kursy-ceny.csv`):** Future Collars „UX Designer & AI” 6 700 zł (10 × 670 zł), IT Media pakiet UX/UI 5 400 zł netto, Alx K-UX 3 790 zł, IT Media kurs Figma 1 900 zł netto, strefakursów ścieżka UX/UI 914 zł (promocja). To ceny widoczne w wyszukiwarce. Na stronę trafiłyby dopiero po sprawdzeniu w cennikach, inaczej „sprawdź w cenniku” z linkiem.

**Zarobki UX designera: dane z licencją.** Otwartych danych o płacach UX nie ma. Raporty, które cytuje AIO, są chronione: Bulldogjob „Badanie Społeczności IT 2025” (UoP mediana 11 500 zł brutto, p25 7 900, p75 15 000; B2B 13 000 zł netto), wynagrodzenia.pl (mediana UI/UX 10 710 zł brutto), Randstad, theprotocol.it, nofluffjobs [S]. Wolno je cytować z podaniem źródła, nie wolno budować z nich własnej bazy. GUS pozwala na ponowne wykorzystanie z podaniem źródła i daty [W: bip.stat.gov.pl], ale nie sprawdzono, czy ma osobny kod zawodu dla UX. Fosa danych jest więc słaba.

**Własny produkt:** szablon portfolio w Figmie, słownik UX w PDF, lista zadań rekrutacyjnych. Popyt na „portfolio ux” to 86 wyszukiwań miesięcznie [V], więc to tylko dodatek.

### 1.4 Fosa i ryzyko

- **Fosa:** narzędzia (kontrast, paleta, generator lorem ipsum) to towar. figma.com sama ma koło kolorów, generator gradientów i bibliotekę fontów [P: stopka figma.com]. Biblioteka wzorców UI po polsku byłaby własną treścią, ale wymaga eksperta, a udział właściciela ma być pasywny.
- **Ryzyko:** brak YMYL i treści prawnych w rdzeniu. Główne ryzyko to AIO (5 z 6) i spadający rynek pracy UX (zawód −46% r/r).

### 1.5 Ocena UX/UI

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 2 | 82,6 tys. informacyjnych, ale połowa to „lorem ipsum” i „paleta kolorów”; kursy i zawód −46…−54% r/r |
| Słabość SERP | 25% | 3 | słownik i narzędzia mają słabe i stare wyniki; kursy zajęte przez szkoły, płace przez portale |
| Zarobek | 25% | 2 | strefakursów 50% i Coursera 15–45% potwierdzone; bootcampy bez programów; 1 996 wyszukiwań kursów |
| Fosa danych / narzędzia | 15% | 2 | brak otwartych danych o płacach; narzędzia łatwe do skopiowania |
| Niskie ryzyko | 15% | 3 | bez YMYL i prawa; AIO 5 z 6 |
| **Wynik ważony** | | **2,40** | |

**Dopasowanie do profilu: 4/5.** Temat zgodny z doświadczeniem. Przewaga eksperta znika jednak, gdy właściciel nie podpisuje treści i nie pokazuje portfolio.

---

## 2. Twórcy wideo w Polsce

### 2.1 Popyt [V]

**Jak zbudowano:** 76 fraz rdzeniowych plus 36 z [L] i SERP (osoby, rankingi, monetyzacja poza platformą). Razem 112 fraz, 111 bez duplikatu („social blade” i „socialblade” mają wspólny wolumen). Nazwy narzędzi i serwisów (Canva, CapCut, ElevenLabs, DaVinci, OBS, Riverside, vidIQ, YouTube Studio, Tipply, Patronite, Zrzutka, Social Blade) oznaczono jako nawigacyjne.

| Grupa | Fraz | Wolumen / mies. | Trend r/r | Uwagi |
|---|---|---|---|---|
| Wszystko (bez duplikatu) | 111 | 1 912 782 | −2,0% | 1 820 089 to marki (canva 1 395 500, capcut 127 083, elevenlabs 71 833, tipply 45 975) |
| **Informacyjne i komercyjne** | 91 | **92 693** | **−4,9%** | najsłabszy 09.2026: 80 380, najmocniejszy 01.2026: 116 540; ważony CPC 0,48 USD |
| Sprzęt | 17 | 72 571 | +0,3% | dji osmo pocket 3 17 300, statyw do telefonu 14 725, gimbal 14 500, green screen 7 600, mikrofon do nagrywania 5 017, mikrofon do youtube 39 |
| **Zarobki twórców** | 34 | **8 861** | **−34,1%** | jak zarabiać na tiktoku 1 382 (CPC 4,44), jak zarabiać na youtube 1 122, ile zarabia youtuber 619, ile płaci youtube za 1000 wyświetleń 88, rpm youtube 100, kalkulator zarobków youtube 39 |
| Kanały i rankingi (encje) | 22 | 8 134 | −9,5% | youtuberzy 2 367, ile zarabia książulo 1 414, polscy youtuberzy 802, ile zarabia mrbeast 624, ile zarabia friz 505, licznik subskrypcji 425, statystyki kanału youtube 42; social blade 7 125 (nawigacyjna) |
| Start kanału | 7 | 1 804 | −4,7% | jak założyć kanał na youtube 1 125, jak zostać youtuberem 459 |
| Narzędzia (bez marek) | 5 | 853 | −15,1% | muzyka bez praw autorskich 694, program do montażu wideo 64 |
| Monetyzacja poza platformą (bez marek) | 6 | 470 | −2,9% | media kit 268, agencja influencer marketingu 153 (CPC 6,14) |

**Wniosek:** poza sprzętem zostaje ok. 20 tys. wyszukiwań miesięcznie, a najbardziej „pieniężna” grupa (zarobki) traci 34% r/r. Sezonowość łagodna: szczyt w 01, dołek w 06–09.

### 2.2 Kto wygrywa i słabość SERP [S][B][T]

Sprawdzono 6 fraz: „ile płaci youtube za 1000 wyświetleń”, „kalkulator zarobków youtube” (narzędzie), „ile zarabia książulo” (encja osoby), „polscy youtuberzy” (hub encji), „mikrofon do nagrywania” (sprzęt), „jak zarabiać na tiktoku”.

| Fraza | Wol. | AIO | Mediana dom. link. domeny (bez platform) | Domeny <50 | Forum/social/wideo | Kto wygrywa |
|---|---|---|---|---|---|---|
| ile płaci youtube za 1000 wyświetleń | 88 | tak | 1 279 | 1 | 3 | GoWork, wideo YouTube, Reddit, wywrota.pl, linkanta (13 domen) |
| kalkulator zarobków youtube | 39 | tak | 1 307 | 2 | 1 | nr 1 socialmarketingmedia.pl (10 domen linkujących); dalej angielskie kalkulatory (livereacting, joinotto, ytface 8, vling, TubeBuddy) |
| ile zarabia książulo | 1 414 | tak | 2 938 | 1 | 4 | Wykop, youtubers.me, plotek.pl, jastrzabpost.pl, X, TikTok, wideo |
| polscy youtuberzy | 802 | tak | 820 | 0 | 2 | mycompanypolska (ranking z 2021), ddob.com, Wikipedia, typelek.sts.pl (bukmacher STS), harbingers.io |
| mikrofon do nagrywania | 5 017 | nie | 354 | 0 | 0 | 8 z 9 to sklepy (lightingcenter, x-kom, skladmuzyczny, mediaexpert, muzyczny.pl) |
| jak zarabiać na tiktoku | 1 382 | tak | 163 | 0 | 2 | TikTok, support.tiktok.com, Reddit, blogi (pawelwojnicz.pl 180, oscarrak.pl 60), biznes.o2.pl |

**Liczby zbiorcze:** 48 wyników organicznych, 47 URL-i ma mniej niż 10 domen linkujących. Mediana domen linkujących domeny: 2 469, bez platform 682; 4 z 32 domen bez platform ma mniej niż 50. 12 z 48 wyników to fora, social i wideo. Tylko 1 z 24 wyników z datą jest sprzed 2023 r. [S][B].

**Konkurenci [T] (ETV w PL):** skalkuluj.pl 42 754 (kalkulatory ogólne), typelek.sts.pl 24 720, **socialblade.com 10 213**, streamerzy.pl 7 228, napoleoncat.com 5 126, ddob.com 3 902, youtubers.me 2 170. **socialmarketingmedia.pl** (ETV 27, 10 domen linkujących) od lipca 2026 robi dokładnie ten klaster: jest 1. na „kalkulator zarobków youtube” i 5. na „ile zarabia książulo” (wpis z 30.07.2026) [S][B].

**AI Overview:** 5 z 6 SERP-ów (bez „mikrofon do nagrywania”). AIO podaje RPM (0,5–5 USD za 1000 wyświetleń, z webepartners.pl i sardynkibiznesu.pl), wzór kalkulatora i linki do hajsbot.pl oraz skalkuluj.pl, a przy „ile zarabia książulo” kwoty z Pudelka i Przeglądu Sportowego. Cytuje małe serwisy (hajsbot.pl ETV 1, getfans.pl 142, sardynkibiznesu.pl 335). Pytanie o zarobki dostaje pełną odpowiedź bez kliknięcia.

### 2.3 Zarobek [P]

| Program | Warunki u źródła | Problem dla polskiego serwisu |
|---|---|---|
| vidIQ | 15% (0–10 sprzedaży), 20% (11–50), 25% (51+), dożywotnio przy aktywnej subskrypcji; wypłata od 10 USD | płatne w USD, polski mały twórca rzadko kupuje |
| TubeBuddy | 15% od zakupów w 365 dni od 1. kliknięcia (warunki od 01.01.2025) | nabór nowych partnerów niepotwierdzony (serwisy trzecie piszą, że zamknięty) [W] |
| Epidemic Sound | do 12 płacących klientów tylko rabaty na własną subskrypcję; potem 50% przez 12 mies. | trzeba mieć subskrypcję i działalność; gotówka dopiero od 13. klienta |
| Riverside | do 20% (do 85+ USD za sprzedaż), wypłaty miesięczne | niszowe narzędzie (6 667 wyszukiwań marki) |
| ElevenLabs | 22% płatności przez 12 mies. | marka ma 71 833 wyszukiwań, ale nawigacyjnych |
| **CapCut** | do 35% cyklicznie, ale **tylko subskrybenci z USA, Wlk. Brytanii, Niemiec i Francji** | polski ruch nie płaci |
| x-kom SalesMasters | „najwyższe prowizje wynoszą aktualnie 11%” (artykuł bez daty) | sprzęt wygrywają sklepy; tabela stawek niesprawdzona |

Ważony CPC informacyjnej części to 0,48 USD [V], więc reklamy display dadzą mało. Najwyższe CPC mają „jak zarabiać na tiktoku” (4,44 USD) i „agencja influencer marketingu” (6,14 USD), obie z małym wolumenem. Reklamodawców dla tych fraz nie sprawdzano.

**Kalkulator zarobków (YouTube, TikTok, Instagram) i dane ze źródłem:** YouTube nie publikuje stawek RPM dla Polski. U źródła potwierdzono tylko progi programu partnerskiego: 1 000 subskrybentów i 4 000 godzin oglądania w 12 mies. albo 10 mln wyświetleń Shorts w 90 dni [P: support.google.com/youtube/answer/72851]. Podział 55% / 45% dla Shorts pochodzi z prasy z 2023 r. i nie potwierdzono go dziś u źródła [W]. Dostępność TikTok Creator Rewards w Polsce jest niepotwierdzona (AIO cytuje napoleoncat.com: „W Polsce TikTok nie płaci za wyświetlenia”) [S]. Uczciwy kalkulator musi więc brać RPM od użytkownika. Wtedy nie różni się od skalkuluj.pl i hajsbot.pl.

### 2.4 Kanały jako strony encji: regulamin YouTube API [P]

Polityka dla deweloperów YouTube API (aktualizacja 2026-10-15) mówi wprost:

- „an API Client must not store statistics retrieved as Non-Authorized Data for more than 30 days. For example, an API Client must not store the subscriber count for a YouTube channel for more than 30 days without authorization from the channel owner.”
- „Your API Clients must not (i) replace API Data with similar, independently calculated data, or (ii) access or use API Data to create new or derived data or metrics.” Szacunek zarobków kanału to metryka pochodna.
- „Do not aggregate API Data except […] channels that are under the same content owner”. Ranking kanałów różnych twórców to agregacja.

Wyjątek: od 01.06.2026 Google dopuszcza „Additional policies for derived metrics and data storage” (aktualizacja 2026-09-14) dla klientów API, którzy przeszli audyt i zaakceptowali poprawkę we wniosku o zwiększenie limitu. Wtedy wolno pokazywać szacunki przychodów jako szacunki stron trzecich, rankingi i historię do 36 miesięcy. Tytuły i nazwy twórców nadal trzeba odświeżać co 30 dni.

**Wniosek:** baza stron kanałów w stylu Social Blade jest możliwa tylko po wniosku do Google i jego akceptacji. To kontakt z firmą i rejestracja, czyli decyzja właściciela, z niepewnym wynikiem. Bez tego wolno pokazać aktualne liczby z API, odświeżane co 30 dni, bez rankingu i bez szacunku zarobków. Social Blade (ETV 10 213 w PL) i youtubers.me już to robią.

### 2.5 Fosa i ryzyko

- **Fosa:** brak otwartych danych o RPM. Dane kanałów zależą od regulaminu jednej platformy. Sprzęt to karty produktów, gdzie wygrywają sklepy.
- **Ryzyko:** strony „ile zarabia [osoba]” to spekulacje o zarobkach realnych ludzi, z ryzykiem naruszenia dóbr osobistych (frazy powiązane w SERP: „książulo wiek”, „książulo majątek”). AIO 5 z 6. Zależność od YouTube API.

### 2.6 Ocena twórców wideo

| Kryterium | Waga | Ocena | Uzasadnienie |
|---|---|---|---|
| Popyt i trend | 20% | 2 | 92,7 tys. informacyjnych, z czego 72,6 tys. to sprzęt; zarobki −34% r/r |
| Słabość SERP | 25% | 3 | dużo wideo, Reddita i plotkarskich portali, małe kalkulatory w top 10; sprzęt zajęty przez sklepy |
| Zarobek | 25% | 2 | programy w USD dla zagranicznych narzędzi; CapCut wyklucza PL; CPC 0,48 USD |
| Fosa danych / narzędzia | 15% | 2 | strony kanałów tylko po audycie Google; RPM bez źródła |
| Niskie ryzyko | 15% | 2 | treści o realnych osobach, AIO 5 z 6, regulamin jednej platformy |
| **Wynik ważony** | | **2,25** | |

**Dopasowanie do profilu: 3/5.** Hobby właściciela, ale serwis o twórcach bez twarzy i bez własnego kanału traci wiarygodność. Konkurenci w AIO to twórcy, którzy pokazują swoje statystyki.

---

## 3. Rachunek po 12 miesiącach (`dane/E-rachunek.csv`)

**Wspólne założenia (jawne, niesprawdzone u źródła):** ruch od 4. miesiąca, wzrost liniowy, rok 1 ≈ 4,5 × przychód z 12. miesiąca. 1,5 odsłony na wizytę, reklamy display RPM 10 zł za 1 000 odsłon (założenie). Udział w adresowalnym popycie po 12 mies.: 3% (ostrożny), 8% (realny). Koszty: domena ok. 100 zł rocznie, treści robią agenci.

**UX/UI.** Adresowalny popyt 42 000 / mies. (82 582 informacyjnych minus „lorem ipsum” i „paleta kolorów”). Kursy: 2% (ostrożny) / 4% (realny) wizyt klika w ofertę, 2% / 3% kupuje, prowizja 100 / 200 zł (50% netto pierwszego zamówienia w strefakursów; ścieżka za 914 zł brutto daje ok. 372 zł). Framer: 0,5% / 1% kliknięć, 1% / 2% konwersji, 150 / 300 zł.

| Wariant | Wizyty / mies. | Kursy | Framer | Reklamy | **Razem w 12. mies.** | Rok 1 |
|---|---|---|---|---|---|---|
| ostrożny | 1 260 | 50 zł | 9 zł | 19 zł | **ok. 80 zł** | ok. 350 zł |
| realny | 3 360 | 806 zł | 202 zł | 50 zł | **ok. 1 060 zł** | ok. 4 760 zł |

**Twórcy wideo.** Adresowalny popyt 27 000 / mies. (ok. 20 tys. zapytań o zarobki, kanały, start i narzędzia plus ok. 10% fraz o sprzęcie). Narzędzia: 60% wizyt, 2% / 4% kliknięć, 5% konwersji, 100 / 150 zł wartości klienta w 12 mies. (vidIQ 15%, ElevenLabs 22%, Riverside do 20%). Sprzęt: 30% wizyt, 2% / 4% kliknięć, 3% / 4% konwersji, 20 zł prowizji (4% od 500 zł, założenie).

| Wariant | Wizyty / mies. | Narzędzia | Sprzęt | Reklamy | **Razem w 12. mies.** | Rok 1 |
|---|---|---|---|---|---|---|
| ostrożny | 810 | 49 zł | 3 zł | 12 zł | **ok. 65 zł** | ok. 290 zł |
| realny | 2 160 | 389 zł | 21 zł | 32 zł | **ok. 440 zł** | ok. 1 990 zł |

Budżet na reklamy nie zmienia wyniku: przy CPC 2,18 USD za „kurs ux” i prowizji 100–200 zł za sprzedaż płatny ruch na kursy się nie zwraca przy konwersji z założeń.

---

## 4. Omijamy

- **Prawo:** umowy z markami i wycena współpracy jako umowa, prawa autorskie i licencje muzyki („muzyka bez praw autorskich” 694 / mies.: tylko porównanie bibliotek bez porad prawnych), oznaczanie reklam u influencerów, RODO w badaniach UX, wymogi ustawy o dostępności (kontrast tylko jako narzędzie WCAG, bez interpretacji przepisów).
- **Podatki i ZUS:** podatki twórców, ZUS, B2B kontra UoP jako wybór podatkowy (forma umowy tylko jako etykieta w danych o płacach).
- **Osoby:** strony „ile zarabia [osoba]”, wiek i majątek youtuberów.
- **Dane bez licencji:** przejmowanie raportów płac (Bulldogjob, nofluffjobs, justjoin.it), scrapowanie ogłoszeń, statystyki kanałów trzymane dłużej niż 30 dni.
- **Afiliacja:** CapCut (wyklucza PL), konta Figma „edukacyjne” z G2A i podobnych.

---

## 5. Czego nie sprawdzono

- Webflow i Udemy (programy partnerskie), stawki x-kom w tabeli SalesMasters, Allegro u źródła.
- Czy TubeBuddy przyjmuje nowych partnerów i jakie jest cookie vidIQ.
- Kod zawodu UX w danych GUS i licencja konkretnej tabeli.
- Podział przychodów YouTube 55% / 45% oraz Creator Rewards TikTok w Polsce u źródła.
- Ceny kursów bezpośrednio w cennikach (są tylko odczyty z SERP i AIO).
- Liczby domen linkujących dla subdomen (np. jastrzabpost.pl 0, dostepnosc.w.prz.edu.pl 0) mogą być zaniżone.

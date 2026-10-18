# Reklamy: zlecenia na strony dla fachowców

Stan: 18.10.2026. Dane wyszukiwań z DataForSEO (Google Ads, Polska, październik 2025 – wrzesień 2026, CPC w USD; w koncie Google Ads ok. × 3,7 zł). Uzupełnia `GOOGLE-ADS.md` (kampania audytu z 12.10.2026).

## Warunek startu

Reklamy ruszają dopiero w etapie `"pelny"` (`src/data/etap.json`). Teraz, w etapie `"blog"`, strony `/audyt-strony/` i `/strona-dla-fachowca/` pokazują „Wkrótce” i nie mają formularza, więc kliknięcie z reklamy nie ma dokąd prowadzić. Przed startem:

- [ ] Adres do korespondencji, etap `"pelny"`, formularz na Zenboxie, strona „Dane i regulamin”.
- [ ] Polityka prywatności dopisuje Meta (formularze kontaktowe Meta) i Google Ads, jeśli je włączamy.
- [ ] Konwersje: Google Ads (strona `/dziekuje/`) i Plausible (cele „Telefon”, „Oferta”).

## Co wiemy z badania rynku (18.10.2026)

Pełne raporty ze źródłami są w `reklamy/badania/`.

**Konkurencja** (`badanie-google-ads.md`, Google Ads Transparency przez DataForSEO):
- **Co się utrzymuje:** długo działają reklamy tekstowe w wyszukiwarce. Freelancer TrendWeb ma te same reklamy od 10.2021, agencja Zdobywcy Sieci od 11.2023. Wideo i grafiki małych firm znikały po kilku dniach albo po miesiącu.
- **Co nie przetrwało:** tania oferta z ceną w reklamie („od 500 zł, gotowa w 48 h”, ruszfirme.pl). Reklamy wyłączono 24.08.2026.
- **Luka:** nikt w próbce nie zaczyna od darmowego audytu. Wejściem jest telefon, wycena albo darmowy okres próbny. Stronę z wizytówką Google łączy tylko jeden freelancer. Nikt nie reklamuje się jako „strony dla fachowców”.
- **Czego nie ustaliliśmy:** treści reklam i stawek konkurencji. Wyniki wyszukiwania sprawdzone w niedzielę w nocy nie miały reklam. Trzeba to powtórzyć w dzień roboczy.

**Fachowcy** (`badanie-odbiorca.md`, ok. 200 komentarzy wykonawców pod 7 polskimi filmami; mała próba, traktować jako kierunek):
- **Polecenia to ich duma.** Najczęstsza wypowiedź to „wszystko z polecenia” (10 razy). Reklama ma polecenia wzmacniać: „klient i tak sprawdzi Cię w Google”.
- **Najsilniejsza emocja to nieufność** (ok. 29 głosów). 12 osób pisze o oszustach „z Google”, którzy dzwonią i straszą, że wizytówka zniknie, a potem żądają kolejnych rat. 17 osób pisze źle o portalach z punktami. „Darmowy audyt wizytówki” brzmi jak ten schemat, dlatego każda kreacja i landing mówi wprost: nie dzwonię, nie jestem z Google, nie proszę o hasła ani kody.
- **Ból portali:** płacenie za kontakt, który nie odbiera, i „castingi, kto taniej”.
- **Lęk przed ukrytymi opłatami** („miała być jednorazówka”). Przekaz: strona jest Twoja.
- **Nienawidzą formularzy, które na końcu żądają telefonu.** Telefon jest opcjonalny.
- **Są aktywni wieczorem (18–23) i w weekendy**, w dzień pracują z telefonem w kieszeni. Pierwszy krok ma zająć 2 minuty na telefonie.
- **Żargon odstrasza:** SEO, leady, „partner Google”, „gwarancja TOP 3”.
- **Polecenia mają dziury zimą** („telefony zamilkły”). Jesień i zima to dobry moment na kampanię Meta.

**Konwersja** (`badanie-konwersja.md`, benchmarki z USA plus badania; liczby z USA traktować jako orientacyjne):
- **Google (WordStream 2026):** usługi dla firm konwertują ok. 4,85% przy koszcie leada ok. 94 USD. W Polsce kliknięcie w „strona internetowa dla firmy” kosztuje 10,87 USD.
- **Meta (WordStream 2025):** lead średnio 27,66 USD, w usługach domowych 41,26 USD, czyli 2–3 razy taniej niż w Google.
- **Formularz Meta a landing:** jedyny kontrolowany test dał ten sam odsetek wartościowych leadów (29%), a z formularza Meta wychodziły o połowę taniej. Prowadzimy oba i porównujemy koszt zamówionego audytu.
- **Szybkość odpowiedzi:** kontakt w ciągu godziny daje ok. 7 razy większą szansę niż kontakt godzinę później (HBR 2011, znane z cytatów). Mail z potwierdzeniem idzie od razu, wideo w 3 dni robocze.
- **Formularz:** każde pole obniża konwersję, a pole telefonu najbardziej (HubSpot). Pola: nazwa firmy albo adres strony, miasto, e-mail. Telefon opcjonalny.
- **Wideo:** pionowe wideo z mówiącą osobą daje niższy koszt wyniku niż grafika (Meta podaje 34,5%; test platformy). Tekst poza górnymi 14% i dolnymi 35% kadru.
- **Język i tempo strony:** prosty język na landingu daje mniej więcej dwa razy wyższą konwersję (Unbounce, korelacja). 53% osób zamyka stronę, która ładuje się dłużej niż 3 s (Google).

## Najważniejszy wniosek z danych

Fachowiec nie szuka strony internetowej. Frazy „strona dla hydraulika”, „strona dla elektryka” i podobne mają w Google 0 wyszukań, a „strona internetowa dla firmy budowlanej” tylko 90 miesięcznie. Fachowiec szuka zleceń: „zlecenia budowlane” to 2 400 wyszukań, a w styczniu 4 400.

Dlatego:

1. **Główny kanał to Facebook i Instagram (Meta).** Tam docieramy do fachowców, którzy o stronie jeszcze nie myślą, i pokazujemy im problem: klient sprawdza ich w Google, zanim zadzwoni.
2. **Google Search jest drugi.** Łapie tych, którzy już szukają strony, ale konkuruje z agencjami i kreatorami stron. Kliknięcie kosztuje tam ok. 30–40 zł.
3. **Wideo (Reels, Shorts, YouTube)** to te same filmy co na Meta. Daje tanie wyświetlenia i buduje rozpoznawalność przed sezonem.

Sezon:
- **Meta od listopada do lutego**, kiedy polecenia cichną i fachowcy mają czas wieczorami.
- **Google od lutego do kwietnia**, kiedy wyszukiwania stron są najwyższe („tworzenie stron internetowych”: 2 400 w sierpniu, 8 100 w marcu).

## Komunikat

Jedna obietnica: **„Sprawdzę, co widzi klient u Ciebie”**. Pod nią w każdej kreacji ten sam pasek zaufania: **Nie dzwonię · Nie jestem z Google · Bez haseł i kodów · Bez zobowiązań**. To odpowiedź na największą obiekcję z badania. Wejściem jest darmowy audyt (wideo w 3 dni robocze), a nie sprzedaż strony. Fachowiec nie kupi strony od nieznajomego z reklamy, ale chętnie zobaczy, jak wypada na tle konkurencji.

| Kąt | Hak | Kreacja |
|---|---|---|
| Dane | „30,3% fachowców w Mapach Google nie podaje w wizytówce żadnej strony” | `a-dane`, film `szukanie` |
| Polecenia | „Polecił Cię sąsiad. Klient i tak sprawdzi Cię w Google.” | `b-polecenia`, film `szukanie` |
| Bez pośrednika | „Bez punktów. Bez licytacji z pięcioma firmami.” | `c-portal` |
| Darmowe wideo | „Nagram Ci wideo o Twojej stronie. Za darmo.” Wystarczy nazwa i miasto, 2 minuty. | `d-wideo`, film `audyt` |
| Twarz (do nagrania) | Kamil na telefonie pokazuje, jak klient widzi fachowca w Mapach Google. | scenariusz niżej |

Kolejność testu: „Polecenia” i „Dane” (najmocniejsze w badaniu), potem „Darmowe wideo” i „Bez pośrednika”.

### Scenariusz filmu z twarzą (30 s, nagrywasz telefonem w pionie)

Meta podaje, że wideo z mówiącą osobą daje najniższy koszt wyniku. Fachowcy ufają tonowi „krótko i na temat”.

1. **0–3 s, twarz do kamery:** „Masz klientów z polecenia? To dobrze. Ale zanim zadzwonią, i tak sprawdzą Cię w Google.”
2. **3–15 s, nagranie ekranu telefonu:** wpisujesz „hydraulik [miasto]” i pokazujesz trzy firmy z najwyższymi ocenami: zdjęcia, opinie, stronę. Nazwy firm zamaż.
3. **15–25 s, twarz:** „Projektuję strony od 7 lat. Za darmo sprawdzę Twoją stronę i wizytówkę i nagram Ci wideo, co poprawić. Nie dzwonię, nie jestem z Google, nie proszę o hasła.”
4. **25–30 s:** plansza końcowa z filmu `audyt` z paskiem zaufania.

Napisy na całym filmie, bo większość ogląda bez dźwięku.

Zasady (z CLAUDE.md i regulaminów reklam):

- **Bez cen w reklamach.** Cena jest na stronie oferty.
- **Bez obietnic pozycji w Google** i bez „gwarantowanych” wyników.
- **Każda liczba ma źródło na kreacji**, np. „Dane własne: 702 wizytówki…”. Przykłady poglądowe są oznaczone („Firmy A i B są zmyślone”).
- **Bez zwracania się do cech odbiorcy.** Meta zabrania reklam, które sugerują, że wiedzą, kim jesteś („Jesteś hydraulikiem z długami?”). Piszemy o kliencie i stronie, nie o odbiorcy.
- **Bez remarketingu.** W Google `ad_personalization` jest zawsze odrzucone.
- **Bez kupowania opinii.**
- **Doświadczenie autora:** tylko „7 lat projektuję strony”.

## Meta (Facebook i Instagram)

- **Cel kampanii:** Potencjalni klienci. Do pierwszych zgłoszeń formularz Meta („Formularz błyskawiczny”, typ „Większa intencja”), bo fachowiec przegląda Facebooka na telefonie między zleceniami i nie chce wychodzić z aplikacji. Pola: imię, telefon albo e-mail, adres strony albo nazwa firmy, miasto. Bez pytań o budżet.
- **Później:** po 20–30 zgłoszeniach test „Konwersje na stronie” z formularzem na `/audyt-strony/`. Daje mniej, ale lepszych zgłoszeń.
- **Formularz Meta:** typ „Większa intencja”. 2 pytania wyboru: branża i „Masz stronę? tak / nie / tylko Facebook”. Pola: nazwa firmy, miasto, e-mail, a telefon opcjonalny. Na ekranie podziękowania: „Wideo z audytem dostaniesz na maila w 3 dni robocze. Nie dzwonię.” Leady pobierane automatycznie, bo dane w Meta znikają po 90 dniach.
- **Harmonogram emisji:** codziennie 17:00–23:00 i całe weekendy, kiedy fachowcy przeglądają telefon.
- **Grupa odbiorców:**
  - Polska, wiek 25–60;
  - zainteresowania: budownictwo, remont, instalacje hydrauliczne, elektryka, stolarstwo, ogrodnictwo; zawody (gdzie Meta je pokazuje): hydraulik, elektryk, stolarz, glazurnik, dekarz;
  - osoby, które są administratorami stron firmowych na Facebooku;
  - bez grup podobnych do klientów i bez remarketingu na start.
- **Umiejscowienia:** Advantage+, ale sprawdzaj wyniki osobno dla Reels i relacji (Stories) oraz dla aktualności (feed).
- **Kreacje na start:** 4 grafiki (kwadrat do aktualności, pion do relacji) i 2 filmy (pion). Dynamiczna kreacja wyłączona, żeby było widać, który kąt działa.
- **Budżet testowy:** 30 zł dziennie przez 14 dni (ok. 420 zł). Po tygodniu wyłącz kreacje z kosztem zgłoszenia ponad 2× średniej.

Teksty do Meta (bez cen):

- **Tekst główny 1 (polecenia):** „Masz klientów z polecenia? Dobrze. Ale zanim zadzwonią, i tak wpiszą Twoją nazwę w Google. Za darmo sprawdzę, co tam zobaczą: stronę, zdjęcia, opinie. Nagram krótkie wideo z listą poprawek. Nie dzwonię, nie jestem z Google i nie proszę o żadne hasła ani kody.”
- **Tekst główny 2 (dane):** „W naszych danych z Map Google 30,3% fachowców nie podaje w wizytówce żadnej strony. Klient, który porównuje trzy firmy, dzwoni do tej, o której wie najwięcej. Sprawdzę, jak wypadasz Ty. Wystarczy nazwa firmy i miasto, a wideo dostaniesz na maila w 3 dni robocze.”
- **Tekst główny 3 (portale):** „Klient sam Cię znajduje, ogląda zdjęcia Twoich realizacji i dzwoni prosto do Ciebie. Bez punktów i bez licytacji z pięcioma firmami. Zacznij od darmowego audytu: sprawdzę Twoją stronę i wizytówkę i powiem, co poprawić najpierw.”
- **Nagłówek:** „Darmowy audyt strony i wizytówki” / „Sprawdzę, co widzi Twój klient”
- **Przycisk:** „Dowiedz się więcej” albo „Zarejestruj się”.

## Google Search

Kampania „Audyt” z `GOOGLE-ADS.md` zostaje. Dochodzi grupa **„Strona dla firmy”**, która kieruje na `/strona-dla-fachowca/`. Tylko dopasowanie do wyrażenia i ścisłe.

| Słowo | Wyszukiwania/mies. | CPC | Uwagi |
|---|---|---|---|
| `"strona internetowa dla firmy"` | 480 | $10.87 | szczyt w marcu 880 |
| `"strona wizytówka"` | 390 | $3.63 | tanio, dobra intencja |
| `"strona wizytówka cena"` | 110 | $3.29 | w reklamie bez ceny, cena na stronie |
| `"strona internetowa dla firmy budowlanej"` | 90 | brak | szczyt w kwietniu 320 |
| `"projektowanie stron internetowych"` | 1 900 | $8.27 | tylko z wykluczeniami, test |

Nie licytujemy „tworzenie stron internetowych” (4 400): dużo osób robi tam stronę samodzielnie albo szuka kursu. Nie licytujemy też „tania strona internetowa” (720), bo to łowcy najniższej ceny.

Dodatkowe wykluczenia: `kreator, wordpress, wix, za darmo, darmowa, sam, samemu, kurs, ai, canva, sklep, praca, szablon`.

Reklama RSA („Strona dla firmy”; nagłówki do 30 znaków, opisy do 90):

- Nagłówki:
  - Strona dla fachowca
  - Strona dla firmy usługowej
  - Klienci dzwonią ze strony
  - Galeria prac i opinie
  - Przycisk „Zadzwoń” na telefonie
  - Najpierw darmowy audyt
  - Wideo w 3 dni robocze
  - Hydraulik, elektryk, remonty
  - 7 lat projektuję strony
  - Strona i wizytówka Google
  - Bez umowy na lata
  - Nie dzwonię z ofertą
- Opisy:
  - „Strona dla fachowca: zdjęcia realizacji, opinie i przycisk »Zadzwoń«. Zacznij od audytu.”
  - „Sprawdzę Twoją stronę i wizytówkę Google. Wideo z poprawkami w 3 dni robocze.”
  - „Porównam Cię z firmami z Twojego miasta. Bez haseł i bez telefonów z ofertą.”

## YouTube i Demand Gen (opcjonalnie, po Meta)

Te same filmy pionowe (`film-szukanie.mp4`, `film-audyt.mp4`) w kampanii Demand Gen w Google Ads: grupy odbiorców „właściciele małych firm” i „budownictwo i remonty”, 20 zł dziennie, cel „kliknięcia”. Start dopiero, gdy Meta pokaże, który kąt działa.

## Landing pod konwersję (do zrobienia przy etapie „pelny”)

- **Pierwszy ekran:** nagłówek z reklamy, pasek zaufania (nie dzwonię, nie jestem z Google, bez haseł i kodów, bez zobowiązań) i formularz od razu widoczny na telefonie.
- **Formularz:** nazwa firmy albo adres strony, miasto, e-mail, a telefon opcjonalny. Obecny `LeadForm` ma 2 kroki i telefon nieobowiązkowy, więc wystarczy dopasować teksty.
- **Dowód:** fragment przykładowego audytu (wideo z demo firmą) i projekty pokazowe. Na start nie ma opinii klientów, więc ich nie udajemy.
- **Widełki cen na stronie oferty**, tak żeby dzwonili ci, którym cena pasuje. W reklamie cen nie ma.
- **„Strona jest Twoja”** z odnośnikiem do FAQ o prawach i domenie.
- **Mail automatyczny** od razu po zgłoszeniu: „Dostałem. Wideo nagram do [data].”
- **Szybkość:** strona statyczna, cel poniżej 2 s na telefonie.

## Mierzenie i decyzje

- **Lejek:** wyświetlenie → kliknięcie → zgłoszenie → audyt wysłany → rozmowa → strona sprzedana. Liczymy koszt **sprzedanej strony**, a nie samego zgłoszenia.
- **Próg:** koszt zgłoszenia do 60 zł na Meta i do 120 zł w Google. Przy sprzedaży co 5–10 audytu wychodzi 300–1 200 zł kosztu pozyskania klienta. To szacunek do sprawdzenia, nie obietnica.
- **Pojemność:** 5 audytów tygodniowo. Wyższy budżet nie ma sensu, dopóki audyty robisz sam.
- **Co tydzień:**
  - raport wyszukiwanych haseł i dopisanie wykluczeń;
  - wyłączenie najsłabszej kreacji;
  - jedna nowa kreacja z najlepszego kąta.

## Pliki

- `reklamy/grafiki/`: 10 grafik (kąty: dane, polecenia, portal, wideo; kwadrat 1080×1080 i pion 1080×1920 oraz 2 poziome 1200×628 do Google). Każda ma pasek zaufania.
- `reklamy/badania/`: trzy raporty z badania rynku z 18.10.2026.
- `reklamy/film-szukanie.mp4` (15 s) i `reklamy/film-audyt.mp4` (14 s): 1080×1920, bez dźwięku, z napisami w kadrze. W Meta dodaj muzykę z biblioteki Meta.
- Źródła filmów (Remotion) i grafik (HTML) są w opisie PR. Zmiana tekstu = nowy render.

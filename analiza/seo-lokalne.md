# SEO lokalne: wnetrzakamila.pl

Stan na 18.10.2026. Dane z DataForSEO (endpointy podane przy liczbach). Dane z Map Google podaję tylko zbiorczo, bez nazw, telefonów i adresów firm. Z żadną firmą się nie kontaktowałem.

## W skrócie

**Profilu Firmy w Google dla „Wnętrza Kamila” ani dla wnetrzakamila.pl nie ma.** Według briefu analizy na stronie nie ma firmy, adresu ani usług. Dziś SEO lokalne tej strony nie dotyczy. Poniżej jest tylko krótki plan na wypadek, gdyby właściciel chciał sprzedawać usługi lokalnie.

## 1. Czy jest Profil Firmy w Google

| Sprawdzenie | Endpoint | Wynik (18.10.2026) |
|---|---|---|
| Profil dla „Wnętrza Kamila” | `/v3/business_data/google/my_business_info/live` (location_code 2616, language_code pl) | `40102 No Search Results` |
| Mapy, fraza „Wnętrza Kamila”, 20 wyników | `/v3/serp/google/maps/live/advanced` (location_code 2616, pl) | 0 z 20 wyników linkuje do wnetrzakamila.pl |
| Google, fraza „wnetrzakamila.pl” | `/v3/serp/google/organic/live/advanced` | strony wnetrzakamila.pl nie ma w top 10; nie ma też panelu firmy |
| Google, fraza „Wnętrza Kamila” / „wnętrza kamila” | `/v3/serp/google/organic/live/advanced` | 3 próby, za każdym razem błąd `40101 Internal SE Server Error`; nie mam wyniku |
| Google, `site:wnetrzakamila.pl` | `/v3/serp/google/organic/live/advanced` | strona jest w indeksie (co najmniej 10 adresów: „O mnie” i poradniki), tytuły kończą się „- Wnętrza Kamila” |

Wniosek: nazwa „Wnętrza Kamila” istnieje tylko jako nazwa bloga. Nie ma wizytówki w Mapach ani panelu wiedzy w wynikach Google.

### Uwaga o nazwie marki

W Mapach na frazę „Wnętrza Kamila” **9 z 20 wyników** to firmy z imieniem „Kamila” w nazwie. Wszystkie 9 mają kategorię „Projektant wnętrz”, „Biuro architekta wnętrz” albo „Architekt”. Jedna z nich nazywa się „Wnętrza Architektura Kamila …”. 19 z 20 profili jest zweryfikowanych przez właściciela (`is_claimed`). Źródło: `/v3/serp/google/maps/live/advanced`, 18.10.2026.

Co to znaczy: nazwa „Wnętrza Kamila” słabo odróżnia się od istniejących projektantek. Gdyby właściciel chciał wejść w usługi lokalne, będzie konkurował o własną nazwę. Warto to wziąć pod uwagę przy decyzji o marce.

Wyniki dla tej frazy skupiają się w okolicach Łodzi. To prawdopodobnie skutek tego, że wyszukiwanie dla całej Polski (location_code 2616) ustawia punkt w środku kraju; kilka profili bez adresu ma dokładnie te same współrzędne. To moja interpretacja, nie potwierdzona przez DataForSEO.

### Spójność danych NAP

Nie ma czego porównywać: na stronie nie ma nazwy firmy, adresu ani telefonu (według briefu analizy). Spójność NAP sprawdzimy dopiero, gdy powstanie firma i profil.

## 2. Jak wygląda konkurencja lokalna (dla orientacji)

Miasto właściciela nie jest znane. Dla orientacji sprawdziłem dwa duże rynki. Źródło: `/v3/serp/google/maps/live/advanced`, location_code 2616, language_code pl, depth 100, 18.10.2026.

| Wskaźnik | „projektant wnętrz Warszawa” | „projektant wnętrz Kraków” |
|---|---|---|
| Wyników zwróconych | 100 (limit zapytania; jest ich co najmniej tyle) | 100 (jak obok) |
| Top 3: ocena | 4,8 / 4,9 / 4,8 | 5,0 / 5,0 / 4,9 |
| Top 3: liczba opinii | 25 / 125 / 62 | 67 / 108 / 15 |
| Top 10: mediana opinii | 57 (od 25 do 125) | 56 (od 15 do 121) |
| Wszystkie 100: mediana opinii | 21 | 19 |
| Wszystkie 100: średnia ocena | 4,79 | 4,88 |
| Top 10: mediana zdjęć w profilu | 64,5 | 74,5 |
| Profile zweryfikowane (`is_claimed`) | 94 ze 100 | 99 ze 100 |
| Profile z linkiem do strony | 96 ze 100 | 98 ze 100 |
| Główna kategoria „Projektant wnętrz” | 94 ze 100 | 94 ze 100 |

Co z tego wynika:

- W obu miastach jest **co najmniej 100 profili** projektantów wnętrz. Rynek jest pełny.
- Do top 10 potrzeba zwykle **kilkudziesięciu opinii** (mediana 56–57) i oceny bliskiej 5,0. W top 3 zdarzają się profile z 15 i 25 opiniami, więc liczba opinii nie jest jedynym czynnikiem.
- Prawie każdy profil ma stronę www i dziesiątki zdjęć realizacji.

## 3. Co by trzeba, gdyby właściciel chciał sprzedawać usługi lokalnie

To lista na wypadek decyzji „tak”. Dziś nic z tego nie jest potrzebne.

**Decyzje właściciela (najpierw):**

1. Jaka usługa: projekt wnętrz, konsultacja, wizualizacja, projekt ogrodu? Na stronie jest wpis „Ile kosztuje wizualizacja mieszkania?”, ale nie wiadomo, czy autorka sama to sprzedaje.
2. Jakie miasto lub obszar dojazdu.
3. Czy usługi działają pod marką „Wnętrza Kamila” (patrz uwaga o nazwie wyżej).
4. Czy jest zarejestrowana działalność. Wytyczne Google dla Profilu Firmy wymagają, żeby firma obsługiwała klientów osobiście, u siebie albo u klienta (support.google.com/business/answer/3038177). Sam blog się nie kwalifikuje. Szczegóły prawne zostawiam właścicielowi.

**Profil Firmy w Google:**

- Kategoria główna „Projektant wnętrz” (tak ma 94% profili w obu miastach), dodatkowe zgodne z ofertą.
- Bez adresu na wizytówce, jeśli autorka pracuje z domu: obszar obsługi zamiast adresu.
- Zdjęcia własnych realizacji (u liderów kilkadziesiąt), opis usług, link do strony usługi.
- Opinie tylko od prawdziwych klientów, bez zachęt. Prośba SMS-em lub mailem tylko do klientów, którzy zgodzili się na kontakt (zasada z CLAUDE.md).

**Strona:**

- Strona usługi z miastem w tytule i nagłówku, cennikiem albo „sprawdź w cenniku”, formularzem kontaktu.
- Te same dane NAP na stronie, w profilu i w katalogach.
- Dane strukturalne `LocalBusiness` (lub `HomeAndConstructionBusiness`) na stronie usługi.
- Portfolio realizacji z opisem i zdjęciami. Dziś blog nie pokazuje realizacji (według briefu).

**Katalogi i spójność:**

- Profile w serwisach z projektantami i wykonawcami (np. Houzz, Oferteo, Fixly, Panorama Firm, homebook.pl), z tymi samymi danymi. Warunki każdego serwisu trzeba sprawdzić przed założeniem.

**Mierzenie:**

- Pozycje w Mapach dla „projektant wnętrz [miasto]” w kilku punktach miasta, co miesiąc, tym samym endpointem.

## Pytania do właściciela

1. Czy w ogóle chcesz sprzedawać usługi (projekt, konsultacje), czy strona zostaje blogiem z zarobkiem z reklam i afiliacji?
2. Jeśli usługi: w jakim mieście i pod jaką nazwą?
3. Czy profil Instagram @wnetrzebezfiltra („Kamila | Wnętrza | Ogród | Inspiracje”) jest Twój? Pokazuje się jako pierwszy wynik na frazę „wnetrzakamila.pl” (`/v3/serp/google/organic/live/advanced`, 18.10.2026).

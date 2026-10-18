# Wnioski z analizy paliwownia.pl i promptowy.com (12.10.2026)

Oba serwisy podpisuje ten sam autor, oba blokują w robots.txt `/polecam/` (przekierowania afiliacyjne). To portfel serwisów jednego operatora.

## paliwownia.pl - model do kopiowania

- **Co to jest:** katalog darmowych kredytów AI/chmury, ulg i dotacji dla polskich firm IT. Na starcie (8.10.2026) od razu ~200 URL-i: 130 stron programów, ~48 poradników, huby, 3 kalkulatory, kalendarz naborów, strony "gotowe odpowiedzi".
- **Technologia:** brak CMS-a. Statyczne HTML-e z własnego generatora, nginx na VPS, 1 plik CSS (~88 KB) + 1 plik JS (~15 KB) z numerem buildu w `?v=`. Backend PHP pod `/api/` tylko do: newslettera, logowania linkiem, Stripe/BLIK, asystenta AI i własnej analityki (kliknięcia, scroll, czas). Wyszukiwarka z indeksu `assets/dane/szukaj.json`. RSS. Sitemap z `lastmod`.
- **Monetyzacja (freemium):** katalog i kalkulatory za darmo; tydzień próbny 49 zł, 30 dni 149 zł, rok 590 zł; usługa "zrobimy za ciebie" 990 zł; kody dla zespołów od 3900 zł; prowizje od doradców (ujawnione).
- **Wiarygodność:** autor z bio, strona "Zasady i źródła", data "sprawdzono" w kilku miejscach, kursy walut z NBP z datą, źródła pod każdym tekstem, zastrzeżenie YMYL w stopce, link "zgłoś błąd".
- **Makiety (fake door):** część przycisków/formularzy "wkrótce" celowo nic nie wysyła - mierzą kliknięcia, zanim zbudują funkcję.

## promptowy.com - czego się nauczyć i czego nie powtarzać

- **Technologia:** WordPress, własny motyw, własne pluginy (`pw/v1`, `pw-app/v1`), LiteSpeed, Cloudflare. 3623 wpisy, 30-50 nowych dziennie.
- **Szybkość przy wydarzeniach:** premiera modelu AI → 6 tekstów w 27 minut (premiera, przewodnik, test po polsku, porównanie, "jak używać", test na 23 zadaniach), news sitemap, schema Article, Web Story do każdego tekstu. Efekt: top 1 na świeżą frazę w ~30 minut, bo nie było konkurencji.
- **Sekcje generowane z danych:** Atlas modeli (dane z API OpenRouter + kursy NBP, 312 URL-i), słownik, pytania, recenzje, "najlepsze AI do...".
- **Twarde liczby:** tylko ~3,1 tys. wizyt organicznych/mies. i ~290 fraz przy 3,6 tys. wpisów. Ruch dają teksty evergreen ("claude cena", "gemini cennik", "prompty po polsku"), często jako źródło w AI Overview. Profil linków spadł z ~5,9 tys. do ~800 w IV-V 2026; spam score 48.
- **Błędy:** najstarsze wpisy z datą `2020-01-01 00:00` (cofnięte daty), brak oznaczenia afiliacji, sekcja "Pytania czytelników" duplikuje FAQ, spis treści z 24 pozycjami.

## Lekcje

1. Baza danych encji (program, produkt, urząd, model) → strony z szablonu → huby → poradniki. Dane to fosa, nie tekst.
2. Narzędzie (kalkulator, sprawdzarka, kalendarz) daje powód do powrotu, linki i leady.
3. Ruch z Google bez produktu jest kruchy - Paliwownia zarabia na intencji ("chcę te pieniądze"), nie na odsłonach.
4. Świeże frazy wygrywa ten, kto jest pierwszy z kilkoma tekstami pod różne intencje i szybką indeksacją.
5. Średni wolumen kłamie - sprawdzaj 12-miesięczny trend (KSeF: 110 tys. → 1,6 tys.).
6. Skala bez wartości dodanej nie działa i jest ryzykowna (scaled content abuse).

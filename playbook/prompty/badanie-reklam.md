# Badanie przed kampanią reklamową (3 agentów równolegle)

Uruchom trzech agentów w tle. Każdy zapisuje raport do `reklamy/badania/` i zwraca 15–25 wniosków. Każde twierdzenie ma źródło (URL albo endpoint i datę). Liczby z USA oznaczamy jako orientacyjne.

## 1. Konkurencja w Google Ads
DataForSEO: Google Ads Transparency (`/v3/serp/google/ads_advertisers`, `/v3/serp/google/ads_search`; sprawdź ścieżki w docs) i SERP z płatnymi wynikami (`/v3/serp/google/organic/live/advanced`, mobile, 3–4 miasta, **w dzień roboczy 9–15**, bo w nocy reklam nie widać). Zbierz:
- reklamodawców, formaty i daty (reklamy działające długo zwykle się opłacają);
- treść reklam i strony docelowe: oferta, cena widoczna lub nie, wejście (wycena, audyt, telefon), długość formularza, dowody;
- luki, które możemy wykorzystać.

Nie wysyłaj formularzy i nie kontaktuj firm.

## 2. Odbiorca
Publiczne dyskusje: fora, komentarze YouTube (vidIQ: wyszukiwanie filmów, komentarze, transkrypcje), Reddit, grupy publiczne. Zbierz:
- skąd odbiorca bierze klientów albo jak wybiera usługę;
- obiekcje z częstością (ile razy spotkane) i złe doświadczenia;
- co przekonuje, jakich słów używa, kiedy i gdzie jest aktywny.

Krótkie cytaty z linkiem i datą, bez danych osobowych.

## 3. Konwersja (twarde dane)
Benchmarki CPC, konwersji i kosztu leada (WordStream/LocaliQ, Unbounce, oficjalne materiały Meta i Google). Do tego:
- formularz Meta kontra landing;
- szybkość odpowiedzi na leada;
- długość formularza;
- szybkość strony;
- kreacje wideo z twarzą kontra grafika;
- zasady reklam Meta (cechy osobiste) i Google (obietnice).

Oddziel twarde dane od opinii.

## Potem
Synteza w `reklamy/STRATEGIA-REKLAM.md` (przykład: `playbook/przyklad-strategia-reklam-niechcieznajda.md`):
- kanały i sezon;
- komunikat z paskiem zaufania (odpowiedź na główną obiekcję);
- kąty kreacji i kolejność testu;
- formularz, harmonogram emisji, landing pod konwersję;
- mierzenie kosztu klienta, a nie kliknięcia.

Kreacje: `playbook/kod/kreacje/` (grafiki HTML i Remotion). Pokaż je właścicielowi na arkuszu i czekaj na decyzję.

# Audyt prawny i aktualności treści

Po QA i przeglądzie wizualnym, przed ustawieniem harmonogramu. Cel: każdy tekst jest zgodny z prawem na dzień audytu, ma aktualne liczby i poprawne źródła, a nic nie namawia czytelnika do łamania prawa ani zasad platform. Treść jest w pełni automatyczna, więc poprawki też: bez znaczników, a co się nie da potwierdzić, wylatuje.

Audyt **nie jest poradą prawną**. Opisuje przepisy i stanowiska urzędów ze źródłami; rzeczy wymagające interpretacji idą do sekcji „Do decyzji użytkownika”.

## Procedura

1. **Migawka przed audytem.** Skopiuj katalog treści (np. `cp -R src/content/poradniki <scratchpad>/przed-audytem/`). Bez tego nie zrobisz diffu ani nie cofniesz złej poprawki. W repozytorium git wystarczy commit albo `git stash`-owalny stan, ale migawka w scratchpadzie działa wszędzie.
2. **Lista aktów i źródeł** dla niszy projektu (przykład PL poniżej). Sprawdź u źródła (ISAP, eli.gov.pl, EUR-Lex, strony urzędów), czy każdy akt obowiązuje i od kiedy, i zapisz to w briefie z datą. Nowe akty (np. wdrożenie DSA) wpisz z numerem Dz.U. i datą stosowania.
3. **Podział na rozłączne zestawy plików.** 4–8 plików na agenta, każdy plik u dokładnie jednego agenta (zwykle według hubów). Dwa agenty nigdy nie edytują tego samego pliku.
4. **Agenci równolegle** (Agent tool, w jednym kroku), każdy z briefem poniżej i swoją listą plików. Agent sprawdza, poprawia swoje pliki i uruchamia `sprawdz.py`.
5. **Diffy.** Po powrocie agentów porównaj z migawką (`diff -ru przed-audytem/ src/content/poradniki/`) i przejrzyj każdą zmianę: czy nie powstał nowy błąd, czy liczby są spójne w `lead`, `tldr`, `cover`, `faq`, `description` i treści, czy styl jest zachowany.
6. **QA całości:** `sprawdz.py` na całym katalogu; jeśli zmieniły się `cover.big`/`cover.sub`, ponowny render okładek tych tekstów.
7. **Raport dla użytkownika** (plik w projekcie, np. `audyt-AAAA-MM-DD.md`): tabela plik → status (OK / poprawiony / do decyzji) → najważniejsza zmiana; lista źródeł prawnych z datą sprawdzenia; sekcja **„Do decyzji użytkownika”** (sprawy biznesowe, interpretacje, ryzyka, których agent nie rozstrzygnął). Nie publikuj niczego przed odpowiedzią na tę sekcję.

## Brief agenta audytu (szablon)

Wypełnij nawiasy. Brief wysyłasz każdemu agentowi z jego listą plików.

```markdown
# Audyt prawny i aktualności treści: [marka]

Projekt: `[ścieżka]` ([stack]). [1–2 zdania: co marka sprzedaje i komu, wejście do lejka.] Dzisiaj jest **[data]**.
Treści: `[katalog]/*.md`. Frontmatter: title, description, lead, tldr, faq, cover (big, sub), sources (title, url, checkedAt), verifiedAt. Treść pod frontmatterem.

## Twoje pliki
[lista ścieżek]

## Zadanie
Każdy plik przeczytaj w całości, łącznie z frontmatterem, FAQ, cover i tldr. Sprawdź:
1. **Zgodność z prawem [kraj/UE] na [data].** Akty do sprawdzenia: [lista z artykułami, z sekcji „Lista aktów” poniżej, dopasowana do niszy].
   Szukaj twierdzeń prawnych nieprawdziwych, nieaktualnych albo podanych jako pewnik, choć są interpretacją. Szukaj porad, które mogłyby skłonić czytelnika do złamania prawa albo zasad platform ([przykłady z niszy, np. kupowanie opinii, zachęty za opinie, SMS bez zgody]). **[Zasady marki, np. „Nigdy nie zachęcamy do kupowania opinii”.]**
2. **Aktualność faktów:** ceny, pakiety, nazwy produktów, procedury platform, cenniki, stawki podatków. Każdą liczbę i warunek, który mógł się zmienić, sprawdź u źródła (WebSearch, WebFetch). Priorytet: liczby z lead, tldr, cover i FAQ (trafiają do wyników wyszukiwania i na okładkę).
3. **Źródła:** twierdzenie prawne wskazuje przepis (ustawa i artykuł) i ma źródło w `sources` ([preferowane domeny, np. isap.sejm.gov.pl, eli.gov.pl, eur-lex.europa.eu, urząd branżowy, pomoc platformy]). Martwe albo przekierowane linki napraw.

## Zasady poprawek
- Poprawiaj **tylko swoje pliki**. Inni agenci równolegle poprawiają pozostałe.
- Treść automatyczna: **żadnych znaczników** [DO UZUPEŁNIENIA] / [NIEZWERYFIKOWANE]. Nie da się potwierdzić → usuń albo przeformułuj na wersję, którą da się potwierdzić. Nie wymyślaj doświadczeń autora.
- Przy prawie: „art. X ustawy Y stanowi…”. Bez opinii prawnych; w sprawach indywidualnych odsyłaj do [prawnika / lekarza / doradcy], bez straszenia.
- Zmieniona liczba → popraw ją wszędzie w pliku: lead, tldr, cover.big i cover.sub, faq, description, treść.
- Sprawdzone źródło: `checkedAt: [data]`. Sprawdzony plik: `verifiedAt: [data]` (i `updatedAt: [data]`, jeśli zmieniłeś treść).
- Styl: `~/.claude/skills/klaster-tresci/references/styl.md` + zasady projektu: [np. maks. jeden myślnik na akapit, bez „nie X, tylko Y”].
- Fakty o autorze: tylko [prawdziwe fakty]. Nigdy [zakazane twierdzenia].
- Nie publikuj, nie wysyłaj formularzy, nie loguj się. Tylko czytasz źródła i edytujesz lokalne pliki.
- Na końcu: `python3 ~/.claude/skills/klaster-tresci/scripts/sprawdz.py [katalog]`; Twoje pliki bez błędów.

## Raport (ostatnia wiadomość), maks. ~25 linii na plik
- **Status:** OK, poprawiony albo do decyzji użytkownika.
- **Zmiany:** było → jest → dlaczego → źródło (URL).
- **Do decyzji użytkownika:** czego nie poprawiłeś, bo wymaga decyzji biznesowej albo konsultacji prawnej.
```

## Lista aktów: przykład dla Polski (stan sprawdzony 13.10.2026)

Przykład z projektu dla małych firm usługowych (strony, wizytówka Google, opinie, marketing). W każdym audycie sprawdź na nowo, czy akty i artykuły są aktualne, i dobierz listę do niszy (np. medycyna: ustawa o zawodach lekarza i lekarza dentysty i zasady reklamy podmiotów leczniczych; finanse: przepisy o kredycie konsumenckim).

| Akt | Przepisy | Czego dotyczy w treściach |
|---|---|---|
| Ustawa o przeciwdziałaniu nieuczciwym praktykom rynkowym (upnpr) | **art. 7 pkt 25 i 26** | praktyki zawsze wprowadzające w błąd dotyczące opinii konsumentów (zapewnianie, że opinie pochodzą od klientów, bez rozsądnych kroków weryfikacji; fałszywe albo zlecane opinie) |
| Ustawa o prawach konsumenta | **art. 7aa** | informacja, czy i jak przedsiębiorca udostępniający opinie zapewnia, że pochodzą od konsumentów |
| Prawo przedsiębiorców | **art. 20 ust. 3** | obowiązki przedsiębiorcy związane z informacjami o działalności (sprawdź brzmienie przed użyciem w tekście) |
| Prawo komunikacji elektronicznej (PKE, od 10.11.2024) | **art. 398 i 399** | zgoda na marketing bezpośredni i niezamówione informacje handlowe (e-mail, SMS, telefon), np. prośby o opinię wysyłane klientom |
| Ustawa o świadczeniu usług drogą elektroniczną (uśude) | **art. 5 i 8** | obowiązki informacyjne usługodawcy i regulamin usługi elektronicznej, w zakresie, który nadal obowiązuje |
| Akt o usługach cyfrowych (DSA) i jego wdrożenie w Polsce | ustawa wdrażająca: **Dz.U. 2026 poz. 1296**, stosowana **od 6.11.2026** | obowiązki platform i usługodawców pośredniczących; teksty pisane przed tą datą muszą mówić o stanie „od 6.11.2026” |
| Ustawa o zwalczaniu nieuczciwej konkurencji | | m.in. reklama wprowadzająca w błąd, porównawcza |
| Kodeks cywilny | art. 23, 24, 43 | dobra osobiste (także osób prawnych), np. odpowiedzi na opinie |
| Kodeks karny | art. 212 | zniesławienie |
| RODO | | dane klienta w odpowiedzi na opinię, zdjęcia realizacji z wizerunkiem lub adresem |
| Prawo autorskie | art. 81 i przepisy o utworach | wizerunek, zdjęcia, teksty |
| Ustawa o informowaniu o cenach | | cena brutto, najniższa cena z 30 dni przy obniżkach |
| Kodeksy etyki zawodów zaufania publicznego | | gdy tekst dotyczy np. kancelarii, gabinetów lekarskich: zasady informowania o działalności |

Poprawki względem wcześniejszego briefu (13.10.2026): opinie konsumentów w upnpr to **art. 7 pkt 25 i 26** (nie „pkt 23b–23c”); doszły art. 7aa ustawy o prawach konsumenta, art. 20 ust. 3 Prawa przedsiębiorców, art. 398 i 399 PKE, art. 5 i 8 uśude oraz polskie wdrożenie DSA (Dz.U. 2026 poz. 1296, od 6.11.2026).

## Czego audyt nie zmienia

- Struktury tekstu, tytułów i fraz głównych bez potrzeby prawnej albo faktowej (kanibalizacja, SEO).
- Dat publikacji wstecz. `publishedAt` zostaje; zmienia się `verifiedAt` i ewentualnie `updatedAt`, a przy istotnej zmianie dopisz datowaną notkę („Aktualizacja 13.10.2026: …”).

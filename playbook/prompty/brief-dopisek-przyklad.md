# Dopisek do briefu (17.10.2026, ważniejszy niż brief tam, gdzie się różnią)

- **Lista slugów do linkowania w briefie jest nieaktualna.** Aktualne poradniki to pliki w `src/content/poradniki/` (`ls`). Linkuj tylko do istniejących plików i do slugów, które tworzysz. `oferta-cenowa-wzor` nie istnieje: jest `oferta-cenowa`.
- Narzędzia: `/narzedzia/koszt-zlecenia/`, `/narzedzia/kod-qr/`, `/narzedzia/stawka-godzinowa/` (kalkulator stawki godzinowej).
- **Żadnych wzorów dokumentów** (decyzja właściciela 17.10.2026): nie dajemy wzorów do skopiowania ani do pobrania dla protokołów, ofert, umów, harmonogramów do podpisu, kosztorysów z pustymi polami itp. Ktoś by ich użył i miał do nas pretensje. Wolno: listy kontrolne, opisy, co powinno być w dokumencie, przykładowe wiadomości SMS/e-mail do klienta.
- **Źródła z licencją niekomercyjną odpadają** (np. wynagrodzenia.pl). Jeśli strona źródła zastrzega użytek niekomercyjny, nie cytuj jej.
- Cel właściciela: zdobyć społeczność fachowców. Teksty mają dawać coś, czym fachowiec chętnie się podzieli: konkretne liczby, porównania, gotowe do użycia kroki.
- `cta.href`: `/strona-dla-fachowca/` albo `/audyt-strony/` (dobierz do tematu); dla Organizacji możesz też dać narzędzie, jeśli pasuje.
- QA: `python3 .claude/skills/klaster-tresci/scripts/sprawdz.py <Twoje pliki> --lp /strona-dla-fachowca/ --known /audyt-strony/ /wizytowka-google/ /poradniki/ /narzedzia/koszt-zlecenia/ /narzedzia/kod-qr/ /narzedzia/stawka-godzinowa/`
- Nowy kolor taśmy nowego klastra NIE jest Twoją sprawą (ustawi go koordynator). Nie zmieniaj `szablon.html`, `dzialy.ts` ani innych plików poza swoimi tekstami.
- Limit: do ~50 wywołań DataForSEO na agenta (w tym search_volume do wyboru fraz: `POST /v3/keywords_data/google_ads/search_volume/live` z `[{"keywords":[...],"location_code":2616,"language_code":"pl"}]`).

#!/usr/bin/env python3
"""QA klastra artykułów (Markdown/MDX z frontmatterem według szablonu skilla).

Użycie:
  sprawdz.py src/content/poradniki [--hub /poradniki/] [--lp /] [--today 2026-10-12] [--known /kalkulator/ /cennik/]

Znane linki: slugi tekstów, huby, --known oraz trasy projektu wykryte automatycznie z src/pages/**
(katalog szukany w górę od katalogu treści; --pages wskazuje go ręcznie, --no-pages wyłącza).
Trasy dynamiczne ([slug]) pasują jako wzorzec, poza katalogiem samych poradników, gdzie liczy się
tylko istniejący slug. Jeśli jest dist/ z buildu, jego strony też są znane.

BŁĄD = do poprawienia przed publikacją. UWAGA = oceń, czy to świadoma decyzja.
Kod wyjścia 1, jeśli są błędy.
"""
import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fm  # noqa: E402

FRAZESY = [
    "w dzisiejszych czasach", "w dobie", "dynamicznie zmieniającym się", "warto zauważyć", "warto podkreślić",
    "należy pamiętać", "nie ulega wątpliwości", "bez wątpienia", "jak sama nazwa wskazuje", "w tym artykule dowiesz się",
    "zapraszamy do lektury", "mamy nadzieję", "podsumowując", "reasumując", "kompleksow", "holistyczn",
    "innowacyjn", "odkryj ", "zanurz się", "na wyższy poziom", "zmieniająca zasady gry", "idealny dla każdego",
    "kluczowy", "kluczowe", "kluczową",
]
ZNACZNIKI = ["[DO UZUPEŁNIENIA", "[NIEZWERYFIKOWANE", "TODO", "TBD", "lorem ipsum"]
WYMAGANE = ["title", "seoTitle", "description", "publishedAt", "verifiedAt", "primaryKeyword", "sources", "hub"]


def as_date(v):
    if v is None:
        return None
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def slug_of(path, meta):
    return str(meta.get("slug") or Path(path).stem)


def first_paragraph(body):
    for block in re.split(r"\n\s*\n", body.strip()):
        b = block.strip()
        if b and not b.startswith(("#", ">", "-", "*", "|", "<", "import ", "export ", "![")):
            return b
    return ""


def internal_links(body):
    md = re.findall(r"\]\((/[^)\s#?]*)", body)
    html = re.findall(r'href="(/[^"#?]*)"', body)
    return md + html


PAGE_EXT = {".astro", ".md", ".mdx", ".html"}


def find_pages(paths):
    """Szuka src/pages w górę od pierwszej ścieżki treści (maks. 6 poziomów)."""
    start = Path(paths[0]).resolve()
    for d in [start, *start.parents][:7]:
        if (d / "src" / "pages").is_dir():
            return d / "src" / "pages"
    return None


def project_routes(pages, content_prefixes):
    """Zwraca (zbiór tras statycznych, lista wzorców tras dynamicznych) z src/pages/**.
    Trasy dynamiczne w katalogu poradników (content_prefixes) pomija: tam link musi trafić w istniejący slug."""
    exact, patterns = set(), []
    for f in pages.rglob("*"):
        if f.suffix not in PAGE_EXT or any(part.startswith("_") for part in f.relative_to(pages).parts):
            continue
        parts = list(f.relative_to(pages).with_suffix("").parts)
        if parts and parts[-1] == "index":
            parts = parts[:-1]
        route = "/".join(parts)
        if "[" not in route:
            exact.add(route)
            continue
        static = "/".join(p for p in parts if "[" not in p)
        prefix = route.split("[")[0].strip("/")
        if prefix in content_prefixes:
            continue
        rx = "/".join(".*" if p.startswith("[...") else "[^/]+" if "[" in p else re.escape(p) for p in parts)
        patterns.append((re.compile(rx), static))
    dist = pages.parent.parent / "dist"
    if dist.is_dir():
        for f in dist.rglob("index.html"):
            exact.add(str(f.parent.relative_to(dist)).strip(".").strip("/"))
    return exact, patterns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--hub", help="ścieżka huba, np. /poradniki/ (domyślnie z frontmattera 'hub')")
    ap.add_argument("--lp", help="ścieżka LP/oferty, np. / albo /audyt/")
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--known", nargs="*", default=[], help="dodatkowe istniejące ścieżki (narzędzia, LP, huby)")
    ap.add_argument("--pages", help="katalog src/pages projektu (domyślnie szukany w górę od katalogu treści)")
    ap.add_argument("--no-pages", action="store_true", help="nie wczytuj tras z src/pages")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today)

    files = []
    for p in a.paths:
        P = Path(p)
        files += sorted(P.rglob("*.md")) + sorted(P.rglob("*.mdx")) if P.is_dir() else [P]
    if not files:
        print("Nie znaleziono plików .md/.mdx")
        return 1

    docs = []
    for f in files:
        meta, body = fm.parse(f.read_text(encoding="utf-8"))
        docs.append((f, meta, body))
    slugs = {slug_of(f, m) for f, m, _ in docs}
    known = {s.strip("/") for s in a.known} | {str(m.get("hub", "")).strip("/") for _, m, _ in docs}
    if a.lp:
        known.add(a.lp.strip("/"))
    patterns = []
    if not a.no_pages:
        pages = Path(a.pages) if a.pages else find_pages(a.paths)
        if pages and pages.is_dir():
            # katalog poradników = rodzic hubów, np. /poradniki/opinie/ → "poradniki"
            prefixes = {"/".join(str(m.get("hub", "")).strip("/").split("/")[:-1]) for _, m, _ in docs if m.get("hub")}
            prefixes |= {str(m.get("hub", "")).strip("/") for _, m, _ in docs if m.get("hub")} - {""}
            exact, patterns = project_routes(pages, prefixes - {""} or {""})
            known |= exact
            print(f"Trasy projektu z {pages}: {len(exact)} stałych, {len(patterns)} dynamicznych")

    errors = warns = 0
    kw_owner = defaultdict(list)
    slug_owner = defaultdict(list)
    summary = []

    for f, m, body in docs:
        E, W = [], []
        slug = slug_of(f, m)
        slug_owner[slug].append(f.name)
        typ = m.get("type", "poradnik")
        draft = m.get("draft", True) is not False

        for k in WYMAGANE:
            if typ == "hub" and k in ("sources", "hub"):
                continue  # hub nie ma huba nadrzędnego, a źródła mają jego teksty
            if not m.get(k):
                E.append(f"brak pola '{k}'")
        st = str(m.get("seoTitle") or "")
        if len(st) > 60:
            E.append(f"seoTitle ma {len(st)} znaków (max 60)")
        desc = str(m.get("description") or "")
        if desc and not 110 <= len(desc) <= 165:
            W.append(f"description ma {len(desc)} znaków (cel 120-160)")
        if desc and not re.search(r"\d", desc):
            W.append("description bez liczby/konkretu")

        pub, ver, upd = as_date(m.get("publishedAt")), as_date(m.get("verifiedAt")), as_date(m.get("updatedAt"))
        for name, d in (("publishedAt", pub), ("verifiedAt", ver), ("updatedAt", upd)):
            if d and d > today:
                (W if draft else E).append(f"{name} {d} jest w przyszłości")
        if pub and upd and upd < pub:
            E.append("updatedAt wcześniejsze niż publishedAt")
        if pub and pub < today - dt.timedelta(days=365 * 3) and draft:
            W.append(f"publishedAt {pub} to ponad 3 lata temu - nowy tekst nie może mieć daty wstecz")

        yrs = re.findall(r"\b(20\d\d)\b", str(m.get("title", "")))
        for y in yrs:
            if int(y) not in (today.year, today.year + 1):
                W.append(f"rok {y} w tytule nie jest bieżący")

        tldr = m.get("tldr") or []
        if typ in ("poradnik", "porownanie") and not 3 <= len(tldr) <= 5:
            W.append(f"tldr ma {len(tldr)} punktów (cel 3-5)")
        faq = m.get("faq") or []
        if typ in ("poradnik", "porownanie", "encja") and not 4 <= len(faq) <= 8:
            W.append(f"FAQ ma {len(faq)} pytań (cel 4-7)")
        for q in faq:
            if isinstance(q, dict) and len(str(q.get("a", "")).split()) > 70:
                W.append(f"zbyt długa odpowiedź FAQ: '{str(q.get('q'))[:40]}...'")

        src = m.get("sources") or []
        if isinstance(src, list) and typ != "hub":
            if len(src) < 2:
                W.append(f"tylko {len(src)} źródło(a) (cel ≥ 2)")
            for s in src:
                if not isinstance(s, dict) or not s.get("url") or not s.get("checkedAt"):
                    E.append(f"źródło bez url/checkedAt: {s}")

        if re.search(r"^#\s", body, re.M):
            E.append("H1 w treści (H1 pochodzi z 'title')")
        h2 = len(re.findall(r"^##\s", body, re.M))
        if typ == "poradnik" and h2 < 4:
            W.append(f"tylko {h2} sekcji H2 (cel 4-7)")
        words = len(re.findall(r"\w+", re.sub(r"<[^>]+>|\(http[^)]*\)", " ", body)))
        if typ == "poradnik" and words < 700:
            W.append(f"tylko {words} słów - czy intencja jest wyczerpana?")

        lead = str(m.get("lead") or first_paragraph(body))
        if lead:
            if len(lead.split()) > 70:
                W.append(f"lead ma {len(lead.split())} słów (cel ≤ 60)")
            if not re.search(r"\d", lead):
                W.append("lead bez liczby - czy odpowiada od razu na pytanie z H1?")
            if re.search(r"w tym (artykule|poradniku|tekście)", lead, re.I):
                W.append("lead zapowiada zamiast odpowiadać ('w tym artykule...')")

        links = internal_links(body)
        targets = {l.strip("/") for l in links}
        if len(set(links)) < 3:
            W.append(f"tylko {len(set(links))} linki wewnętrzne w treści (cel ≥ 3)")
        hub = (a.hub or str(m.get("hub") or "")).strip("/")
        if hub and hub not in targets:
            W.append(f"treść nie linkuje do huba /{hub}/")
        if a.lp is not None:
            cta = m.get("cta") or {}
            if a.lp.strip("/") not in targets and not (isinstance(cta, dict) and cta.get("href")):
                W.append("brak linku/CTA do LP")
        for t in sorted(targets):
            last = t.split("/")[-1] if t else ""
            if t and t not in known and last not in slugs and t not in slugs and not any(rx.fullmatch(t) for rx, _ in patterns):
                W.append(f"link do nieznanej strony /{t}/ (sprawdź, czy istnieje)")
        for r in m.get("related") or []:
            if str(r).strip("/").split("/")[-1] not in slugs:
                E.append(f"related '{r}' nie istnieje w klastrze")
        if slug in targets:
            W.append("tekst linkuje sam do siebie")

        low = body.lower()
        found = [p for p in FRAZESY if p in low]
        if found:
            W.append("frazesy: " + ", ".join(sorted(set(found))))
        marks = sum(body.count(z) + str(m).count(z) for z in ZNACZNIKI)
        if marks:
            (E if not draft else W).append(f"{marks} znaczników do uzupełnienia/weryfikacji" + ("" if draft else " przy draft: false"))
        if re.search(r"/polecam/|ref=|aff", body) and not m.get("affiliate"):
            W.append("wygląda na link partnerski, a affiliate nie jest true")

        pk = str(m.get("primaryKeyword") or "").strip().lower()
        if pk:
            kw_owner[pk].append(f.name)

        errors += len(E)
        warns += len(W)
        summary.append((f.name, words, h2, len(set(links)), len(faq), len(E), len(W)))
        if E or W:
            print(f"\n{f}")
            for e in E:
                print(f"  BŁĄD   {e}")
            for w in W:
                print(f"  UWAGA  {w}")

    print()
    for k, owners in kw_owner.items():
        if len(owners) > 1:
            errors += 1
            print(f"BŁĄD   kanibalizacja: fraza '{k}' w {', '.join(owners)}")
    for k, owners in slug_owner.items():
        if len(owners) > 1:
            errors += 1
            print(f"BŁĄD   zduplikowany slug '{k}' w {', '.join(owners)}")

    print("\nplik | słowa | H2 | linki wewn. | FAQ | błędy | uwagi")
    for row in summary:
        print(" | ".join(str(x) for x in row))
    print(f"\nRazem: {len(docs)} plików, {errors} błędów, {warns} uwag")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Renderuje okładki z SZABLONU PROJEKTU (HTML) - skrypt nie ma własnego wyglądu.

Wygląd projektujesz w projekcie (np. src/okladki/szablon.html) z jego marki.
Skrypt tylko podstawia dane z frontmattera i robi PNG przez headless Chrome/Edge/Brave.

Miejsca na dane w szablonie (wartości są escapowane):
  {{brand}} {{kicker}} {{category}} {{big}} {{sub}} {{title}} {{slug}}
  {{format}}  - og | hero (użyj np. <body data-format="{{format}}"> i CSS per format)
  {{width}} {{height}}
  {{meta.KLUCZ}} - dowolne pole skalarne z frontmattera, np. {{meta.readingTime}}

Przykłady:
  okladka.py --template src/okladki/szablon.html --from-dir src/content/poradniki --out public/okladki
  okladka.py --template src/okladki/szablon.html --slug proba --kicker "SEO · AUDYT" --big "14 dni" \
      --sub "OD ZGŁOSZENIA DO RAPORTU" --title "Ile trwa audyt SEO" --out /tmp/okladki
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fm  # noqa: E402

SIZES = {"og": (1200, 630), "hero": (1600, 900)}
CHROMES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge",
]


def find_chrome():
    for c in CHROMES:
        if os.path.exists(c):
            return c
        if shutil.which(c):
            return shutil.which(c)
    return None


def fill(template, data):
    def rep(m):
        key = m.group(1).strip()
        if key.startswith("meta."):
            val = (data.get("meta") or {}).get(key[5:], "")
        else:
            val = data.get(key, "")
        return html.escape("" if val is None else str(val))

    out = re.sub(r"\{\{\s*([\w.]+)\s*\}\}", rep, template)
    left = re.findall(r"\{\{[^}]*\}\}", out)
    if left:
        print(f"  uwaga: niepodstawione miejsca w szablonie: {set(left)}", file=sys.stderr)
    return out


def render(chrome, html_path, png_path, W, H, budget=3000, scale=1):
    """Zrzut strony do PNG. Każde wywołanie ma własny, tymczasowy profil Chrome,
    więc równoległe rendery (wątki, kilka procesów) nie blokują się nawzajem."""
    profile = tempfile.mkdtemp(prefix="okladka-chrome-")
    try:
        cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={scale}",
               f"--user-data-dir={profile}", "--no-first-run", "--no-default-browser-check",
               f"--window-size={W},{H}", f"--virtual-time-budget={budget}",
               f"--screenshot={os.path.abspath(png_path)}", Path(html_path).resolve().as_uri()]
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    return os.path.exists(png_path)


def data_from_md(path):
    meta, _ = fm.parse(Path(path).read_text(encoding="utf-8"))
    cov = meta.get("cover") or {}
    scal = {k: v for k, v in meta.items() if not isinstance(v, (dict, list))}
    return {
        "slug": meta.get("slug") or Path(path).stem,
        "kicker": meta.get("kicker") or meta.get("category") or "",
        "category": meta.get("category") or "",
        "big": cov.get("big") or "",
        "sub": cov.get("sub") or "",
        "title": cov.get("label") or meta.get("title") or "",
        "meta": scal,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--template", required=True, help="szablon HTML okładki zaprojektowany w projekcie")
    ap.add_argument("--from", dest="from_md", help="jeden plik .md/.mdx z frontmatterem")
    ap.add_argument("--from-dir", help="katalog z artykułami - okładka dla każdego")
    ap.add_argument("--slug")
    ap.add_argument("--brand", default="")
    ap.add_argument("--kicker", default="")
    ap.add_argument("--big", default="")
    ap.add_argument("--sub", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--formats", default="og,hero", help="og,hero albo nazwa=SZERxWYS, np. kwadrat=1080x1080")
    ap.add_argument("--out", default=".")
    ap.add_argument("--keep-html", action="store_true", help="zostaw wypełnione HTML-e (do debugowania)")
    a = ap.parse_args()

    tpl_path = Path(a.template)
    template = tpl_path.read_text(encoding="utf-8")
    formats = {}
    for f in a.formats.split(","):
        f = f.strip()
        if "=" in f:
            name, size = f.split("=")
            w, h = size.lower().split("x")
            formats[name] = (int(w), int(h))
        elif f in SIZES:
            formats[f] = SIZES[f]

    if a.from_dir:
        jobs = [data_from_md(p) for p in sorted(Path(a.from_dir).rglob("*.md*"))]
    elif a.from_md:
        jobs = [data_from_md(a.from_md)]
    elif a.slug:
        jobs = [{"slug": a.slug, "kicker": a.kicker, "category": "", "big": a.big, "sub": a.sub,
                 "title": a.title, "meta": {}}]
    else:
        ap.error("podaj --from, --from-dir albo --slug")
    for j in jobs:
        j["brand"] = a.brand

    chrome = find_chrome()
    os.makedirs(a.out, exist_ok=True)
    for j in jobs:
        for fmt, (W, H) in formats.items():
            data = dict(j, format=fmt, width=W, height=H)
            # plik tymczasowy obok szablonu, żeby działały względne ścieżki do fontów i logo
            # nazwa szablonu i PID w nazwie: równoległe rendery (też kilka procesów na tym samym szablonie) nie nadpisują się
            tmp = tpl_path.parent / f".okladka-{tpl_path.stem}-{j['slug']}-{fmt}-{os.getpid()}.html"
            tmp.write_text(fill(template, data), encoding="utf-8")
            png = os.path.join(a.out, f"{j['slug']}-{fmt}.png")
            if chrome and render(chrome, tmp, png, W, H):
                print(png)
            else:
                print(f"nie wyrenderowano {png} - wypełniony HTML: {tmp}", file=sys.stderr)
                continue
            if not a.keep_html:
                tmp.unlink(missing_ok=True)
    if not chrome:
        print("Brak Chrome/Edge/Brave/Chromium. Alternatywy: npx playwright screenshot, albo generowanie przy buildzie "
              "(satori + @resvg/resvg-js) z tych samych pól cover.*", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Arkusz opcji do wyboru przez użytkownika: siatka z numerami i nazwami, zapis do PNG.

Opcje to pliki HTML, SVG albo obrazy (PNG/JPG/WebP). HTML-e renderuje najpierw osobno
(równolegle, przez okladka.render), więc ich skrypty dopasowujące tekst mają pełny czas.
Arkusz nie ma wyglądu marki: neutralne tło, duże numery, nazwy opcji. Użytkownik odpowiada numerem.

Nazwa opcji: PLIK=Nazwa w argumencie, albo <title> w HTML/SVG, albo nazwa pliku.

Przykłady:
  arkusz.py opcje/*.html --size 1200x630 --cols 3 --title "Okładki: runda 1" --out arkusz.png
  arkusz.py logo-01.png=Kryształ logo-02.png=Połysk --cols 5 --out logo.png
  # okładki: 5 opcji × 6 tekstów, jeden wiersz = jedna opcja (numer na wiersz, podpisy na miniaturach)
  arkusz.py a/*.png b/*.png c/*.png --grupuj 6 --nazwy "Karta,Kryształ,Połysk,Liczba,Ilustracja" --out okladki.png

Równoległe uruchomienia są bezpieczne: każdy przebieg ma własny katalog tymczasowy,
każdy render własny profil Chrome.
"""
import argparse
import html
import math
import os
import re
import shutil
import struct
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import okladka  # noqa: E402

IMG = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", head[16:24])
    return None


def svg_size(path):
    s = Path(path).read_text(encoding="utf-8", errors="ignore")[:4000]
    m = re.search(r'viewBox="\s*[-\d.]+[ ,]+[-\d.]+[ ,]+([\d.]+)[ ,]+([\d.]+)', s)
    if m:
        return float(m.group(1)), float(m.group(2))
    w, h = re.search(r'\swidth="([\d.]+)', s), re.search(r'\sheight="([\d.]+)', s)
    return (float(w.group(1)), float(h.group(1))) if w and h else None


def title_of(path):
    if Path(path).suffix.lower() in (".html", ".htm", ".svg"):
        s = Path(path).read_text(encoding="utf-8", errors="ignore")[:6000]
        m = re.search(r"<title>(.*?)</title>", s, re.S | re.I)
        if m and m.group(1).strip():
            return html.unescape(m.group(1).strip())
    return re.sub(r"^\d+[-_ ]*", "", Path(path).stem).replace("-", " ").replace("_", " ")


def parse_items(args):
    items = []
    for a in args:
        path, _, name = a.partition("=")
        P = Path(path)
        if P.is_dir():
            for f in sorted(P.iterdir()):
                if f.suffix.lower() in IMG | {".html", ".htm", ".svg"} and not f.name.startswith("."):
                    items.append({"path": f.resolve(), "name": title_of(f)})
        elif P.exists():
            items.append({"path": P.resolve(), "name": name or title_of(P)})
        else:
            print(f"pomijam: brak pliku {path}", file=sys.stderr)
    return items


def prerender(items, size, chrome, tmp, jobs):
    """HTML → PNG w katalogu tymczasowym tego przebiegu (unikalne nazwy, bez kolizji)."""
    W, H = size

    def one(i_it):
        i, it = i_it
        if it["path"].suffix.lower() not in (".html", ".htm"):
            return
        png = Path(tmp) / f"opcja-{i:03d}.png"
        if okladka.render(chrome, it["path"], png, W, H):
            it["img"] = png
        else:
            print(f"nie wyrenderowano {it['path']}", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(one, enumerate(items)))
    for it in items:
        it.setdefault("img", it["path"])


def build(items, out, *, cols=None, cell=420, size=None, title="", note="", group=1, names=None,
          bg="#e8e8e6", ink="#141414", cell_bg="#ffffff", start=1, jobs=4, keep_html=False):
    """Buduje arkusz i zapisuje PNG. Zwraca ścieżkę PNG albo None. Używane też przez logo.py."""
    chrome = okladka.find_chrome()
    if not chrome:
        print("Brak Chrome/Edge/Brave/Chromium - nie zrobię PNG.", file=sys.stderr)
        return None
    if not items:
        print("Brak opcji.", file=sys.stderr)
        return None
    tmp = tempfile.mkdtemp(prefix="arkusz-")
    try:
        if size is None:
            first = items[0]["path"]
            size = (png_size(first) if first.suffix.lower() == ".png" else svg_size(first) if first.suffix.lower() == ".svg" else None) or (1200, 630)
        W, H = int(size[0]), int(size[1])
        prerender(items, (W, H), chrome, tmp, jobs)

        groups = [items[i:i + group] for i in range(0, len(items), group)]
        if group > 1:
            cols = group
            thumb_w = cell
        else:
            cols = cols or min(5, max(1, math.ceil(math.sqrt(len(items)))))
            thumb_w = cell
        thumb_h = round(thumb_w * H / W)
        pad, gap, cap = 28, 22, 54 if group == 1 else 26
        label_w = 120 if group > 1 else 0
        width = pad * 2 + label_w + cols * thumb_w + (cols - 1) * gap
        head = (70 if title else 0) + (34 if note else 0)
        if group > 1:
            rows = len(groups)
            row_h = thumb_h + cap
            height = pad * 2 + head + rows * row_h + (rows - 1) * (gap + 14)
        else:
            rows = math.ceil(len(items) / cols)
            row_h = thumb_h + cap
            height = pad * 2 + head + rows * row_h + (rows - 1) * gap

        def fig(it, num=None, small=False):
            src = Path(it["img"]).resolve().as_uri()
            # numer pod miniaturą, nie na niej: nie zasłania logo ani etykiety w rogu opcji
            badge = f'<b class="nr">{num}</b>' if num is not None else ""
            cls = "cap small" if small else "cap"
            return (f'<figure style="width:{thumb_w}px"><div class="th" style="height:{thumb_h}px"><img src="{src}"></div>'
                    f'<figcaption class="{cls}">{badge}<span>{html.escape(it["name"])}</span></figcaption></figure>')

        body = []
        if group > 1:
            for gi, g in enumerate(groups):
                nm = (names[gi] if names and gi < len(names) else "")
                body.append(f'<section class="row"><div class="lab"><b class="nr big">{start + gi}</b>'
                            f'<span>{html.escape(nm)}</span></div>{"".join(fig(it, small=True) for it in g)}</section>')
        else:
            body.append('<section class="grid">' + "".join(fig(it, start + i) for i, it in enumerate(items)) + "</section>")

        page = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>
*{{margin:0;box-sizing:border-box}}
body{{width:{width}px;height:{height}px;overflow:hidden;background:{bg};color:{ink};padding:{pad}px;
  font-family:-apple-system,"Segoe UI",Inter,Helvetica,Arial,sans-serif}}
h1{{font-size:30px;font-weight:800;letter-spacing:-.01em;height:56px;margin-bottom:14px;display:flex;align-items:flex-end}}
.note{{font-size:16px;opacity:.7;height:22px;margin:-6px 0 12px}}
.grid{{display:grid;grid-template-columns:repeat({cols},{thumb_w}px);gap:{gap}px}}
.row{{display:grid;grid-template-columns:{label_w}px repeat({cols},{thumb_w}px);gap:{gap}px;align-items:start;margin-bottom:{gap + 14}px}}
.row:last-child{{margin-bottom:0}}
.lab{{display:flex;flex-direction:column;gap:8px;padding-top:4px}}
.lab span{{font-size:14px;font-weight:700;line-height:1.3}}
figure{{margin:0}}
.th{{position:relative;background:{cell_bg};outline:1px solid rgba(0,0,0,.12);overflow:hidden}}
.th img{{display:block;width:100%;height:100%;object-fit:contain}}
.nr{{display:inline-grid;place-items:center;min-width:40px;height:40px;padding:0 10px;border-radius:20px;background:{ink};color:{bg};
  font-size:22px;font-weight:800;font-variant-numeric:tabular-nums}}
.nr.big{{min-width:56px;height:56px;border-radius:28px;font-size:30px;align-self:flex-start}}
.cap{{display:flex;align-items:center;gap:10px;font-size:17px;font-weight:700;padding-top:10px;white-space:nowrap;overflow:hidden}}
.cap span{{overflow:hidden;text-overflow:ellipsis}}
.cap.small{{display:block;font-size:13px;font-weight:600;opacity:.75;padding-top:6px;text-overflow:ellipsis}}
</style></head><body>
{f'<h1>{html.escape(title)}</h1>' if title else ''}{f'<p class="note">{html.escape(note)}</p>' if note else ''}
{''.join(body)}
</body></html>"""
        sheet = Path(tmp) / "arkusz.html"
        sheet.write_text(page, encoding="utf-8")
        if keep_html:
            keep = Path(out).with_suffix(".html")
            shutil.copy(sheet, keep)
            print(f"HTML arkusza: {keep}", file=sys.stderr)
        os.makedirs(Path(out).resolve().parent, exist_ok=True)
        ok = okladka.render(chrome, sheet, out, width, height, budget=5000)
        return out if ok else None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("opcje", nargs="+", help="pliki lub katalogi; PLIK=Nazwa nadaje nazwę opcji")
    ap.add_argument("--out", required=True, help="plik PNG arkusza")
    ap.add_argument("--size", help="rozmiar renderu opcji HTML/SVG, np. 1200x630 (domyślnie z pierwszego pliku)")
    ap.add_argument("--cols", type=int, help="liczba kolumn (domyślnie ~pierwiastek z liczby opcji, maks. 5)")
    ap.add_argument("--cell", type=int, default=420, help="szerokość miniatury w px (domyślnie 420)")
    ap.add_argument("--grupuj", type=int, default=1, help="ile kolejnych plików tworzy jedną opcję (wiersz)")
    ap.add_argument("--nazwy", help="nazwy opcji przy --grupuj, rozdzielone przecinkami (albo | gdy nazwy mają przecinki)")
    ap.add_argument("--title", default="", help="tytuł arkusza, np. 'Logo: runda 2'")
    ap.add_argument("--note", default="", help="podpis pod tytułem, np. 'Odpowiedz numerem albo: połącz 2 z 5'")
    ap.add_argument("--start", type=int, default=1, help="pierwszy numer (przy kolejnej rundzie, np. 11)")
    ap.add_argument("--tlo", default="#e8e8e6", help="tło arkusza")
    ap.add_argument("--tlo-komorki", default="#ffffff", help="tło pod opcją (np. ciemne dla logo na ciemnym)")
    ap.add_argument("--jobs", type=int, default=4, help="ile renderów naraz")
    ap.add_argument("--keep-html", action="store_true")
    a = ap.parse_args()

    size = tuple(int(x) for x in a.size.lower().split("x")) if a.size else None
    items = parse_items(a.opcje)
    names = [n.strip() for n in a.nazwy.split("|" if "|" in a.nazwy else ",")] if a.nazwy else None
    lum = sum(int(a.tlo.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) / 3 if re.fullmatch(r"#[0-9a-fA-F]{6}", a.tlo) else 255
    out = build(items, a.out, cols=a.cols, cell=a.cell, size=size, title=a.title, note=a.note, group=a.grupuj,
                names=names, bg=a.tlo, ink="#141414" if lum > 128 else "#f2f2f2", cell_bg=a.tlo_komorki,
                start=a.start, jobs=a.jobs, keep_html=a.keep_html)
    if out:
        print(out)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

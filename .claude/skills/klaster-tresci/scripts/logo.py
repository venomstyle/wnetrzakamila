#!/usr/bin/env python3
"""Arkusz logo w kontekście: każda opcja na jednej karcie w kilku zastosowaniach.

Karta opcji pokazuje:
  1) nagłówek strony (tło nagłówka marki, logo ~40 px wysokości, menu, przycisk),
  2) kartę przeglądarki z favikoną 18 px i tytułem strony,
  3) znak 40 px (awatar, stopka, okładka),
  4) logo na jasnym tle i na ciemnym tle.
Tak widać od razu, które logo rozpada się w 18 px albo ginie na ciemnym tle.

Opcja = PELNE.svg[,ZNAK.svg][=Nazwa]. Bez ZNAK.svg favikona i 40 px używają pełnego logo.
SVG są wstawiane do strony (inline), więc tekst w SVG używa fontów z --css (np. @font-face marki).

Przykład:
  logo.py opcje/01.svg,opcje/01-znak.svg=Kryształ opcje/02.svg,opcje/02-znak.svg=Połysk ... \\
      --nazwa "Szkliwo" --naglowek "#0e2a3a" --akcent "#3bb8c4" --css fonty.css --out logo-runda1.png
"""
import argparse
import html
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arkusz  # noqa: E402

CARD_W, CARD_H = 1200, 760


def symbol(svg_path, sid):
    """Zamienia plik SVG na <symbol> (jedna kopia identyfikatorów, wiele użyć przez <use>)."""
    s = Path(svg_path).read_text(encoding="utf-8")
    s = re.sub(r"<\?xml[^>]*\?>|<!DOCTYPE[^>]*>|<!--.*?-->", "", s, flags=re.S).strip()
    m = re.search(r"<svg\b([^>]*)>(.*)</svg>", s, re.S)
    if not m:
        raise SystemExit(f"to nie jest SVG: {svg_path}")
    attrs, inner = m.groups()
    vb = re.search(r'viewBox="([^"]+)"', attrs)
    if vb:
        viewbox = vb.group(1)
    else:
        w, h = re.search(r'width="([\d.]+)', attrs), re.search(r'height="([\d.]+)', attrs)
        viewbox = f"0 0 {w.group(1) if w else 100} {h.group(1) if h else 100}"
    _, _, vw, vh = (float(x) for x in re.split(r"[ ,]+", viewbox.strip()))
    # identyfikatory wewnątrz (gradienty, maski) dostają prefiks opcji
    ids = set(re.findall(r'\bid="([^"]+)"', inner))
    for i in ids:
        inner = re.sub(rf'\bid="{re.escape(i)}"', f'id="{sid}-{i}"', inner)
        inner = re.sub(rf'url\(#{re.escape(i)}\)', f'url(#{sid}-{i})', inner)
        inner = re.sub(rf'href="#{re.escape(i)}"', f'href="#{sid}-{i}"', inner)
    return f'<symbol id="{sid}" viewBox="{viewbox}">{inner}</symbol>', vw / vh


def use(sid, ratio, h):
    return f'<svg class="u" style="height:{h}px;width:{h * ratio:.1f}px" viewBox="0 0 {ratio * 100:.3f} 100"><use href="#{sid}" width="{ratio * 100:.3f}" height="100"/></svg>'


def card(full, mark, name, brand, a, css):
    sym_full, r_full = symbol(full, "pelne")
    sym_mark, r_mark = symbol(mark, "znak") if mark else (None, r_full)
    mid = "znak" if mark else "pelne"
    menu = "".join(f"<span>{html.escape(x)}</span>" for x in a.menu.split(","))
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>{html.escape(name)}</title><style>
{css}
*{{margin:0;box-sizing:border-box}}
body{{width:{CARD_W}px;height:{CARD_H}px;overflow:hidden;background:#f3f3f1;font-family:-apple-system,"Segoe UI",Inter,Arial,sans-serif;color:#1a1a1a;
  display:grid;grid-template-columns:1fr 1fr;grid-template-rows:150px 230px 1fr;gap:14px;padding:14px}}
.p{{position:relative;border-radius:6px;overflow:hidden;outline:1px solid rgba(0,0,0,.08)}}
.p em{{position:absolute;left:12px;bottom:8px;font:600 12px/1 -apple-system,Arial,sans-serif;font-style:normal;letter-spacing:.06em;text-transform:uppercase;opacity:.55}}
.naglowek{{grid-column:1/-1;background:{a.naglowek};color:{a.naglowek_tekst};display:flex;align-items:center;gap:36px;padding:0 40px}}
.naglowek .menu{{display:flex;gap:28px;margin-left:auto;font-size:17px;font-weight:600;opacity:.85}}
.naglowek .btn{{background:{a.akcent};color:{a.akcent_tekst};font-weight:700;padding:12px 20px;border-radius:8px;font-size:16px}}
.karta{{background:#dfe1e5;padding:22px 0 0 22px}}
.tab{{display:flex;align-items:center;gap:10px;width:330px;height:44px;padding:0 14px;background:#fff;border-radius:12px 12px 0 0;font-size:14px;color:#333}}
.tab .x{{margin-left:auto;opacity:.4}}
.pasek{{height:46px;background:#fff;margin-right:0;display:flex;align-items:center;padding:0 14px;gap:10px}}
.pasek i{{flex:1;height:30px;border-radius:15px;background:#f1f3f4;font:14px/30px -apple-system,Arial;font-style:normal;padding-left:14px;color:#555}}
.mini{{background:#fff;display:flex;align-items:center;justify-content:center;gap:34px}}
.mini .kolo{{width:64px;height:64px;border-radius:50%;background:{a.naglowek};display:grid;place-items:center}}
.mini .kw{{width:64px;height:64px;border-radius:14px;background:{a.akcent};color:{a.akcent_tekst};display:grid;place-items:center}}
.jasne{{background:#ffffff;display:grid;place-items:center}}
.ciemne{{background:{a.ciemne};display:grid;place-items:center;color:#fff}}
.dol{{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.u{{display:block;overflow:visible}}
</style></head><body>
<svg width="0" height="0" style="position:absolute">{sym_full}{sym_mark or ''}</svg>
<div class="p naglowek">{use('pelne', r_full, a.wys)}<div class="menu">{menu}</div><span class="btn">{html.escape(a.przycisk)}</span><em>nagłówek · {a.wys} px</em></div>
<div class="p karta"><div class="tab">{use(mid, r_mark, 18)}<span>{html.escape(brand)}: poradniki</span><span class="x">✕</span></div>
  <div class="pasek"><i>{html.escape(a.domena)}/poradniki/</i></div><em>karta przeglądarki · 18 px</em></div>
<div class="p mini">{use(mid, r_mark, 40)}<span class="kolo">{use(mid, r_mark, 34)}</span><span class="kw">{use(mid, r_mark, 34)}</span>{use(mid, r_mark, 24)}<em>znak · 40 / 34 / 24 px</em></div>
<div class="dol"><div class="p jasne">{use('pelne', r_full, 96)}<em>jasne tło</em></div><div class="p ciemne" style="color:{a.ciemne_tekst}">{use('pelne', r_full, 96)}<em>ciemne tło</em></div></div>
</body></html>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("opcje", nargs="+", help="PELNE.svg[,ZNAK.svg][=Nazwa]")
    ap.add_argument("--nazwa", required=True, help="nazwa marki (tytuł karty przeglądarki)")
    ap.add_argument("--domena", default="example.pl")
    ap.add_argument("--naglowek", default="#ffffff", help="tło nagłówka strony")
    ap.add_argument("--naglowek-tekst", default="#1a1a1a")
    ap.add_argument("--akcent", default="#1a1a1a", help="kolor przycisku i kafla znaku")
    ap.add_argument("--akcent-tekst", default="#ffffff")
    ap.add_argument("--ciemne", default="#14171a", help="ciemne tło do testu")
    ap.add_argument("--ciemne-tekst", default="#ffffff", help="currentColor na ciemnym tle")
    ap.add_argument("--menu", default="Poradniki,Cennik,O nas")
    ap.add_argument("--przycisk", default="Umów wizytę")
    ap.add_argument("--wys", type=int, default=40, help="wysokość logo w nagłówku, px")
    ap.add_argument("--css", help="plik CSS dołączany do karty (np. @font-face fontów marki, ścieżki bezwzględne)")
    ap.add_argument("--cols", type=int, default=2)
    ap.add_argument("--cell", type=int, default=600)
    ap.add_argument("--title", default="")
    ap.add_argument("--note", default="Odpowiedz numerem. Możesz też: „kolejny zestaw”, „połącz 2 z 5”, „popraw 3: …”.")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--out", required=True)
    ap.add_argument("--keep-html", action="store_true", help="zostaw karty HTML obok PNG")
    a = ap.parse_args()

    css = Path(a.css).read_text(encoding="utf-8") if a.css else ""
    tmp = tempfile.mkdtemp(prefix="logo-")
    try:
        items = []
        for i, spec in enumerate(a.opcje):
            files, _, name = spec.partition("=")
            full, _, mark = files.partition(",")
            name = name or arkusz.title_of(full)
            p = Path(tmp) / f"opcja-{i:02d}.html"
            p.write_text(card(full, mark or None, name, a.nazwa, a, css), encoding="utf-8")
            items.append({"path": p.resolve(), "name": name})
        if a.keep_html:
            keep = Path(a.out).with_suffix("")
            keep.mkdir(parents=True, exist_ok=True)
            for it in items:
                shutil.copy(it["path"], keep / it["path"].name)
        out = arkusz.build(items, a.out, cols=a.cols, cell=a.cell, size=(CARD_W, CARD_H), title=a.title or f"Logo: {a.nazwa}",
                           note=a.note, start=a.start)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if out:
        print(out)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

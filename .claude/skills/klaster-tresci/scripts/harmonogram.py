#!/usr/bin/env python3
"""Rozkłada publikację tekstów klastrami: hub wychodzi razem z pierwszym tekstem klastra,
potem reszta klastra, w wybrane dni tygodnia. Ustawia publishedAt i updatedAt
(data w przyszłości = wpis zaplanowany; build pomija go do tej daty).

--caly-klaster: każdy klaster (hub i wszystkie jego teksty) wychodzi jednego dnia,
jeden klaster na dzień publikacji (--na-dzien nie ma wtedy znaczenia).

Domyślnie tylko pokazuje plan. Zapis: --zapisz. Zatwierdzenie szkiców: --zatwierdz (draft: false).

  harmonogram.py src/content/poradniki --start 2026-10-20 --dni pn,sr,pt
  harmonogram.py src/content/poradniki --start 2026-10-20 --dni pn,czw --kolejnosc opinie-google,wizytowka-google --zapisz --zatwierdz
  harmonogram.py src/content/poradniki --start 2026-10-19 --dni pn,sob --caly-klaster --kolejnosc strona-firmowa,wizytowka-i-opinie
"""
import argparse
import datetime as dt
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fm  # noqa: E402

DNI = {"pn": 0, "wt": 1, "sr": 2, "czw": 3, "pt": 4, "sob": 5, "nd": 6}


def as_date(v):
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except (TypeError, ValueError):
        return None


def set_field(text, key, value):
    head, sep, body = text.partition("\n---\n")
    if re.search(rf"^{key}:.*$", head, re.M):
        head = re.sub(rf"^{key}:.*$", f"{key}: {value}", head, count=1, flags=re.M)
    else:
        head = head + f"\n{key}: {value}"
    return head + sep + body


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("katalog")
    ap.add_argument("--start", default=(dt.date.today() + dt.timedelta(days=1)).isoformat())
    ap.add_argument("--dni", default="pn,sr,pt", help="dni publikacji, np. pn,sr,pt")
    ap.add_argument("--na-dzien", type=int, default=1, help="ile tekstów jednego dnia (hub nie liczy się do limitu)")
    ap.add_argument("--kolejnosc", default="", help="kolejność klastrów: slugi hubów po przecinku")
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--zapisz", action="store_true")
    ap.add_argument("--zatwierdz", action="store_true", help="ustaw draft: false w zaplanowanych plikach")
    ap.add_argument("--caly-klaster", action="store_true", help="hub i wszystkie teksty klastra jednego dnia")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today)
    days = {DNI[d.strip()] for d in a.dni.split(",") if d.strip()}

    docs = []
    for f in sorted(Path(a.katalog).rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        m, _ = fm.parse(text)
        pub = as_date(m.get("publishedAt"))
        published = m.get("draft") is False and pub and pub <= today
        if published:
            continue  # już na stronie: nie ruszamy
        docs.append({"file": f, "text": text, "m": m, "slug": str(m.get("slug") or f.stem)})
    if not docs:
        print("Brak tekstów do zaplanowania.")
        return 0

    hubs = {"/poradniki/" + d["slug"] + "/": d for d in docs if d["m"].get("type") == "hub"}
    clusters = OrderedDict()
    for d in docs:
        if d["m"].get("type") == "hub":
            continue
        clusters.setdefault(str(d["m"].get("hub") or ""), []).append(d)
    order = [f"/poradniki/{s.strip()}/" for s in a.kolejnosc.split(",") if s.strip()]
    keys = sorted(clusters, key=lambda k: (order.index(k) if k in order else len(order), -len(clusters[k])))

    # Jednostka publikacji: lista tekstów, które wychodzą tego samego dnia.
    units = []
    for k in keys:
        items = clusters[k]
        hub = [hubs[k]] if k in hubs else []
        if a.caly_klaster:
            units.append(hub + items)
        else:
            units.append(hub + items[:1])  # hub razem z pierwszym tekstem klastra
            units += [[d] for d in items[1:]]
    per_day = 1 if a.caly_klaster else a.na_dzien

    day = max(dt.date.fromisoformat(a.start), today)
    plan, used = [], 0
    for unit in units:
        while day.weekday() not in days or used >= per_day:
            day += dt.timedelta(days=1)
            used = 0
        plan += [(day, d) for d in unit]
        used += 1

    print("data       | dzień | slug | klaster | uwagi")
    for day_, d in plan:
        ver = as_date(d["m"].get("verifiedAt"))
        note = "sprawdź fakty ponownie (>60 dni od weryfikacji)" if ver and (day_ - ver).days > 60 else ""
        print(f"{day_} | {list(DNI)[day_.weekday()]:>5} | {d['slug']} | {d['m'].get('hub') or 'hub'} | {note}")
        if a.zapisz:
            t = set_field(d["text"], "publishedAt", day_.isoformat())
            t = set_field(t, "updatedAt", day_.isoformat())
            if a.zatwierdz:
                t = set_field(t, "draft", "false")
            d["file"].write_text(t, encoding="utf-8")
    print(f"\n{len(plan)} pozycji, od {plan[0][0]} do {plan[-1][0]}." + ("" if a.zapisz else " Podgląd: dodaj --zapisz, żeby zapisać daty."))
    return 0


if __name__ == "__main__":
    sys.exit(main())

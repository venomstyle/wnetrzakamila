"""Minimalny parser frontmattera YAML (podzbiór używany w szablonie skilla).

Obsługuje: skalary, listy inline [a, b], listy blokowe skalarów, listy blokowe
słowników (- q: ...\n    a: ...), zagnieżdżone słowniki (cover:). Jeśli jest
PyYAML, używa go zamiast tego parsera.
"""
import re


def _scalar(v):
    v = v.strip()
    if v == "" or v in ("~", "null"):
        return None
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x) for x in re.split(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)", inner)]
    if v in ("true", "false"):
        return v == "true"
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


def _strip_comment(line):
    out, q = [], None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _parse_block(lines, i, indent):
    """Parsuje blok o danym wcięciu; zwraca (wartość, następny indeks)."""
    # lista?
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith("- "):
        items = []
        while i < len(lines):
            ln = lines[i]
            if not ln.strip():
                i += 1
                continue
            ind = len(ln) - len(ln.lstrip())
            if ind < indent or not ln.lstrip().startswith("- "):
                break
            body = ln.lstrip()[2:]
            if re.match(r"^[\w-]+:(\s|$)", body):
                # słownik w liście
                sub_indent = ind + 2
                fake = [" " * sub_indent + body]
                j = i + 1
                while j < len(lines):
                    l2 = lines[j]
                    if l2.strip() and (len(l2) - len(l2.lstrip())) < sub_indent:
                        break
                    fake.append(l2)
                    j += 1
                val, _ = _parse_block(fake, 0, sub_indent)
                items.append(val)
                i = j
            else:
                items.append(_scalar(body))
                i += 1
        return items, i
    d = {}
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        ind = len(ln) - len(ln.lstrip())
        if ind < indent:
            break
        m = re.match(r"^\s*([\w-]+):\s*(.*)$", ln)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2)
        if rest.strip() == "":
            # zagnieżdżony blok
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                nind = len(lines[j]) - len(lines[j].lstrip())
                if nind > ind or lines[j].lstrip().startswith("- "):
                    val, i = _parse_block(lines, j, nind)
                    d[key] = val
                    continue
            d[key] = None
            i += 1
        else:
            d[key] = _scalar(rest)
            i += 1
    return d, i


def parse(text):
    """Zwraca (frontmatter: dict, body: str)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw) or {}
        # daty z PyYAML -> str dla spójności
        def norm(x):
            if isinstance(x, dict):
                return {k: norm(v) for k, v in x.items()}
            if isinstance(x, list):
                return [norm(v) for v in x]
            if hasattr(x, "isoformat"):
                return x.isoformat()
            return x

        return norm(data), body
    except ImportError:
        pass
    lines = [_strip_comment(l) for l in raw.splitlines()]
    data, _ = _parse_block(lines, 0, 0)
    return data, body

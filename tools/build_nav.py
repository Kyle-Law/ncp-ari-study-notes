#!/usr/bin/env python3
"""Build nav.js and add it to every study-note page.

Run from anywhere after adding or moving notes:
    python3 tools/build_nav.py

Pages live in folders named <section>.<kind><n> (e.g. 1.T2, 2.SR15, 1.O1).
Section names come from the "## " headings in README.md, in order.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDER_RE = re.compile(r"^(\d+)\.(T|SR|O)(\d+)$")
KIND_ORDER = {"T": 0, "SR": 1, "O": 2}
KIND_NAME = {"T": "Exam topics", "SR": "Suggested readings", "O": "Other"}
TAG = '<script src="../nav.js" defer></script>'


def page_title(path):
    m = re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8"), re.S | re.I)
    return html.unescape(m.group(1).strip()) if m else path.stem


def section_names():
    heads = re.findall(r"^## (.+)$", (ROOT / "README.md").read_text(encoding="utf-8"), re.M)
    return {str(i): h.strip() for i, h in enumerate(heads, 1)}


def collect():
    pages = []
    for d in ROOT.iterdir():
        m = FOLDER_RE.match(d.name)
        if not (d.is_dir() and m):
            continue
        sec, kind, num = m.groups()
        for f in sorted(d.glob("*.html")):
            pages.append({
                "key": (int(sec), KIND_ORDER[kind], int(num), f.name),
                "path": f"{d.name}/{f.name}",
                "section": sec,
                "kind": kind,
                "code": f"{kind}{num}",
                "title": page_title(f),
            })
    pages.sort(key=lambda p: p["key"])
    for p in pages:
        del p["key"]
    return pages


def inject(path):
    text = path.read_text(encoding="utf-8")
    if "nav.js" in text:
        return False
    i = text.lower().rfind("</body>")
    text = text[:i] + TAG + "\n" + text[i:] if i != -1 else text + "\n" + TAG + "\n"
    path.write_text(text, encoding="utf-8")
    return True


def main():
    pages = collect()
    data = {"sections": section_names(), "kinds": KIND_NAME, "pages": pages}
    template = (ROOT / "tools" / "nav.template.js").read_text(encoding="utf-8")
    out = template.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, indent=1))
    (ROOT / "nav.js").write_text(out, encoding="utf-8")
    added = [p["path"] for p in pages if inject(ROOT / p["path"])]
    print(f"nav.js: {len(pages)} pages; added script tag to {len(added)} page(s)")
    for a in added:
        print("  +", a)


if __name__ == "__main__":
    main()

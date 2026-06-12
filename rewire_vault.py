"""Replace any lingering art.html/media-gallery references with the new vault.html
target. Handles deep anchors (art.html#wing-N) too."""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]

SUBS = [
    # art.html anchor-form → vault.html anchor-form
    (r'href="art\.html#wing-4"',     'href="vault.html#wing-4"'),
    (r'href="art\.html#wing-(\d+)"', r'href="vault.html#wing-\1"'),
    (r'href="art\.html"',            'href="vault.html"'),
    # media-gallery now lives in vault as Wing 8 (On Film)
    (r'href="story-media\.html#media-gallery"', 'href="vault.html#wing-8"'),
]

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    original = text
    for pat, repl in SUBS:
        text = re.sub(pat, repl, text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  patched: {name}")
    else:
        print(f"  no changes: {name}")

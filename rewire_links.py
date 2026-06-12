"""Rewire every link that pointed at the four deleted pages over to story-media.html
anchored sections. Also fix the nav-parent href and update "Media" label → "Media Gallery"
in nav and footer."""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "art.html", "about.html", "buy.html", "story-media.html"]

# Specific deep anchors must be substituted BEFORE the bare URL patterns.
URL_SUBS = [
    (r'href="characters\.html#world-shakers"',  'href="story-media.html#world-shakers"'),
    (r'href="characters\.html#voltaires"',      'href="story-media.html#voltaires"'),
    (r'href="characters\.html#monsters"',       'href="story-media.html#monsters"'),
    (r'href="characters\.html#supporting"',     'href="story-media.html#characters"'),
    (r'href="characters\.html"',                'href="story-media.html#characters"'),
    (r'href="issues\.html#(issue-\d+)"',        r'href="story-media.html#\1"'),
    (r'href="issues\.html"',                    'href="story-media.html#issues"'),
    (r'href="media\.html"',                     'href="story-media.html#media-gallery"'),
    (r'href="story\.html"',                     'href="story-media.html#story"'),
]

# The nav-parent dropdown link should point to the top of the page (no hash).
# rebuild_nav.py originally set it to story.html; URL_SUBS will have turned that into
# story-media.html#story; correct it back to plain story-media.html.
PARENT_FIX = (
    r'<a href="story-media\.html#story" class="nav-parent',
    '<a href="story-media.html" class="nav-parent'
)

# Rename "Media" label to "Media Gallery" in both nav submenu and footer Explore.
MEDIA_LABEL = (
    r'(href="story-media\.html#media-gallery">)Media(</a>)',
    r'\1Media Gallery\2'
)

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    original = text

    for pat, repl in URL_SUBS:
        text = re.sub(pat, repl, text)
    text = re.sub(PARENT_FIX[0], PARENT_FIX[1], text)
    text = re.sub(MEDIA_LABEL[0], MEDIA_LABEL[1], text)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  patched: {name}")
    else:
        print(f"  no changes: {name}")

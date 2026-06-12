"""Rebuild the navigation HTML on every page to the new flat structure:
    Home | Story & Media | The Vault | About | [Where to Buy CTA]

No more dropdown. Story & Media and The Vault are now direct top-level links.
Also rewrites the footer Explore list to match.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]

NAV_ITEMS = [
    ("index.html",       "Home"),
    ("story-media.html", "Story &amp; Media"),
    ("vault.html",       "The Vault"),
    ("about.html",       "About"),
]

def build_nav(page: str) -> str:
    items = []
    for href, label in NAV_ITEMS:
        active = ' class="active"' if href == page else ''
        items.append(f'        <li><a href="{href}"{active}>{label}</a></li>')
    nav_links = "\n".join(items)

    return (
        '<ul class="nav-links" id="primary-nav">\n'
        f'{nav_links}\n'
        '        <li class="nav-cta-wrap"><a href="buy.html" class="nav-cta">Where to Buy</a></li>\n'
        '      </ul>'
    )


def build_footer_explore() -> str:
    return (
        '<h4>Explore</h4>\n'
        '        <a href="buy.html">Where to Buy</a>\n'
        '        <a href="story-media.html#story">The Story</a>\n'
        '        <a href="story-media.html#characters">Characters</a>\n'
        '        <a href="story-media.html#issues">Issues</a>\n'
        '        <a href="vault.html">The Vault</a>\n'
        '        <a href="about.html">About</a>\n'
        '      </div>'
    )


nav_re = re.compile(r'<ul class="nav-links" id="primary-nav">[\s\S]*?</ul>')
footer_re = re.compile(r'<h4>Explore</h4>[\s\S]*?</div>')

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    new_nav = build_nav(name)
    text, n = nav_re.subn(new_nav, text, count=1)
    text, f = footer_re.subn(build_footer_explore(), text, count=1)
    path.write_text(text, encoding="utf-8")
    print(f"  {name}: nav={n} footer={f}")

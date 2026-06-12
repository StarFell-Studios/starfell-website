"""Rebuild the <ul class="nav-links"> nav block on every page.

New structure: Home | Story & Media (dropdown) | About | Where to Buy (CTA)
"Story & Media" parent links to story.html and opens a hover dropdown listing
the five creative pages (Story, Characters, Issues, Museum, Media).
The parent gets .active when on any of those five pages.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story.html", "characters.html", "issues.html",
         "media.html", "art.html", "about.html", "buy.html"]

SUB_PAGES = {"story.html", "characters.html", "issues.html", "art.html", "media.html"}

def build_nav(page: str) -> str:
    home_active   = ' class="active"' if page == "index.html" else ''
    about_active  = ' class="active"' if page == "about.html"  else ''
    parent_active = ' active' if page in SUB_PAGES else ''

    def sub(href, label):
        active = ' class="active"' if page == href else ''
        return f'            <li><a href="{href}"{active}>{label}</a></li>'

    submenu = "\n".join([
        sub("story.html",      "The Story"),
        sub("characters.html", "Characters"),
        sub("issues.html",     "Issues"),
        sub("art.html",        "Museum"),
        sub("media.html",      "Media"),
    ])

    return (
        '<ul class="nav-links" id="primary-nav">\n'
        f'        <li><a href="index.html"{home_active}>Home</a></li>\n'
        '        <li class="nav-has-submenu">\n'
        f'          <a href="story.html" class="nav-parent{parent_active}" aria-haspopup="true">Story &amp; Media <span class="nav-caret" aria-hidden="true">▾</span></a>\n'
        '          <ul class="nav-submenu" role="menu">\n'
        f'{submenu}\n'
        '          </ul>\n'
        '        </li>\n'
        f'        <li><a href="about.html"{about_active}>About</a></li>\n'
        '        <li class="nav-cta-wrap"><a href="buy.html" class="nav-cta">Where to Buy</a></li>\n'
        '      </ul>'
    )


nav_re = re.compile(r'<ul class="nav-links" id="primary-nav">[\s\S]*?</ul>')

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    new_nav = build_nav(name)
    new_text, count = nav_re.subn(new_nav, text, count=1)
    path.write_text(new_text, encoding="utf-8")
    print(f"  {name}: nav blocks replaced = {count}")

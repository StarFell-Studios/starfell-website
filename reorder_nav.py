"""Reorder nav and footer Explore lists on all pages.

New order: Home, Where to Buy, The Story, Characters, Issues, Media, About.
Footer Explore omits Home (matches existing convention).
The .active class is preserved on whichever link matches the current page.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")

PAGES = ["index.html", "story.html", "characters.html", "issues.html",
         "media.html", "about.html", "buy.html"]

NAV_ORDER = [
    ("index.html",      "Home"),
    ("buy.html",        "Where to Buy"),
    ("story.html",      "The Story"),
    ("characters.html", "Characters"),
    ("issues.html",     "Issues"),
    ("media.html",      "Media"),
    ("about.html",      "About"),
]

# Footer Explore drops Home
FOOTER_ORDER = [(h, l) for (h, l) in NAV_ORDER if h != "index.html"]

nav_re = re.compile(
    r'(<ul class="nav-links" id="primary-nav">\s*\n)(.*?)(\s*</ul>)',
    re.DOTALL
)
footer_re = re.compile(
    r'(<h4>Explore</h4>\s*\n)(.*?)(\s*</div>)',
    re.DOTALL
)

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")

    # ---- Nav block ----
    nav_items = []
    for href, label in NAV_ORDER:
        active = ' class="active"' if href == name else ''
        nav_items.append(f'        <li><a href="{href}"{active}>{label}</a></li>')
    new_nav = "\n".join(nav_items)
    text, ncount = nav_re.subn(lambda m: f"{m.group(1)}{new_nav}\n{m.group(3).lstrip()}", text)
    # subn's lambda inserts a leading 8-space indent already in new_nav lines

    # The replacement above strips the closing-tag's leading whitespace; restore proper indent
    # by patching the literal closing-tag indentation
    text = text.replace("</ul>", "      </ul>", 1) if "      </ul>" not in text else text

    # ---- Footer Explore block (replace_all since it appears once per page) ----
    explore_items = [f'        <a href="{href}">{label}</a>' for (href, label) in FOOTER_ORDER]
    new_explore = "\n".join(explore_items)
    text, fcount = footer_re.subn(lambda m: f"{m.group(1)}{new_explore}\n      </div>", text, count=1)

    path.write_text(text, encoding="utf-8")
    print(f"  {name}: nav={ncount} footer={fcount}")

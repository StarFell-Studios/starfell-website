"""Remove the Facebook social icon from nav-social and the Facebook link from
the footer Follow section on every page. The href was https://www.facebook.com/
with no actual page — a broken link. Re-add later if a real URL is provided."""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story.html", "characters.html", "issues.html",
         "media.html", "art.html", "about.html", "buy.html"]

# Match the entire Facebook anchor in the nav-social row.
# The anchor contains aria-label="Facebook" and the FB SVG path.
nav_fb_re = re.compile(
    r'\s*<a\s+href="https://www\.facebook\.com/"[^>]*aria-label="Facebook"[^>]*>.*?</a>',
    re.DOTALL
)

# Match the Facebook line in the footer Follow column.
footer_fb_re = re.compile(
    r'\s*<a\s+href="https://www\.facebook\.com/"[^>]*>\s*Facebook\s*</a>',
)

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    original = text

    text, nav_count    = nav_fb_re.subn("", text, count=1)
    text, footer_count = footer_fb_re.subn("", text, count=1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  {name}: nav-icon={nav_count}, footer-link={footer_count}")
    else:
        print(f"  {name}: no Facebook references found")

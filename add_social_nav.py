"""Replace the <nav class="site-nav">...</nav> block on every page with a new
version that includes inline SVG social icons (Instagram, Facebook, YouTube).
Also adds a YouTube link to the footer's "Follow" section."""

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

INSTAGRAM_SVG = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.31-1.46.72-2.13 1.38C1.35 2.68.94 3.35.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.31.79.72 1.46 1.38 2.13.67.66 1.34 1.07 2.13 1.38.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.31 1.46-.72 2.13-1.38.66-.67 1.07-1.34 1.38-2.13.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.31-.79-.72-1.46-1.38-2.13C21.32 1.35 20.65.94 19.86.63 19.1.33 18.22.13 16.95.07 15.67.01 15.26 0 12 0zm0 5.84A6.16 6.16 0 0 0 5.84 12 6.16 6.16 0 0 0 12 18.16 6.16 6.16 0 0 0 18.16 12 6.16 6.16 0 0 0 12 5.84zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.41-11.85a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88z"/>'
    '</svg>'
)

FACEBOOK_SVG = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.69.24 2.69.24v2.97h-1.52c-1.49 0-1.96.93-1.96 1.89v2.26h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07z"/>'
    '</svg>'
)

YOUTUBE_SVG = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M23.5 6.2a3.02 3.02 0 0 0-2.13-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.51A3.02 3.02 0 0 0 .5 6.2C0 8.07 0 12 0 12s0 3.93.5 5.8c.27 1.03 1.08 1.84 2.12 2.14 1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14c.5-1.87.5-5.8.5-5.8s0-3.93-.5-5.8zM9.55 15.59V8.41l6.34 3.59-6.34 3.59z"/>'
    '</svg>'
)


def build_nav(active_page: str) -> str:
    li_lines = []
    for href, label in NAV_ORDER:
        active = ' class="active"' if href == active_page else ''
        li_lines.append(f'        <li><a href="{href}"{active}>{label}</a></li>')
    li_html = "\n".join(li_lines)

    return f"""<nav class="site-nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo" aria-label="StarFell home">
        <img src="assets/logos/StarFell_retro_logo.webp" alt="StarFell">
      </a>
      <ul class="nav-links" id="primary-nav">
{li_html}
      </ul>
      <div class="nav-social" aria-label="StarFell on social media">
        <a href="https://www.instagram.com/starfell_studios/" target="_blank" rel="noopener" aria-label="Instagram">{INSTAGRAM_SVG}</a>
        <a href="https://www.facebook.com/" target="_blank" rel="noopener" aria-label="Facebook">{FACEBOOK_SVG}</a>
        <a href="https://www.youtube.com/@starfellstudios597" target="_blank" rel="noopener" aria-label="YouTube">{YOUTUBE_SVG}</a>
      </div>
      <button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    </div>
  </nav>"""


nav_re = re.compile(r'<nav class="site-nav">[\s\S]*?</nav>')

# Footer "Follow" section: add YouTube link if missing
footer_follow_re = re.compile(
    r'(<h4>Follow</h4>\s*\n\s*<a href="https://www\.instagram\.com/starfell_studios/"[^>]*>Instagram — @starfell_studios</a>\s*\n\s*<a href="https://www\.facebook\.com/"[^>]*>Facebook</a>)',
)
youtube_footer_link = '\n        <a href="https://www.youtube.com/@starfellstudios597" target="_blank" rel="noopener">YouTube — @starfellstudios597</a>'

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")

    new_nav = build_nav(name)
    text, ncount = nav_re.subn(new_nav, text, count=1)

    # Insert YouTube link in footer if not already there
    if "@starfellstudios597" not in text or text.count("@starfellstudios597") < 2:
        text, fcount = footer_follow_re.subn(lambda m: m.group(1) + youtube_footer_link, text, count=1)
    else:
        fcount = 0

    path.write_text(text, encoding="utf-8")
    print(f"  {name}: nav={ncount} footer-youtube-added={fcount}")

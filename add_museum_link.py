"""Insert Museum nav link (and footer Explore link) between Issues and Media
on every existing page (art.html already has it)."""

from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story.html", "characters.html", "issues.html",
         "media.html", "about.html", "buy.html"]

nav_before  = '        <li><a href="issues.html">Issues</a></li>\n        <li><a href="media.html">Media</a></li>'
nav_after   = '        <li><a href="issues.html">Issues</a></li>\n        <li><a href="art.html">Museum</a></li>\n        <li><a href="media.html">Media</a></li>'
nav_active_before = '        <li><a href="issues.html" class="active">Issues</a></li>\n        <li><a href="media.html">Media</a></li>'
nav_active_after  = '        <li><a href="issues.html" class="active">Issues</a></li>\n        <li><a href="art.html">Museum</a></li>\n        <li><a href="media.html">Media</a></li>'
nav_media_active_before = '        <li><a href="issues.html">Issues</a></li>\n        <li><a href="media.html" class="active">Media</a></li>'
nav_media_active_after  = '        <li><a href="issues.html">Issues</a></li>\n        <li><a href="art.html">Museum</a></li>\n        <li><a href="media.html" class="active">Media</a></li>'

footer_before = '        <a href="issues.html">Issues</a>\n        <a href="media.html">Media</a>'
footer_after  = '        <a href="issues.html">Issues</a>\n        <a href="art.html">Museum</a>\n        <a href="media.html">Media</a>'

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    if "art.html" in text and 'href="art.html">Museum</a>' in text:
        print(f"  skip (already linked): {name}")
        continue

    original = text
    # Try each nav variant (Issues active, Media active, neither active)
    for before, after in [(nav_active_before, nav_active_after),
                          (nav_media_active_before, nav_media_active_after),
                          (nav_before, nav_after)]:
        if before in text:
            text = text.replace(before, after, 1)
            break

    # Footer Explore
    if footer_before in text:
        text = text.replace(footer_before, footer_after, 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  patched: {name}")
    else:
        print(f"  NO MATCH: {name}")

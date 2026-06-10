"""Re-indent the closing </ul> tag of the nav list to 6 spaces on every page."""

from pathlib import Path
import re

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")

pattern = re.compile(
    r'(<ul class="nav-links" id="primary-nav">.*?</li>)\s*\n[ \t]*</ul>',
    re.DOTALL,
)

for p in DOCS.glob("*.html"):
    text = p.read_text(encoding="utf-8")
    new_text = pattern.sub(lambda m: m.group(1) + "\n      </ul>", text, count=1)
    if new_text != text:
        p.write_text(new_text, encoding="utf-8")
        print(f"  fixed: {p.name}")
    else:
        print(f"  clean: {p.name}")

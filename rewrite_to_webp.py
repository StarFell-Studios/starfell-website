"""Rewrite every assets/*.png|jpg|jpeg reference in HTML/CSS/MD to assets/*.webp.

We only touch paths under 'assets/' so unrelated mentions of png/jpg are untouched.
URL-encoded variants (spaces in filenames -> %20) are handled by the regex.
"""

import re
from pathlib import Path

ROOT = Path(r"D:\Projects\StarFell_website\StarFell Website")

# Files to rewrite
TARGETS = [
    ROOT / "docs" / "index.html",
    ROOT / "docs" / "story.html",
    ROOT / "docs" / "characters.html",
    ROOT / "docs" / "issues.html",
    ROOT / "docs" / "media.html",
    ROOT / "docs" / "about.html",
    ROOT / "docs" / "buy.html",
    ROOT / "docs" / "css" / "styles.css",
    ROOT / "README.md",
]

# Match `assets/<anything>.<ext>` where ext is png/jpg/jpeg, case-insensitive.
# Allow URL-encoded spaces (%20), spaces, and other path chars.
pattern = re.compile(r"(assets/[^'\")\s]+?)\.(png|jpg|jpeg)\b", re.IGNORECASE)

def to_webp(match):
    return match.group(1) + ".webp"

total_changes = 0
for path in TARGETS:
    if not path.exists():
        print(f"  skip (missing): {path}")
        continue
    text = path.read_text(encoding="utf-8")
    new_text, n = pattern.subn(to_webp, text)
    if n > 0:
        path.write_text(new_text, encoding="utf-8")
    print(f"  {n:3d} replacements in {path.relative_to(ROOT).as_posix()}")
    total_changes += n

print(f"\nTotal replacements: {total_changes}")

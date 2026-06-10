"""Reverse the cp1252-as-utf8 mojibake introduced by PowerShell Set-Content -Encoding utf8.

When you read UTF-8 bytes as cp1252 and then re-save as UTF-8, every multi-byte
UTF-8 character ends up as a sequence of cp1252 mojibake characters. To undo:
  1. Read the corrupted file as UTF-8
  2. Encode the resulting string as cp1252 (recovers the original bytes)
  3. Decode those bytes as UTF-8 (restores the original characters)
Then write back as UTF-8 WITHOUT a BOM (which the PowerShell save also added).
"""

from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story.html", "characters.html", "issues.html",
         "media.html", "about.html", "buy.html"]

# Telltale mojibake substrings to detect corruption before fixing.
TELLTALES = ("â€",  "Â·", "â˜", "â†")

for name in PAGES:
    path = DOCS / name
    raw = path.read_bytes()

    # Strip UTF-8 BOM if present
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]

    text = raw.decode("utf-8", errors="strict")

    if not any(t in text for t in TELLTALES):
        print(f"  clean: {name}")
        continue

    # Reverse the corruption
    fixed = text.encode("cp1252", errors="replace").decode("utf-8", errors="replace")

    path.write_bytes(fixed.encode("utf-8"))  # No BOM
    print(f"  fixed: {name}  ({len(text)} -> {len(fixed)} chars)")

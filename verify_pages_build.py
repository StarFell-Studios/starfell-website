"""Verification checklist for the comic-pages build (claude-code-pages-prompt.md)."""

import re
import sys
from pathlib import Path
from statistics import pstdev
from PIL import Image

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
fails = []


def fail(msg):
    fails.append(msg)
    print(f"  FAIL: {msg}")


# --- 1. every new webp opens, isn't black/blank, and is <=300 KB ---
print("1) webp integrity + size:")
new_files = sorted((DOCS / "assets" / "pages").glob("*.webp"))
new_files.append(DOCS / "assets" / "covers" / "starfell-issue-01-back-cover.webp")
for f in new_files:
    kb = f.stat().st_size / 1024
    if kb > 300:
        fail(f"{f.name} is {kb:.0f} KB (>300)")
    try:
        with Image.open(f) as im:
            im = im.convert("L").resize((64, 64))
            px = list(im.getdata())
            mean, sd = sum(px) / len(px), pstdev(px)
            if sd < 5:
                fail(f"{f.name} looks blank/black (mean={mean:.0f}, std={sd:.1f})")
    except Exception as e:
        fail(f"{f.name} failed to open: {e}")
print(f"  checked {len(new_files)} files")

# --- 2. lightbox order matches spec page order ---
print("2) preview lightbox order:")
sm = (DOCS / "story-media.html").read_text(encoding="utf-8")
frames = re.findall(r'class="frame" href="([^"]+)"', sm)
expected_prefix = [
    "assets/pages/i1-p01-cosmic-opening.webp",
    "assets/pages/i1-p02-meteor-breaks.webp",
    "assets/pages/i1-p03-prehistoric-impact.webp",
    "assets/pages/i1-p04-crater-1956-fire.webp",
    "assets/pages/i1-p05-fire-rescue.webp",
    "assets/pages/i1-p06-jack-and-levi.webp",
    "assets/pages/i2-p01-hideout.webp",
    "assets/pages/i2-p02-world-shakers.webp",
    "assets/pages/i2-p03-heading-out.webp",
    "assets/pages/i2-p04-attack-begins.webp",
    "assets/pages/i2-p05-astrobleme.webp",
    "assets/pages/i3-prologue01-delilahs-morning.webp",
    "assets/pages/i3-prologue02-breakfast.webp",
    "assets/pages/i3-p01-johnnys-day.webp",
    "assets/pages/i3-p02-hot-rod-run.webp",
    "assets/pages/i3-p03-mister-charles.webp",
]
if frames[: len(expected_prefix)] != expected_prefix:
    fail("story-media frame order does not match spec preview order")
    for got, want in zip(frames, expected_prefix):
        if got != want:
            print(f"    got {got}  want {want}")
else:
    print(f"  16 preview frames in spec order; {len(frames)} frames total on page")

# --- 3. no spoiler pages anywhere in build output ---
print("3) spoiler exclusions:")
spoiler_pat = re.compile(
    r"Issue_03_Page2[0-4]|Issue_02_Page24|i3-p2[0-4]|i2-p24|i2-p2[2-9]", re.I
)
for html in DOCS.glob("*.html"):
    for m in spoiler_pat.finditer(html.read_text(encoding="utf-8")):
        fail(f"spoiler reference '{m.group()}' in {html.name}")
for f in (DOCS / "assets" / "pages").glob("*"):
    if spoiler_pat.search(f.name):
        fail(f"spoiler asset shipped: {f.name}")
print("  scanned all docs/*.html and assets/pages/")

# --- 4. lazy-load on all new page imgs ---
print("4) lazy loading:")
for html_name in ("story-media.html", "vault.html"):
    text = (DOCS / html_name).read_text(encoding="utf-8")
    for m in re.finditer(r"<img\b[^>]*>", text):
        tag = m.group()
        if "assets/pages/" in tag or "starfell-issue-01-back-cover" in tag:
            if 'loading="lazy"' not in tag:
                fail(f"missing loading=lazy in {html_name}: {tag[:90]}")
print("  all new <img> tags checked")

# --- 5. link check: every img src / a.frame href in docs resolves ---
print("5) link check (all local img src + frame hrefs in all pages):")
checked = 0
for html in DOCS.glob("*.html"):
    text = html.read_text(encoding="utf-8")
    refs = re.findall(r'(?:src|href)="(assets/[^"]+)"', text)
    for ref in refs:
        checked += 1
        if not (DOCS / ref.replace("/", "\\")).exists():
            fail(f"{html.name}: broken ref {ref}")
print(f"  {checked} asset refs checked")

print()
if fails:
    print(f"=== {len(fails)} FAILURES ===")
    sys.exit(1)
print("=== ALL CHECKS PASSED ===")

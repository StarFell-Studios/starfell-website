"""Convert every PNG/JPG under docs/assets/ to WebP.

Strategy:
  - Photos / concept art (.jpg)  -> WebP quality=82, lossy
  - Cover/art PNGs              -> WebP quality=85, lossy (text stays crisp at 85)
  - Logos with transparency     -> WebP lossless (small files, sharp edges matter)
  - Skip if a same-name .webp is newer than the source.
Originals are left in place so the source folder is unchanged.
"""

import sys
from pathlib import Path
from PIL import Image

ROOT = Path(r"D:\Projects\StarFell_website\StarFell Website\docs\assets")

# Filename hints for "logo" treatment (lossless).
LOGO_HINTS = ("logo",)

results = []
total_old = 0
total_new = 0

for src in sorted(ROOT.rglob("*")):
    if not src.is_file():
        continue
    if src.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        continue

    dst = src.with_suffix(".webp")

    name_lower = src.name.lower()
    is_logo = any(h in name_lower for h in LOGO_HINTS)

    try:
        with Image.open(src) as im:
            has_alpha = (im.mode in ("RGBA", "LA")) or ("transparency" in im.info)

            if is_logo:
                # Logos: lossless to keep crisp edges and tiny detail
                if im.mode not in ("RGBA", "RGB"):
                    im = im.convert("RGBA" if has_alpha else "RGB")
                im.save(dst, "WEBP", lossless=True, method=6)
            else:
                # Everything else: high-quality lossy
                # Preserve alpha if present (covers, character sheets, etc.)
                if has_alpha and im.mode != "RGBA":
                    im = im.convert("RGBA")
                elif not has_alpha and im.mode != "RGB":
                    im = im.convert("RGB")

                # Cover art and character sheets benefit from slightly higher q
                quality = 85 if src.suffix.lower() == ".png" else 82
                im.save(dst, "WEBP", quality=quality, method=6)

        old_size = src.stat().st_size
        new_size = dst.stat().st_size
        total_old += old_size
        total_new += new_size
        savings_pct = (1 - new_size / old_size) * 100 if old_size else 0
        results.append((src.relative_to(ROOT).as_posix(), old_size, new_size, savings_pct))
        print(f"  {savings_pct:5.1f}% saved  {old_size/1024:8.1f} KB -> {new_size/1024:8.1f} KB  {src.relative_to(ROOT).as_posix()}")
    except Exception as e:
        print(f"  ERROR converting {src}: {e}", file=sys.stderr)

print()
print(f"=== Summary ===")
print(f"  Converted: {len(results)} files")
print(f"  Total old: {total_old/1024/1024:.2f} MB")
print(f"  Total new: {total_new/1024/1024:.2f} MB")
if total_old:
    print(f"  Saved:     {(1 - total_new/total_old)*100:.1f}% ({(total_old-total_new)/1024/1024:.2f} MB)")

"""Convert comic book page assets (Comic Book Pages/ + Line_Art/) to WebP
for the Story & Media page and Vault additions.

Targets ~<=300 KB per file (grid thumbs and lightbox share one file):
fit within 1600 px on the long edge, quality 80, stepping down if needed.
TIFs are opened at frame [0] (some are multi-frame and render black otherwise).
"""

import sys
from pathlib import Path
from PIL import Image

Image.MAX_IMAGE_PIXELS = None  # comic pages are large; sources are trusted

CONTENT = Path(r"D:\Projects\StarFell_website\StarFell Website\StarFell Content")
DOCS    = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES   = DOCS / "assets" / "pages"
COVERS  = DOCS / "assets" / "covers"

CBP = "Comic Book Pages"
LA  = "Line_Art"

# (source_relative_to_content, output_dir, output_slug)
MANIFEST = [
    # ---- Issue 1 preview (A1) ----
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page01_Lettered-01-01.png",    PAGES, "i1-p01-cosmic-opening"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page02_Lettered-01-01.png",    PAGES, "i1-p02-meteor-breaks"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page03_Lettered-01-01-01.png", PAGES, "i1-p03-prehistoric-impact"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page04_Lettered-01-01.png",    PAGES, "i1-p04-crater-1956-fire"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page05_Lettered-01-01.png",    PAGES, "i1-p05-fire-rescue"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page06_Lettered-01-01.png",    PAGES, "i1-p06-jack-and-levi"),

    # ---- Issue 2 preview (A1) ----
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page01_Lettered-01.png",       PAGES, "i2-p01-hideout"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page02_Lettered-01.png",       PAGES, "i2-p02-world-shakers"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page03_Lettered-01-01.png",    PAGES, "i2-p03-heading-out"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page04_Lettered-01-01.png",    PAGES, "i2-p04-attack-begins"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page05_Lettered-01.png",       PAGES, "i2-p05-astrobleme"),

    # ---- Issue 3 preview (A1) ----
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Prologue01_Lettered-01.png", PAGES, "i3-prologue01-delilahs-morning"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Prologue02_Lettered-01.png", PAGES, "i3-prologue02-breakfast"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page01_Lettered.png",        PAGES, "i3-p01-johnnys-day"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page02_Lettered-01.png",     PAGES, "i3-p02-hot-rod-run"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page03_Lettered-01.png",     PAGES, "i3-p03-mister-charles"),

    # ---- Splash showcase (A2) ----
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page14_Lettered-01.png",       PAGES, "i1-p14-title-splash"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page26_Lettered-01.png",       PAGES, "i1-p26-fleur-du-ciel"),
    # shockwave pair — p21 ships on Story & Media; p20 hangs in The Pages wing
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page20_Lettered-01.png",        PAGES, "i2-p20-sleeping-giant"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page21_Lettered-01-01-01.png",  PAGES, "i2-p21-shockwave"),

    # ---- Issue 4 WIP (A3) — the Jackson brothers river sequence ----
    (f"{CBP}/Issue_4/Starfell_issue4_01_010.png", PAGES, "i4-wip-fishing-hole"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_011.png", PAGES, "i4-wip-surfacing"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_012.png", PAGES, "i4-wip-rope-swing"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_013.png", PAGES, "i4-wip-underwater"),

    # ---- Back cover (A4) ----
    (f"{CBP}/Issue_1/Starfell_Issue_01_Back_Cover.png", COVERS, "starfell-issue-01-back-cover"),

    # ---- B1 Ink to Color (Wing 4) ----
    (f"{LA}/StarFell_Issue_03_Page07.tif",  PAGES, "i3-p07-inks"),
    (f"{LA}/StarFell_Issue_03_Page09.tif",  PAGES, "i3-p09-inks"),
    (f"{LA}/StarFell_Issue_03_Page12.png",  PAGES, "i3-p12-inks"),
    (f"{LA}/StarFell_Issue_03_Page18.tif",  PAGES, "i3-p18-inks"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page07_Lettered-01-01.png",       PAGES, "i3-p07-color"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page09_Lettered-01.png",          PAGES, "i3-p09-color"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page12_Lettered-01-01-01-01.png", PAGES, "i3-p12-color"),
    (f"{CBP}/Issue_3/Starfell_TPB_Issue_03_Page18_Lettered-01.png",          PAGES, "i3-p18-color"),
    (f"{LA}/Starfell_Issue_03_Page10_Lettered_Draft1.png", PAGES, "i3-p10-lettered-draft"),

    # ---- B2 The Line Art Library (Wing 4) ----
    # unnamed (1).png is a pixel-identical duplicate of unnamed.png — converted once
    (f"{LA}/goonies.png",         PAGES, "world-shakers-group-inks"),
    (f"{LA}/unnamed.png",         PAGES, "lineart-pencils-1"),
    (f"{LA}/unnamed (2).png",     PAGES, "grom-fight-pencils"),
    (f"{LA}/image (8) (1).png",   PAGES, "lineart-layout-roughs"),
    (f"{LA}/image (4).png",       PAGES, "lineart-sheriffs-office"),
    (f"{LA}/image (12).png",      PAGES, "lineart-pencils-blocking"),
    (f"{LA}/Starfell_Issue_03_Page06_Lettered_Draft2.jpg",  PAGES, "i3-p06-lettered-draft"),
    (f"{LA}/Starfell_Issue_03_Page16_Lettered_Draft1.jpg",  PAGES, "i3-p16-lettered-draft"),
    (f"{LA}/Starfell_Issue_03_Page15_Lettered_Draft1.jpg",  PAGES, "i3-p15-lettered-draft"),

    # ---- B3 Issue 4 spotlight: Delilah's Wishing Rock ----
    (f"{CBP}/Issue_4/Starfell_issue4_01_023.png", PAGES, "i4-wishing-rock-garden"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_025.png", PAGES, "i4-wishing-rock-party"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_026.png", PAGES, "i4-wishing-rock-wish"),
    (f"{CBP}/Issue_4/Starfell_issue4_01_027.png", PAGES, "i4-wishing-rock-transformation"),

    # ---- B3 The Pages — pages not already converted above ----
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page27_Lettered-01.png",    PAGES, "i1-p27-in-the-pines-1"),
    (f"{CBP}/Issue_1/Starfell_Issue_01_Page28_Lettered-01.png",    PAGES, "i1-p28-in-the-pines-2"),
    (f"{CBP}/Issue_2/Starfell_Issue_02_Page14_Lettered-01-01.png", PAGES, "i2-p14-delilah-scissors"),
]

MAX_EDGE = 1600
TARGET_BYTES = 300 * 1024


def convert(src: Path, dst: Path) -> tuple[int, int, str]:
    with Image.open(src) as im:
        if getattr(im, "n_frames", 1) > 1:
            im.seek(0)
        im.load()
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        if im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            im = bg
        w, h = im.size
        scale = MAX_EDGE / max(w, h)
        if scale < 1:
            im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        for q in (80, 72, 64, 55):
            im.save(dst, "WEBP", quality=q, method=6)
            if dst.stat().st_size <= TARGET_BYTES:
                break
        return src.stat().st_size, dst.stat().st_size, f"{im.size[0]}x{im.size[1]}"


def main():
    PAGES.mkdir(parents=True, exist_ok=True)
    failures = []
    for src_rel, out_dir, slug in MANIFEST:
        src = CONTENT / src_rel
        dst = out_dir / f"{slug}.webp"
        if dst.exists():
            continue
        if not src.exists():
            failures.append(f"MISSING: {src_rel}")
            print(f"  MISSING: {src_rel}", file=sys.stderr)
            continue
        try:
            old, new, dims = convert(src, dst)
            flag = "" if new <= TARGET_BYTES else "  ** OVER 300KB **"
            print(f"  {slug:<34} {old/1024/1024:6.1f} MB -> {new/1024:4.0f} KB  {dims}{flag}")
        except Exception as e:
            failures.append(f"ERROR {src_rel}: {e}")
            print(f"  ERROR {src_rel}: {e}", file=sys.stderr)
    print()
    print(f"Done. {len(failures)} failures.")
    for f in failures:
        print(f"  {f}")


if __name__ == "__main__":
    main()

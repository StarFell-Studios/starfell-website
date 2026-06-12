"""Copy + convert all StarFell Museum (art.html) assets from StarFell Content/
to docs/assets/museum/wing{N}/ with clean slug filenames, converted to WebP.

Reads source paths from the manifest below. Each tuple is:
    (source_rel_path, wing_number, slug)

Already-on-site assets (covers, character sheets, environment finals) are
referenced by their existing docs/assets/ paths in art.html — not re-copied.
"""

import sys
from pathlib import Path
from PIL import Image

CONTENT = Path(r"D:\Projects\StarFell_website\StarFell Website\StarFell Content")
DOCS    = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
MUSEUM  = DOCS / "assets" / "museum"

# (source_relative_to_content, wing_number, output_slug)
MANIFEST = [
    # ============================================================
    # WING 1 — First Marks: Character Design
    # ============================================================

    # The Portrait Series (centerpiece row)
    ("Concept Art/Char/Levi/Attachment_1604844287.png",        1, "portrait-levi"),
    ("Concept Art/Final/Johnny.jpg",                            1, "portrait-johnny"),
    ("Concept Art/Char/Delilah/Delilah fix3.png",               1, "portrait-delilah"),
    ("Concept Art/Char/Aliester/Alistier.jpg",                  1, "portrait-alistair"),

    # Levi development
    ("Concept Art/Char/Levi/boy_sketch.jpg",                    1, "levi-pose-studies"),
    ("Concept Art/Char/Levi/Levi Levins.jpg",                   1, "levi-model-sheet"),
    ("Concept Art/Char/Levi/1 (1).jpg",                         1, "levi-grayscale"),
    ("Concept Art/Char/Levi/Boy on the stairs_.jpg",            1, "levi-on-stairs"),
    ("Concept Art/Final/levi_final.jpg",                        1, "levi-porch-final"),

    # Johnny development
    ("Concept Art/Char/Johnny/Johnny_v2.jpg",                   1, "johnny-jacket-study"),
    ("Concept Art/Char/Johnny/gunslinger small.png",            1, "johnny-gunslinger"),

    # Delilah development
    ("Concept Art/Char/Delilah/12.jpg",                         1, "delilah-scissors"),
    ("Concept Art/Char/Delilah/Attachment_1606246947.png",      1, "delilah-costume-sheet"),

    # Alistair development
    ("Concept Art/Char/Aliester/Attachment_1602_sketch.jpg",    1, "alistair-exploration"),
    ("Concept Art/Char/Aliester/18 (1).jpg",                    1, "alistair-wheelchair-study"),

    # Lina Jane development
    ("Concept Art/Char/Lina Jane/1.jpg",                        1, "lina-cloak-painting"),

    # ============================================================
    # WING 2 — The Bestiary
    # ============================================================
    ("Concept Art/ref/Baddies/monsters/Cat Fish/catfish monster.jpg",  2, "first-fat-lance"),
    ("Concept Art/ref/Baddies/monsters/Cat Fish/environment.jpg",       2, "monster-on-street-sketch"),

    # ============================================================
    # WING 3 — The Sky Falls
    # ============================================================
    ("Concept Art/ref/enviroment/crater_glowing.jpg",           3, "crater-glow-study"),
    ("Concept Art/Final/starfell_wip.jpg",                      3, "welcome-to-starfell-wip"),
    ("Concept Art/Final/starfell_logo.jpg",                     3, "logo-study"),

    # ============================================================
    # WING 4 — Pencils to Print
    # ============================================================

    # Alistair triptych
    ("misc images/alistair_1.png",                              4, "alistair-stage-pencils"),
    ("misc images/alistair_2.png",                              4, "alistair-stage-inks"),
    ("misc images/alistair_3.png",                              4, "alistair-stage-final"),

    # Cover process
    ("misc images/cover2.png",                                  4, "cover-stage-pencils"),
    ("misc images/cover4.png",                                  4, "cover-stage-inks"),
    ("misc images/cover1.png",                                  4, "cover-stage-color"),

    # Tree climb sequence
    ("misc images/tree_climb1.png",                             4, "tree-climb-1"),
    ("misc images/tree_climb2.png",                             4, "tree-climb-2"),
    ("misc images/tree_climb3.png",                             4, "tree-climb-3"),

    # Maitland & the mud-creature triptych
    ("misc images/maitland1.png",                               4, "maitland-mud-pencils"),
    ("misc images/maitland 2.png",                              4, "maitland-mud-inks"),
    ("misc images/maitland 3.png",                              4, "maitland-mud-final"),

    # Selected pencil pages + finished color
    ("misc images/day1.png",                                    4, "interior-day-1"),
    ("misc images/day3.png",                                    4, "interior-day-3"),
    ("misc images/day5.png",                                    4, "interior-day-finished"),

    # Issue 4 inks contact sheet
    ("misc images/issue_4_inks.png",                            4, "issue-4-inks-contact"),

    # ============================================================
    # WING 6 — Location Scouting
    # ============================================================
    ("Concept Art/ref/Characters/Levi Levins/levi house.jpg",   6, "scout-levi-house"),
    ("Concept Art/ref/Characters/Levi Levins/levi_street.jpg",  6, "scout-downtown-street"),
    ("Concept Art/ref/Characters/Levi Levins/levi_environment.jpg", 6, "scout-town"),
    ("Concept Art/ref/Characters/johnny/johnny_environment.jpg",6, "scout-old-calaboose"),

    # ============================================================
    # WING 7 — Beyond the Page (AI-assisted live-action concept)
    # ============================================================

    # Cast studies
    ("Live Action/Characters/Levi Levins.png",                  7, "la-levi"),
    ("Live Action/Characters/Johnny Gale.png",                  7, "la-johnny"),
    ("Live Action/Characters/Delilah.png",                      7, "la-delilah"),
    ("Live Action/Characters/Alistair Voltaire.png",            7, "la-alistair"),
    ("Live Action/Characters/Lilith_Voltaire.png",              7, "la-lilith"),
    ("Live Action/Characters/Miles Maitland.png",               7, "la-miles"),
    ("Live Action/Characters/Lina Jane.png",                    7, "la-lina"),
    ("Live Action/Characters/Kristy Leigh.png",                 7, "la-kristy"),
    ("Live Action/Characters/Dash Jackson.png",                 7, "la-dash"),
    ("Live Action/Characters/Lucas Jackson.png",                7, "la-lucas"),
    ("Live Action/Characters/Horace.png",                       7, "la-horace"),
    ("Live Action/Characters/Levi_mask.png",                    7, "la-levi-mask"),

    # Shot images
    ("Live Action/Shot Images/Levi_on_bridge.png",              7, "shot-bridge-tentacles"),
    ("Live Action/Shot Images/levi_bike.png",                   7, "shot-levi-bike"),
    ("Live Action/Shot Images/Delilah_Gate.png",                7, "shot-delilah-gate"),
    ("Live Action/Shot Images/aliestar_hallway.png",            7, "shot-alistair-hallway"),
    ("Live Action/Shot Images/river_attack.png",                7, "shot-river-attack"),
    ("Live Action/Shot Images/dash_lucas_tentacles.png",        7, "shot-jackson-brothers"),
    ("Live Action/Shot Images/snail_shot.png",                  7, "shot-mutant-snail"),
    ("Live Action/Shot Images/Miles_plant.png",                 7, "shot-miles-specimen"),
    ("Live Action/Shot Images/lina_library.png",                7, "shot-lina-library"),
    ("Live Action/Shot Images/town_clean.png",                  7, "shot-town-clean"),
    ("Live Action/Shot Images/square.png",                      7, "shot-square"),
    ("Live Action/Shot Images/lucas_eyes.png",                  7, "shot-b-movie-frame"),
]


def convert_and_save(src: Path, dst: Path, quality: int = 82) -> tuple[int, int]:
    """Open src, save as WebP at given quality, return (old_bytes, new_bytes)."""
    with Image.open(src) as im:
        has_alpha = (im.mode in ("RGBA", "LA")) or ("transparency" in im.info)
        if has_alpha and im.mode != "RGBA":
            im = im.convert("RGBA")
        elif not has_alpha and im.mode != "RGB":
            im = im.convert("RGB")
        im.save(dst, "WEBP", quality=quality, method=6)
    return src.stat().st_size, dst.stat().st_size


def main():
    # Pre-create wing folders
    for n in range(1, 8):
        (MUSEUM / f"wing{n}").mkdir(parents=True, exist_ok=True)

    total_old = 0
    total_new = 0
    missing = []
    converted = 0

    for src_rel, wing, slug in MANIFEST:
        src = CONTENT / src_rel
        dst = MUSEUM / f"wing{wing}" / f"{slug}.webp"

        if not src.exists():
            missing.append(src_rel)
            print(f"  MISSING: {src_rel}", file=sys.stderr)
            continue

        try:
            old, new = convert_and_save(src, dst)
            total_old += old
            total_new += new
            converted += 1
            savings = (1 - new / old) * 100 if old else 0
            print(f"  w{wing}/{slug:<30}  {old/1024:7.0f} KB -> {new/1024:6.0f} KB  ({savings:4.1f}%)")
        except Exception as e:
            print(f"  ERROR  {src_rel}: {e}", file=sys.stderr)

    print()
    print(f"=== Summary ===")
    print(f"  Converted: {converted} files")
    if missing:
        print(f"  Missing:   {len(missing)} (paths below)")
        for m in missing:
            print(f"             - {m}")
    print(f"  Total old: {total_old/1024/1024:.2f} MB")
    print(f"  Total new: {total_new/1024/1024:.2f} MB")
    if total_old:
        print(f"  Saved:     {(1 - total_new/total_old)*100:.1f}%")


if __name__ == "__main__":
    main()

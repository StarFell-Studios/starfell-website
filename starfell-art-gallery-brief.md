# StarFell Art Section — "The StarFell Museum" Creative Brief

**For:** Claude Code — new Art section on the existing StarFell site
**Concept:** A curated museum of everything it took to make StarFell — from first pencil sketch to printed page to live-action dream. Every image reviewed and identified; all paths verified against `StarFell Content/`.
**Curation rules agreed with Mike:** In-house reference material only (no scraped third-party movie stills/photos — the bulk of `Concept Art/ref/` stays internal). Live-action AI development imagery IS included, as its own clearly-labeled wing.

---

## Museum Concept & Layout

One page (`art.html` or `/museum/`) organized as **seven wings**, each a scrollable "room" with a wing title, 1–2 sentence wall text, and a masonry/grid of framed pieces. Every piece gets a **museum placard**: title, medium ("Digital pencils", "Character turnaround", "Concept painting"), and a one-line caption. Click → full-screen lightbox with placard text. Sticky side-nav or top filter chips to jump between wings.

Style: gallery-dark walls (deep night blue/near-black), thin cream "frames" around art, pink crystal glow on hover, halftone/paper texture in wing headers. Period museum typography ("EST. 1962" energy).

**Build notes:**
- Generate web derivatives: ≤300 KB WebP thumbnails, ≤1.5 MB lightbox versions. Never ship the multi-MB originals.
- Rename files to clean slugs on copy (e.g., `alistair-pencils.webp`) — several sources have spaces, parens, or AI-tool gibberish names.
- Exclude all `Thumbs.db` and all `.psd` files.
- All paths below are relative to `StarFell Content/`.

---

## Wing 1 — First Marks: Character Design

*Wall text: "Every hero starts as a scribble. The cast of StarFell evolved through sketches, grayscale paintings, and turnaround sheets before ever facing a monster."*

Organize by character, sketch → final reading order:

**Levi Levins**
- `Concept Art/Char/Levi/boy_sketch.jpg` — grayscale pose studies with the BB gun (digital sketch)
- `Concept Art/Char/Levi/IMG_20201107_062737_805.jpg` — early pencil sketch
- `Concept Art/Char/Levi/Levi Levins.jpg`, `Levi Levins.png`, `Levi_Levins.jpg` — turnaround/expression model sheets (pick the cleanest two)
- `Concept Art/Char/Levi/Attachment_1604844287.png` — model sheet, red striped shirt
- `Concept Art/Char/Levi/1 (1).jpg` — grayscale full-figure painting, goggles & gun
- `Concept Art/Char/Levi/Boy on the stairs_.jpg` — color painting, Levi on the porch steps
- `Concept Art/Final/levi_final.jpg` — final porch piece
- `Character Sheets/Levi_Character_sheet.png` — finished production turnaround

**Johnny Gale**
- `Concept Art/Char/Johnny/Johnny_v2.jpg` — grayscale study, leather jacket
- `Concept Art/Final/Johnny_v3.png` — color full-figure, denim
- `Concept Art/Char/Johnny/gunslinger small.png` — "The Gunslinger," purple-lit painting with gun
- `Concept Art/Final/Johnny.jpg` — final purple-lit portrait
- `Character Sheets/Gemini_Generated_Image_lvex5vlvex5vlvex.png` — production turnaround (rename `johnny-turnaround`)

**Delilah Voltaire**
- `Concept Art/Char/Delilah/IMG_20201123_131741_054.jpg`, `IMG_20201123_131742_490.jpg` — first hair/face pencil studies
- `Concept Art/Char/Delilah/Attachment_1606246947.png`, `Attachment_1606246951.jpg`, `Attachment_1606246955.png` — costume & hair model sheets (purple vs. green dress iterations; pick two)
- `Concept Art/Char/Delilah/12.jpg` — grayscale painting, scissors in hand
- `Concept Art/Char/Delilah/Delilah fix3.png` — final purple-lit portrait, green dress
- `Character Sheets/Gemini_Generated_Image_qx12okqx12okqx12.png` — production turnaround (rename `delilah-turnaround`)

**Alistair Voltaire**
- `Concept Art/Char/Aliester/Attachment_1602_sketch.jpg` — sepia exploration sheet (faces, canes, wheelchair)
- `Concept Art/Char/Aliester/Attachment_1602506291.jpg` or `Attachment_1602506295.png` — color model sheet (pick one)
- `Concept Art/Char/Aliester/18 (1).jpg` — grayscale wheelchair painting
- `Concept Art/Char/Aliester/Aleister_.jpg` — dark portrait against the wallpaper
- `Concept Art/Char/Aliester/Alistier.jpg` — final purple-lit wheelchair portrait (StarFell logo signed)

**Lina Jane**
- `Concept Art/Char/Lina Jane/1.jpg` — grayscale painting, green hooded cloak (same piece as `Concept Art/Final/1.jpg`; use once)
- `Character Sheets/Gemini_Generated_Image_h3tf2xh3tf2xh3tf.png` — production turnaround, cloak & scrapbook (rename `lina-jane-turnaround`)

**The rest of the cast — production turnarounds (sub-grid):**
- `Character Sheets/Miles_character_sheet.png` — Miles Maitland
- `Character Sheets/Dash_char_sheet.jpg` — Dash Jackson
- `Character Sheets/Kristy_Leigh_character_sheet.jpg` — Kristy Leigh
- `Character Sheets/Sheriff_minor.png` — The Sheriff
- `Character Sheets/Gemini_Generated_Image_kzk68okzk68okzk6.png` — Dr. Maitland (rename `dr-maitland-turnaround`)

**Curator's note for placards:** the unified purple-lit portrait series (Levi `Concept Art/Char/Levi/Attachment_1604844287.png` companion piece, Johnny, Delilah, Alistair — all signed with the StarFell logo) should be presented together as "The Portrait Series" centerpiece row at the top of this wing.

---

## Wing 2 — The Bestiary: Monsters of StarFell

*Wall text: "The crystals don't create. They corrupt. Local wildlife, local legends — grown wrong."*

- `Concept Art/Final/CATFISH_CREATURE.jpg` — **Fat Lance**, the final boss. Full-width hero piece of the wing. Underwater concept painting.
- `Concept Art/Final/Mutant_snail.jpg` — the mutated Tulotoma snail, moody red concept painting.
- `Character Sheets/Gemini_Generated_Image_8p0ikt8p0ikt8p0i.jpg` — Mutant Snail turnaround sheet with human scale comparison (rename `mutant-snail-turnaround`). Placard: based on Wetumpka's real endangered Tulotoma snail.
- `Concept Art/ref/Baddies/monsters/Cat Fish/catfish monster.jpg` — early photo-manipulation: a real catfish grows tentacles (in-house edit; the first Fat Lance).
- `Concept Art/ref/Baddies/monsters/Cat Fish/environment.jpg` — monster sketch over a downtown street photo — first composition study for the museum attack.
- `Concept Art/Final/environment_monster.jpg` — final piece: Fat Lance prowling downtown StarFell at night (use `_lighten` variant only if the dark one muddies on screen).

---

## Wing 3 — The Sky Falls: Meteor & Environments

*Wall text: "Sixty thousand years of patience, painted."*

- `Concept Art/Final/meteor.jpg` — the meteor, pink core glowing, deep space
- `Concept Art/Final/meteor_earth.jpg` — atmospheric entry over Earth
- `Concept Art/Final/starfalling.jpg` — the fall over the Alabama river valley (photo composite)
- `Concept Art/Final/crater.jpg` — the astrobleme, active and glowing at night
- `Concept Art/Final/crater_inactive.jpg` — the crater, dormant by day (companion piece — hang side-by-side as a before/after pair)
- `Concept Art/ref/enviroment/crater_glowing.jpg` — early glow study over a waterfall photo (in-house edit)
- `Concept Art/Final/bridge_tentacle_bright.jpg` — the bridge at night, tentacles coiled beneath (the series' signature environment; consider `_3strip.jpg` cinematic crop as the wing banner)
- `Concept Art/Final/starfell_wip.jpg` — "Welcome to StarFell": sunset bridge with UFOs, town sign
- `Concept Art/Final/Illustration_boyvsmonster.jpg` — early key art: a kid with his gear, alone in a dark alley
- `Concept Art/Final/starfell_logo.jpg` — art-deco bridge logotype study (brand case, small)

---

## Wing 4 — Pencils to Print: Making the Pages

*Wall text: "Script by Mike Uhlir. Pencils and inks by Lucas Assis. Colors by Gui Sabino. Letters by Leo McGovern. This is how a page is born."*

All from `misc images/`. The stars here are the **stage triptychs** — present them as horizontal process strips (pencils → inks → colors):

- **Alistair triptych:** `alistair_1.png` → `alistair_2.png` → `alistair_3.png` (face study through three production stages — the wing's lead exhibit)
- **Cover process:** `cover2.png` (pencils) → `cover4.png` (inks) → `cover1.png` / `cover.png` / `cover3.png` (color variants — pick the strongest color plus the two stages)
- **Tree climb sequence:** `tree_climb1.png`, `tree_climb2.png`, `tree_climb3.png` — kids fleeing up a tree, art-to-page progression
- **Maitland and the mud-creature:** `maitland1.png`, `maitland 2.png`, `maitland 3.png`
- **Pencilled pages:** `d1.png`, `d2.png`, `d3.png`, `d4.png`, `day1.png`, `day2.png`, `day3.png`, `day4.png`, `day5.png` — raw pencils/inks of interior pages (curate ~6 strongest; `day5` appears to be a finished color page — use it as the "and finally…" close of a strip)
- **Ink sheet:** `issue_4_inks.png` — contact sheet of Issue 4 inked pages; show as a single "drawing board" piece
- **`PXL_20230718_180150264.00_00_09_22.Still001.jpg`** — real-world photo still of the cover art (behind-the-scenes shot; optional, good for authenticity)
- **Dark panel excerpts:** `water.png`, `water2.png`, `water_3.png` — moody interior panels (optional fillers; use if the grid needs rhythm)

Caption note: exact issue numbers for the pencil pages are unconfirmed — caption them "Interior pencils, StarFell (issue TBC)" until Mike labels them.

---

## Wing 5 — The Covers Gallery

*Wall text: "Every issue, every variant — including guest covers."*

Hang in series order, variants grouped. All from `Covers/`:

| File | Placard |
|---|---|
| `Starfell_Issue_01_Front_Cover.png` | Issue #1 — Levi vs. the tentacles, Franks' Grocery |
| `StarFell_Cover_Issue2_A.png` | Issue #2, Cover A — The World Shakers |
| `StarFell_Cover_Issue2_B (1).png` | Issue #2, Cover B — Delilah's camera |
| `StarFell_Cover_Issue2_Ashley.png` + `_Ashley_v2.png` | Issue #2, variant — mutant snail vs. sneaker (pick v2 unless Mike prefers both) |
| `StarFell_Cover_Issue3_A.png` | Issue #3, Cover A — Johnny in the Old Calaboose |
| `StarFell_Cover_Issue3_B.png` | Issue #3, Cover B — the horror in Miles' glasses |
| `Starfell_issue4 COVER A.png` | Issue #4, Cover A — candles, skull, and Voltaire secrets |
| `StarFell_Issue_04_Cover B.png` | Issue #4, Cover B — EC-Comics pulp pastiche ("Mutants, Mystery and Mayhem!") |
| `StarFell_Issue_Five_Cover_A.png` | Issue #5, Cover A — rooftop, tentacles rising |
| `StarFell_Issue_Five_cover_B.png` | Issue #5, Cover B — Kristy & Miles ("Tell me that was a snail") |
| `Dayone_Bridge_Cover_v2.png` | StarFell: Day One TPB — the ride into town |

Guest-artist credit on relevant placards: Will Robson (Spawn Kills, Spider-Man, Guardians of the Galaxy, Howard the Duck).

---

## Wing 6 — Location Scouting: Wetumpka Becomes StarFell

*Wall text: "StarFell is a real place. Its name is Wetumpka, Alabama — a town built inside an 85-million-year-old impact crater. Mike photographed it street by street, then handed it to the monsters."*

Pair real photos with their fictional counterparts (two-up "then/now" frames):

- `Concept Art/ref/Characters/Levi Levins/levi house.jpg` (+ `levi house_2.jpg`) ↔ `Concept Art/Final/levi_final.jpg` — the real house that became Levi's home, and the painting of Levi on its steps
- `Concept Art/ref/Characters/johnny/johnny_environment.jpg` — the real 1820 Old Calaboose, photo-edited with a "StarFell" historical marker ↔ `Covers/StarFell_Cover_Issue3_A.png`
- `Concept Art/ref/Characters/Levi Levins/levi_street.jpg`, `levi_environment.jpg` — downtown streets ↔ `Concept Art/Final/environment_monster.jpg`
- `Concept Art/ref/Baddies/monsters/Cat Fish/environment.jpg` — street photo with the first monster sketched in

⚠️ **Verify with Mike that these photos are his own** before publishing this wing — they appear to be location-scout shots, but confirm. Everything else in `Concept Art/ref/` (movie stills, fashion photos, actor collages, product shots) is third-party reference and stays OFF the site.

---

## Wing 7 — Beyond the Page: The Live-Action Dream

*Wall text: "What would Day One look like through a 35mm lens? AI-assisted development art exploring StarFell as live action."*
**Label this wing clearly as AI-assisted concept/development imagery.**

**Cast studies** (from `Live Action/Characters/` — photoreal character boards; curate one per character):
`Levi Levins.png` (or `_color_corrected`), `Johnny Gale.png` (or `_color_corrected`), `Delilah.png` (or `Delilah_large.png`), `Alistair Voltaire.png`, `Lilith_Voltaire.png`, `Miles Maitland.png`, `Lina Jane.png` (or `Lina Jane Hood.png`), `Kristy Leigh.png`, `Dash Jackson.png`, `Lucas Jackson.png`, `Horace.png`, `Moses Maitland.png`, `Levi_mask.png` (the goggles/mask close-up)

**Cinematic frames** (from `Live Action/Shot Images/` — curated selection, strongest first):
- `Levi_on_bridge.png` / `Levi_on_bridge_fall_v2.png` — aerial: tentacles take the bridge
- `levi_bike.png` — Levi riding the bridge into town
- `Delilah_Gate.png` — Delilah behind the estate gate
- `aliestar_hallway.png` — Alistair in the chair, hallway gloom
- `river_attack.png` — tentacles erupt from the river
- `dash_lucas_tentacles.png` — the brothers vs. the river
- `snail_shot.png` — mutant snail, red glow, Old Calaboose
- `Miles_plant.png` (or `_offset`) — Miles and the specimen
- `lina_library.png` (or `_yella`) — Lina Jane in the library
- `museum_clean.png`, `town_clean.png`, `square.png`, `building.png` — clean plates of the town (caption: "before the monsters")
- `signmaster_cinematic_wide-angle_21_aspect_ratio_a_young_girl__424dc6de-693f-416a-9696-aa90657913d2_3.png` and `signmaster_cinematic_wide-angle_an_20_yearold_girl_floating_i_f762642a-caa7-4157-b298-f4b1f38bfb25_3.png` — Lina Jane's power awakening (pink energy; rename `lina-jane-power-1/2`)
- `lucas_eyes.png` — b&w cartoon gag frame (the monster-movie-within-the-movie; fun closer)

Skip the remaining `Gemini_Generated_Image_*`/`unnamed*` shot files unless Mike flags favorites — the above are the strongest and most story-legible.

---

## Do NOT use (for clarity)

- Anything in `Concept Art/ref/` not explicitly listed above (third-party copyrighted reference)
- All `.psd` working files, all `Thumbs.db`
- `pitch/` pages (sales document — already covered elsewhere on the site)
- `StarFell_TPB_Draft_lowres.pdf` (full book; site previews are handled on the Issues page)
- `Concept Art/ref/Baddies/monsters/Cat Fish/bridge_tentacle_bright.jpg` (duplicate of the Final version)
- `Concept Art/Final/Char/*` duplicates (`1.jpg`, `12.jpg`, `18 (1).jpg`, `2 (1).jpg`, `Johnny_v2.jpg` repeat pieces already listed from `Char/` folders)

## Open items for Mike

1. Confirm the location-scout photos in Wing 6 are his own shots.
2. Label the pencil pages in Wing 4 with issue numbers.
3. Pick Cover A or both Ashley variants for Issue 2.
4. Confirm the "AI-assisted" label wording for Wing 7.

---

*Every file path above verified to exist on disk. Curated from a full visual review of all 460+ files in `StarFell Content/` (contact-sheet pass over every folder, including all 83 TPB pages previously read).*

# PROMPT FOR CLAUDE CODE — Comic Pages Update: Story & Media + The Vault

New source folders have been added to `StarFell Content/`: **`Comic Book Pages/`** (Issue_1–Issue_4, full lettered color pages) and **`Line_Art/`** (Issue 3 inks and lettered drafts). Every page has been visually reviewed and curated below. Build the following.

**Global rules:**
- Convert everything to WebP before use (≤300 KB grid thumbs, ≤1.5 MB lightbox). Never ship source PNG/TIF (some TIFs are 50+ MB — convert with ImageMagick `convert file.tif[0] -resize 1600x -quality 82 out.webp`).
- Rename to clean slugs (e.g., `i1-p14-title-splash.webp`). Skip `Thumbs.db`, `.kpf`, `.kcb`, `_KC/` folders (Kindle Create build junk), and `.tif` duplicates of pages that exist as PNG.
- SPOILER RULE: the site stays spoiler-free. Issue previews = opening pages only. The pages marked ⚠️ below are ending/reveal pages — do NOT use them anywhere public.
- Filenames below are exact; suffixes like `-01-01` matter.

---

## PART A — STORY & MEDIA page additions

### A1. Per-issue "Read the First Pages" previews
Add a preview lightbox (sequential reader, swipe/arrow nav) to each issue block, using these exact pages in order:

**Issue 1 preview (6 pages)** — from `Comic Book Pages/Issue_1/`:
1. `Starfell_Issue_01_Page01_Lettered-01-01.png` — cosmic opening, Byron caption
2. `Starfell_Issue_01_Page02_Lettered-01-01.png` — the meteor breaks apart
3. `Starfell_Issue_01_Page03_Lettered-01-01-01.png` — prehistoric impact
4. `Starfell_Issue_01_Page04_Lettered-01-01.png` — crater → 1956 fire
5. `Starfell_Issue_01_Page05_Lettered-01-01.png` — the fire rescue begins
6. `Starfell_Issue_01_Page06_Lettered-01-01.png` — Jack and Levi

**Issue 2 preview (5 pages)** — from `Comic Book Pages/Issue_2/`:
1. `Starfell_Issue_02_Page01_Lettered-01.png` — the hideout, one week later
2. `Starfell_Issue_02_Page02_Lettered-01.png` — the World Shakers
3. `Starfell_Issue_02_Page03_Lettered-01-01.png` — heading out
4. `Starfell_Issue_02_Page04_Lettered-01-01.png` — the attack begins
5. `Starfell_Issue_02_Page05_Lettered-01.png` — "MILES..." / the astrobleme

**Issue 3 preview (5 pages)** — from `Comic Book Pages/Issue_3/`:
1. `Starfell_TPB_Issue_03_Prologue01_Lettered-01.png` — Delilah's morning
2. `Starfell_TPB_Issue_03_Prologue02_Lettered-01.png` — breakfast at Fleur Du Ciel
3. `Starfell_TPB_Issue_03_Page01_Lettered.png` — Johnny's day begins
4. `Starfell_TPB_Issue_03_Page02_Lettered-01.png` — the hot rod run
5. `Starfell_TPB_Issue_03_Page03_Lettered-01.png` — Mister Charles

### A2. Splash Page Showcase (new band on Story & Media)
A full-width horizontal strip titled something like "From the Pages" — the book's biggest single images, click-to-lightbox:
- `Issue_1/Starfell_Issue_01_Page14_Lettered-01.png` — **the title splash**: full-page bridge into StarFell with the logo. The signature image of Issue 1 — make this the band's anchor.
- `Issue_2/Starfell_Issue_02_Page05_Lettered-01.png` — the astrobleme at golden hour.
- `Issue_2/Starfell_Issue_02_Page20_Lettered-01.png` and `Starfell_Issue_02_Page21_Lettered-01-01-01.png` — the pink shockwave sequence (verify at full size; use the strongest single page of the two).
- `Issue_1/Starfell_Issue_01_Page26_Lettered-01.png` — the Fleur Du Ciel estate reveal.

### A3. Issue 4 "In Production" strip
Short band: "Issue 4 — on the drawing board now." Use 3–4 colored work-in-progress pages from `Comic Book Pages/Issue_4/` (unlettered, safe to tease). Recommended after eyeballing at full size: `Starfell_issue4_01_009.png`, `Starfell_issue4_01_010.png`, `Starfell_issue4_01_011.png` (underwater/river tentacle pages — gorgeous teal work), plus one of the tree/rock pages (`_017.png`/`_018.png`). Avoid any page that shows a clear story resolution; they're unlettered so risk is low. Caption as "work in progress — colors by Gui Sabino." Skip `_001.tif`–`_008.tif` where a PNG sibling doesn't exist unless conversion looks clean.

### A4. Issue covers — completeness
`Comic Book Pages/Issue_1/` also contains `Starfell_Issue_01_Back_Cover.png` and inside covers. Add the back cover to the Covers gallery in the Vault (placard: "Issue #1 back cover").

---

## PART B — THE VAULT additions

### B1. New exhibit inside Wing 4 (Pencils to Print): "Ink to Color"
The gold here is that `Line_Art/` contains Issue 3 ink pages that match finished color pages in `Comic Book Pages/Issue_3/`. Build side-by-side pairs (same layout as Wing 6 then/now):

| Inks (Line_Art/) | Final color (Comic Book Pages/Issue_3/) | Placard |
|---|---|---|
| `StarFell_Issue_03_Page07.tif` | `Starfell_TPB_Issue_03_Page07_Lettered-01-01.png` | "Page 7 — inks by Lucas Assis / colors by Gui Sabino" |
| `StarFell_Issue_03_Page09.tif` | `Starfell_TPB_Issue_03_Page09_Lettered-01.png` | "Page 9 — ink to color" |
| `StarFell_Issue_03_Page12.png` | `Starfell_TPB_Issue_03_Page12_Lettered-01-01-01-01.png` | "Page 12 — night scene: heavy blacks to moonlight" |
| `StarFell_Issue_03_Page18.tif` | `Starfell_TPB_Issue_03_Page18_Lettered-01.png` | "Page 18 — ink to color" |

(Ignore `Page09 (1).tif`, `Page12.tif`, `Page12meh.png` — duplicates/rejects. The `*_Lettered_Draft1/2.jpg` files in Line_Art are b&w lettered drafts — pick ONE, e.g. `Starfell_Issue_03_Page10_Lettered_Draft1.jpg`, as a single exhibit showing the lettering stage: "Letters before color — Leo McGovern's pass on the inked page.")

### B2. "The Line Art Library" — full exhibit (Wing 4)
A dedicated grid of raw line art, ordered to read as a craft progression: pencils → layouts → inks → lettered drafts. All from `Line_Art/`:

| # | File | Placard |
|---|---|---|
| 1 | `unnamed.png` | "Pencils — first pass on the page" |
| 2 | `unnamed (1).png` | "Pencils — figures and a monster finding their shapes" |
| 3 | `unnamed (2).png` | "Pencils — roughing in the darkness" |
| 4 | `image (8) (1).png` | "Layout roughs — the page before the page" |
| 5 | `image (4).png` | "Inks — the Sheriff's office, Lucas Assis" |
| 6 | `image (12).png` | "Inks — clean blacks, no color yet" |
| 7 | `Starfell_Issue_03_Page06_Lettered_Draft2.jpg` | "Lettered draft — Leo McGovern's balloons on raw inks" |
| 8 | `Starfell_Issue_03_Page16_Lettered_Draft1.jpg` | "Lettered draft — night action before color" |

Bonus piece if the grid wants a 9th: `Starfell_Issue_03_Page15_Lettered_Draft1.jpg` — it still carries the editor's cyan correction mark. Placard: "Lettered draft, editor's note included — this is what a real working page looks like."

Centerpiece above the grid:
- `Line_Art/goonies.png` — dense group inked illustration of the whole kid cast (clear Goonies homage). Placard: "The World Shakers — group inks." Rename `world-shakers-group-inks.webp`. Give it a wide/featured frame.

(Still ignore: `Page09 (1).tif`, `Page12.tif`, `Page12meh.png` — duplicates/rejects. `Page09_Lettered_Draft1.jpg` and `Page10_Lettered_Draft1.jpg/png` are spare drafts; the Page10 draft is already used in B1's lettering exhibit.)

### B3. New Vault wing: "Wing Eight — The Pages"
A reading-room style gallery of the best finished pages (color, lettered) — the craft on full display. Same frame/placard/lightbox system. Curated set:

**From Issue 1:**
- `Starfell_Issue_01_Page01_Lettered-01-01.png` — "The dream that was not all a dream" (Byron opening)
- `Starfell_Issue_01_Page03_Lettered-01-01-01.png` — "Impact, 60,000 years ago"
- `Starfell_Issue_01_Page14_Lettered-01.png` — "The title splash" (also on Story & Media; fine to repeat)
- `Starfell_Issue_01_Page26_Lettered-01.png` — "Welcome to Fleur Du Ciel"
- `Starfell_Issue_01_Page27_Lettered-01.png` + `Starfell_Issue_01_Page28_Lettered-01.png` — "In the Pines" transformation pages (body-horror highlight; tonally a tease, not a plot spoiler — Issue 1's public cliffhanger)

**From Issue 2:**
- `Starfell_Issue_02_Page02_Lettered-01.png` — the World Shakers assembled
- `Starfell_Issue_02_Page05_Lettered-01.png` — the astrobleme
- `Starfell_Issue_02_Page20_Lettered-01.png` — the shockwave
- `Starfell_Issue_02_Page14_Lettered-01-01.png` — Delilah & the scissors (verify content at full size; swap for a neighboring estate page if mismatched)

**From Issue 3:**
- `Starfell_TPB_Issue_03_Prologue01_Lettered-01.png` — Delilah wakes (bats and teddy bears)
- `Starfell_TPB_Issue_03_Page03_Lettered-01.png` — Mister Charles ("Johnny Angel")
- `Starfell_TPB_Issue_03_Page12_Lettered-01-01-01-01.png` — the night pages (pairs with its inks in B1)

**Issue 4 Spotlight — "Delilah's Wishing Rock" (featured sub-section of this wing):**
Four work-in-progress color pages from `Comic Book Pages/Issue_4/` — Delilah's flashback, presented as a connected strip in this order, labeled "Issue 4 — work in progress, colors by Gui Sabino":
- `Starfell_issue4_01_023.png` — "The garden, years ago" (young Delilah at the estate)
- `Starfell_issue4_01_025.png` — "The party" (the glow begins)
- `Starfell_issue4_01_026.png` — "The wish" — THE key page: young Delilah in the blue dress kneeling in pink flame. The strongest single image of the set; make it the spotlight's lead/lightbox cover.
- `Starfell_issue4_01_027.png` — "What the wish made" (the transformation bursts loose)
These are unlettered WIP pages — beautiful and mysterious rather than story-spoiling, and approved by Mike for the site.

⚠️ **Do NOT use publicly:** `Starfell_TPB_Issue_03_Page20`–`Page24` (the GROM battle and the final-page reveal) and `Starfell_Issue_02_Page24` (Lina Jane's scrapbook ending) — these are the book's biggest spoilers. If Mike wants a "Spoiler Room" later, gate it behind a click-through warning.

### B4. Wing nav update
Add the new wing to the Vault's chip nav and adjust wing numbering. Keep wall-text in the established voice (warm Southern, then unsettling). Suggested wall text for The Pages: "Script, pencils, inks, colors, letters — five crafts, one page. These are the finished pages the way they shipped, hung like the originals they are."

---

## Verification checklist for you (Claude Code)
1. Every webp opens and isn't black/blank (the big TIFs sometimes render black — use `[0]` frame and check output).
2. Lightbox order matches the page numbers above.
3. No ⚠️ page appears anywhere in the build output.
4. Lazy-load everything; page-grid thumbs ≤300 KB.
5. Run a link check over new `<img>`/`<a>` srcs before committing.

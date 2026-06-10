# StarFell — Official Site

Static website for **StarFell**, the horror sci-fi comic series by Mike Uhlir, published by StarFell Studios.

> *The Goonies* meets *Stranger Things* — Lovecraft meets *The Sandlot*.
> Mutants, Monsters, and Mayhem in 1962 Alabama.

---

## What's in here

Pure HTML / CSS / JS. No build step. No frameworks. No package.json. Drop it on any static host and it works.

```
docs/
├── index.html          Home — hero, teasers, cover strip, pull-quotes
├── story.html          The Story — meteor → town → Day One → invasion
├── characters.html     World Shakers · Voltaires · Supporting Cast · Monsters
├── issues.html         Day One #1–3 + coming-soon teasers for #4–6
├── about.html          Mike's story, the real Wetumpka crater, the team
├── buy.html            Amazon + Sweet Home Books + retail/press contacts
├── css/
│   └── styles.css      Single stylesheet — design tokens, components, responsive
├── js/
│   └── main.js         Mobile nav, character tabs, expandable bios, lazy bg images
└── assets/
    ├── logos/          Brand wordmarks (retro logo + neon banner)
    ├── covers/         Issue covers (TPB + #1–5 variants)
    ├── characters/     Character turnaround sheets
    ├── concept/        Story-page backdrops (crater, bridge, meteor, etc.)
    └── monsters/       Fat Lance + mutant snail
```

---

## Hosting on GitHub Pages

The site is set up to publish from the `/docs` folder of a repo's default branch — the cleanest GitHub Pages workflow for repos that contain non-web assets at the root.

### One-time setup

1. **Create a GitHub repo** for the site (public, or paid GitHub Pro for private Pages).
2. **Push the project** so that this `docs/` folder exists at the repo root:
   ```bash
   git init
   git add docs/ README.md
   git commit -m "Initial StarFell site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```
3. In GitHub, go to **Settings → Pages**.
4. Under **Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main` · **Folder:** `/docs`
   - Click **Save**.
5. Wait ~30 seconds. The site will be live at `https://<your-username>.github.io/<your-repo>/`.

### Custom domain (e.g. `starfellstudios.com`)

1. In **Settings → Pages → Custom domain**, enter your domain and save.
2. GitHub will write a `CNAME` file into `docs/` on your behalf. Don't delete it.
3. At your DNS provider, point the domain to GitHub Pages:
   - **Apex domain** (`starfellstudios.com`): four A records pointing to
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
   - **www subdomain**: a CNAME record pointing to `<your-username>.github.io`.
4. Back in **Settings → Pages**, tick **Enforce HTTPS** once the cert provisions (can take a few minutes to a few hours).

### Updating the site

Every push to `main` redeploys automatically. To edit copy or swap an image:

```bash
# edit a file in docs/
git add docs/
git commit -m "Update <whatever>"
git push
```

GitHub Pages picks the change up within ~30 seconds.

---

## Local preview

No build step needed. Just serve `docs/` over any static server. From the repo root:

```powershell
# Python (any version with http.server)
python -m http.server 8000 --directory docs

# Or, if you have Node installed
npx serve docs
```

Then open <http://localhost:8000/>.

> ⚠️ Don't open `index.html` directly with `file://` — the lazy-loaded background images use relative paths and modern browsers block some `file://` features. A local server (above) is two seconds of setup.

---

## Design notes

- **Aesthetic:** Norman Rockwell's Saturday morning, ten seconds before the sky splits. Warm autumn Americana (rust, mustard, faded teal, cream paper) violated by the meteor's pink/magenta glow.
- **Typography:** *Limelight* for retro-deco display, *Special Elite* for typewriter-stamp accents, *Cormorant Garamond* for serif body. All loaded from Google Fonts.
- **Motion:** Restrained. A slow background zoom on the hero, a soft pink pulse on the logo. Dread is slow.
- **Responsive:** Mobile-first grids that collapse cleanly at <820px (hamburger nav) and <720px (single-column issue layout).
- **Accessibility:** Honors `prefers-reduced-motion`, uses semantic landmarks, all interactive controls are keyboard-reachable.

---

## Image asset optimization (optional)

The committed assets are full-resolution source files (some 5–8 MB PNGs). The site works fine as-is on a fast connection but could be much faster on mobile. If you want to optimize before going live:

```powershell
# Example: convert covers to WebP at 1200px wide using ImageMagick
magick mogrify -resize 1200x -format webp -quality 82 docs/assets/covers/*.webp
```

Then either swap `.png` → `.webp` references in the HTML, or keep both and use `<picture>` elements.

---

## Brand & content

- **Logo:** `docs/assets/logos/StarFell_retro_logo.webp` (transparent, pink beveled wordmark) — used in nav, hero, and as favicon.
- **Footer logo:** `docs/assets/logos/banner_logo.webp` (neon-outline wordmark for dark backgrounds).
- **OG image:** `docs/assets/covers/Dayone_Bridge_Cover_v2.webp`.
- **Copy:** all text is canonical, sourced from the StarFell creative brief — no placeholder lorem ipsum.

---

## Credits

Site built for StarFell Studios. Creative direction sourced from `starfell-site-brief.md`.

- **Created & written by:** Mike Uhlir
- **Art:** Lucas "Lks" Assis
- **Colors:** Guilherme "Gui" Sabino
- **Letters:** Leo McGovern
- **Edits:** Tiffany Crook
- **Guest cover artist:** Will Robson

For press, retail, or interview requests: **mike@starfellstudios.com**

---

*Thanks for stopping by. Y'all come back now. The crater's still glowing.*

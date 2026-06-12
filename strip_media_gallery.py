"""Remove the entire Media Gallery section and lightbox markup from story-media.html."""

import re
from pathlib import Path

path = Path(r"D:\Projects\StarFell_website\StarFell Website\docs\story-media.html")
text = path.read_text(encoding="utf-8")
orig_len = len(text)

# Delete the SECTION 4 — MEDIA GALLERY block (from its opening comment through </section>).
gallery_re = re.compile(
    r'\n\s*<!-- ===+\n\s+SECTION 4 — MEDIA GALLERY\n\s+===+ -->\n'
    r'\s*<section class="page-section" id="media-gallery">[\s\S]*?</section>\n',
)
text, n1 = gallery_re.subn("\n", text, count=1)

# Delete the lightbox markup (only the Media Gallery used it on this page).
lightbox_re = re.compile(
    r'\n\s*<!-- ===+ LIGHTBOX[^>]*-->\n'
    r'\s*<div class="lightbox" id="lightbox"[\s\S]*?</div>\n\s*</div>\n',
)
text, n2 = lightbox_re.subn("\n", text, count=1)

# Update the page hero subtitle if it still mentions four sections.
text = re.sub(
    r"The story, the people, the issues, and the work behind it all\.",
    "The story, the people, and the issues — all in one place.",
    text,
)

# Update the section nav chips — remove the Media Gallery chip.
text = re.sub(
    r'\s*<a href="#media-gallery" class="section-chip">Media Gallery</a>',
    "",
    text,
)

path.write_text(text, encoding="utf-8")
print(f"  Gallery section removed: {n1}")
print(f"  Lightbox removed:        {n2}")
print(f"  Length: {orig_len} → {len(text)} ({orig_len - len(text)} chars cut)")

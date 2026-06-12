"""Switch all major body-copy paragraph font-sizes to `inherit` so they
cascade from the responsive body (1.2rem base / 1.3rem ≥1024px).

Leaves smaller UI labels (footer text, ai-notice, museum placard captions)
slightly smaller for visual hierarchy.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
CSS = DOCS / "css" / "styles.css"

# Each entry: (uniquely-matchable pattern, replacement that keeps surrounding props)
CSS_PATCHES = [
    # .section-head p
    (r'(\.section-head p \{ )font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .story-block p
    (r'(\.story-block p \{ )font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .issue p
    (r'(\.issue p \{ )font-size: 1\.205rem;',
     r'\1font-size: inherit;'),
    # .about-grid p
    (r'(\.about-grid p \{ )font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .buy-card ul li
    (r'(\.buy-card ul li \{[\s\S]{0,80}?)font-size: 1\.175rem;',
     r'\1font-size: inherit;'),
    # .page-hero p (inline declaration in shorthand)
    (r'(\.page-hero p \{[\s\S]{0,160}?)font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .media-item .video-meta p
    (r'(\.media-item \.video-meta p \{[\s\S]{0,80}?)font-size: 1\.225rem;',
     r'\1font-size: inherit;'),
    # .museum-hero .lead
    (r'(\.museum-hero \.lead \{[\s\S]{0,150}?)font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .page-section-header p
    (r'(\.page-section-header p \{[\s\S]{0,80}?)font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .wall-text
    (r'(\.wall-text \{[\s\S]{0,80}?)font-size: 1\.275rem;',
     r'\1font-size: inherit;'),
    # .char-card p
    (r'(\.char-card p \{ )font-size: 1rem;',
     r'\1font-size: inherit;'),
    # .char-card .bio-full
    (r'(\.char-card \.bio-full \{[\s\S]{0,60}?)font-size: 1rem;',
     r'\1font-size: inherit;'),
    # .exhibit-text
    (r'(\.exhibit-text \{[\s\S]{0,80}?)font-size: 1\.175rem;',
     r'\1font-size: inherit;'),
    # .lightbox-caption
    (r'(\.lightbox-caption \{[\s\S]{0,80}?)font-size: 1\.175rem;',
     r'\1font-size: inherit;'),
    # .retailer p (card descriptions)
    (r'(\.retailer p \{ color: var\(--bone\); )font-size: 1\.105rem;',
     r'\1font-size: inherit;'),
]

# Inline italic emphasis paragraphs — change to em so they scale proportionally
# with the responsive body.
HTML_PATCHES = [
    (r'font-size:\s*1\.375rem', 'font-size: 1.15em'),
]


def apply_patches(text, patches):
    changed = 0
    for pat, repl in patches:
        new_text, n = re.subn(pat, repl, text)
        if n:
            changed += n
            text = new_text
    return text, changed


css_text = CSS.read_text(encoding="utf-8")
new_css, n_css = apply_patches(css_text, CSS_PATCHES)
CSS.write_text(new_css, encoding="utf-8")
print(f"  styles.css: {n_css} declarations switched to inherit")

for name in ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]:
    p = DOCS / name
    text = p.read_text(encoding="utf-8")
    new_text, n = apply_patches(text, HTML_PATCHES)
    if n:
        p.write_text(new_text, encoding="utf-8")
    print(f"  {name}: {n} inline emphasis sizes scaled")

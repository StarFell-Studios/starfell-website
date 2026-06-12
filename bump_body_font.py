"""Bump body-copy font-sizes site-wide by 0.125rem (~2px).

Targets paragraph/description/body copy. Leaves headings, display titles,
typewriter-stamp labels, and small UI text alone.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
CSS = DOCS / "css" / "styles.css"

# Each entry is (uniquely-matchable-pattern, replacement).
# Patterns include surrounding context so we don't accidentally hit headings.
CSS_PATCHES = [
    # body default
    (r'(font-family: var\(--font-body\);\s*\n\s*)font-size: 1\.125rem;',
     r'\1font-size: 1.25rem;'),
    # .section-head p (1.15 → 1.275)
    (r'(\.section-head p \{ )font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .story-block p
    (r'(\.story-block p \{ )font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .issue p (1.08 → 1.205)
    (r'(\.issue p \{ )font-size: 1\.08rem;',
     r'\1font-size: 1.205rem;'),
    # .about-grid p
    (r'(\.about-grid p \{ )font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .buy-card ul li
    (r'(\.buy-card ul li \{[\s\S]{0,80}?)font-size: 1\.05rem;',
     r'\1font-size: 1.175rem;'),
    # .retailer p (.98 → 1.105)
    (r'(\.retailer p \{ color: var\(--bone\); )font-size: \.98rem;',
     r'\1font-size: 1.105rem;'),
    # .footer-col a, .footer-col p
    (r'(\.footer-col a, \.footer-col p \{[\s\S]{0,80}?)font-size: \.98rem;',
     r'\1font-size: 1.105rem;'),
    # .page-hero p
    (r'(\.page-hero p \{[\s\S]{0,150}?)font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .media-item .video-meta p (1.1 → 1.225)
    (r'(\.media-item \.video-meta p \{[\s\S]{0,80}?)font-size: 1\.1rem;',
     r'\1font-size: 1.225rem;'),
    # .contact-form input / textarea
    (r'(\.contact-form input\[type="text"\][\s\S]{0,300}?)font-size: 1\.05rem;',
     r'\1font-size: 1.175rem;'),
    # .museum-hero .lead
    (r'(\.museum-hero \.lead \{[\s\S]{0,150}?)font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .ai-notice
    (r'(\.ai-notice \{[\s\S]{0,250}?)font-size: \.98rem;',
     r'\1font-size: 1.105rem;'),
    # .page-section-header p
    (r'(\.page-section-header p \{[\s\S]{0,80}?)font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .wall-text
    (r'(\.wall-text \{[\s\S]{0,80}?)font-size: 1\.15rem;',
     r'\1font-size: 1.275rem;'),
    # .exhibit-text (1.05 → 1.175)
    (r'(\.exhibit-text \{[\s\S]{0,80}?)font-size: 1\.05rem;',
     r'\1font-size: 1.175rem;'),
    # .placard .caption
    (r'(\.placard \.caption \{[\s\S]{0,80}?)font-size: \.98rem;',
     r'\1font-size: 1.105rem;'),
    # .lightbox-caption
    (r'(\.lightbox-caption \{[\s\S]{0,80}?)font-size: 1\.05rem;',
     r'\1font-size: 1.175rem;'),
]

# Inline HTML font-size bumps
HTML_PATCHES = [
    (r'font-size:\s*1\.15rem',  'font-size: 1.275rem'),
    (r'font-size:\s*1\.1rem(?!\d)',   'font-size: 1.225rem'),
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
new_css, css_changed = apply_patches(css_text, CSS_PATCHES)
CSS.write_text(new_css, encoding="utf-8")
print(f"  styles.css: {css_changed} declarations bumped")

for name in ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]:
    p = DOCS / name
    text = p.read_text(encoding="utf-8")
    new_text, n = apply_patches(text, HTML_PATCHES)
    if n:
        p.write_text(new_text, encoding="utf-8")
    print(f"  {name}: {n} inline font-sizes bumped")

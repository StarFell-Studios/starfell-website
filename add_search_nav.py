# -*- coding: utf-8 -*-
"""Insert the Vault search component into the nav of every page.

Sits immediately before the .nav-social block (i.e. to its left). Idempotent:
re-running replaces the existing block rather than duplicating it.
"""
import re
from pathlib import Path

DOCS = Path(__file__).parent / "docs"
PAGES = ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]

MARKER = "data-nav-search"

BLOCK = """      <!-- ============ VAULT SEARCH ============ -->
      <div class="nav-search" data-nav-search>
        <button type="button" class="nav-search-toggle" aria-label="Search the Vault" aria-expanded="false" aria-controls="nav-search-panel">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="20.5" y1="20.5" x2="16.5" y2="16.5"></line></svg>
        </button>
        <div class="nav-search-panel" id="nav-search-panel">
          <div class="nav-search-bar">
            <input type="search" class="nav-search-input" placeholder="Search the Vault — try “Delilah”, “concept art”, “Wetumpka”…" aria-label="Search all Vault images" autocomplete="off" spellcheck="false">
            <div class="nav-search-results" role="listbox" aria-label="Vault search results"></div>
          </div>
        </div>
      </div>
"""

SOCIAL_LINE = '      <div class="nav-social" aria-label="StarFell on social media">'

# Matches a previously-inserted block (comment through the outer .nav-search
# close at 6-space indent) so re-runs replace rather than duplicate.
EXISTING_RE = re.compile(
    r'[ \t]*<!-- =+ VAULT SEARCH =+ -->\n(?:.*\n)*?      </div>\n'
)

MAIN_JS = '  <script src="js/main.js"></script>'
SEARCH_JS = '  <script src="search-index.js"></script>'


def main():
    for name in PAGES:
        path = DOCS / name
        src = path.read_text(encoding="utf-8")

        # Remove any prior insertions first (idempotent).
        src = EXISTING_RE.sub("", src)
        src = src.replace(SEARCH_JS + "\n", "")

        if SOCIAL_LINE not in src:
            raise SystemExit(f"{name}: could not find nav-social insertion point")
        src = src.replace(SOCIAL_LINE, BLOCK + SOCIAL_LINE, 1)

        # Load the embedded index fallback just before main.js (file:// safe).
        if MAIN_JS in src:
            src = src.replace(MAIN_JS, SEARCH_JS + "\n" + MAIN_JS, 1)
        else:
            raise SystemExit(f"{name}: could not find main.js script tag")

        path.write_text(src, encoding="utf-8")
        print(f"Inserted search nav + index fallback into {name}")


if __name__ == "__main__":
    main()

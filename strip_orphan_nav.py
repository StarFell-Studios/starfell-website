"""Remove the dangling orphan <li> items left after the closing </ul> of the
new nav. The previous rebuild substituted the outer <ul class="nav-links">
through the *inner* </ul> of the old nav-submenu, leaving these stragglers:

      </ul>
        </li>
        <li><a href="about.html">About</a></li>
        <li class="nav-cta-wrap"><a href="buy.html" class="nav-cta">Where to Buy</a></li>
      </ul>

We collapse that whole tail back to a single </ul>.
"""

import re
from pathlib import Path

DOCS = Path(r"D:\Projects\StarFell_website\StarFell Website\docs")
PAGES = ["index.html", "story-media.html", "vault.html", "about.html", "buy.html"]

# Match the legitimate </ul> followed by the orphan group followed by an extra </ul>.
orphan_re = re.compile(
    r'</ul>\s*'
    r'</li>\s*'
    r'<li><a href="about\.html"[^>]*>About</a></li>\s*'
    r'<li class="nav-cta-wrap"><a href="buy\.html" class="nav-cta">Where to Buy</a></li>\s*'
    r'</ul>'
)

for name in PAGES:
    path = DOCS / name
    text = path.read_text(encoding="utf-8")
    new_text, n = orphan_re.subn("</ul>", text, count=1)
    if n:
        path.write_text(new_text, encoding="utf-8")
        print(f"  cleaned: {name}")
    else:
        print(f"  already clean: {name}")

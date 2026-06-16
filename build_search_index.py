# -*- coding: utf-8 -*-
"""Build docs/search-index.json from the image cards in docs/vault.html.

Also stamps each <figure class="piece"> with a stable id (vault-item-N) so
search results can deep-link to and highlight the matching card.

Static-only: the output JSON is consumed client-side by docs/js/main.js.
"""
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

DOCS = Path(__file__).parent / "docs"
VAULT = DOCS / "vault.html"

# Concise section labels keyed by wing id (mirror the sticky wing-nav chips).
WING_LABELS = {
    "wing-1": "First Marks",
    "wing-2": "Bestiary",
    "wing-3": "Sky Falls",
    "wing-4": "Pencils to Print",
    "wing-5": "Covers",
    "wing-6": "Location Scouting",
    "wing-7": "Beyond the Page",
    "wing-8": "The Pages",
    "wing-9": "On Film",
}

# Canonical character roster with aliases. Order matters: longer/full names first.
CHARACTERS = [
    ("Levi Levins", ["levi levins", "levi"]),
    ("Johnny Gale", ["johnny gale", "johnny"]),
    ("Delilah Voltaire", ["delilah voltaire", "delilah"]),
    ("Alistair Voltaire", ["alistair voltaire", "alistair", "the patriarch", "patriarch"]),
    ("Lilith Voltaire", ["lilith voltaire", "lilith"]),
    ("Miles Maitland", ["miles maitland", "dr. maitland", "dr maitland", "maitland", "miles"]),
    ("Lina Jane", ["lina jane", "lina"]),
    ("Dash Jackson", ["dash jackson", "dash"]),
    ("Lucas Jackson", ["lucas jackson"]),
    ("Kristy Leigh", ["kristy leigh", "kristy"]),
    ("Horace", ["horace"]),
    ("Fat Lance", ["fat lance"]),
    ("Mister Charles", ["mister charles", "mr. charles"]),
    ("Mutant River Snail", ["mutant river snail", "mutant snail", "river snail", "snail"]),
    ("Mud-Creature", ["mud-creature", "mud creature"]),
    ("GROM", ["grom"]),
]

# Map keywords found in data-medium / title to canonical art-type tags.
ART_TYPE_RULES = [
    ("character sheet", ["character sheet", "model sheet", "turnaround", "expression studies", "pose studies", "costume"]),
    ("concept art", ["concept", "color painting", "grayscale painting", "grayscale full-figure", "moody concept", "underwater concept", "photo composite painting", "key art", "study", "exploration"]),
    ("cover art", ["cover", "trade paperback"]),
    ("location photo", ["location scout", "photo edit", "in-house photo"]),
    ("line art", ["ink", "pencil", "color over inks", "line art"]),
    ("comic page", ["page", "interior page", "splash", "prologue", "final color page", "final color"]),
    ("cinematic frame", ["cinematic frame", "ai-assisted frame", "ai-assisted cinematic", "clean plate", "close-up", "b-movie", "ai-assisted gag", "ai-assisted character study", "ai-assisted"]),
    ("branding", ["brand exploration", "logotype", "art-deco"]),
]

STOPWORDS = set("""a an the and or of to in on at by for with from is it its as into
this that these those one two three four five day night i ii iii final inks pencils color
study studies page over not all out under but his her him she he was were been""".split())


class VaultParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.frames = []
        self.wing_id = None
        self.wing_title = ""
        self.exhibit_title = ""
        self.figure_id = ""
        self._capture = None          # which text field we're accumulating
        self._buf = []
        self._cur_frame = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "section" and "wing" in cls.split():
            self.wing_id = a.get("id")
            self.wing_title = ""
        elif tag == "figure" and "piece" in cls.split():
            self.figure_id = a.get("id", "")
        elif tag in ("h2", "h3") and "wing-title" in cls:
            self._start_capture("wing_title")
        elif tag == "h3" and "exhibit-title" in cls:
            self._start_capture("exhibit_title")
        elif tag == "a" and "frame" in cls.split():
            self._cur_frame = {
                "href": a.get("href", ""),
                "title": html.unescape(a.get("data-title", "")),
                "medium": html.unescape(a.get("data-medium", "")),
                "caption": html.unescape(a.get("data-caption", "")),
                "alt": "",
                "wing_id": self.wing_id,
                "section": WING_LABELS.get(self.wing_id, ""),
                "section_full": self.wing_title.strip(),
                "exhibit": self.exhibit_title.strip(),
                "figure_id": self.figure_id,
            }
        elif tag == "img" and self._cur_frame is not None and not self._cur_frame["alt"]:
            self._cur_frame["alt"] = html.unescape(a.get("alt", ""))

    def handle_endtag(self, tag):
        if self._capture and tag in ("h2", "h3"):
            text = "".join(self._buf).strip()
            setattr(self, self._capture, text)
            self._capture = None
            self._buf = []
        elif tag == "a" and self._cur_frame is not None:
            self.frames.append(self._cur_frame)
            self._cur_frame = None

    def handle_data(self, data):
        if self._capture:
            self._buf.append(data)

    def _start_capture(self, field):
        self._capture = field
        self._buf = []


def detect_characters(text):
    low = text.lower()
    found = []
    for canonical, aliases in CHARACTERS:
        if any(alias in low for alias in aliases):
            found.append(canonical)
    return found


def detect_art_types(medium, title):
    low = (medium + " " + title).lower()
    types = []
    for canonical, kws in ART_TYPE_RULES:
        if any(kw in low for kw in kws):
            types.append(canonical)
    return types


def keywords_from(*texts):
    words = set()
    for t in texts:
        for w in re.findall(r"[a-zA-Z][a-zA-Z'-]+", t.lower()):
            if len(w) >= 3 and w not in STOPWORDS:
                words.add(w)
    return words


FIGURE_RE = re.compile(r'<figure class="(piece[^"]*)"(\s+id="vault-item-\d+")?\s*>')


def stamp_vault_ids(src):
    """Give every <figure class="piece..."> a stable id in document order.

    Idempotent: an existing vault-item id is replaced with the index-aligned one.
    """
    counter = {"n": 0}

    def repl(m):
        i = counter["n"]
        counter["n"] += 1
        return f'<figure class="{m.group(1)}" id="vault-item-{i}">'

    new_src, count = FIGURE_RE.subn(repl, src)
    return new_src, count


def main():
    src = VAULT.read_text(encoding="utf-8")

    src, stamped = stamp_vault_ids(src)
    VAULT.write_text(src, encoding="utf-8")
    print(f"Stamped {stamped} figure ids into vault.html")

    parser = VaultParser()
    parser.feed(src)
    print(f"Parsed {len(parser.frames)} frames")

    index = []
    for i, f in enumerate(parser.frames):
        item_id = f["figure_id"] or f"vault-item-{i}"
        if item_id != f"vault-item-{i}":
            raise SystemExit(f"id mismatch at {i}: figure has {item_id!r}")
        title = f["title"] or f["alt"] or f["exhibit"] or "Untitled"
        description = f["caption"] or f["alt"]
        characters = detect_characters(f["title"] + " " + f["caption"] + " " + f["alt"])
        art_types = detect_art_types(f["medium"], f["title"])
        primary_char = characters[0] if characters else ""

        tags = set()
        tags.update(t.lower() for t in characters)
        tags.update(art_types)
        if f["medium"]:
            tags.update(keywords_from(f["medium"]))
        if f["section"]:
            tags.add(f["section"].lower())
            tags.update(keywords_from(f["section"]))
        if f["section_full"]:
            tags.update(keywords_from(f["section_full"]))
        if f["exhibit"]:
            tags.update(keywords_from(f["exhibit"]))
        tags.update(keywords_from(f["title"], f["caption"]))
        # Drop tags that merely duplicate stray single chars
        tags = sorted(t for t in tags if t and len(t) >= 2)

        index.append({
            "id": item_id,
            "title": title,
            "description": description,
            "medium": f["medium"],
            "tags": tags,
            "character": primary_char,
            "characters": characters,
            "artTypes": art_types,
            "section": f["section"],
            "sectionFull": f["section_full"],
            "wing": f["wing_id"],
            "exhibit": f["exhibit"],
            "path": f["href"],
        })

    out = DOCS / "search-index.json"
    out.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out} ({len(index)} entries)")

    # Embedded fallback: lets search work even when the site is opened over
    # file:// (where fetch() of a local JSON is blocked by the browser).
    out_js = DOCS / "search-index.js"
    compact = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    out_js.write_text(
        "/* Auto-generated by build_search_index.py — do not edit by hand. */\n"
        "window.STARFELL_SEARCH_INDEX = " + compact + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_js} ({len(index)} entries)")

    # Quick sanity stats
    from collections import Counter
    secs = Counter(e["section"] for e in index)
    print("By section:", dict(secs))
    chars = Counter(c for e in index for c in e["characters"])
    print("Top characters:", chars.most_common(8))
    no_char = [e["title"] for e in index if not e["characters"]]
    print(f"Entries with no character: {len(no_char)}")


if __name__ == "__main__":
    main()

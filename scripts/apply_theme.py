#!/usr/bin/env python3
"""
TOCO Technologies — Section theme assignment (white / black / blue).

Runs after the page generators. For every generated page it walks the
<section class="sec" ...> blocks in order and assigns a palette class:
  theme-light  -> white
  theme-alt    -> soft grey-white
  theme-dark   -> black
  theme-blue   -> royal-blue band
Hero / page-hero sections are left untouched (they are always black).
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Section palettes per page type (in document order, excluding the hero).
HOME = [
    "light",  # client logo marquee
    "light",  # what we build
    "dark",   # AI working inside your business (CSS mockups)
    "alt",    # products showcase
    "light",  # where to begin
    "blue",   # stats counters
    "light",  # industries chips
    "alt",    # portfolio
    "dark",   # process timeline
    "light",  # testimonials slider
    "alt",    # FAQ
    "light",  # CTA (blue card on white)
]
DETAIL = [
    "light",  # what's included
    "dark",   # how it works
    "blue",   # benefits / results
    "light",  # tech stack
    "alt",    # FAQ
    "light",  # related links
    "alt",    # CTA (blue card)
]
ABOUT = ["light", "dark", "alt", "light"]
HUB = ["light", "alt"]
SINGLE_LIGHT = ["light"]
SINGLE_ALT = ["alt"]

SECTION_RE = re.compile(r'<section class="sec(?: theme-\w+)?"([^>]*)>')
STYLE_RE = re.compile(r'\s*style="([^"]*)"')
STRIP_DECLS = re.compile(r'(background|border-top|border-bottom)\s*:[^;]*;?')


def palette_for(rel_path):
    p = rel_path.replace(os.sep, "/")
    if p == "index.html":
        return HOME
    if re.match(r"^(services|products)/[^/]+/index\.html$", p):
        return DETAIL
    if p == "about/index.html":
        return ABOUT
    if p == "contact/index.html":
        return SINGLE_LIGHT
    if p in ("privacy-policy/index.html", "terms-of-service/index.html"):
        return SINGLE_ALT
    return HUB


def clean_style(style):
    if not style:
        return ""
    style = STRIP_DECLS.sub("", style)
    # Tech-stack strip used a tight top padding that only worked on one shared background.
    style = style.replace("padding-top:10px;padding-bottom:50px;", "")
    return style.strip()


def apply(rel_path):
    path = os.path.join(ROOT_DIR, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    seq = palette_for(rel_path)
    idx = {"n": 0}

    def repl(m):
        n = idx["n"]
        idx["n"] += 1
        if n < len(seq):
            theme = seq[n]
        else:
            theme = "light" if n % 2 == 0 else "alt"
        rest = m.group(1)
        sm = STYLE_RE.search(rest)
        style = clean_style(sm.group(1)) if sm else ""
        rest = STYLE_RE.sub("", rest)
        style_attr = f' style="{style}"' if style else ""
        return f'<section class="sec theme-{theme}"{style_attr}{rest}>'

    new_html = SECTION_RE.sub(repl, html)

    # CTA band is always a blue card.
    new_html = new_html.replace('class="card cta-band rv"', 'class="card cta-band theme-blue rv"')

    if new_html != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
    return idx["n"]


def main():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("scripts", "assets", "node_modules")]
        for name in files:
            if name == "index.html" or name == "404.html":
                rel = os.path.relpath(os.path.join(root, name), ROOT_DIR)
                apply(rel)
                count += 1
    print(f"Applied white/black/blue section themes to {count} pages.")


if __name__ == "__main__":
    main()

"""Generate the social preview card for the grounding-verifier write-up.

WHY IT CARRIES NO NUMBERS.

The first version of this card was hand-made and had four figures painted on
it. Within one review round every one of them was wrong: it advertised
"27.35% -> 0.00%" and "Nine instances" after the page had moved to
32.17% -> 5.75% and ten, and it led with 0.00% -- the single number the page
now spends a paragraph explaining it deliberately refuses to print, because it
is an engine check rather than a result.

So a share of that link put the retracted headline in the preview, on a page
whose subject is documents drifting away from the code. That is the same
failure as the hand-typed verdicts table, in a new artifact created while
fixing the hand-typed verdicts table.

Two ways out: regenerate the card from the eval on every change, or take the
numbers off it. Numbers off is better. A preview card is not a place anyone
should be reading a measurement from -- it cannot show a denominator, cannot
say which population it is over, and cannot be checked -- and a figure that
needs three qualifying sentences is exactly the figure that must not appear
without them. The card names the project and the idea. The page carries the
evidence, where it can be argued with.

Run:  python tools/make_og_image.py
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "img", "grounding-verifier-og.png")

# Site palette (assets/css/style.css, dark theme).
BG = (13, 16, 19)
GRID = (18, 21, 25)
TEXT = (235, 219, 178)
DIM = (168, 160, 145)
FAINT = (124, 118, 106)
ACCENT = (131, 165, 152)     # --accent
AMBER = (215, 153, 33)       # --accent-2


def _font(names, size):
    for n in names:
        p = os.path.join(r"C:\Windows\Fonts", n)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def build():
    mono = lambda s: _font(["consola.ttf"], s)
    sans = lambda s: _font(["segoeui.ttf", "arial.ttf"], s)
    sansb = lambda s: _font(["seguisb.ttf", "segoeuib.ttf", "arialbd.ttf"], s)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill=GRID)
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill=GRID)

    d.text((64, 60), "KIMSKAW  ·  AI SAFETY", font=mono(20), fill=FAINT)

    d.text((64, 116), "A Safety Gate for AI", font=sansb(64), fill=TEXT)
    d.text((64, 190), "That Takes Action", font=sansb(64), fill=TEXT)

    d.text((64, 296), "A deterministic check on what an AI proposes to do.",
           font=sans(30), fill=DIM)
    d.text((64, 340), "No model inside the check, so it cannot hallucinate",
           font=sans(30), fill=DIM)
    d.text((64, 380), "the decision.", font=sans(30), fill=DIM)

    d.line([(64, 452), (150, 452)], fill=ACCENT, width=3)

    # No count here either. It was "Nine", then "Ten", then "Eleven"
    # within three review rounds -- a number on a preview card is a
    # number nobody will remember to change.
    d.text((64, 480), "One fail-open bug, found again and again,", font=sans(28), fill=TEXT)
    d.text((64, 518), "and the four-line rule that finally caught it.",
           font=sans(28), fill=AMBER)

    d.text((64, 574),
           "grounding-verifier  ·  lab Azure Sentinel tenant  ·  stdlib Python",
           font=mono(19), fill=FAINT)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    return OUT


if __name__ == "__main__":
    path = build()
    print("%s  %d bytes" % (path, os.path.getsize(path)))

"""Generate the social preview cards for the site and the grounding-verifier write-up.

WHY IT CARRIES NO NUMBERS.

The first version of this card was hand-made with four figures painted on it.
Within one review round every one of them was stale: it was still advertising
an old ratio and an old instance count after the page had moved on, and it led
with the one number the page now spends a paragraph explaining it deliberately
refuses to print, because that number is an engine check rather than a result.

So sharing the link put a retracted headline in the preview, on a page whose
subject is documents drifting away from the code. The same failure as the
hand-typed verdicts table, in a new artifact created while fixing the
hand-typed verdicts table.

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
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "grounding-verifier-og.png")
OUT_SITE = os.path.join(ROOT, "assets", "img", "site-og.png")

# Site palette (assets/css/style.css, dark theme).
BG = (13, 16, 19)
GRID = (18, 21, 25)
TEXT = (235, 219, 178)
DIM = (168, 160, 145)
FAINT = (124, 118, 106)
ACCENT = (131, 165, 152)     # --accent
AMBER = (215, 153, 33)       # --accent-2


# Searched in order. The Windows faces are what the cards were designed
# against; the rest keep the output legible for anyone who clones this.
FONT_DIRS = [
    r"C:\Windows\Fonts",
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts",
    "/System/Library/Fonts/Supplemental",
    "/System/Library/Fonts",
    "/Library/Fonts",
]


def _font(names, size):
    """First of `names` that exists in any font dir, else PIL's default.

    The default is bitmap and ignores `size`, so a missing font is visible
    rather than silently producing a card at the wrong scale.
    """
    for n in names:
        for d in FONT_DIRS:
            path = os.path.join(d, n)
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    pass
    return ImageFont.load_default()


MONO = ["consola.ttf", "DejaVuSansMono.ttf", "LiberationMono-Regular.ttf", "Menlo.ttc", "Courier New.ttf"]
SANS = ["segoeui.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf", "Helvetica.ttc", "Arial.ttf", "arial.ttf"]
SANSB = ["seguisb.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf"]


def build():
    mono = lambda s: _font(MONO, s)
    sans = lambda s: _font(SANS, s)
    sansb = lambda s: _font(SANSB, s)

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

    # No count here either. It changed in three consecutive review
    # rounds -- a number on a preview card is a number nobody will
    # remember to change.
    d.text((64, 480), "One fail-open bug, found again and again,", font=sans(28), fill=TEXT)
    d.text((64, 518), "and the four-line rule that finally caught it.",
           font=sans(28), fill=AMBER)

    d.text((64, 574),
           "grounding-verifier  ·  lab Azure Sentinel tenant  ·  stdlib Python",
           font=mono(19), fill=FAINT)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    return OUT


def build_site():
    """The card for the site root, shared far more often than any project page.

    Same rule as the write-up card: it names the work and the idea, and carries
    no measurement. It is a first impression, not evidence.
    """
    mono = lambda s: _font(MONO, s)
    sans = lambda s: _font(SANS, s)
    sansb = lambda s: _font(SANSB, s)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill=GRID)
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill=GRID)

    d.text((64, 60), "KIMSKAW  ·  CLOUD & SECURITY ENGINEERING", font=mono(20), fill=FAINT)

    d.text((64, 128), "Builds things that", font=sansb(72), fill=TEXT)
    d.text((64, 212), "run themselves.", font=sansb(72), fill=TEXT)

    d.text((64, 330), "Securing and automating Microsoft cloud environments,",
           font=sans(30), fill=DIM)
    d.text((64, 372), "and AI that gets verified rather than trusted.",
           font=sans(30), fill=DIM)

    d.line([(64, 452), (150, 452)], fill=ACCENT, width=3)

    d.text((64, 484), "Entra ID  ·  Sentinel  ·  Purview  ·  Defender  ·  Intune",
           font=sans(28), fill=TEXT)
    d.text((64, 526), "Probative  ·  grounding-verifier  ·  a Raspberry Pi that runs the lab",
           font=sans(28), fill=AMBER)

    d.text((64, 574), "kimskaw.github.io", font=mono(19), fill=FAINT)

    os.makedirs(os.path.dirname(OUT_SITE), exist_ok=True)
    img.save(OUT_SITE, "PNG", optimize=True)
    return OUT_SITE


if __name__ == "__main__":
    for path in (build(), build_site()):
        print("%s  %d bytes" % (path, os.path.getsize(path)))

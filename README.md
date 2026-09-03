# kimskaw.github.io

Personal portfolio, cloud & security engineering, self-hosted infrastructure, and AI project write-ups.

Hand-built static site: vanilla HTML/CSS/JS, no build step, no frameworks, no trackers.

## Structure

```
index.html                     single page: hero / certs / work / stack / contact
projects/probative.html          LLM triage pipeline write-up (inlined SVG pipeline diagram)
projects/grounding-verifier.html  the safety gate extracted from Probative
projects/home-server.html         Raspberry Pi infrastructure write-up
assets/css/style.css           design system (Gruvbox palette, v4 structure)
assets/js/main.js              theme toggle, mobile nav, scroll reveal, scrollspy
assets/img/                    images (.webp used on pages, originals kept as source)
```

## Design system

Gruvbox palette on a one-accent, two-typeface, four-radius structure.

| Token group | Values |
|---|---|
| Accent | `--accent` blue (single primary), `--accent-2` amber for warnings only |
| Domain dots | `--dot-lab` / `--dot-cloud` / `--dot-ai`, wayfinding labels only, never card tinting |
| Type | Inter (variable 400–800) + IBM Plex Mono (400/500/600) |
| Scale | `--fs-h1` … `--fs-xs`, spacing `--s1`…`--s9` on a 4px base, radii `--r1`…`--r4` |
| Elevation | one `--shadow` token, hover only |

Dark is the default surface. Light theme is a designed second surface under `[data-theme="light"]`,
and the initial theme follows `prefers-color-scheme` unless the visitor has toggled it.

## Conventions

- Every page carries `canonical`, `theme-color`, and Open Graph tags.
- Images ship as `.webp` with explicit `width`/`height` and `loading="lazy"` below the fold.
- Article prose runs the full content width (`--content-max`, 1240px), matching tables and diagrams.
- Nav markup is duplicated per page (no build step), change it in `index.html` and all of `projects/*.html` together.

## Local preview

```bash
python -m http.server 8899
# http://localhost:8899/
```

## Copy conventions

- No em dashes: use a colon for label/definition, a comma for an aside, a semicolon or full stop to join clauses, parentheses for a true parenthetical.
- Finding cards are capped at two sentences.

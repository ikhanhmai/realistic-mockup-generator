---
name: realistic-mockup-generator
description: Generate photorealistic product mockups with a brand logo realistically integrated into 3D surfaces — not flat overlays. Uses Gemini Nano Banana Pro (gemini-3-pro-image-preview) with IMAGE-REFERENCE INPUT so the exact logo is preserved, combined with explicit 3D-integration prompt engineering to force proper curvature wrap, lighting match, material infusion, and perspective. Activate when user asks for: product mockups, brand mockups, apparel mockups, packaging mockups, signage mockups, sticker mockups, realistic logo application on products, or any "place logo on X" task where flat compositing looks fake.
---

# Realistic Mockup Generator

Generate commercial-grade product mockups where a brand logo appears as if it's **truly printed/adhered to the product surface** with proper 3D integration — not a flat digital overlay.

## The Problem This Solves

Generic AI image generators have two failure modes:
1. **Redesign the logo** — asked to "put a logo", the AI creates a new/different logo every time
2. **Flat overlay** — compositing the logo as a 2D sticker on top looks obviously pasted, ignoring surface curvature, lighting, material

This skill solves both by:
1. Passing the actual logo PNG as a **reference image input** to the Gemini model (preserves exact design)
2. Using a **precise 3D-integration prompt template** that demands curvature wrap, lighting match, material infusion, perspective

## When to Use

| Task | Fit? |
|------|------|
| "Generate a mockup of our logo on a laptop" | ✅ Primary use case |
| "Put the brand on a water bottle / t-shirt / mug / tote bag" | ✅ |
| "Create signage mockup for storefront" | ✅ |
| "Apply logo to packaging/label" | ✅ |
| "Design a new logo" | ❌ Use `logo-design` skill |
| "Generic product photo without branding" | ❌ Use `ai-artist` / `ai-multimodal` directly |
| "Social media ad image" | ❌ Use `banner-design` |

## Quick Start

```bash
# Rasterize SVG logo to PNG first (Nano Banana accepts PNG input)
magick logo.svg -background none -resize 1024x logo-1024.png

# Generate mockup
python3 scripts/generate.py \
  --logo logo-1024.png \
  --product laptop \
  --output laptop-mockup.png \
  --aspect 4:3
```

## Supported Product Types (Built-in Templates)

| `--product` | Description | Aspect |
|-------------|-------------|--------|
| `laptop` | MacBook on desk, sticker application with perspective | 4:3 |
| `bottle` | Matte white water bottle, cylindrical print wrap | 3:4 |
| `tshirt` | Folded cotton tee flat-lay, fabric print | 1:1 |
| `duffel` | Athletic gym bag, large side-panel print | 4:3 |
| `shopfront` | Modern building awning signage | 16:9 |
| `fb-cover` | Stadium badminton court banner | 16:9 |
| `mug` | Ceramic coffee mug, cylindrical wrap | 1:1 |
| `tote` | Canvas tote bag, screen print | 4:5 |
| `businesscard` | Premium card on surface, pad print | 3:2 |
| `custom` | Provide your own prompt via `--prompt` | any |

## Key Technique (Prompt Engineering)

Every template enforces these **6 critical directives**:

1. **Use EXACT logo from reference** — "Do not redesign, restyle, or modify any element"
2. **Curvature / Perspective match** — Logo bends with surface geometry
3. **Lighting integration** — Same light direction/intensity as scene
4. **Material infusion** — Reads as part of surface (print, not sticker) OR with realistic sticker edge
5. **Appropriate sizing/positioning** — Centered on hero surface, natural scale
6. **Protected logo integrity** — Explicit "do not alter colors/text/proportions"

See `references/prompt-templates.md` for full template library.

## Dependencies

- **API key**: `GEMINI_API_KEY` in environment or `.env` (loaded from repo's `.claude/.env`)
- **Model**: `gemini-3-pro-image-preview` (Nano Banana Pro — best for high-quality + image input)
- **SDK**: `google-genai` (installed in project venv)
- **Logo format**: PNG with alpha channel recommended (1024px long edge)

## Workflow

```
┌──────────────────────┐
│  Your Brand Logo     │
│  (SVG or PNG)        │
└──────────┬───────────┘
           │ Rasterize SVG → PNG (ImageMagick)
           ▼
┌──────────────────────┐
│  logo-1024.png       │
│  (1024px, RGBA)      │
└──────────┬───────────┘
           │
           │  + Product-specific prompt template
           │  + Reference image input
           ▼
┌──────────────────────┐
│  Gemini Nano Banana  │
│  Pro (image + text)  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Photorealistic      │
│  mockup PNG with     │
│  logo integrated 3D  │
└──────────────────────┘
```

## Example Output

A laptop mockup generated with this skill shows the logo:
- Conforming to lid's 15° perspective angle
- Receiving warm golden-hour window light
- Soft edge shadow indicating sticker thickness
- Subtle laminate highlight matching scene
- Logo artwork 100% identical to source

Compare to a flat-composite overlay which looks obviously pasted on.

## Tips & Tricks

- **Iterate on position words**: "upper-center", "chest-height", "40% from top" — be specific
- **Force material semantics**: "silk-screen print infused into fabric" vs "vinyl die-cut sticker with 3mm border"
- **Match light direction**: Include the scene's light source in logo integration directive
- **Protect text**: Gemini may slightly restyle text — reinforce "do not alter italic DK-26 text"
- **Iterate if needed**: If output fails, retry with stronger directives — "DO NOT redesign", "MUST match reference"

## References

| File | Purpose |
|------|---------|
| `references/prompt-templates.md` | Full prompt templates for each product type |
| `scripts/generate.py` | Main CLI script |

## Related Skills

- `logo-design` — when you need to DESIGN a logo (not apply existing one)
- `ai-artist` — for non-product creative image generation
- `ai-multimodal` — for blank photo/scene generation (no logo integration)
- `cip-design` — for full corporate identity program deliverables
- `banner-design` — for ad/social banner composition

## Known Limitations

- Gemini occasionally reinterprets small logo elements (e.g., subtle text) — use higher-res reference PNG (1024px+)
- Very complex surfaces (mesh fabric, extreme curvature) may require iteration
- Animation/multi-frame mockups not supported — static images only
- Fully transparent logo backgrounds work best (PNG with alpha)

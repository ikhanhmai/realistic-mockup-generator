# Realistic Mockup Generator

Generate **photorealistic product mockups** where your brand logo appears as if it's truly printed, adhered, or embossed on real products — not a flat digital overlay.

Uses **Google Gemini** (Nano Banana Pro) with a reference-image technique that preserves your **exact logo** while integrating it with proper 3D perspective, lighting, surface curvature, and material properties.

## Why This Exists

When you ask AI image generators to "put a logo on a laptop," two things go wrong:

1. **The AI redesigns your logo** — it creates something similar but not your actual logo
2. **It looks flat** — no perspective, no lighting match, no surface integration

This tool solves both:
- Your logo PNG is passed as a **reference image** — preserved exactly
- A **6-directive prompt template** forces proper 3D integration

## Quick Start

### 1. Get a Gemini API Key (free)

Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and click "Create API Key." Copy it.

### 2. Install

```bash
git clone https://github.com/ikhanhmai/realistic-mockup-generator.git
cd realistic-mockup-generator
pip install google-genai
```

### 3. Set your API key

**Mac/Linux:**
```bash
export GEMINI_API_KEY="paste-your-key-here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=paste-your-key-here
```

Or create a file called `.env` in the project folder:
```
GEMINI_API_KEY=paste-your-key-here
```

### 4. Prepare your logo

Your logo should be a **PNG image file**, ideally:
- At least **1024 pixels** wide
- With a **transparent background**

> Don't have a PNG? Open your logo in any image editor (even Paint) and "Save As" PNG.

### 5. Generate your first mockup

```bash
python generate.py \
  --logo my-logo.png \
  --product laptop \
  --brand "My Brand" \
  --output laptop-mockup.png
```

Wait ~15-30 seconds. Your mockup is saved as `laptop-mockup.png`.

## Product Types

| Command | What You Get |
|---------|-------------|
| `--product laptop` | MacBook on desk, logo as vinyl sticker on lid |
| `--product bottle` | White water bottle, logo as printed graphic |
| `--product tshirt` | Navy + orange t-shirts, logo as chest print |
| `--product duffel` | Athletic gym bag, logo on side panel |
| `--product shopfront` | Modern building, logo on signage |
| `--product fb-cover` | Stadium court, logo in banner position |
| `--product mug` | Ceramic coffee mug, logo as print |
| `--product tote` | Canvas tote bag, logo as screen-print |
| `--product businesscard` | Premium card, logo as offset print |
| `--product custom` | Your own description (add `--prompt "..."`) |

### Examples

```bash
# Water bottle
python generate.py --logo logo.png --product bottle --brand "Acme" -o bottle.png

# T-shirts
python generate.py --logo logo.png --product tshirt --brand "Acme" -o shirts.png

# Shop signage
python generate.py --logo logo.png --product shopfront --brand "Acme" -o store.png

# Custom scene
python generate.py --logo logo.png --product custom \
  --prompt "A leather notebook on marble desk, logo embossed on cover" \
  --aspect 4:3 -o notebook.png

# Batch: all products at once
for p in laptop bottle tshirt duffel shopfront mug; do
  python generate.py --logo logo.png --product $p --brand "Acme" -o mockup-$p.png
done
```

## How It Works

```
Your Logo (PNG) ──► Sent as REFERENCE IMAGE to Gemini
                    (model sees your exact logo, not a text description)
                         +
                    Product-specific prompt template
                    (scene + 6 integration directives)
                         │
                         ▼
                    Google Gemini generates photorealistic scene
                    with logo integrated into 3D surface
                         │
                         ▼
                    Output: Mockup PNG
```

### The 6 Integration Directives

Every template enforces these for realism:

1. **Perspective / Curvature** — logo follows surface geometry
2. **Lighting** — logo receives same light as the scene
3. **Material** — how the logo is applied (sticker, screen-print, ceramic glaze, etc.)
4. **Size & Position** — real-world scale and placement
5. **Edge Treatment** — sticker border vs flush print
6. **Logo Integrity** — explicit "do not redesign" instruction

## All Options

```
python generate.py --help

  --logo LOGO        Path to your logo PNG (1024px+ recommended)
  --product PRODUCT  Product type (see table) or "custom"
  --brand BRAND      Your brand name
  --output, -o       Where to save the output PNG
  --prompt PROMPT    Custom scene description (for --product custom)
  --aspect ASPECT    Override aspect ratio (e.g. 4:3, 16:9, 1:1)
```

## Tips for Best Results

| Tip | Why |
|-----|-----|
| Use high-res PNG (1024px+) | More detail for Gemini to reproduce |
| Transparent background | Blends naturally with product surface |
| Simple, high-contrast logos | Reproduce most faithfully |
| Retry if result isn't perfect | AI generation has variance |
| Include `--brand` flag | Reinforces logo identity in prompt |

## FAQ

**Is this free?**
The tool is free and open source (MIT). You need a Gemini API key — the [free tier](https://ai.google.dev/pricing) works for many mockups.

**How is this different from Canva mockups?**
Canva pastes your logo flat on top of a template. This tool generates the scene with your logo **physically integrated** into the 3D surface — with real lighting, shadows, and material properties.

**Can I use the generated images commercially?**
The tool is MIT licensed. Generated images are subject to [Google's Gemini terms](https://ai.google.dev/terms).

**Can I add new product types?**
Yes! See [templates/PROMPT_TEMPLATES.md](templates/PROMPT_TEMPLATES.md) for the template format. PRs welcome.

## Writing Custom Templates

See [templates/PROMPT_TEMPLATES.md](templates/PROMPT_TEMPLATES.md) for the full guide.

Key structure for any new product:
```
CRITICAL INSTRUCTION: Use this EXACT logo from reference image...
SCENE: [camera, lighting, environment details]
LOGO INTEGRATION:
  1) Perspective/Curvature
  2) Lighting match
  3) Material type
  4) Size/Position
  5) Edge treatment
  6) Logo integrity
```

## Contributing

PRs welcome! Ideas:
- New product templates (packaging, vehicle wrap, cap/hat, jersey, etc.)
- Improved prompts for existing products
- Batch generation mode
- Support for additional AI models

## License

MIT — see [LICENSE](LICENSE)

## Credits

Built with [Google Gemini](https://ai.google.dev/) image generation API.

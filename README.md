# Realistic Mockup Generator — Claude Code Skill

A **Claude Code skill** that generates photorealistic product mockups where your brand logo is truly integrated into 3D surfaces — not a flat digital overlay.

Uses **Google Gemini Nano Banana Pro** with image-reference input to preserve your **exact logo** while integrating it with proper 3D perspective, lighting, curvature, and material properties.

## What Is a Claude Code Skill?

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) is Anthropic's CLI for AI-powered development. **Skills** are reusable knowledge + scripts that Claude Code can activate automatically when relevant. When you install this skill, Claude will automatically use it whenever you ask for product mockups.

## Installation

### Option A: Copy into your project (recommended)

```bash
# From your project root
mkdir -p .claude/skills
cp -r realistic-mockup-generator/.claude/skills/realistic-mockup-generator .claude/skills/
```

### Option B: Clone directly

```bash
cd your-project
git clone https://github.com/ikhanhmai/realistic-mockup-generator.git /tmp/rmg
cp -r /tmp/rmg/.claude/skills/realistic-mockup-generator .claude/skills/
rm -rf /tmp/rmg
```

### Option C: For Claude Teams / Organizations

1. Go to your Claude Teams workspace settings
2. Navigate to **Skills** or **Shared Resources**
3. Upload the `.claude/skills/realistic-mockup-generator/` folder
4. All team members can now use the skill in their Claude Code sessions

## Setup

### 1. Get a Gemini API Key (free)

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Click **"Create API Key"**
3. Copy the key

### 2. Add the key to your project

Create or edit `.claude/.env` in your project:

```
GEMINI_API_KEY=your-api-key-here
```

### 3. Install Python dependency

```bash
pip install google-genai
```

### 4. Prepare your logo

Your logo should be a **PNG file** (1024px+ recommended, transparent background).

Convert SVG to PNG if needed:
```bash
magick your-logo.svg -background none -resize 1024x your-logo.png
```

## Usage

### Natural Language (just ask Claude)

Once installed, simply ask Claude Code in natural language:

```
"Generate a realistic mockup of our logo on a laptop"
"Create a water bottle mockup with our brand"
"Make a t-shirt mockup with this logo"
"Put our logo on a shop front signage"
```

Claude will automatically activate the `realistic-mockup-generator` skill.

### Direct CLI Usage

```bash
python .claude/skills/realistic-mockup-generator/scripts/generate.py \
  --logo path/to/logo.png \
  --product laptop \
  --brand "Your Brand" \
  --output mockup.png
```

### Product Types

| `--product` | Description | Aspect |
|-------------|-------------|--------|
| `laptop` | MacBook on desk, logo as vinyl sticker | 4:3 |
| `bottle` | White water bottle, logo as print | 3:4 |
| `tshirt` | Navy + orange tees, chest screen-print | 1:1 |
| `duffel` | Athletic gym bag, side panel print | 4:3 |
| `shopfront` | Building signage on navy board | 16:9 |
| `fb-cover` | Stadium court banner | 16:9 |
| `mug` | Ceramic mug, cylindrical print | 1:1 |
| `tote` | Canvas tote, screen-print | 4:5 |
| `businesscard` | Premium card, offset print | 3:2 |
| `custom` | Your own prompt (`--prompt "..."`) | any |

### Examples

```bash
SCRIPT=".claude/skills/realistic-mockup-generator/scripts/generate.py"

# Single mockup
python $SCRIPT --logo logo.png --product bottle --brand "Acme" -o bottle.png

# Custom scene
python $SCRIPT --logo logo.png --product custom \
  --prompt "A leather notebook on marble desk, logo embossed on cover" \
  --aspect 4:3 -o notebook.png

# Batch: all products
for p in laptop bottle tshirt duffel shopfront mug; do
  python $SCRIPT --logo logo.png --product $p --brand "Acme" -o mockup-$p.png
done
```

## How It Works

```
Your Logo (PNG)
     │
     ├─ Passed as REFERENCE IMAGE to Gemini API
     │  (model sees your exact logo pixels, not a text description)
     │
     ├─ + Product-specific prompt template with 6 directives:
     │   1) Perspective / Curvature match
     │   2) Lighting integration
     │   3) Material type (sticker, print, emboss, etc.)
     │   4) Size & Position
     │   5) Edge treatment
     │   6) "Do NOT redesign the logo" enforcement
     │
     ▼
Google Gemini (gemini-3-pro-image-preview)
     │
     ▼
Photorealistic mockup PNG
(logo integrated into 3D surface with real lighting)
```

## File Structure

```
.claude/skills/realistic-mockup-generator/
├── SKILL.md                     ← Skill entry point (Claude reads this)
├── scripts/
│   └── generate.py              ← Main CLI script with 9 product templates
└── references/
    └── prompt-templates.md      ← Full prompt template library
```

### What Each File Does

| File | Purpose |
|------|---------|
| `SKILL.md` | Tells Claude Code **when** to activate this skill and **how** to use it. Claude reads this automatically. |
| `scripts/generate.py` | The actual Python script that calls Gemini API with your logo + prompt template. |
| `references/prompt-templates.md` | Full prompt library for all 9 product types + guide for writing custom templates. |

## Customization

### Add New Product Templates

Edit `references/prompt-templates.md` and add a new section following the template pattern. Then add the template to `generate.py`'s `TEMPLATES` dictionary.

### Modify Existing Templates

Each template has clearly labeled sections for scene description and the 6 integration directives. Tweak wording to change:
- **Lighting** (golden hour → studio → dramatic)
- **Material** (vinyl sticker → screen-print → embroidery)
- **Background** (home office → gym → studio)

### Use with Claude Teams

1. Install the skill in your team's shared `.claude/skills/` directory
2. All team members get access to realistic mockup generation
3. Brand-specific customizations can be added to the templates (your brand colors, typical products, etc.)

## Tips for Best Results

| Tip | Why |
|-----|-----|
| Logo PNG at 1024px+ | More detail for Gemini to reproduce |
| Transparent background | Blends naturally with product surface |
| High-contrast logos | Reproduce most faithfully |
| Retry on poor results | AI generation has variance |
| Include `--brand` flag | Reinforces logo identity in prompt |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `GEMINI_API_KEY missing` | Add key to `.claude/.env` or `export GEMINI_API_KEY=...` |
| `No module named 'google.genai'` | Run `pip install google-genai` |
| Logo looks different | Use higher-res PNG (2048px+), retry |
| Script not found | Check path: `.claude/skills/realistic-mockup-generator/scripts/generate.py` |
| Skill not activating | Ensure `SKILL.md` is in `.claude/skills/realistic-mockup-generator/` |

## FAQ

**Is this free?**
The skill is MIT licensed. You need a Gemini API key — [free tier](https://ai.google.dev/pricing) works for many mockups.

**Does this work with Claude Teams?**
Yes. Install the skill in your team's shared `.claude/skills/` directory. All members can use it.

**How is this different from Canva/Figma mockups?**
Traditional tools paste logos flat on templates. This generates scenes with logos **physically integrated** into 3D surfaces — real lighting, shadows, and material properties.

**Can I use generated images commercially?**
Tool is MIT licensed. Generated images are subject to [Google's Gemini terms](https://ai.google.dev/terms).

## Contributing

PRs welcome:
- New product templates (packaging, vehicle wrap, cap/hat, jersey, banner, etc.)
- Improved prompts for existing products
- Batch generation mode
- Support for additional AI models (DALL-E, Flux, etc.)

## License

MIT — see [LICENSE](LICENSE)

## Credits

Built with [Google Gemini](https://ai.google.dev/) image generation API.
Designed as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill.

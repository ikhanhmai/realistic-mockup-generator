#!/usr/bin/env python3
"""
Realistic Mockup Generator — Gemini Nano Banana Pro with image-reference input.

Produces photorealistic product mockups where a brand logo is integrated into 3D
surfaces with proper curvature, lighting, and material properties. The logo is
preserved EXACTLY (never redesigned) by passing it as a reference image input
to the Gemini model alongside detailed 3D-integration prompt directives.

Usage:
  python3 generate-realistic-mockup-with-reference-logo-and-3d-integration-prompting.py \
    --logo /path/to/logo.png \
    --product laptop \
    --brand "MyBrand" \
    --output mockup.png

Product types with built-in templates:
  laptop, bottle, tshirt, duffel, shopfront, fb-cover, mug, tote, businesscard

Custom prompt:
  python3 generate-realistic-mockup-with-reference-logo-and-3d-integration-prompting.py \
    --logo logo.png --product custom --prompt "..." --output out.png --aspect 4:3
"""

import argparse
import os
import sys
from pathlib import Path


def load_env():
    """Load .env from common locations (project .claude/.env, ~/.claude/.env)"""
    candidates = [
        Path.cwd() / ".claude" / ".env",
        Path(__file__).resolve().parent.parent.parent.parent / ".env",
        Path.home() / ".claude" / ".env",
    ]
    for p in candidates:
        if p.exists():
            for line in p.read_text().splitlines():
                if '=' in line and not line.strip().startswith('#'):
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"\''))
            return


# ============ PROMPT TEMPLATES ============

UNIVERSAL_INTEGRITY = """CRITICAL INSTRUCTION: The attached image is the {brand} logo. You MUST use this EXACT logo (same shape, colors, text, proportions) without modifying any element. Do NOT redesign, restyle, reinterpret, or recolor any part of it. Reproduce the logo artwork FAITHFULLY from the reference image.

"""

INTEGRITY_FOOTER = "\n\n6) LOGO ARTWORK MUST REMAIN EXACTLY AS REFERENCE — do not alter proportions, colors, text style, internal elements, or any design detail.\n\nOutput: commercial-grade product photograph. Ultra-realistic, 4K, sharp focus."

TEMPLATES = {
    "laptop": ("4:3", """SCENE: Photorealistic commercial product mockup of a silver aluminum MacBook Pro laptop, closed lid, 3/4 front angle, on a warm oak wooden desk in a modern home office. Natural golden-hour sunlight from left window casts soft diffused highlights on the aluminum. Shallow depth of field with houseplant, ceramic coffee mug, and leather desk pad softly blurred in background. Shot on Canon EOS R5 85mm f/1.8, cinematic editorial product photography.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) PERSPECTIVE: Sticker follows laptop lid perspective (~15° tilt away from camera). Sticker is slightly foreshortened to match lid plane.
2) LIGHTING: Receives same warm left-window light — highlights on left edge, soft shadow on right. Warm golden tint bleeds subtly into sticker.
3) MATERIAL: High-quality vinyl die-cut sticker with glossy laminate finish. Physically bonded to aluminum with subtle edge shadow showing 0.15mm thickness and minor ambient reflection on laminate surface.
4) SIZE/POSITION: Centered on lid (where Apple logo would be), ~10cm wide real-world scale.
5) EDGE: Thin white die-cut border (3mm) with soft cast shadow."""),

    "bottle": ("3:4", """SCENE: Photorealistic commercial product photograph of a premium matte white stainless steel sports water bottle standing upright on a seamless light gray studio background. Soft studio lighting with gentle gradient shadow beneath. Subtle highlight gradient along one side revealing cylindrical 3D form. Shot on Canon EOS R5 macro lens at f/8.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) CURVATURE WRAP: Logo MUST visually conform to cylindrical curvature. Edges near sides of visible bottle face appear slightly foreshortened/compressed — simulating a print following the 3D surface. Center flat-on, sides curve away.
2) LIGHTING: Receives same soft highlight gradient — slightly brighter on light-facing side, subtle shadow on opposite side.
3) MATERIAL: High-quality matte/semi-gloss print INFUSED INTO bottle's matte white finish. NOT a sticker — no edge shadow, no vinyl thickness. Print reads as part of bottle surface (silk-screen or UV print).
4) SIZE/POSITION: Centered horizontally, ~40% from top, width ~60% of visible bottle width.
5) EDGE: No edge shadow (it's a print, not a sticker)."""),

    "tshirt": ("1:1", """SCENE: Photorealistic flat-lay top-down product photography of two premium cotton crew-neck t-shirts folded neatly on clean light gray linen surface. LEFT shirt solid NAVY BLUE, RIGHT shirt solid ORANGE. Soft natural window light from above creating gentle fabric folds and subtle shadows showing cotton texture. Professional e-commerce merchandise shot.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM (apply to BOTH shirts identically):
1) FABRIC INTEGRATION: Logo follows subtle fabric drape and folds. Micro wrinkles visible on print matching fabric texture. Print ink sits ON fabric (slight raised feel) but follows contours.
2) LIGHTING: Same top-down soft window light — gentle highlight on raised folds, subtle shadow in creases.
3) MATERIAL: High-quality silk-screen print — matte ink finish, slightly raised texture above fabric, reads as absorbed into cotton weave.
4) SIZE/POSITION: Centered on chest of each folded shirt, ~30% of shirt width.
5) EDGE: Soft screen-print edge where ink meets fabric weave (slight micro bleed into fibers)."""),

    "duffel": ("4:3", """SCENE: Photorealistic product photograph of premium black athletic duffel gym bag with black nylon fabric, double handles, shoulder strap, side pocket. Bag on dark hardwood gym floor. 3/4 angle showing large flat front side panel. Dramatic directional studio lighting from left. Professional locker room blurred in background.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) FABRIC CONFORMITY: Logo follows nylon's subtle weave texture. Micro highlights match the weave pattern underneath.
2) LIGHTING: Same left directional studio light — logo's left side slightly brighter, right side darker.
3) MATERIAL: High-quality screen-print or heat-transfer on nylon — matte finish integrated with fabric. Slight raised ink texture.
4) SIZE/POSITION: Centered on front side panel, large — ~40-50% of panel width.
5) EDGE: Screen-print edge blending into nylon weave, no vinyl thickness."""),

    "shopfront": ("16:9", """SCENE: Photorealistic architectural photography of a modern facility storefront entrance. Polished concrete walls, large glass entrance doors revealing interior. Horizontal rectangular sign board above entrance — smooth matte navy blue material. Potted plants flank entrance. Natural daytime lighting, blue sky. Canon EOS R5 architectural shot.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) PERSPECTIVE: Logo on flat sign-board plane in proper architectural perspective.
2) LIGHTING: Receives same natural daylight — soft ambient illumination, gentle top-down shadow. Color temperature matches sky (slightly cool).
3) MATERIAL: High-quality printed/painted signage — matte or semi-gloss finish. Integrated into sign-board surface (not floating sticker).
4) SIZE/POSITION: Centered on sign board, width ~30-40% of sign-board width.
5) EDGE: Clean painted/printed edge. No sticker border."""),

    "fb-cover": ("16:9", """SCENE: Photorealistic cinematic horizontal banner composition. Premium badminton court with green playing surface, crisp white lines, badminton net, stadium lighting, atmospheric lens flare. LEFT THIRD of image clean darker area (bokeh-like soft gradient) reserved as negative space. Editorial hero banner for social media cover.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) PERSPECTIVE: Logo is flat graphic overlay (not physically in scene) — crisp with subtle drop shadow separating from background.
2) LIGHTING: Mild warm glow around logo matching scene's light temperature. Subtle rim light on edges.
3) MATERIAL: Digital graphic overlay with slight glow/halo for visibility on complex background.
4) SIZE/POSITION: Centered in left-third negative space area. Width ~25-30% of banner width.
5) EDGE: Soft halo glow for contrast against busy background."""),

    "mug": ("1:1", """SCENE: Photorealistic product photo of a matte white ceramic coffee mug on wooden table, slight front-low angle. Soft window light from right creating warm highlights on the ceramic curve. Shallow depth of field with cozy cafe blur.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) CURVATURE WRAP: Logo conforms to mug's cylindrical surface. Edges on curved sides foreshortened.
2) LIGHTING: Same right-window warm light — gradient across logo matches mug's illumination.
3) MATERIAL: High-temperature ceramic print — matte finish, absorbed into ceramic glaze. Looks kiln-fired permanent.
4) SIZE/POSITION: Front-facing center, ~60% of visible mug width.
5) EDGE: No edge — ceramic print blends into glaze."""),

    "tote": ("4:5", """SCENE: Photorealistic product photo of natural beige canvas tote bag with leather handles, upright on clean surface. Soft daylight creating natural fabric texture highlights.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) FABRIC CONFORMITY: Logo follows canvas weave texture. Micro-highlights match underlying weave.
2) LIGHTING: Matches scene's soft daylight illumination.
3) MATERIAL: Screen-print ink absorbed into canvas weave. Slight ink raise.
4) SIZE/POSITION: Centered on front panel, ~45% of bag's visible width.
5) EDGE: Ink meets canvas with natural slight bleed into weave fibers."""),

    "businesscard": ("3:2", """SCENE: Photorealistic product photo of a premium business card resting at slight angle on clean neutral surface (wood or marble). Soft studio lighting showing card thickness and paper texture. Macro detail.

LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:
1) PERSPECTIVE: Logo flat on card surface, perspective matches card angle.
2) LIGHTING: Same soft studio light — subtle highlight on card face.
3) MATERIAL: High-quality offset print with crisp flat ink, slight paper absorption.
4) SIZE/POSITION: Centered on card with appropriate brand hierarchy.
5) EDGE: Clean offset-print edge."""),
}


def build_prompt(brand: str, product: str, custom: str = None) -> tuple:
    """Return (prompt_text, aspect_ratio) for the product type."""
    if product == "custom":
        if not custom:
            sys.exit("--prompt required when --product custom")
        return UNIVERSAL_INTEGRITY.format(brand=brand) + custom + INTEGRITY_FOOTER, None
    if product not in TEMPLATES:
        sys.exit(f"Unknown product: {product}. Choose: {', '.join(TEMPLATES.keys())}, custom")
    aspect, body = TEMPLATES[product]
    return UNIVERSAL_INTEGRITY.format(brand=brand) + body + INTEGRITY_FOOTER, aspect


def generate(logo_path: str, prompt: str, output: str, aspect: str):
    """Call Gemini with image reference + prompt, save output image."""
    load_env()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY missing — set in environment or .claude/.env")

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("Install google-genai: pip install google-genai")

    client = genai.Client(api_key=api_key)

    logo_bytes = Path(logo_path).read_bytes()
    mime = "image/png" if logo_path.lower().endswith(".png") else "image/jpeg"

    print(f"→ Logo: {logo_path} ({len(logo_bytes)} bytes, {mime})")
    print(f"→ Output: {output}, aspect: {aspect}")
    print(f"→ Model: gemini-3-pro-image-preview (Nano Banana Pro)")

    resp = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[
            types.Part.from_bytes(data=logo_bytes, mime_type=mime),
            prompt,
        ],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_config=types.ImageConfig(aspect_ratio=aspect),
        ),
    )

    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.mime_type.startswith("image/"):
            Path(output).parent.mkdir(parents=True, exist_ok=True)
            Path(output).write_bytes(part.inline_data.data)
            print(f"✓ Saved {Path(output).stat().st_size} bytes")
            return
    sys.exit("No image returned by model")


def main():
    parser = argparse.ArgumentParser(
        description="Generate photorealistic product mockups with exact logo integrated in 3D",
    )
    parser.add_argument("--logo", required=True, help="Path to logo PNG (1024px recommended)")
    parser.add_argument("--product", required=True,
                        choices=list(TEMPLATES.keys()) + ["custom"],
                        help="Product type (or 'custom' with --prompt)")
    parser.add_argument("--brand", default="the brand", help="Brand name for prompt context")
    parser.add_argument("--output", "-o", required=True, help="Output image path")
    parser.add_argument("--prompt", help="Custom prompt (required if --product custom)")
    parser.add_argument("--aspect", help="Override aspect ratio (e.g. 4:3, 16:9)")
    args = parser.parse_args()

    if not Path(args.logo).exists():
        sys.exit(f"Logo not found: {args.logo}")

    prompt, default_aspect = build_prompt(args.brand, args.product, args.prompt)
    aspect = args.aspect or default_aspect or "1:1"
    generate(args.logo, prompt, args.output, aspect)


if __name__ == "__main__":
    main()

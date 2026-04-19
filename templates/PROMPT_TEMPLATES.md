# Prompt Templates — 3D-Integrated Logo Mockups

Reusable prompt templates for each product type. All templates follow the same 6-directive structure that forces 3D realism while preserving the exact logo.

## Universal Directive Header (used in every template)

```
CRITICAL INSTRUCTION: The attached image is the {BRAND_NAME} logo. You MUST use
this EXACT logo (same shape, colors, text, proportions) without modifying any
element. Do NOT redesign, restyle, reinterpret, or recolor any part of it.
Reproduce the logo artwork FAITHFULLY from the reference image.
```

## The 6 Critical Integration Directives

Include these after the scene description in every prompt:

```
LOGO INTEGRATION REQUIREMENT — APPLY WITH FULL 3D PHOTOREALISM:

1) PERSPECTIVE/CURVATURE: Logo MUST conform to the surface's 3D geometry
   (perspective angle for flat surfaces, cylindrical wrap for curved surfaces,
   fabric drape for cloth). {SURFACE_SPECIFIC_DETAIL}

2) LIGHTING INTEGRATION: Logo surface receives SAME lighting as the scene —
   same light direction, intensity, color temperature, highlights, shadows.
   {LIGHT_SPECIFIC_DETAIL}

3) MATERIAL/SURFACE INTEGRATION: Logo appears as {MATERIAL_TYPE} — {DETAIL}.
   NOT a flat digital overlay.

4) SIZE AND POSITION: Logo centered at {POSITION}, approximately {SIZE_DETAIL}.

5) EDGE/BORDER TREATMENT: {EDGE_DETAIL} (e.g., subtle shadow for stickers,
   no edge for screen prints, thread indent for embroidery).

6) LOGO ARTWORK MUST REMAIN EXACTLY AS REFERENCE — do not alter proportions,
   colors, text style, internal elements, or any design detail.
```

---

## Template Library by Product Type

### 1. LAPTOP STICKER (aspect: 4:3)

```
CRITICAL INSTRUCTION: [UNIVERSAL HEADER]

SCENE: Photorealistic commercial product mockup of a silver aluminum MacBook
Pro laptop, closed lid, 3/4 front angle, on a warm oak wooden desk in a modern
home office. Natural golden-hour sunlight from left window casts soft diffused
highlights on the aluminum. Shallow depth of field with houseplant, ceramic
coffee mug, and leather desk pad softly blurred in background. Shot on Canon
EOS R5 85mm f/1.8, cinematic editorial product photography.

LOGO INTEGRATION:
1) PERSPECTIVE: Sticker follows laptop lid perspective (~15° tilt away from
   camera). Sticker is slightly foreshortened to match lid plane.
2) LIGHTING: Receives same warm left-window light — highlights on left edge,
   soft shadow on right. Warm golden tint bleeds subtly into sticker.
3) MATERIAL: High-quality vinyl die-cut sticker with glossy laminate finish.
   Physically bonded to aluminum with subtle edge shadow showing 0.15mm
   thickness and minor ambient reflection on laminate surface.
4) SIZE/POSITION: Centered on lid (where Apple logo would be), ~10cm wide
   real-world scale.
5) EDGE: Thin white die-cut border (3mm) with soft cast shadow.
6) [LOGO INTEGRITY DIRECTIVE]

Output: commercial-grade product photo. Ultra-realistic, 4K, sharp focus.
```

### 2. WATER BOTTLE (aspect: 3:4)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic commercial product photograph of a premium matte white
stainless steel sports water bottle standing upright on a seamless light gray
studio background. Soft studio lighting with gentle gradient shadow beneath.
Subtle highlight gradient along one side of the cylindrical bottle revealing
its curved 3D form. Shot on Canon EOS R5 with macro lens at f/8. 4K detail.

LOGO INTEGRATION:
1) CURVATURE WRAP: Logo MUST visually conform to cylindrical curvature. Edges
   near sides of visible bottle face appear slightly foreshortened/compressed,
   simulating a print following the 3D surface. Center appears flat-on, sides
   curve away from viewer.
2) LIGHTING: Receives same soft highlight gradient — slightly brighter on
   light-facing side, subtle shadow on opposite side. Gradient change
   matches bottle's cylindrical lighting.
3) MATERIAL: High-quality matte/semi-gloss print INFUSED INTO bottle's matte
   white finish. NOT a sticker — no edge shadow, no vinyl thickness. Print
   reads as part of bottle surface itself (silk-screen or UV print).
4) SIZE/POSITION: Centered horizontally on front, ~40% from top, logo width
   ~60% of visible bottle width.
5) EDGE: No edge shadow (it's a print, not a sticker).
6) [LOGO INTEGRITY DIRECTIVE]

Output: commercial product shot with logo as real printed graphic on
cylindrical surface.
```

### 3. T-SHIRTS FLAT-LAY (aspect: 1:1)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic flat-lay top-down product photography of two premium
cotton crew-neck t-shirts folded neatly on clean light gray linen surface.
LEFT shirt: solid NAVY BLUE. RIGHT shirt: solid ORANGE. Soft natural window
light from above creating gentle fabric folds and subtle shadows showing
cotton texture. Professional e-commerce merchandise shot.

LOGO INTEGRATION (apply to BOTH shirts):
1) FABRIC INTEGRATION: Logo follows subtle fabric drape and folds. Micro
   wrinkles visible on print surface matching shirt's fabric texture.
   Print ink sits ON fabric (slight raised feel) but follows fabric contours.
2) LIGHTING: Same top-down soft window light — gentle highlight on raised
   folds, subtle shadow in creases. Print receives same illumination.
3) MATERIAL: High-quality silk-screen print — matte ink finish, slightly
   raised texture above fabric surface, reads as absorbed into cotton weave.
4) SIZE/POSITION: Centered on chest of each folded shirt, ~30% of shirt
   width, clearly visible on the folded display.
5) EDGE: Soft screen-print edge where ink meets fabric weave (slight micro
   bleed into fibers).
6) [LOGO INTEGRITY DIRECTIVE] + BOTH logos must be IDENTICAL.

Output: professional apparel flat-lay with two identical logos on contrast shirts.
```

### 4. DUFFEL BAG (aspect: 4:3)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic product photograph of premium black athletic duffel gym
bag with black nylon fabric, double handles, shoulder strap, side pocket. Bag
sits on dark hardwood gym floor. 3/4 angle showing large flat front side panel.
Dramatic directional studio lighting from left with soft highlights and deep
shadows. Professional locker room/sports facility hinted in blurred background.

LOGO INTEGRATION:
1) FABRIC CONFORMITY: Logo follows nylon's subtle weave texture. Micro
   highlights within logo match the weave pattern underneath.
2) LIGHTING: Same left directional studio light — logo's left side slightly
   brighter, right side darker, matching bag's illumination curve.
3) MATERIAL: High-quality screen-print or heat-transfer on nylon — matte
   finish, visually integrated with fabric. Slight raised ink texture.
4) SIZE/POSITION: Centered on front side panel, large — ~40-50% of panel width.
5) EDGE: Screen-print edge blending into nylon weave, no vinyl thickness.
6) [LOGO INTEGRITY DIRECTIVE]

Output: editorial commercial sports equipment photo with logo printed on bag.
```

### 5. SHOP FRONT / SIGNAGE (aspect: 16:9)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic architectural photography of a modern facility storefront
entrance. Building has clean modern facade with polished concrete walls, large
glass entrance doors revealing interior. Above entrance: horizontal rectangular
sign board made of smooth matte {NAVY/etc} material. Potted plants flank the
entrance. Natural daytime lighting, soft shadows, blue sky. Canon EOS R5
architectural shot.

LOGO INTEGRATION:
1) PERSPECTIVE: Logo rendered on flat sign-board plane in proper perspective
   matching architectural viewing angle.
2) LIGHTING: Receives same natural daylight — soft ambient illumination,
   gentle top-down shadow. Color temperature matches sky (slightly cool).
3) MATERIAL: High-quality printed/painted signage — matte or semi-gloss
   finish. Integrated into sign-board surface (not a floating sticker).
   Slight weathering/ambient feel for realism.
4) SIZE/POSITION: Centered on sign board, logo width ~30-40% of sign-board width.
5) EDGE: Clean painted/printed edge. No sticker border.
6) [LOGO INTEGRITY DIRECTIVE]

Output: commercial real-estate architectural photo with integrated signage.
```

### 6. SOCIAL MEDIA COVER BANNER (aspect: 16:9)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic cinematic horizontal banner composition. {CONTEXT_SCENE
e.g. premium badminton court with green playing surface, crisp white lines,
badminton net, stadium lighting, atmospheric lens flare}. LEFT THIRD of image
is a clean darker area (bokeh-like soft gradient) reserved as negative space.
Editorial hero banner composition for social media cover.

LOGO INTEGRATION:
1) PERSPECTIVE: Logo is a flat graphic overlay (not physically in scene) —
   rendered crisp with subtle drop shadow separating from the background.
2) LIGHTING: Mild warm glow around logo matching scene's light temperature.
   Subtle rim light on logo edges.
3) MATERIAL: Digital graphic overlay with slight glow/halo for visibility
   on complex background.
4) SIZE/POSITION: Centered in left-third negative space area. Logo width
   ~25-30% of banner width.
5) EDGE: Soft halo glow for contrast against busy background.
6) [LOGO INTEGRITY DIRECTIVE]

Output: professional social media cover banner with logo in negative space.
```

### 7. MUG / CERAMIC (aspect: 1:1)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic product photo of a matte white ceramic coffee mug on a
wooden table surface, viewed from a slight front-low angle. Soft window light
from right creating warm highlights on the ceramic curve. Steam rising
optionally. Shallow depth of field with cozy cafe background blur.

LOGO INTEGRATION:
1) CURVATURE WRAP: Logo conforms to mug's cylindrical surface. Edges on
   curved sides appear foreshortened.
2) LIGHTING: Same right-window warm light — gradient across logo matches
   the mug's illumination.
3) MATERIAL: High-temperature ceramic print — matte finish, absorbed into
   ceramic glaze. Looks like kiln-fired permanent print.
4) SIZE/POSITION: Front-facing center of mug, ~60% of visible mug width.
5) EDGE: No edge — ceramic print blends into glaze.
6) [LOGO INTEGRITY DIRECTIVE]
```

### 8. TOTE BAG / CANVAS (aspect: 4:5)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic product photo of a natural beige canvas tote bag with
leather handles, positioned upright on a clean surface. Soft daylight creates
natural fabric texture highlights. Product photography aesthetic.

LOGO INTEGRATION:
1) FABRIC CONFORMITY: Logo follows canvas weave texture — micro-highlights
   within logo match underlying weave pattern.
2) LIGHTING: Matches scene's soft daylight illumination.
3) MATERIAL: Screen-print ink absorbed into canvas weave. Slight ink raise.
4) SIZE/POSITION: Centered on front panel, ~45% of bag's visible width.
5) EDGE: Ink meets canvas with natural slight bleed into weave fibers.
6) [LOGO INTEGRITY DIRECTIVE]
```

### 9. BUSINESS CARD (aspect: 3:2)

```
[UNIVERSAL HEADER]

SCENE: Photorealistic product photo of a premium business card laid flat or
resting at angle on a clean neutral surface (wood/marble/linen). Soft studio
lighting showing the card's thickness and paper texture. Macro detail.

LOGO INTEGRATION:
1) PERSPECTIVE: Logo flat on card surface, perspective matches card angle
   in frame.
2) LIGHTING: Same soft studio light — subtle highlight on card face.
3) MATERIAL: High-quality offset print, foil-stamp, or letterpress (specify).
   For foil: metallic reflection that catches scene light. For letterpress:
   slight indent into card with shadow. For offset: crisp flat print.
4) SIZE/POSITION: Centered on card, appropriate for brand hierarchy.
5) EDGE: Matches print method (clean for offset, shiny for foil, indented for
   letterpress).
6) [LOGO INTEGRITY DIRECTIVE]
```

---

## Authoring New Templates

When writing templates for new product types:

1. **Start with scene** — camera, lighting, environment, style references
2. **Identify surface type** — flat, curved, fabric, textured
3. **Pick material fit** — sticker, silk-screen, embroidery, foil stamp, UV print
4. **Map lighting direction** — tell model to match the scene's light source
5. **Specify size/position in real-world terms** — "10cm wide", "chest height"
6. **Reinforce logo integrity** at start AND end of prompt
7. **Test with 1 image first** before batch — verify lighting/curvature work

## Anti-Patterns to Avoid

- ❌ "Put the logo on the product" — too vague, AI will regenerate logo
- ❌ Just describing the logo in text — reference image input is critical
- ❌ Generic "photorealistic" without material specifics
- ❌ Not reinforcing logo-integrity directive (AI will drift)
- ❌ Asking for multiple different products in one prompt (split into batch)

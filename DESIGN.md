---
version: alpha
name: Playground-VoltAgent-inspired-design
description: A VoltAgent-inspired design direction for this static site: near-black canvas, electric green accent, restrained developer-tool layout, precise borders, and code-oriented visual details.

colors:
  primary: "#00d992"
  primary_soft: "#2fd6a1"
  primary_deep: "#10b981"
  on_primary: "#101010"
  ink: "#f2f2f2"
  ink_strong: "#ffffff"
  body: "#bdbdbd"
  mute: "#8b949e"
  hairline: "#3d3a39"
  canvas: "#101010"
  canvas_soft: "#1a1a1a"

typography:
  sans: "Inter, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
  mono: "SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
  display:
    size: "clamp(42px, 8vw, 72px)"
    weight: 400
    line_height: 1
    letter_spacing: 0
  heading:
    size: "clamp(28px, 4vw, 40px)"
    weight: 400
    line_height: 1.12
    letter_spacing: 0
  body:
    size: "16px"
    weight: 400
    line_height: 1.65
    letter_spacing: 0
  mono:
    size: "13px"
    weight: 400
    line_height: 1.55
    letter_spacing: 0

radius:
  small: "6px"
  medium: "8px"
  pill: "999px"

spacing:
  unit: "4px"
  page_x: "clamp(20px, 5vw, 48px)"
  section_y: "clamp(56px, 8vw, 96px)"

components:
  page:
    background: "{colors.canvas}"
    text: "{colors.ink}"
  nav:
    background: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    height: "64px"
  button_primary:
    background: "{colors.primary}"
    text: "{colors.on_primary}"
    radius: "{radius.small}"
    padding: "12px 16px"
  button_secondary:
    background: "transparent"
    text: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    radius: "{radius.small}"
    padding: "12px 16px"
  card:
    background: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    radius: "{radius.medium}"
    shadow: "none"
  code_panel:
    background: "{colors.canvas_soft}"
    border: "1px solid {colors.hairline}"
    radius: "{radius.medium}"
    font: "{typography.mono}"
---

# Design Direction

Use a continuous near-black surface with a single electric-green accent. The interface should feel like a polished developer tool: restrained, precise, readable, and code-aware.

## Visual Rules

- Use `#101010` as the dominant canvas.
- Reserve `#00d992` for primary calls to action, status marks, links, and active details.
- Use thin `#3d3a39` borders for structure.
- Keep corners tight: 6px for buttons, 8px for cards and code panels.
- Avoid decorative gradients, soft light patches, heavy shadows, glass panels, and large soft rounded cards.
- Use code snippets, terminal rows, status dots, metrics, and fine dividers as the main visual texture.

## Type Rules

- Use Inter or the system sans stack for all normal text.
- Use SF Mono or the system mono stack for code, commands, metrics, and small technical labels.
- Keep letter spacing at 0.
- Use regular-weight large headings. The design should read calm and technical.

## Layout Rules

- Build with full-width dark bands and a constrained inner container.
- Keep hero content useful in the first viewport: headline, short lead, actions, and a code/mock terminal visual.
- Cards should be individual repeated items only. Do not place cards inside cards.
- Feature sections should use clear grids with consistent gaps.
- Mobile layout should collapse to one column with touch targets of at least 44px.

## Copy Rules

- Write direct, concrete Chinese.
- Avoid promotional filler.
- Avoid contrast-pair sentence structures that sound like generated marketing copy.
- Prefer short product-like statements over abstract positioning.

---
name: pedi-design
description: Design, implement, or review Pedi-branded websites, mobile apps, product interfaces, internal tools, and marketing surfaces. Use when work must follow Pedi's visual identity, UI tokens, component conventions, responsive behavior, or accessibility standards; do not use for products unrelated to Pedi.
---

# Pedi Design

Create experiences that feel modern, dependable, accessible, friendly, and recognizably Pedi. Preserve the user's requested platform, framework, scope, and existing product behavior.

## Required reference

Read [references/design-system.md](references/design-system.md) before making visual or interaction decisions. It is the canonical source for Pedi colors, typography, spacing, shape, components, imagery, responsive behavior, accessibility, and motion.

When an existing Pedi implementation conflicts with the reference, do not silently replace an established product convention. Identify the conflict and use the supplied reference as the default unless the user or repository provides a newer authoritative rule.

## Workflow

1. Inspect the existing surface, design tokens, shared components, assets, and framework conventions before editing. Reuse established Pedi primitives when they conform to the reference.
2. Identify the primary user task and information hierarchy. Keep one clearly dominant action per screen or section, using Pedi Red deliberately rather than as decoration.
3. Apply the design system through reusable tokens or theme primitives where the codebase supports them. Avoid scattering unexplained literal values across components.
4. Adapt the experience for its context: consumer surfaces should feel spacious; admin and data-heavy surfaces may be denser without sacrificing readability.
5. Verify responsive states, keyboard focus, labels, contrast, touch targets, non-color status cues, loading and error states, and reduced-motion behavior where motion is present.
6. Review the result against the checklist below and validate it using the project's normal checks. When visual tooling is available, inspect the rendered result at representative mobile and desktop widths.

## Design decisions

- Consistency takes priority over novelty. Extend established patterns before inventing new ones.
- Pedi Red is the primary action and brand color; Pedi Navy supplies contrast and secondary emphasis. Semantic colors communicate state, not decoration.
- Use Outfit for display and high-emphasis UI, and Inter for functional, dense, or long-form content. Use readable fallbacks when the fonts are unavailable and do not claim the branded typography is complete until the fonts are loaded.
- Prefer whitespace, alignment, borders, and restrained elevation over heavy shadows, gradients, or decorative containers.
- Use rounded forms consistently without turning ordinary buttons, inputs, and cards into pills.
- Pair destructive wording with an icon or confirmation when warranted because the primary brand color is also red.
- Do not invent brand assets, photography rules, or product-specific interaction patterns that the reference does not define. Ask for or preserve authoritative assets when exact brand reproduction depends on them.

## Completion checklist

- The primary task and action hierarchy are immediately clear.
- Colors, type roles, spacing, radii, surfaces, and icon treatment follow the reference.
- Pedi Red is not overused and competing primary actions have been removed.
- Forms have visible labels, clear focus and validation states, and helpful errors.
- Status is communicated by text or icons in addition to color.
- Mobile is an adapted layout, not merely a shrunken desktop layout.
- Text remains readable, controls have adequate targets, and keyboard navigation is visible.
- Animation is subtle, fast, purposeful, and respects reduced-motion preferences when implemented.
- The result fits the surrounding Pedi product while remaining recognizably part of the same ecosystem.

# Pedi Brand and Design System

This is the canonical design reference for the `pedi-design` skill. Apply it across Pedi products, websites, mobile applications, internal systems, marketing materials, and other branded experiences.

Pedi should feel **modern, dependable, accessible, friendly, and distinctly Pedi**.

## 1. Brand principles

- **Simple:** Prioritize the user's primary task and avoid unnecessary visual complexity.
- **Approachable:** Use comfortable spacing, clear language, rounded forms, and thoughtful hierarchy rather than an overly corporate tone.
- **Trustworthy:** Make payments, bookings, transportation, events, and other important interactions clear, predictable, reliable, and transparent.
- **Consistent:** Keep colors, typography, spacing, components, interactions, and terminology coherent across the ecosystem.
- **Purposeful:** Every visual element should support the content or task. Decoration must not compete with primary actions.

## 2. Color tokens

| Role | Value | Use |
| --- | --- | --- |
| Pedi Red | `#DD1600` | Primary buttons, active navigation, important calls to action, brand highlights, selected states, appropriate links, and key branded elements |
| Pedi Navy | `#1B2E4B` | Secondary actions, navigation, dark sections, strong supporting elements, selected secondary states, and contrast with Pedi Red |
| Heading | `#313131` | Titles, headings, card titles, important values, and high-emphasis text |
| Paragraph | `#575757` | Body copy, descriptions, supporting information, and standard labels |
| Gray Accent | `#A7A9B7` | Secondary metadata, sufficiently contrasting borders, placeholders, low-emphasis elements, and disabled supporting content |
| Background | `#F9F9F9` | Default application and website background |
| White | `#FFFFFF` | Cards, modals, inputs, elevated surfaces, content containers, and text on sufficiently dark backgrounds |
| Success Green | `#00B81F` | Successful transactions, confirmed bookings, completed actions, positive statuses, and available or active states |
| Warning Yellow | `#FBBB00` | Warnings, pending states, attention indicators, and processing states |
| Information Blue | `#3B82F4` | Information, help, badges, neutral system notifications, and appropriate contextual links |
| Inactive Red | `#FFB4AB` | Inactive brand controls, subtle red backgrounds, selected backgrounds, and low-emphasis destructive states |

Visual priority is **Pedi Red → Pedi Navy → neutrals → semantic accents**.

- Keep Pedi Red recognizable by using it selectively against neutral backgrounds.
- Use semantic colors to communicate meaning, not decoration.
- Avoid several strong accents in one area unless status differentiation or data visualization requires them.
- Never rely on color alone for status; add a label, icon, pattern, or other cue.

## 3. Typography

### Typeface roles

- **Outfit** expresses the Pedi brand. Use it for display text, page and section headings, card titles, important numbers, prominent labels, buttons, and other high-emphasis UI. Recommended weights: 400 Regular, 500 Medium, 600 SemiBold, and 700 Bold. Prefer Medium and SemiBold over excessive Bold.
- **Inter** is the functional interface face. Use it for body copy, descriptions, form fields, tables, metadata, supporting labels, information-dense interfaces, and long-form content. Recommended weights: 400 Regular, 500 Medium, and 600 SemiBold.

### Type hierarchy

| Style | Typeface | Size | Weight | Typical use |
| --- | --- | --- | --- | --- |
| Display | Outfit | 40–48px | SemiBold or Bold | Major marketing statements and high-impact content |
| H1 | Outfit | 32px | SemiBold | Primary page heading |
| H2 | Outfit | 24px | SemiBold | Major section heading |
| H3 | Outfit | 20px | SemiBold | Subsection or card-group heading |
| H4 | Outfit | 18px | Medium or SemiBold | Card and component heading |
| Body Large | Inter | 16px | Regular | Prominent body content |
| Body | Inter | 14–16px | Regular | Default interface and body text |
| Small | Inter | 12–14px | Regular or Medium | Metadata, helper text, and supporting information |

Use a predictable hierarchy rather than choosing sizes independently for every screen. Do not reduce type excessively to fit more content; readability wins.

## 4. Spacing

Use a 4px-based system with these preferred tokens:

`4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64`

- 4–8px: tightly related elements.
- 12–16px: spacing inside smaller components.
- 20–24px: normal card and container padding.
- 32–48px: major content groups.
- 48–64px or more: major website sections.
- Prefer whitespace to unnecessary dividers.

## 5. Corners and shape

| Element | Radius |
| --- | --- |
| Small controls | 6–8px |
| Inputs and buttons | 8–12px |
| Cards | 12–16px |
| Large containers and modals | 16–20px |
| Pills and badges | Fully rounded |

Use the same radius for components with the same function. Pedi should feel modern and approachable, not excessively rounded. Do not use pill shapes for ordinary buttons, cards, or inputs.

## 6. Components

### Buttons

- **Primary:** Pedi Red (`#DD1600`) background with white (`#FFFFFF`) text. Reserve it for the most important action in a screen or section, such as Book Ride, Continue, Pay Now, or Confirm Booking.
- **Secondary:** Pedi Navy, a neutral surface, or an outline depending on context. Keep it subordinate to the primary action.
- **Tertiary:** Text or a subtle control for low-priority actions.
- **Destructive:** Use red intentionally and include clear wording. Because Pedi Red is also the brand color, add an icon or confirmation when appropriate to remove ambiguity.

### Cards and surfaces

- White surface.
- 12–16px radius.
- 16–24px internal padding.
- Subtle border or restrained shadow.
- Clear content hierarchy.

Cards organize information; they are not decoration. Avoid heavy shadows. Prefer spacing, borders, and subtle elevation.

### Forms

Every input needs a visible label, a clear and consistent focus state, inline validation, clear errors, and an adequate touch target. Add helpful placeholders only where useful; a placeholder never replaces the label. Keep form behavior simple and predictable.

### Icons

Use one consistent icon family within a product. Icons should be simple, recognizable, modern, visually aligned with adjacent text, and consistent in stroke weight. Do not mix filled, outlined, illustrated, and 3D styles within one functional interface. Icons support meaning and do not replace necessary labels.

## 7. Imagery and illustration

Choose imagery that is authentic, human, active, optimistic, clean, and relevant to the real Pedi experience. Avoid generic corporate stock photography. Keep illustrations and 3D assets stylistically consistent across an experience.

## 8. Layout and density

- Group related information and put important content before supporting content.
- Use strong alignment and predictable grids rather than arbitrary decorative positioning.
- Do not fill every available space.
- Consumer-facing products should generally feel spacious.
- Administrative and data-heavy products may be denser while remaining readable.

## 9. Responsive behavior

Design mobile-first where appropriate and adapt naturally across mobile, tablet, laptop, and desktop. Do not simply shrink a desktop layout. Reconsider navigation, tables, forms, action placement, and content hierarchy for each available width. Preserve comfortable mobile touch targets.

## 10. Accessibility

Accessibility is part of the design system, not an optional enhancement.

- Maintain sufficient text and control contrast.
- Make keyboard focus clearly visible.
- Associate accessible labels with form controls.
- Use meaningful button labels.
- Provide adequate touch targets.
- Keep content hierarchy logical.
- Pair status color with text, icons, or another cue.
- Place text on brand or accent colors only when the contrast remains readable.

## 11. Motion and interaction

Use subtle, fast motion to communicate loading, state transitions, success, expanding or collapsing content, navigation transitions, and contextual feedback. Motion should improve orientation or communicate state, not merely make an interface look dynamic.

## 12. Visual signature

A Pedi surface generally combines light neutral backgrounds, white surfaces, strong typography, Pedi Red primary actions, Pedi Navy contrast, restrained borders, soft elevation, comfortable whitespace, consistent rounded corners, and purposeful semantic colors. It should feel polished without becoming overly decorative.

## 13. Avoid

- Overusing Pedi Red.
- Decorative accent colors or arbitrary colors outside the system.
- Mixed icon styles.
- Excessive gradients or heavy shadows.
- Over-rounding every component.
- Crowding the interface with unnecessary information.
- Multiple competing primary actions.
- Sacrificing readability for visual style.
- Inconsistent spacing between similar components.

## 14. Consistency rule

Consistency takes priority over novelty. New components should reuse established colors, typography, spacing, interaction patterns, and visual principles whenever possible. Pedi products do not need to look identical, but moving between them should feel like moving within one recognizable ecosystem.

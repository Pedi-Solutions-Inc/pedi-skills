#!/usr/bin/env python3
"""Build Pedi token references from the Figma variable export.

Reads the Pedi collections in ../figma-variables and writes:
  references/tokens.css  CSS custom properties (light, dark, and system theme)
  references/tokens.md   Compact token tables for the skill to read

Typography is not in the Figma variable export, so it comes from
../typography.json. Edit that file to change fonts or the type scale.

Only the Pedi collections listed below are used. The other kit exports in
figma-variables/ (M3, Apple Appearance/Sizes, SDS, font themes) are ignored.

Usage: python3 scripts/build_tokens.py
"""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "figma-variables"
OUT = ROOT / "references"

PRIMITIVES = "Style.tokens.json"
LIGHT = "1. Color modes/Light mode.tokens.json"
DARK = "1. Color modes/Dark mode.tokens.json"
DIMENSIONS = {
    "Radius": "Mode 1.tokens.json",
    "Spacing": "Mode 1.tokens 2.json",
    "Width": "Mode 1.tokens 3.json",
    "Container": "Value.tokens.json",
}
TYPOGRAPHY = ROOT / "typography.json"
# Primitive ramps summarized in tokens.md; every ramp is still emitted to CSS.
MD_RAMPS = ["Base", "Brand", "Gray (light mode)", "Gray (dark mode)", "Error", "Warning", "Success", "Blue"]


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"\([^)]*\d+[^)]*\)", "", text)  # drop "(900)", "(1,024px)" hints
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    for key, child in node.items():
        if not key.startswith("$"):
            yield from walk(child, path + (key,))


def load(name):
    return json.loads((SRC / name).read_text())


def color(value):
    if isinstance(value, str):
        return value
    alpha = round(value.get("alpha", 1), 2)
    if alpha >= 1:
        return value["hex"].upper()
    r, g, b = (round(c * 255) for c in value["components"])
    return f"rgb({r} {g} {b} / {alpha:g})"


def primitive_var(figma_name):
    # "Colors/Brand/500" -> --color-brand-500
    return "--color-" + slug("-".join(figma_name.split("/")[1:]))


def semantic_var(path):
    # ("Colors", "Text", "text-primary (900)") -> --color-text-primary
    # ("Component colors", "Components", "Buttons", "Primary", "button-primary-bg") -> --color-button-primary-bg
    return "--color-" + slug(path[-1])


def resolve(token, index):
    """Return (display value, css value, alias label) for a semantic token."""
    value = token["$value"]
    if isinstance(value, str) and value.startswith("{"):
        ref = tuple(value.strip("{}").split("."))
        target = index[ref]
        display, _, _ = resolve(target, index)
        return display, f"var({semantic_var(ref)})", semantic_var(ref)
    alias = token.get("$extensions", {}).get("com.figma.aliasData", {}).get("targetVariableName")
    if alias and alias.startswith("Colors/"):
        return color(value), f"var({primitive_var(alias)})", primitive_var(alias)
    return color(value), color(value), ""


def typography_vars():
    """Return (css lines, md lines) for the settings in typography.json."""
    config = json.loads(TYPOGRAPHY.read_text())
    css, md = [], ["", "## Typography", "",
                   "Edit `typography.json` and rerun the script to change fonts or the scale. "
                   "Components use these variables, never literal font names or sizes.", "",
                   "| Token | Value |", "| --- | --- |"]
    for name, value in config["families"].items():
        css.append(f"  --font-family-{name}: {value};")
        md.append(f"| `--font-family-{name}` | `{value}` |")
    for name, value in config["weights"].items():
        css.append(f"  --font-weight-{name}: {value};")
        md.append(f"| `--font-weight-{name}` | {value} |")
    md += ["", "| Style | Family | Size / line height | Weight | Tracking |", "| --- | --- | --- | --- | --- |"]
    for name, style in config["styles"].items():
        css += [
            f"  --text-{name}-family: var(--font-family-{style['family']});",
            f"  --text-{name}-size: {style['size']}px;",
            f"  --text-{name}-line-height: {style['lineHeight']}px;",
            f"  --text-{name}-weight: var(--font-weight-{style['weight']});",
            f"  --text-{name}-tracking: {style['tracking']};",
        ]
        md.append(f"| `--text-{name}-*` | {style['family']} | {style['size']} / {style['lineHeight']}px "
                  f"| {style['weight']} | {style['tracking']} |")
    return css, md


def main():
    primitives = list(walk(load(PRIMITIVES)["Colors"], ("Colors",)))
    light = dict(walk(load(LIGHT)))
    dark = dict(walk(load(DARK)))

    names = {}
    for path in light:
        name = semantic_var(path)
        if name in names and names[name] != path:
            raise SystemExit(f"Duplicate token name {name}: {names[name]} and {path}")
        names[name] = path

    rows = []
    for path, token in light.items():
        rows.append((path, resolve(token, light), resolve(dark[path], dark)))

    # tokens.css
    css = ["/* Generated by scripts/build_tokens.py from figma-variables/ and typography.json. Do not edit. */", "", ":root {"]
    css.append("  /* Primitives */")
    for path, token in primitives:
        css.append(f"  {primitive_var('/'.join(path))}: {color(token['$value'])};")
    for label, file in DIMENSIONS.items():
        css.append(f"  /* {label} */")
        for path, token in walk(load(file)):
            css.append(f"  --{slug(path[-1])}: {token['$value']}px;")
    type_css, type_md = typography_vars()
    css.append("  /* Typography (typography.json) */")
    css += type_css
    css.append("  /* Semantic: light */")
    css.append("  color-scheme: light;")
    css += [f"  {semantic_var(p)}: {l[1]};" for p, l, _ in rows]
    css.append("}")
    dark_block = [f"  {semantic_var(p)}: {d[1]};" for p, _, d in rows]
    css += ["", "@media (prefers-color-scheme: dark) {", '  :root:not([data-theme="light"]) {', "    color-scheme: dark;"]
    css += ["  " + line for line in dark_block]
    css += ["  }", "}", "", ':root[data-theme="dark"] {', "  color-scheme: dark;"] + dark_block + ["}", ""]
    (OUT / "tokens.css").write_text("\n".join(css))

    # tokens.md
    md = [
        "# Pedi Design Tokens",
        "",
        "Generated by `scripts/build_tokens.py` from the Figma export in `figma-variables/`. Do not edit by hand; "
        "re-export from Figma and rerun the script. CSS custom properties for every token are in "
        "[tokens.css](tokens.css).",
        "",
        "Semantic tokens reference primitives, and components should use semantic tokens only. "
        "The alias column names the primitive or semantic token each value resolves from.",
        "",
        "## Primitive color ramps",
        "",
        "| Ramp | " + " | ".join(["25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]) + " |",
        "| --- |" + " --- |" * 12,
    ]
    ramps = load(PRIMITIVES)["Colors"]
    for ramp in MD_RAMPS:
        if ramp == "Base":
            continue
        values = [color(ramps[ramp][step]["$value"]) for step in ramps[ramp]]
        md.append(f"| {ramp} | " + " | ".join(f"`{v}`" for v in values) + " |")
    md.append("")
    md.append("Base: `--color-base-white` `#FFFFFF`, `--color-base-black` `#000000`, `--color-base-transparent`. "
              "Other ramps (Gray blue, Gray cool, Moss, Teal, Cyan, Indigo, Violet, Purple, Fuchsia, Pink, Rosé, "
              "Orange, Yellow, and others) are available in tokens.css for data visualization and utility badges only.")

    groups = {}
    for row in rows:
        path = row[0]
        group = path[1] if path[0] == "Colors" else path[2] if path[1] == "Components" else path[1]
        groups.setdefault((path[0], group), []).append(row)

    for (top, group), items in groups.items():
        if top == "Component colors" and group == "Utility":
            continue
        md += ["", f"## {'Semantic' if top == 'Colors' else 'Component'}: {group}", "",
               "| Token | Light | Light alias | Dark | Dark alias |", "| --- | --- | --- | --- | --- |"]
        for path, l, d in items:
            md.append(f"| `{semantic_var(path)}` | `{l[0]}` | {l[2] or '—'} | `{d[0]}` | {d[2] or '—'} |")

    utility = sorted({p[2] for p, _, _ in rows if p[:2] == ("Component colors", "Utility")})
    md += ["", "## Component: Utility", "",
           "Tinted badge, tag, and chart colors named `--color-utility-<hue>-<step>` for hues: "
           + ", ".join(utility) + ". They flip between themes; see tokens.css for values."]

    for label, file in DIMENSIONS.items():
        md += ["", f"## {label}", "", "| Token | Value |", "| --- | --- |"]
        for path, token in walk(load(file)):
            md.append(f"| `--{slug(path[-1])}` | {token['$value']}px |")
    md += type_md
    md.append("")
    (OUT / "tokens.md").write_text("\n".join(md))
    print(f"Wrote {len(rows)} semantic tokens to references/tokens.css and references/tokens.md")


if __name__ == "__main__":
    main()

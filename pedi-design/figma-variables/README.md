# Figma variables

Raw variable export from the Pedi Figma file. `scripts/build_tokens.py` compiles the Pedi collections into `references/tokens.md` and `references/tokens.css`. Rerun it after re-exporting.

## Pedi collections (used)

| File | Collection |
| --- | --- |
| `Style.tokens.json` | Primitive color ramps, including the Pedi `Brand` ramp (500 = `#DD1600`) |
| `1. Color modes/Light mode.tokens.json` | Semantic and component colors, light theme |
| `1. Color modes/Dark mode.tokens.json` | Semantic and component colors, dark theme |
| `Mode 1.tokens.json` | Radius |
| `Mode 1.tokens 2.json` | Spacing |
| `Mode 1.tokens 3.json` | Widths and paragraph max width |
| `Value.tokens.json` | Container padding and max width |

## Other kit exports (not used)

These come from third-party UI kits in the Figma file and are not Pedi tokens. The skill ignores them.

- `M3/`, `Baseline.tokens*.json`, `Font theme/`: Material 3 kit
- `Appearance/`, `Sizes/`, `Context/`, `Responsive/`, `Mode 1.tokens 4.json`: Apple kit (system colors, control sizes, Liquid Glass)
- `Color/`, `Dark.tokens.json`, `Default.tokens.json`, `Value.tokens 2.json`: other kit leftovers

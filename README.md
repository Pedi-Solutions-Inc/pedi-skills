# Pedi Skills

Reusable agent skills for building consistent Pedi products. The skills use the portable `SKILL.md` format and can be installed in both Codex and Claude Code.

## Available skills

### `pedi-design`

Designs, implements, and reviews Pedi-branded websites, mobile apps, product interfaces, internal tools, and marketing surfaces. It includes Pedi's current color, typography, spacing, component, responsive, accessibility, imagery, and motion guidance.

### `pedi-layout`

Designs, implements, and reviews authenticated Pedi application shells with a collapsible sidebar, sticky utility header, breadcrumbs, an independent content scroll region, and consistent page composition.

## Install

Clone or download this repository, then run the commands below from its root.

### Codex — personal installation

```sh
mkdir -p ~/.codex/skills
cp -R pedi-design ~/.codex/skills/
cp -R pedi-layout ~/.codex/skills/
```

The skills are then available across your Codex projects. Invoke them explicitly as `$pedi-design` or `$pedi-layout`, or ask Codex for matching Pedi design or application-layout work and let it select the appropriate skill automatically.

### Claude Code — personal installation

```sh
mkdir -p ~/.claude/skills
cp -R pedi-design ~/.claude/skills/
cp -R pedi-layout ~/.claude/skills/
```

The skills are then available across Claude Code projects. Invoke them explicitly as `/pedi-design` or `/pedi-layout`, or make a request that matches a skill description for automatic selection.

### Claude Code — project installation

To share the skill with one repository instead of installing it globally:

```sh
mkdir -p /path/to/project/.claude/skills
cp -R pedi-design /path/to/project/.claude/skills/
cp -R pedi-layout /path/to/project/.claude/skills/
```

Commit the copied skill directories in that project so the team receives the same guidance.

### Use one checkout in both tools

If you plan to edit the skill locally, symlink one checkout instead of copying it. Replace `/absolute/path/to/pedi-skills` with this repository's absolute path.

```sh
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s /absolute/path/to/pedi-skills/pedi-design ~/.codex/skills/pedi-design
ln -s /absolute/path/to/pedi-skills/pedi-design ~/.claude/skills/pedi-design
ln -s /absolute/path/to/pedi-skills/pedi-layout ~/.codex/skills/pedi-layout
ln -s /absolute/path/to/pedi-skills/pedi-layout ~/.claude/skills/pedi-layout
```

## Usage examples

In Codex:

```text
$pedi-design review this checkout flow and fix any design-system violations.
$pedi-layout build an authenticated app shell with a collapsible sidebar and sticky header.
```

In Claude Code:

```text
/pedi-design redesign this booking screen for mobile and desktop.
/pedi-layout review this dashboard shell and fix its scroll and content direction.
```

Automatic invocation also works with requests such as:

```text
Build a responsive Pedi payment confirmation page using this project's existing stack.
Create an authenticated Pedi operations dashboard with persistent navigation and a focused content area.
```

## Compatibility

The shared contract is intentionally portable:

- Each skill's `SKILL.md` uses standard YAML frontmatter and Markdown instructions.
- Detailed guidance lives in relative Markdown references that either agent can read.
- The skills contain no tool-specific runtime dependencies and preserve the target project's framework.
- Each `agents/openai.yaml` adds Codex display metadata. Claude Code does not need these files; the portable instructions remain in `SKILL.md`.

## Updating

For copied installations, replace the installed skill directory with the newer repository version. Symlinked installations update automatically when the checkout changes.

## Repository layout

```text
pedi-skills/
├── README.md
├── pedi-design/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── design-system.md
└── pedi-layout/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── app-shell.md
```

## Maintaining the design system

Update `pedi-design/references/design-system.md` when Pedi's authoritative design guidelines change. Keep `SKILL.md` focused on decision-making and workflow so the detailed reference is only loaded for relevant work.

Update `pedi-layout/references/app-shell.md` when the canonical Pedi app shell changes materially. Keep product-specific routes, permissions, and domain menus out of the reusable guidance.

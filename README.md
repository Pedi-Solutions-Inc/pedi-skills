# Pedi Skills

Reusable agent skills for building consistent Pedi products. The skills use the portable `SKILL.md` format and can be installed in both Codex and Claude Code.

## Available skills

### `pedi-design`

Designs, implements, and reviews Pedi-branded websites, mobile apps, product interfaces, internal tools, and marketing surfaces. It includes Pedi's current color, typography, spacing, component, responsive, accessibility, imagery, and motion guidance.

## Install

Clone or download this repository, then run the commands below from its root.

### Codex — personal installation

```sh
mkdir -p ~/.codex/skills
cp -R pedi-design ~/.codex/skills/
```

The skill is then available across your Codex projects. Invoke it explicitly as `$pedi-design`, or ask Codex for Pedi design work and let it select the skill automatically.

### Claude Code — personal installation

```sh
mkdir -p ~/.claude/skills
cp -R pedi-design ~/.claude/skills/
```

The skill is then available across Claude Code projects. Invoke it explicitly as `/pedi-design`, or make a request that matches its description for automatic selection.

### Claude Code — project installation

To share the skill with one repository instead of installing it globally:

```sh
mkdir -p /path/to/project/.claude/skills
cp -R pedi-design /path/to/project/.claude/skills/
```

Commit `.claude/skills/pedi-design` in that project so the team receives the same guidance.

### Use one checkout in both tools

If you plan to edit the skill locally, symlink one checkout instead of copying it. Replace `/absolute/path/to/pedi-skills` with this repository's absolute path.

```sh
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s /absolute/path/to/pedi-skills/pedi-design ~/.codex/skills/pedi-design
ln -s /absolute/path/to/pedi-skills/pedi-design ~/.claude/skills/pedi-design
```

## Usage examples

In Codex:

```text
$pedi-design review this checkout flow and fix any design-system violations.
```

In Claude Code:

```text
/pedi-design redesign this booking screen for mobile and desktop.
```

Automatic invocation also works with requests such as:

```text
Build a responsive Pedi payment confirmation page using this project's existing stack.
```

## Compatibility

The shared contract is intentionally portable:

- `pedi-design/SKILL.md` uses standard YAML frontmatter and Markdown instructions.
- Detailed guidance lives in a relative Markdown reference that either agent can read.
- The skill contains no tool-specific commands, runtime dependencies, or framework assumptions.
- `pedi-design/agents/openai.yaml` adds Codex display metadata. Claude Code does not need this file; the portable skill instructions remain in `SKILL.md`.

## Updating

For copied installations, replace the installed `pedi-design` directory with the newer repository version. Symlinked installations update automatically when the checkout changes.

## Repository layout

```text
pedi-skills/
├── README.md
└── pedi-design/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── design-system.md
```

## Maintaining the design system

Update `pedi-design/references/design-system.md` when Pedi's authoritative design guidelines change. Keep `SKILL.md` focused on decision-making and workflow so the detailed reference is only loaded for relevant work.

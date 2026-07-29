# Ecommerce Visual Orchestrator

A reusable Codex skill for planning, generating, revising, and quality-checking ecommerce main images and continuous detail-page masters.

## Included

- Five-image main-set planning with a model-first white-background catalog image
- Product construction consistency rules
- Concise ecommerce copy and prompt guidance
- Continuous long detail-page planning
- Deterministic lossless slicing and pixel-perfect reconstruction checks
- Lightweight execution: planning by default, explicit approval before ImageGen
- One-sample-first generation and at most one automatic retry

## Install

### Download ZIP

1. On GitHub, select **Code → Download ZIP**, then extract it.
2. Copy the `ecommerce-visual-orchestrator` folder into your Codex skills directory:

   - Windows: `%USERPROFILE%\.codex\skills\`
   - macOS/Linux: `~/.codex/skills/`

3. Restart Codex.

The installed file should be:

```text
~/.codex/skills/ecommerce-visual-orchestrator/SKILL.md
```

### Install from GitHub

Use Codex's skill installer with this repository and the path:

```text
ecommerce-visual-orchestrator
```

## Use

Invoke the skill explicitly:

```text
Use $ecommerce-visual-orchestrator to plan five ecommerce main images.
```

or:

```text
Use $ecommerce-visual-orchestrator to create one continuous 800×8000 detail-page master and ten 800×800 slices.
```

Provide product facts, reference images, target platform and market, copy language, and required dimensions. Missing facts should be marked as missing rather than invented.

The skill does not generate images during planning or prompt-writing tasks. ImageGen runs only after an explicit generation or editing request.

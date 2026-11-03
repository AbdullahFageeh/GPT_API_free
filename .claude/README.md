# Claude Code setup

Review and planning helpers for Claude Code, taken from
[ECC](https://github.com/affaan-m/ECC) (MIT licensed) at commit `b38be6a` (v2.2.3).
Only the pieces that fit this repo were copied. There are no hooks, MCP servers,
or install scripts.

## Agents (`.claude/agents/`)

| Agent | Use it for |
|-------|-----------|
| `code-reviewer` | General review of a change: correctness, security, quality |
| `security-reviewer` | Leaked API keys, unsafe input handling, vulnerable dependencies |
| `python-reviewer` | `demo/*.py` |
| `go-reviewer` | `demo/demo_go.go` |
| `typescript-reviewer` | `demo/demo_nodejs.js` |
| `planner` | A written plan before larger changes |

Ask for one by name, for example: "use the security-reviewer agent on demo/".

## Commands (`.claude/commands/`)

- `/ecc-review` reviews uncommitted changes, or a PR when given a number or URL.
  It asks before posting anything to GitHub.
- `/ecc-plan <what to build>` writes a plan and waits for your OK before changing code.

These are upstream's `/code-review` and `/plan`, renamed so they don't replace
Claude Code's built-in `/code-review` or `/plan`.

## Changes from upstream

- Softened "MUST BE USED" descriptions so agents are not launched on every edit.
- Removed references to ECC skills and commands that are not included here.
- Added Python and Go audit commands to `security-reviewer`.
- `/ecc-review` now confirms before posting a GitHub review.

## License

The files above are copied from ECC under the MIT License:

    MIT License
    
    Copyright (c) 2026 Affaan Mustafa
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

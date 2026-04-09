# ask-sc

Ask a question about a screenshot using Qwen 2.5 VL via `llama-mtmd-cli`.


Usefull tool for coding agetns that need visual feedback when crafing UI elements on web components or rendered document layouts.

## Requirements
- Python >= 3.14
- `llama-mtmd-cli` in PATH
- Model files at (Get using lm-studio, `Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf` and `mmproj-F16.gguf` from `unsloth/Qwen2.5-VL-7B-Instruct-GGUF`):
  - `~/.cache/lm-studio/models/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf`
  - `~/.cache/lm-studio/models/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/mmproj-F16.gguf`

## Install
```bash
uv tool install git+https://github.com/Srakai/ask-sc
```

## Usage
```bash
ask-sc /path/to/screenshot.png "What is shown?"
```

## AI Agent Usage Guide


```markdown
## `ask-sc` Tool — Guidelines for AI Agents

### What it does
Analyzes screenshot images of rendered documents (PDF pages, UI screenshots) and answers specific questions about layout, typography, and visual elements.

### Benefits
- **Visual verification** — Only way for text-based agents to "see" rendered output (PDFs, compiled LaTeX, HTML)
- **Targeted layout checks** — Good at confirming whether specific elements are present/absent on a page (e.g., "is there a bullet symbol before each list item?")
- **Structural analysis** — Can identify column alignment, panel boundaries, table structure, and element positioning
- **Iterative workflow** — Enables a fix→compile→render→verify loop without human eyes

### Limitations
- **Hallucination-prone on open-ended queries** — Asking "find all problems" produces false positives and misses real issues. It reported "z Zamawiającego" as a line-start orphan on pages where it didn't actually occur
- **Unreliable for small text** — Cannot reliably read fine print, footnotes, or text in narrow table cells
- **Confirmation bias** — Tends to say "looks good" on generic checks even when issues exist
- **Cannot compare** — Cannot reliably diff two versions of a page or notice subtle spacing changes

### Prompt Guidelines

| Do | Don't |
|----|-------|
| Ask **one specific question per query** | Ask "check everything on this page" |
| Describe **what you expect** based on the source code | Ask open-ended "what's wrong?" |
| Use **yes/no verification** ("Is there a bullet symbol before each `\item`?") | Ask it to "find all issues" |
| Name **exact elements** to check ("the `Przygotowano dla:` block at bottom-left") | Use vague references ("the text at the bottom") |
| Cross-reference its answers with **source code logic** — if it claims an issue, verify in code before fixing | Trust its answers blindly |
| Ask about **one page at a time** | Send multiple pages in one query |

### Recommended Workflow

1. **Know what to expect** — Read the source code first, understand what each page should contain
2. **Render pages to images** — Use `pdftoppm` or similar to convert each PDF page to PNG
3. **Query page-by-page** with a specific checklist derived from the code
4. **Verify claimed issues in source** before applying fixes — the tool frequently reports phantom problems
5. **Re-render and re-check** only the affected pages after fixes, not the whole document

### Key Lesson
**The tool is a verification aid, not a discovery tool.** Use your understanding of the source code to form hypotheses, then use `ask-sc` to confirm or deny. Never use it as the sole source of truth for what's on a page.
```

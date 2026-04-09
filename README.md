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


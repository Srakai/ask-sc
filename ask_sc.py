"""ask-sc: Ask a question about a screenshot using Qwen 2.5 VL."""

import argparse
import os
import shutil
import subprocess
import sys

MODEL_PATH = os.path.expanduser(
    "~/.cache/lm-studio/models/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf"
)
MMPROJ_PATH = os.path.expanduser(
    "~/.cache/lm-studio/models/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/mmproj-F16.gguf"
)
DEFAULT_PROMPT = "Describe what the user is doing in this screenshot."


def run(image_path: str, prompt: str, temp: float = 0.2, max_tokens: int = 256) -> str:
    cli = shutil.which("llama-mtmd-cli")
    if not cli:
        print("Error: llama-mtmd-cli not found in PATH", file=sys.stderr)
        sys.exit(1)

    image_path = os.path.abspath(image_path)
    if not os.path.isfile(image_path):
        print(f"Error: image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        cli,
        "-m", MODEL_PATH,
        "--mmproj", MMPROJ_PATH,
        "--image", image_path,
        "--temp", str(temp),
        "-n", str(max_tokens),
        "-p", prompt,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f"Error: llama-mtmd-cli failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description="Ask a question about a screenshot")
    parser.add_argument("image", help="Path to the screenshot image")
    parser.add_argument("prompt", nargs="?", default=DEFAULT_PROMPT, help="Prompt/question about the image")
    parser.add_argument("--temp", type=float, default=0.2, help="Temperature (default: 0.2)")
    parser.add_argument("--max-tokens", type=int, default=256, help="Max tokens (default: 256)")
    args = parser.parse_args()

    output = run(args.image, args.prompt, args.temp, args.max_tokens)
    print(output)


if __name__ == "__main__":
    main()

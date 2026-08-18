#!/bin/bash
set -euo pipefail

# Only run in Claude Code on the web (remote) sessions.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install uv (Python package/project manager) if not already present, so
# Python-based tooling (scripts, future automation) has it available.
if ! command -v uv >/dev/null 2>&1; then
  installer="$(mktemp)"
  curl -LsSf https://astral.sh/uv/install.sh -o "$installer"
  sh "$installer"
  rm -f "$installer"
fi

UV_BIN_DIR="$HOME/.local/bin"
if [ -d "$UV_BIN_DIR" ] && [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$UV_BIN_DIR:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi

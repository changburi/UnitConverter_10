#!/usr/bin/env bash
# Run Python from stdin; emit JSON hook response on stdout.
set -euo pipefail

if command -v python3 >/dev/null 2>&1; then
  exec python3 -
elif command -v python >/dev/null 2>&1; then
  exec python -
else
  echo '{"additional_context":"[hook error] python not found"}' >&1
  exit 1
fi

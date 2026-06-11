#!/usr/bin/env bash
# postToolUse(Write): src/ or tests/ edit → pytest hint + touch flag.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
STATE_DIR="${SCRIPT_DIR}/state"
FLAG_FILE="${STATE_DIR}/touched_src_tests.flag"

INPUT="$(cat)"

export PROJECT_ROOT STATE_DIR FLAG_FILE INPUT

"${SCRIPT_DIR}/_python.sh" <<'PY'
import json
import os
from pathlib import Path

raw = os.environ.get("INPUT", "")

try:
    payload = json.loads(raw) if raw.strip() else {}
except json.JSONDecodeError:
    print("{}")
    raise SystemExit(0)

tool_input = payload.get("tool_input") or payload.get("input") or {}
path_str = (
    tool_input.get("path")
    or tool_input.get("file_path")
    or tool_input.get("target_file")
    or ""
)

if not path_str:
    print("{}")
    raise SystemExit(0)

project_root = Path(os.environ["PROJECT_ROOT"]).resolve()
state_dir = Path(os.environ["STATE_DIR"])
flag_file = Path(os.environ["FLAG_FILE"])

try:
    rel = Path(path_str)
    if not rel.is_absolute():
        rel = (project_root / rel).resolve()
    else:
        rel = rel.resolve()
    rel_to_root = rel.relative_to(project_root)
except (ValueError, OSError):
    print("{}")
    raise SystemExit(0)

parts = rel_to_root.parts
if not parts:
    print("{}")
    raise SystemExit(0)

top = parts[0].lower()
if top not in ("src", "tests"):
    print("{}")
    raise SystemExit(0)

state_dir.mkdir(parents=True, exist_ok=True)
flag_file.touch()

rel_display = rel_to_root.as_posix()
if top == "tests":
    sub = parts[1].lower() if len(parts) >= 2 else ""
    if sub == "boundary":
        pytest_cmd = "python -m pytest tests/boundary -v"
        track = "UI Track (boundary)"
    elif sub in ("entity", "control"):
        pytest_cmd = f"python -m pytest tests/{sub} -v"
        track = f"Logic Track ({sub})"
    else:
        pytest_cmd = "python -m pytest tests/entity tests/control -v"
        track = "Logic Track (entity + control)"
    hint = (
        f"[Hook postToolUse] `{rel_display}` 작성됨.\n"
        f"- Test Loop: `{pytest_cmd}`\n"
        f"- Track: {track}\n"
        f"- 전체 회귀: `python -m pytest tests/ -v`"
    )
else:
    hint = (
        f"[Hook postToolUse] `{rel_display}` 작성됨.\n"
        f"- Test Loop: `python -m pytest tests/ -v` (src 변경 후 전체 회귀)\n"
        f"- Logic: `python -m pytest tests/entity tests/control -v`"
    )

print(json.dumps({"additional_context": hint}, ensure_ascii=False))
PY

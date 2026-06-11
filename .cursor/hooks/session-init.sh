#!/usr/bin/env bash
# UnitConverter_10 — sessionStart: inject project context for Agent.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Consume hook stdin (session metadata); not required for context build.
cat >/dev/null || true

export PROJECT_ROOT

"${SCRIPT_DIR}/_python.sh" <<'PY'
import json
import os
from pathlib import Path

project_root = Path(os.environ["PROJECT_ROOT"])
rules_path = project_root / ".cursorrules"
rules_exists = rules_path.is_file()

context_lines = [
    "# UnitConverter_10 Session Context (sessionStart Hook)",
    "",
    "## 프로젝트",
    "- **코드명:** MagicSquare_1004",
    "- **저장소:** UnitConverter_10 — 길이 단위 변환 CLI (meter | feet | yard)",
    "",
    "## SSOT (Single Source of Truth)",
    "- **Rule 헌법:** `.cursorrules`"
    + (" — 파일 존재 ✓" if rules_exists else " — ⚠ 파일 없음"),
    "- **변환 상수:** README + `src/entity/constants.py` (MagicConstant SSOT)",
    "- **Logic Test ID:** `.cursor/skills/unit-converter-tdd/reference.md` (D-*)",
    "- **절차 Skill:** `.cursor/skills/unit-converter-tdd/SKILL.md`",
    "",
    "## Dual-Track TDD",
    "- **Track 1 Logic:** entity, control — Domain Mock 금지 — `tests/entity/test_d_*`, `tests/control/test_d_*`",
    "- **Track 2 UI:** boundary — stdin/stdout Mock 허용 — `tests/boundary/test_u_*`",
    "- **Phase:** RED → GREEN → REFACTOR (skip / xfail / assert 완화 금지)",
    "",
    "## ECB",
    "- **의존:** boundary → control → entity (역방향 import 금지)",
    "- **entity:** E001~E005 처리·검사·메시지 금지; stdlib·typing·`src/entity/*`만 import",
    "- **control:** InputValidator (E001~E005), Solver",
    "- **boundary:** InputHandler, ResultDisplay (E001~E007 표시)",
    "",
    "## 슬래시 Command (등록됨)",
    "- `/tdd-red` — RED만: `tests/`만 수정, `src/` 금지, pytest FAIL 확인",
    "",
    "## pytest (Test Loop)",
    "```bash",
    "python -m pytest tests/entity tests/control -v   # Logic Track",
    "python -m pytest tests/boundary -v             # UI Track",
    "python -m pytest tests/ -v                     # 전체 회귀",
    "```",
    "",
    "TDD 작업 시 응답 첫 줄: `Phase: RED|GREEN|REFACTOR | Layer: ... | Track: Logic|UI | TestID: D-xxx|U-xxx`",
    "git commit / push — 사용자 명시 요청 시만.",
]

print(json.dumps({"additional_context": "\n".join(context_lines)}, ensure_ascii=False))
PY

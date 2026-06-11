
## Unit Converter (Python)

![unit-converter](./unit-converter.jpg)

길이 단위(meter · feet · yard) 변환 CLI — **Mom Test 문제 정의 · ECB · Dual-Track TDD · Cursor 8계층** 실습 프로젝트.

**Repository:** https://github.com/changburi/UnitConverter_10

---

### Overview

- 사용자가 입력한 길이(`단위:값`)를 기반으로, 해당 값을 다른 모든 단위로 변환해 출력하는 프로그램.
- 새로운 단위를 추가할 때 기존 코드의 변경이 최소화되도록 설계한다 (OCP).
- 각 단위 변환 로직은 테스트 코드로 검증한다 (Dual-Track TDD).

---

### 프로젝트 구조

```
UnitConverter_10/
├── UnitConverter.py          # 레거시 CLI (Activity 1~3)
├── src/
│   ├── entity/               # LengthInput, ConversionResult, UnitRatio
│   ├── control/              # InputValidator, Solver
│   └── boundary/             # InputHandler, ResultDisplay
├── tests/
│   ├── entity/               # Logic Track — test_d_*.py
│   ├── control/
│   ├── boundary/             # UI Track — test_u_*.py
│   └── test_converter.py     # 레거시 통합 테스트 (6 passed)
├── docs/PRD.md
├── Report/                   # Mom Test · 문제 정의 · 세션 보고서
├── Prompt/                   # 인터뷰 로그 · Transcript
├── .cursorrules              # Rule (헌법)
├── .cursor/
│   ├── skills/unit-converter-tdd/
│   ├── commands/             # /tdd-red, /review-ecb
│   └── hooks.json            # sessionStart, postToolUse(Write)
└── pyproject.toml
```

---

### 가상환경 설정 및 실행

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 의존성 (pytest)
pip install pytest

# 레거시 CLI 실행
python UnitConverter.py

# 테스트 (전체)
python -m pytest tests/ -v

# Logic Track
python -m pytest tests/entity tests/control -v

# UI Track
python -m pytest tests/boundary -v

# 가상환경 비활성화
deactivate
```

---

### ECB 아키텍처

| Layer | 역할 |
|-------|------|
| **entity** | 순수 변환 (E001~E005 처리 금지) |
| **control** | InputValidator (E001~E005), Solver |
| **boundary** | InputHandler, ResultDisplay (E001~E007 표시) |

의존 방향: `boundary → control → entity`

---

### Dual-Track TDD

| Track | Layer | 테스트 ID | 파일 |
|-------|-------|-----------|------|
| **Logic** | entity, control | `D-*` | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` |
| **UI** | boundary | `U-*` | `tests/boundary/test_u_*.py` |

- Logic Track: Domain Mock **금지**
- UI Track: stdin/stdout Mock **허용**
- Phase: **RED → GREEN → REFACTOR** (skip / xfail / assert 완화 금지)
- 상수 SSOT: `src/entity/constants.py` (예정) — `3.28084`, `1.09361`

---

### Cursor AI (8계층)

| 계층 | 경로 |
|------|------|
| **Rule** | `.cursorrules` |
| **Skill** | `.cursor/skills/unit-converter-tdd/SKILL.md` |
| **Command** | `/tdd-red`, `/review-ecb` |
| **Hook** | `.cursor/hooks.json` |

상세: [`Report/03.Session3_CursorDesign_Closing_Report.md`](Report/03.Session3_CursorDesign_Closing_Report.md)

---

### ARRR 실습 순서

| 글자 | Phase | Command | 산출 |
|------|-------|---------|------|
| **A**rrange | RED 설계 | `/red-test-plan` | C2C·설계표 (tests/src **미생성**) |
| **R**ED | RED | `/red-skeleton` | `pytest.fail` · conftest |
| **R**un | GREEN | `/green-minimal` | entity/control/boundary 최소 · assert PASS |
| **R**efine | Golden+Refactor | `/golden-master` → `/refactor-smell` → `/refactor-safe` | Approval · smell · safe |

세션 Export: `/export` — `Report/NN.REPORT.md` + `Prompting/NN.Export-Transcript.md`

슬래시 단독 입력: 모든 ARRR Command는 `/이름` 만으로 동작 (추가 질문 금지).

---

### REFACTOR To-Do

> **전제 (2026-06-11):** `python -m pytest tests/ -v` → **11 passed**  
> **스캔 범위:** `src/` · `tests/` (+ 레거시 `UnitConverter.py`)  
> **Change Budget (`/refactor-safe` 1회):** 파일 ≤ 3 · 클래스 ≤ 1 · 메서드 ≤ 3

#### 스멜 표 (`/refactor-smell` 결과)

| # | P | 유형 | Track | 파일:함수 | 내용 | Budget | 권고 |
|---|-----|------|-------|-----------|------|--------|------|
| 1 | **P0** | Magic Number | Logic+UI | `UnitConverter.py:main` | `3.28084`·`1.09361` 리터럴 4회 — `constants.py` SSOT 미사용 | ✅ 1파일·1함수 | ECB `validate`/`solve` 또는 최소 `constants` import로 치환 |
| 2 | **P0** | ECB 위반 (아키텍처 이탈) | Logic+UI | `UnitConverter.py:main` | 검증·변환·출력을 루트 스크립트에 중복 구현 — `src/` ECB 미경유 | ✅ 1파일·1함수 | `boundary.cli.process_input_line` 또는 control+entity thin wrapper로 위임 |
| 3 | **P1** | Duplicated Code | Logic | `validation.py:validate_number`, `validate` | `float()` try/except 블록 2회 (각 4~5줄, 합 ~10줄) | ✅ 1파일·1헬퍼 | `_parse_float(value_str) -> float \| ValidationError` 추출 후 공용 |
| 4 | **P1** | Duplicated Code | Logic | `solver.py:solve` | 동일 f-string 패턴 3회 (`meter`/`feet`/`yard`) | ✅ 1파일·1헬퍼 | `(UNIT_METER,"meter"), …` 순회 또는 `_format_line(...)` |
| 5 | **P1** | Magic Number (테스트 SSOT) | Logic | `tests/test_converter.py` (모듈) | `METER_TO_FEET`/`METER_TO_YARD` 로컬 재정의 — entity SSOT와 이중 유지 | ✅ 1파일 | `from src.entity.constants import …` 로 통일 |
| 6 | **P1** | Feature Envy / boundary 우회 | UI | `demo_gui.py:_on_convert` | `f"{unit}:{value_str}"` 조립 + `validate`→`solve` 직접 호출 — `cli.process_input_line` 미사용 | ⚠️ 1파일·1메서드 | 공통 orchestration을 boundary로 올리거나 GUI는 `process_input_line` + 코드 표시만 분기 |
| 7 | **P2** | Long Method | UI | `demo_gui.py:_build_widgets` | ~42줄 — 위젯 배치·힌트·버튼 한 메서드 | ⚠️ 클래스 1·메서드 2+ | `_build_input_row` / `_build_actions` 등 private 분리 |
| 8 | **P2** | Long Method | — | `UnitConverter.py:main` | ~32줄 — 파싱·검증·변환·출력 4책임 (P0 리팩터 시 함께 해소) | (P0와 동일) | P0 후보와 통합 처리 |
| 9 | **P2** | Duplicated Code | Logic | `tests/entity/test_d_loc_01.py` | D-LOC-02/03 Given-When-Then 구조 반복 | △ | 공통 헬퍼보다 현 상태 유지 권장 (의미 변경 위험) |
| 10 | **P2** | Mysterious Name | Logic | `boundary/cli.py:process_input_line` | 오류 시 `message`만 반환 — 코드(`E001`) 소실 | △ | `ValidationError` 전체 반환 또는 `format_error()` boundary 헬퍼 검토 |

**ECB 점검 (`src/` 내부):** entity→boundary/control import 없음 · entity E001~E005 없음 · `boundary → control → entity` 준수 · 격자 `34/16/4` 리터럴 없음 ✅

#### `/refactor-safe` 후보 (Budget 내)

| 순위 | 대상 | 리팩터 (1문장) | Budget |
|------|------|----------------|--------|
| **1 (P0)** | `UnitConverter.py:main` | ECB 경유 thin CLI — `process_input_line` 호출 또는 control+entity 위임, 매직넘버 제거 | 파일 1 · 함수 1 ✅ |
| **2 (P1)** | `validation.py` | `_parse_float` 헬퍼로 `validate_number`/`validate` 중복 제거 | 파일 1 · 메서드 1 ✅ |
| **3 (P1)** | `solver.py:solve` | 단위별 출력 3줄을 SSOT 단위 튜플 순회로 통합 | 파일 1 · 메서드 1 ✅ |

#### 다음 단계

**P0 1건**이 있으므로, **`UnitConverter.py` ECB·SSOT 정리**를 먼저 골라 `/refactor-safe`를 실행한다.

```
/refactor-safe
Phase: REFACTOR | Layer: boundary | Track: Logic+UI | TestID: D-LOC-01
대상: P0 #1 — UnitConverter.py → process_input_line (또는 control+entity) 위임
```

P0 적용 후 `python -m pytest tests/ -v`로 레거시 6건(`tests/test_converter.py`) 포함 **11 passed** 유지.

---

### 후속 (예정)

| # | 작업 | Command / 비고 |
|---|------|----------------|
| 1 | D-LOC-01 Approval Test | `/golden-master` — `str(unit_convert(2.5,"meter"))` |
| 2 | `golden-master.md` Command 예시 갱신 | `find_blank_coords` → `unit_convert` |
| 3 | control E004/E005 · boundary 추가 테스트 | `/red-skeleton` → `/green-minimal` |
| 4 | Activity 4 — 설정·동적 단위·출력 포맷 | README 추가 요구사항 |
| 5 | git commit | 사용자 요청 시 |

---

### 문서

| 문서 | 설명 |
|------|------|
| [`docs/PRD.md`](docs/PRD.md) | 제품 요구사항 · FR/NFR · AC |
| [`Report/01.UnitConverter_ProblemDefinition_Report.md`](Report/01.UnitConverter_ProblemDefinition_Report.md) | Mom Test · 문제 정의 |
| [`Report/MomTest_Report.md`](Report/MomTest_Report.md) | Mom Test 인터뷰 보고서 |
| [`Prompt/Session3_Transcript_Export.md`](Prompt/Session3_Transcript_Export.md) | 세션 Transcript |

---

### 기본 요구사항

1. 사용자 입력 예시:
   ```
   meter:2.5
   ```
   → 출력:
   ```
   2.5 meter = 8.2 feet
   2.5 meter = 2.7 yard
   ...
   ```

2. 현재 지원 단위:
   - meter
   - feet
   - yard

3. 새로운 단위가 추가될 때도 기존 코드의 변경이 최소화되도록 할 것.

4. 각 단위 간 변환이 정확히 계산되도록 테스트 코드를 작성할 것.

### 비즈니스 로직

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`
- feet/yard 간의 비율은 meter 기반으로 계산.

### 품질 요구사항

- OCP를 만족하는 설계
- SRP를 만족하는 클래스 구성
- 입력 값 검증 (음수, 잘못된 형식, 없는 단위) — E001~E007

### 추가 요구사항 (Activity 4)

- **설정 외부화** — 변환 비율 JSON/YAML
- **동적 단위 등록** — `1 cubit = 0.4572 meter`
- **출력 포맷** — JSON / CSV / 표

---

## 생성형AI를 활용한 Activities (6 시간)

1. 문제 코드 및 기본 요구사항 분석 (0.5시간)
   - 기본 코드구조, 로직 이해 · Mom Test · PRD
2. 기본 요구사항 및 품질 요구사항 구현 (2시간)
   - OCP/SRP · ECB 클래스 · 입력값 검증
3. TC 구현 (0.5시간)
   - Dual-Track TDD · Cursor Rule/Skill/Command/Hook
4. 추가 요구사항 구현 (2시간)
   - 3개 요구사항 구현 및 TC 작성
5. 회고 및 발표 (1시간)
   - 실습 목표와 달성도 · AI 활용 · TC · 클린코드 회고

---

*작성자: 오창조의불 · 리뷰어: 박일용, 박철만, 배대웅, 신대혁*

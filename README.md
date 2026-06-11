
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

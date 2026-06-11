# UnitConverter_10 — GUI Demo

> **목적:** 숫자 입력·단위 변환을 **눈으로 확인**하는 최소 데모 (수동 스모크)  
> **범위:** ECB `control` 검증 + `entity` 변환 · **자동 pytest 대체 아님**

---

## 1. 실행 방법

### GUI 데모

```bash
# 프로젝트 루트에서
python demo_gui.py
```

- **숫자 검증:** 값만 `validate_number` (E002 숫자 오류 · E005 빈 값)
- **단위 변환:** `unit:value` 형식으로 `validate` → `solve` → meter/feet/yard 3줄 출력

### 레거시 CLI (비교용)

```bash
python UnitConverter.py
# 입력 예: meter:2.5
```

---

## 2. GUI에서 확인할 것

| 동작 | 입력 예 | 기대 |
|------|---------|------|
| 숫자 검증 OK | `2.5` | `OK — 유효한 숫자: 2.5` |
| 숫자 검증 FAIL | `abc` | `[E002] Invalid number: abc` |
| 숫자 검증 FAIL | *(빈칸)* | `[E005] Empty value` |
| 변환 OK | `2.5` + `meter` | 3줄 (meter / feet / yard) |
| 변환 FAIL | `cubit` 단위는 콤보박스에 없음 — CLI 형식 오류는 숫자+미지원 조합 시 validate 경유 |

**단위 변환 수치**는 `src/entity/constants.py` SSOT (`3.28084`, `1.09361`)와 동일해야 한다.

---

## 3. 제약 사항

| # | 제약 |
|---|------|
| 1 | **데모 전용** — `demo_gui.py`는 boundary 스모크 UI이며 PRD Activity 4·웹 UI **아님** |
| 2 | **ECB** — GUI는 `control.validation` · `control.solver` · `entity.conversion`만 호출 (entity에 E001~E005 로직 없음) |
| 3 | **의존성** — Python 표준 라이브러리 `tkinter`만 사용 (별도 pip 패키지 없음) |
| 4 | **tkinter 미포함 Python** — 일부 Linux 빌드는 `python3-tk` 패키지 설치 필요 |
| 5 | **Golden Master / Approval Test** — GUI 출력은 golden 파일 대상 **아님** (Logic·boundary pytest가 SSOT) |
| 6 | **가상환경** — `.venv` 없으면 시스템 `python` 사용 (`python demo_gui.py`) |
| 7 | **git** — 데모 추가만, 커밋은 사용자 요청 시 |

---

## 4. 테스트 실행 방법 (자동 회귀)

GUI와 **별도**로 pytest로 회귀를 확인한다.

```bash
# 전체
python -m pytest tests/ -v

# Track A — Logic (entity + control)
python -m pytest tests/entity tests/control -v

# Track B — UI (boundary)
python -m pytest tests/boundary -v
```

**통과 기준 (현재):** 11 passed

| Track | 파일 | 내용 |
|-------|------|------|
| Logic | `tests/entity/test_d_loc_01.py` | `unit_convert` meter/feet/yard |
| UI | `tests/boundary/test_u_in_01.py` | E001 · E003 메시지 |
| 레거시 | `tests/test_converter.py` | CLI 통합 6건 |

GUI 수동 확인 후 위 명령으로 **자동 테스트 green** 유지를 권장한다.

---

## 5. 아키텍처 (데모 경로)

```
demo_gui.py (boundary 스모크)
    → control.validation (E002/E005/E001/E003)
    → control.solver
        → entity.conversion (unit_convert)
        → entity.constants (SSOT)
```

---

## 6. 관련 문서

- [PRD.md](PRD.md) — FR-01~04
- [README.md](../README.md) — 프로젝트 구조 · ECB
- `.cursorrules` — Dual-Track TDD · Entity 금지 규칙

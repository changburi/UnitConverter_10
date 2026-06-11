# RED Test Plan — C2C·설계표

UnitConverter_10 Dual-Track TDD **RED 설계 단계만** 수행한다.  
**tests/·src/ 파일 생성·수정 금지** — 설계표·플랜·ECB 점검 표만 출력한다.  
헌법: `.cursorrules` · SSOT: `docs/PRD.md` · Export: `.cursor/commands/export.md` · Skill: `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 슬래시 단독 입력 (고정 컨텍스트)

`/red-test-plan` **만** 입력해도 아래를 **질문 없이** 적용한다.

```
Phase: RED | Layer: entity | Track: Logic | TestID: D-LOC-01
RED 묶음: D-LOC-01 ~ D-LOC-03 (FR-LOC-01)
FR: FR-LOC-01 — 격자 blank 좌표 (PRD 미등재 · RED 설계 합의)
대상 함수: find_blank_coords(grid)
SSOT: src/entity/constants.py — GRID_ROWS=34, GRID_COLS=16, GRID_SUBGRID=4
```

---

## 필수 선언

**응답 첫 줄 (고정 형식):**

```
Phase: RED | Layer: entity | Track: Logic | TestID: D-LOC-01
```

---

## 절차

1. **FR-LOC-01 합의 계약** — `docs/PRD.md`에 FR-LOC-01 **없음** 명시 · RED 설계 계약 표
2. **C2C (Rule 1~3)** — Rule 1 PRD/계약 인용 · Rule 2 To-Do **1개** · Rule 3 Given/When/Then
3. **Track B RED 설계표** — D-LOC-01~03 (Invariant · Expected RED Failure)
4. **테스트 플랜** — 파일·함수·conftest·pytest · RED 묶음
5. **ECB 점검 표** — entity E001~E005 금지 · Logic Mock 금지 · SSOT
6. **보고** — `/red-skeleton` 준비 **한 줄**

---

## 출력 표 (필수 4종)

### 1. FR-LOC-01 합의 계약

| 항목 | 내용 |
|------|------|
| blank | `GRID_BLANK` (= 0, constants SSOT) |
| 좌표 | 1-index `(row, col)`, row-major |
| 격자 SSOT | 34 / 16 / 4 → `constants.py` |

### 2. Track B RED 설계표

| Test ID | 대상 | Given→Then | Invariant | Expected RED Failure |
|---------|------|------------|-----------|----------------------|
| **D-LOC-01** | `find_blank_coords` | G1(0×2) → `[(2,2),(3,3)]` | row-major · 1-index | `pytest.fail` / ImportError |
| D-LOC-02 | 동일 | G2 → `[(1,1)]` | 행→열 순 | RED 예정 |
| D-LOC-03 | 동일 | G3 → `[]` | `[]` ≠ None | RED 예정 |

### 3. 테스트 플랜 (D-LOC-01)

| 항목 | 내용 |
|------|------|
| 파일 | `tests/entity/test_d_loc_01.py` |
| 함수 | `test_d_loc_01_blank_coords_row_major` |
| conftest | `grid_g1` (4×4, 0 두 칸) |
| pytest | `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v` |
| RED 묶음 | D-LOC-01 ~ D-LOC-03 |

### 4. ECB 점검

| 체크 | 판정 |
|------|------|
| entity E001~E005 | emit 금지 ✅ |
| Logic Domain Mock | 금지 ✅ |
| SSOT | constants only ✅ |

---

## 보고

| 항목 | 내용 |
|------|------|
| **TestID** | D-LOC-01 (묶음 D-LOC-01~03) |
| **산출** | 설계표 4종 (tests/src 미생성) |
| **다음** | `/red-skeleton` |

---

## 금지

- `tests/` · `src/` 생성·수정 · GREEN · REFACTOR · **추가 질문**
- skip · xfail · git commit (사용자 요청 시만)

---

## ARRR

| **A**rrange | **R**ED | **R**un | **R**efine |
|-------------|----------|---------|-------------|
| **`/red-test-plan`** | `/red-skeleton` | `/green-minimal` | `/golden-master` → `/refactor-smell` → `/refactor-safe` |

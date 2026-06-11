# UnitConverter_10 — D-LOC-01 RED Transcript Export

> **Export일:** 2026-06-11  
> **브랜치:** `red`  
> **범위:** `/red-test-plan` → `/red-skeleton` (D-LOC-01)  
> **형식:** 대화·작업 요약 Transcript (가공)

---

## Timeline

| # | 주제 | 산출물 |
|---|------|--------|
| 17 | `/red-test-plan` — FR-LOC-01 C2C·설계표 | 설계표 (tests/src 미생성) |
| 18 | `/red-skeleton` — D-LOC-01 1차 | `tests/conftest.py`, `test_d_loc_01.py`, `constants.py`, Skill |
| 19 | pytest 노드 ID 수정 | 클래스 → 모듈 레벨 함수 |
| 20 | `/red-skeleton` — D-LOC-01 재실행 | RED FAIL 확인 |
| 21 | Report · Transcript Export | `Report/05.*`, 본 문서 |

---

## Part A — `/red-test-plan`

### A1. 요청

```
Phase: red | Layer: entity | Track: Logic
RED 묶음: D-LOC-01 (FR-LOC-01)
금지: tests/·src/ 수정, GREEN/REFACTOR, skip/xfail
```

### A2. PRD FR-LOC-01

- `docs/PRD.md`에 **FR-LOC-01 없음**
- **합의 계약:** 격자 값 **0** → **1-index row-major** `(row, col)` 리스트
- SSOT: `34 / 16 / 4` → `src/entity/constants.py`
- UnitConverter **FR-03**(meter 정규화)과 **별 트랙**

### A3. To-Do (판단 1개)

| To-Do | 판단 |
|-------|------|
| 1-index vs 0-index | ✅ **1-index `(2,2),(3,3)`** — `.cursorrules` · 스켈레톤 Then과 일치 |

### A4. Track B RED 설계표

| Test ID | 대상 | Given→Then | Invariant |
|---------|------|------------|-----------|
| D-LOC-01 | `find_blank_coords` | G1 → `[(2,2),(3,3)]` | row-major · 1-index · 0=blank |
| D-LOC-02 | 동일 | G2 → `[(1,1)]` | 행→열 순 |
| D-LOC-03 | 동일 | G3 → `[]` | 빈 리스트 ≠ None |

### A5. 테스트 플랜

| 항목 | 내용 |
|------|------|
| 파일 | `tests/entity/test_d_loc_01.py` |
| 함수명 | `test_d_loc_01_blank_coords_row_major` (+ D-LOC-02/03 후보) |
| conftest | `grid_g1` (0×2), `grid_g2`/`grid_g3` 예정 |
| pytest | `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v` |
| RED 묶음 | **D-LOC-01 ~ D-LOC-03** |

**한 줄:** `/red-skeleton`으로 넘길 준비 완료.

---

## Part B — `/red-skeleton` (D-LOC-01)

### B1. 규칙

- AAA 주석 (Given / When / Then)
- Then = `pytest.fail("RED: D-LOC-01 — …")` **한 줄만**
- assert · skip · xfail · 통과 더미 **금지**
- **src/ 수정 금지** (스켈레톤 2차 실행 시)
- 상수 `34/16/4` — `entity/constants.py` import (픽스처만)

### B2. 생성·수정 파일

| 경로 | 내용 |
|------|------|
| `tests/conftest.py` | `grid_g1` — 4×4, 0 at (2,2)·(3,3) |
| `tests/entity/test_d_loc_01.py` | RED 스켈레톤 |
| `src/entity/constants.py` | `GRID_ROWS/COLS/SUBGRID` (1차 스켈레톤) |
| `.cursor/skills/red-skeleton/SKILL.md` | Skill |

### B3. G1 격자 (`grid_g1`)

```python
[
    [1, 1, 1, 1],
    [1, 0, 1, 1],  # (2,2)
    [1, 1, 0, 1],  # (3,3)
    [1, 1, 1, 1],
]
```

### B4. 최종 테스트 코드

```python
def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
```

> **수정 사유:** 클래스 `TestDLoc01BlankCoords::` 노드 ID → 사용자 명령 `::test_d_loc_01_blank_coords_row_major` 와 불일치 (exit 4) → **모듈 레벨 함수**로 변경.

### B5. pytest 결과

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

```
FAILED — RED: D-LOC-01 — 구현 없음, 의도적 실패
1 failed in 0.28s
```

| 항목 | 값 |
|------|-----|
| Test ID | D-LOC-01 |
| FAIL | `RED: D-LOC-01 — 구현 없음, 의도적 실패` |
| 변경 (최종) | `tests/conftest.py`, `tests/entity/test_d_loc_01.py` only |

---

## Part C — ECB · Dual-Track

| Track | Layer | ID | Mock |
|-------|-------|-----|------|
| Logic | entity | D-LOC-* | ❌ Domain Mock |
| UI | boundary | U-IN-* | ✅ stdin/stdout (별도) |

- `find_blank_coords`: entity 순수 함수 — **E001~E005 emit 금지**
- `grid_g*` conftest: **실 데이터**, 로직 없음

---

## Part D — 대화 로그 (요약)

### User → `/red-test-plan`

- C2C · Track B · 테스트 플랜 · ECB 점검 표 요청
- tests/src 생성 금지

### Assistant

- FR-LOC-01 합의 계약 정리
- D-LOC-01~03 Given/When/Then
- `/red-skeleton` 준비 완료 한 줄

### User → `/red-skeleton` (×3)

- D-LOC-01만, AAA + pytest.fail
- 실행 명령 + 보고 형식 지정

### Assistant

- 1차: Skill + conftest + test + constants 생성
- 2차: 클래스 → 모듈 함수 (노드 ID)
- 3차: pytest FAIL 확인 · 보고

### User → Report · Transcript Export

- `Report/05.*`, `Prompt/Session_D_LOC_01_Transcript_Export.md`

---

## Part E — 재사용 프롬프트

```
/red-test-plan
Phase: red | Layer: entity | Track: Logic
이번 RED 묶음: D-LOC-01 (FR-LOC-01)
(표 4종 — tests/·src/ 만들지 마)

/red-skeleton
Phase: red | Layer: entity | Track: Logic
Test ID: D-LOC-01
파일: tests/entity/test_d_loc_01.py
픽스처: tests/conftest.py (G1 격자 — 0이 2개, row-major)
(AAA + pytest.fail only · src/ 수정 금지)
```

---

## Part F — 미완료 체크리스트

- [x] D-LOC-01 RED 스켈레톤
- [x] `tests/conftest.py` `grid_g1`
- [x] `src/entity/constants.py` SSOT
- [ ] D-LOC-02 / D-LOC-03 RED 스켈레톤
- [ ] `find_blank_coords` GREEN (`src/entity/`)
- [ ] D-LOC-02/03 conftest (`grid_g2`, `grid_g3`)
- [ ] U-IN-01~02 boundary RED

---

## Part G — Git (로컬, Export 시점)

| 상태 | 파일 |
|------|------|
| Modified | `README.md` |
| Untracked | `Report/04.*`, `Report/05.*`, `Prompt/*`, `tests/conftest.py`, `tests/entity/test_d_loc_01.py`, `src/entity/constants.py`, `.cursor/skills/red-skeleton/` |
| HEAD | `6dfb1af` — session 3 Cursor design |

---

*End of D-LOC-01 RED Transcript Export*

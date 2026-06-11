# UnitConverter_10 — ARRR 실습 Checklist

> **갱신일:** 2026-06-11  
> **현재 Test ID:** D-LOC-01 · **Phase:** EXPORT  
> **RED 묶음:** D-LOC-01 ~ D-LOC-03 (FR-LOC-01)

---

## ARRR Command 체인

| # | Command | TestID | 상태 |
|---|---------|--------|------|
| A | `/red-test-plan` | D-LOC-01~03 | [x] |
| R | `/red-skeleton` | D-LOC-01 | [x] |
| R | `/green-minimal` | D-LOC-01 | [x] |
| R | `/golden-master` | D-LOC-01 | [ ] *(Command 갱신 ✅ · 실행 ⏳)* |
| R | `/refactor-smell` | D-LOC-01 | [ ] *(Command 갱신 ✅ · 실행 ⏳)* |
| R | `/refactor-safe` | D-LOC-01 | [ ] |
| — | `/export-session` | D-LOC-01 | [x] |

---

## D-LOC (Logic · entity)

| Test ID | RED skeleton | GREEN | Golden | Refactor |
|---------|--------------|-------|--------|----------|
| D-LOC-01 | [x] | [x] | [ ] | [ ] |
| D-LOC-02 | [ ] | [ ] | [ ] | [ ] |
| D-LOC-03 | [ ] | [ ] | [ ] | [ ] |

### conftest 픽스처

- [x] `grid_g1` — G1 `[(2,2),(3,3)]`
- [ ] `grid_g2` — G2 `[(1,1)]`
- [ ] `grid_g3` — G3 `[]`

### SSOT (`src/entity/constants.py`)

- [x] `GRID_ROWS` / `GRID_COLS` / `GRID_SUBGRID`
- [x] `GRID_BLANK` / `GRID_INDEX_BASE`

---

## UnitConverter (PRD FR-01~06 · 별 트랙)

| 항목 | 상태 |
|------|------|
| `/tdd-red` D-001~005 (entity) | [ ] |
| D-006~011 (control) | [ ] |
| U-IN-01~02 (boundary) | [ ] |
| `tests/test_converter.py` 회귀 | [x] *(7/7 중 6건)* |

---

## D-SOL (별도 · 미착수)

| Test ID | RED | GREEN | Golden |
|---------|-----|-------|--------|
| D-SOL-01 | [ ] | [ ] | [ ] *(test_d_sol_01.py 없음)* |

---

## Cursor · Harness

| 항목 | 상태 |
|------|------|
| `.cursorrules` | [x] |
| `unit-converter-tdd` Skill | [x] |
| `unit-converter-docs` Skill | [x] |
| ARRR Commands 7종 | [x] |
| `/review-ecb` | [ ] |

---

## 문서 Export

| 파일 | Phase | 상태 |
|------|-------|------|
| `Report/07.D_LOC_01_ARRR_Session_Report.md` | EXPORT | [x] |
| `Prompt/Session_D_LOC_01_ARRR_Transcript_Export.md` | EXPORT | [x] |
| `Prompt/ARRR_Checklist.md` | 누적 | [x] |

---

## Git *(기록만 — commit 사용자 요청)*

- [ ] 로컬 변경 검토
- [ ] commit *(사용자 요청 시)*
- [ ] push *(사용자 요청 시)*

---

## 다음 액션 (1줄)

> `/golden-master` D-LOC-01 Approval Test → `/refactor-smell` (P0 1건 골라 `/refactor-safe`)

---

*End of ARRR Checklist — 2026-06-11*

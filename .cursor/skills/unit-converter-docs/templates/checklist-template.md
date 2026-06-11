# UnitConverter_10 — ARRR 실습 Checklist

> **갱신일:** {YYYY-MM-DD}  
> **현재 Test ID:** {TestID} · **Phase:** {Phase}  
> **RED 묶음:** D-LOC-01 ~ D-LOC-03 (FR-LOC-01)

---

## ARRR Command 체인

| # | Command | TestID | 상태 |
|---|---------|--------|------|
| A | `/red-test-plan` | D-LOC-01~03 | [ ] |
| R | `/red-skeleton` | D-LOC-01 | [ ] |
| R | `/green-minimal` | D-LOC-01 | [ ] |
| R | `/golden-master` | D-LOC-01 | [ ] |
| R | `/refactor-smell` | D-LOC-01 | [ ] |
| R | `/refactor-safe` | D-LOC-01 | [ ] |
| — | `/export` | {TestID} | [ ] |

---

## D-LOC (Logic · entity)

| Test ID | RED | GREEN | Golden | Refactor |
|---------|-----|-------|--------|----------|
| D-LOC-01 | [ ] | [ ] | [ ] | [ ] |
| D-LOC-02 | [ ] | [ ] | [ ] | [ ] |
| D-LOC-03 | [ ] | [ ] | [ ] | [ ] |

### SSOT · conftest

- [ ] `GRID_*` · `GRID_BLANK` · `GRID_INDEX_BASE`
- [ ] `grid_g1` · `grid_g2` · `grid_g3`

---

## PRD FR-01~06 (UnitConverter · 별 트랙)

| 항목 | 상태 |
|------|------|
| D-001~005 entity | [ ] |
| D-006~011 control | [ ] |
| U-* boundary | [ ] |
| `tests/test_converter.py` 회귀 | [ ] |

---

## Cursor · Export

| 항목 | 상태 |
|------|------|
| `.cursorrules` | [x] |
| `unit-converter-tdd` Skill | [ ] |
| `unit-converter-docs` Skill | [ ] |
| ARRR Commands 6종 | [ ] |
| `Report/NN.REPORT.md` | [ ] |
| `Prompt/ARRR_Checklist.md` | [ ] |

---

## Git *(commit 사용자 요청)*

- [ ] commit · [ ] push

---

## 다음 액션

> {`/command` 한 줄}

---

*End of ARRR Checklist — {YYYY-MM-DD}*

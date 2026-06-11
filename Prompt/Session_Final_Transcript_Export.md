# UnitConverter_10 — Final Transcript Export

> **Export일:** 2026-06-11  
> **브랜치:** `red`  
> **범위:** Mom Test → ECB → Harness → Cursor 8계층 → Hook → RED 설계 → README  
> **형식:** 세션 전체 대화·작업 요약 (가공)

---

## Timeline

| # | 주제 | 산출물 |
|---|------|--------|
| 1 | Mom Test 인터뷰 (페르소나 A) | `Report/MomTest_Report.md`, `Prompt/MomTest_Interview_Log.md` |
| 2 | Mom Test 워크북 · 시뮬레이션 (페르소나 B) | 진짜 문제 · 증거 3줄 |
| 3 | Mom Test 질문 10개 (✅/❌) | 5카테고리 인터뷰 질문 |
| 4 | Mom Test 채점 | 8/10 · 보완 질문 1개 |
| 5 | 문제 정의 · PRD | `Report/01.*`, `docs/PRD.md` |
| 6 | ECB 개념분석 | Entity / Control / Boundary |
| 7 | Harness · pytest | `pyproject.toml`, `src/`, `tests/`, 6 passed |
| 8 | `.cursorrules` · Rule 리뷰 | ECB · Dual-Track · E001~E007 |
| 9 | Skill · Command | `unit-converter-tdd`, `/tdd-red`, `/review-ecb` |
| 10 | Tool/MCP · Loop SC-1~5 | pytest 성공 기준 |
| 11 | Hook | `sessionStart`, `postToolUse(Write)` |
| 12 | 세션 3 마무리 · GitHub | `Report/03.*`, push `main`/`spec` |
| 13 | RED 플랜 (Logic) | D-LOC-01~03 · `test_d_loc_01.py` |
| 14 | RED 플랜 (UI) | U-IN-01~02 · E001/E003 |
| 15 | README 갱신 | 구조 · ECB · Cursor · pytest |
| 16 | 종합 보고 | `Report/04.*`, 본 Transcript |
| 17 | `/red-test-plan` FR-LOC-01 | C2C · D-LOC-01~03 설계표 |
| 18 | `/red-skeleton` D-LOC-01 | `tests/conftest.py`, `test_d_loc_01.py` |
| 19 | RED 보고 · Transcript | `Report/05.*`, `Session_D_LOC_01_Transcript_Export.md` |

---

## Part A — Mom Test

### A1. 실인터뷰 (페르소나 A)

- feet→meter 암산 어려움 · meter/feet/yard 차이 모름
- **행동:** 인터넷 단위 변환기 검색
- **비용:** 10분+, 사이트 4~5개, UI depth 포기
- **진짜 문제:** 읽기 중단 + 탐색·선별 비용
- **표면 (❌):** ~~자동 변환 프로그램~~

### A2. 시뮬레이션 (페르소나 B · ⚠️ 가상)

- yard PDF 공백 · 블로그/위키 5분 · 3.28084 곱/나눗 3분
- **진짜 문제:** PDF·검색만으로 코딩 시작 지연

### A3. 채점 · 8계층 권고

- **8/10** — 실수·Loop↔증거 연결 △
- **권고:** Test Loop ↔ Hook **구멍** → `stop` Hook

---

## Part B — 문서 · Report

| 파일 | 역할 |
|------|------|
| `Report/01` | Mom Test + ECB + Test Loop |
| `Report/03` | 세션 3 Cursor 마무리 |
| `Report/04` | 프로젝트 종합 |
| `docs/PRD.md` | FR-01~06, AC |
| `README.md` | 실행 · 구조 · 8계층 |

---

## Part C — ECB · Dual-Track

```
boundary → control → entity
```

| Track | Layer | ID | Mock |
|-------|-------|-----|------|
| Logic | entity, control | D-* / D-LOC-* | ❌ Domain Mock |
| UI | boundary | U-* / U-IN-* | ✅ stdin/stdout |

- entity **E001~E005 emit 금지**
- SSOT: `src/entity/constants.py` (예정)

---

## Part D — Cursor 8계층

| 계층 | 산출물 |
|------|--------|
| Rule | `.cursorrules` |
| Skill | `.cursor/skills/unit-converter-tdd/` + `reference.md` |
| Command | `tdd-red.md`, `review-ecb.md` |
| Hook | `hooks.json`, `session-init.sh`, `hint-after-src-test-write.sh` |
| Loop | `python -m pytest tests/ -v` |

---

## Part E — RED (Logic · FR-LOC-01)

### Logic — D-LOC-01~03 (격자 blank 좌표)

| ID | Given | Then |
|----|-------|------|
| D-LOC-01 | `grid_g1` (0×2) | `[(2,2),(3,3)]` ✅ RED 스켈레톤 |
| D-LOC-02 | `grid_g2` (0×1) | `[(1,1)]` ⏳ |
| D-LOC-03 | `grid_g3` (0×0) | `[]` ⏳ |

- 파일: `tests/entity/test_d_loc_01.py`
- pytest: `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v`
- 상세: `Report/05.*`, `Prompt/Session_D_LOC_01_Transcript_Export.md`

### UI — U-IN-01~02

| ID | Given | Then |
|----|-------|------|
| U-IN-01 | `meter2.5` | E001 |
| U-IN-02 | `cubit:1` | E003 |

- 파일: `tests/boundary/test_u_in_01.py`

---

## Part F — Git

| 항목 | 내용 |
|------|------|
| Remote | https://github.com/changburi/UnitConverter_10 |
| 브랜치 | `main`, `spec`, `red` |
| 커밋 | `19ca222` Mom Test/PRD · `6dfb1af` Cursor design |

---

## Part G — 재사용 프롬프트

```
# Mom Test
UnitConverter_10 STEP 1 — Mom Test 인터뷰 (질문 1개, 과거 사실)

# RED
/tdd-red
Phase: RED | Layer: entity | Track: Logic | TestID: D-LOC-01

# ECB Review
/review-ecb
범위: src/, tests/
```

---

## Part H — 미완료 체크리스트

- [x] `tests/entity/test_d_loc_01.py` RED (D-LOC-01)
- [x] `src/entity/constants.py` (GRID 34/16/4)
- [ ] D-LOC-02 / D-LOC-03 RED 스켈레톤
- [ ] `find_blank_coords` entity GREEN
- [ ] `tests/boundary/test_u_in_01.py` RED
- [ ] `stop` Hook
- [ ] Activity 4

---

*End of Final Transcript Export*

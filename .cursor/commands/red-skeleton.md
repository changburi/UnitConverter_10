# RED Skeleton — pytest.fail 스켈레톤

UnitConverter_10 Dual-Track TDD **RED 스켈레톤 단계만** 수행한다.  
헌법: `.cursorrules` · Skill: `.cursor/skills/red-skeleton/SKILL.md` · ARRR: `.cursor/skills/unit-converter-tdd/SKILL.md` · 선행: `/red-test-plan`

---

## 슬래시 단독 입력 (고정 컨텍스트)

```
Phase: RED | Layer: entity | Track: Logic | TestID: D-LOC-01
파일: tests/entity/test_d_loc_01.py
함수: test_d_loc_01_blank_coords_row_major
픽스처: tests/conftest.py — grid_g1 (4×4, 0 두 칸)
Then: pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패") 한 줄만
src/: constants.py SSOT만 · find_blank_coords 구현 금지
```

---

## 필수 선언

```
Phase: RED | Layer: entity | Track: Logic | TestID: D-LOC-01
```

---

## 절차

1. 설계표 확인 — G1 → `[(2,2),(3,3)]`
2. `tests/conftest.py` — `grid_g1` (로직 없음 · `GRID_*` import)
3. `tests/entity/test_d_loc_01.py` — **모듈 레벨 함수** (클래스 래퍼 금지)
4. AAA 주석 · `pytest.fail` **한 줄만**
5. pytest **FAILED** 확인
6. 보고 — Test ID · FAIL · 변경 파일 `tests/`만

---

## pytest

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

**RED 완료:** FAILED + `RED: D-LOC-01`

---

## 보고

| **TestID** | D-LOC-01 |
| **FAIL** | `FAILED … RED: D-LOC-01 — 구현 없음, 의도적 실패` |
| **변경 파일** | `tests/conftest.py`, `tests/entity/test_d_loc_01.py` |
| **다음** | `/green-minimal` |

---

## 금지

- src/ 구현 · assert · skip · xfail · D-LOC-02/03 동시 · GREEN · **추가 질문** · git commit

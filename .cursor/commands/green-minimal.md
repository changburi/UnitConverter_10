# GREEN Minimal — entity 최소 구현

UnitConverter_10 **GREEN 단계 (entity Logic 최소 구현)** 만 수행한다.  
헌법: `.cursorrules` · Skill: `.cursor/skills/green-minimal/SKILL.md` · ARRR: `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 슬래시 단독 입력 (고정 컨텍스트)

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-LOC-01
RED 대상: tests/entity/test_d_loc_01.py
구현: src/entity/loc.py — find_blank_coords(grid)
SSOT: GRID_BLANK, GRID_INDEX_BASE → constants.py
Then: assert result == [(2, 2), (3, 3)]
```

---

## 필수 선언

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-LOC-01
```

---

## 절차

1. **RED 재확인** — pytest.fail FAILED
2. **`find_blank_coords`** — row-major · SSOT · E001~E005 금지 · ECB
3. **`pytest.fail` → assert** 교체
4. **PASS:**  
   `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v`  
   `python -m pytest tests/entity/test_d_loc_01.py -v`
5. **회귀:** `python -m pytest tests/ -v`
6. **(선택) REPL** — G1 → `[(2,2),(3,3)]`

---

## 보고

| **PASS Test ID** | D-LOC-01 |
| **변경 파일** | `src/entity/loc.py`, `constants.py`, `tests/entity/test_d_loc_01.py` |
| **회귀** | 실패 시 즉시 수정 |
| **다음** | `/golden-master` |

---

## 금지

- D-LOC-02/03 동시 · REFACTOR · assert 완화 · **추가 질문** · git commit

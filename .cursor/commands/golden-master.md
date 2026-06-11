# Golden Master — Approval Test 구축·검증

UnitConverter_10 **GREEN PASS 후 Golden Master(Approval Test)** 구축·검증.  
`.cursorrules`: snapshot 재생성은 **`UPDATE_GOLDEN=1` 또는 사용자 승인** 시만.  
헌법: `.cursorrules` · SSOT: `docs/PRD.md` · ARRR: `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 슬래시 단독 입력 (고정 컨텍스트)

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-LOC-01
전제: tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major PASS
Golden ID: d-loc-01
Golden: tests/golden/d-loc-01.approved.txt
Act: str(find_blank_coords(grid_g1))
```

---

## 필수 선언

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-LOC-01
```

---

## 전제

대상 Test ID **pytest PASS**. 미충족 → **중단** · `/green-minimal` 선행.

---

## 절차

### 1. `tests/_approval.py`

`assert_matches_golden(golden_id: str, actual: str) -> None`  
경로: `tests/golden/{golden_id}.approved.txt`  
`UPDATE_GOLDEN=1` → 기준 생성 · 없으면 전문 일치 assert

### 2. 테스트에 Approval assert 추가 (unit assert **유지**)

```python
from tests._approval import assert_matches_golden
assert_matches_golden("d-loc-01", str(find_blank_coords(grid_g1)))
```

### 3. 기준 생성

```bash
UPDATE_GOLDEN=1 python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

```powershell
$env:UPDATE_GOLDEN=1; python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

### 4. matched 확인 (`UPDATE_GOLDEN` 없음)

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/ -v
```

---

## 포맷 고정

> **int[6] 1-index** — E001~ (E000·0-index enum 금지)

| 영역 | 규칙 | 예 |
|------|------|-----|
| Logic 좌표 | 1-index · `str(list)` | `[(2, 2), (3, 3)]` |
| 오류 문자열 | boundary 표시 그대로 | FR-04 E001 메시지 |
| golden | **수동 편집 우회 금지** | diff → 코드 수정 후 `UPDATE_GOLDEN=1` 승인 |

---

## 보고

| **golden 경로** | `tests/golden/d-loc-01.approved.txt` |
| **matched** | matched / mismatch |
| **diff 요약** | mismatch 시 expected vs actual |
| **다음** | `/refactor-smell` |

---

## 금지

- golden 수동 편집 · assert 완화 · D-LOC-02/03 동시 · **추가 질문** · git commit

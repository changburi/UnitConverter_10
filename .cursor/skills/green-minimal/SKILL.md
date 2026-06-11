---
name: green-minimal
description: >-
  UnitConverter_10 entity Logic Track GREEN 최소 구현. RED pytest.fail 확인 후
  src/entity 최소 코드·assert 교체·PASS. /red-skeleton 다음 단계. D-LOC-01 등.
---

# GREEN Minimal Skill

`/green-minimal` — **Phase: GREEN** entity Logic Track **최소 구현**만 수행한다.  
헌법: `.cursorrules` · 선행: `/red-skeleton` 또는 RED 스켈레톤(`pytest.fail`) 완료

---

## 필수 선언

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-xxx
```

기본 예시 (D-LOC-01):

```
Phase: GREEN | Layer: entity | Track: Logic | TestID: D-LOC-01
RED 대상: D-LOC-01 (tests/entity/test_d_loc_01.py)
```

---

## 언제 사용

- `/red-skeleton` 완료 후 **단일 Test ID** GREEN이 필요할 때
- `pytest.fail("RED: …")` 상태에서 **최소 `src/entity/` 구현** + assert 교체
- **REFACTOR / 다른 RED 묶음 ID / control·boundary** — 이 Skill 범위 **아님**

---

## 절차

1. **RED 재확인** — 의도적 fail/`pytest.fail` 상태인지 pytest 실행
2. **`src/entity/`** 에 `find_blank_coords()` 최소 구현
   - 하드코딩·매직넘버 금지 → `entity/constants.py` SSOT
   - E001~E005 raise/return 금지
   - ECB: entity는 boundary/control import 금지
3. **RED 스켈레톤의 `pytest.fail` 제거** → 실제 assert로 교체
4. **PASS 확인:**
   ```bash
   python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
   python -m pytest tests/entity/test_d_loc_01.py -v
   ```
5. **(선택) REPL 스모크** — G1 입력 vs Then `[(2,2),(3,3)]`

---

## Step 1 — RED 재확인

대상 테스트 파일·함수만 실행. **FAILED** + `RED: {TestID}` 메시지여야 GREEN 착수 가능.

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

| 결과 | 조치 |
|------|------|
| FAILED (`pytest.fail` / ImportError) | Step 2 진행 |
| PASSED | 이미 GREEN — 중복 구현 금지, 사용자 확인 |
| FAILED (다른 assert) | RED 스켈레톤 상태 복원 후 재확인 |

---

## Step 2 — entity 최소 구현 (D-LOC-01)

**파일:** `src/entity/loc.py` — `find_blank_coords(grid)`

| 규칙 | 내용 |
|------|------|
| SSOT | `GRID_BLANK`, `GRID_INDEX_BASE` 등 `src/entity/constants.py`만 |
| 스캔 | row-major 이중 루프, blank → 1-index `(row, col)` |
| Entity 금지 | E001~E005 처리·검사·오류 문자열·raise |
| ECB | `from src.control` / `from src.boundary` **금지** |
| Logic Mock | Domain Mock **금지** — conftest 실 데이터만 |

**상수 추가 예 (SSOT):**

| 상수 | 용도 |
|------|------|
| `GRID_BLANK` | blank 칸 값 (0 리터럴 금지) |
| `GRID_INDEX_BASE` | 0-based → 1-index 변환 |

---

## Step 3 — assert 교체

RED 스켈레톤 Then을 **실제 assert**로 교체. AAA 주석 유지.

```python
from src.entity.loc import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    result = find_blank_coords(grid_g1)
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    assert result == [(2, 2), (3, 3)]
```

- `pytest.fail("RED: …")` **삭제**
- `pytest.approx` · assert 완화 · skip · xfail **금지**

---

## Step 4 — PASS 확인

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/entity/test_d_loc_01.py -v
```

**회귀 실패 시** — 즉시 수정 후 위 명령 재실행. 다른 Test ID 동시 수정 금지.

전체 회귀(선택·권장):

```bash
python -m pytest tests/ -v
```

---

## Step 5 — (선택) REPL 스모크

```python
from tests.conftest import grid_g1  # 또는 conftest 픽스처와 동일 데이터 구성
from src.entity.loc import find_blank_coords

g = grid_g1()
find_blank_coords(g)  # 기대: [(2, 2), (3, 3)]
```

---

## 금지

- 이번 RED 묶음 **외 ID** 동시 해결 (예: D-LOC-01 GREEN 중 D-LOC-02/03 구현)
- **REFACTOR** (이름 정리·대규모 이동·중복 제거)
- assert 완화 · skip · xfail · MagicConstant 리터럴 산재
- control / boundary Layer 수정 (요청 없으면)
- git commit/push (사용자 요청 시만)

---

## 완료 보고 형식

한국어로 보고한다.

| 항목 | 내용 |
|------|------|
| **PASS Test ID** | D-xxx |
| **변경 파일** | `src/entity/*.py`, `tests/entity/test_d_*.py` 목록 |
| **Loop 결과** | 실행한 pytest 명령 + passed/failed |
| **회귀** | 실패 시 수정 내역 (없으면 "없음") |
| **ECB** | entity E001~E005 미사용 · import 방향 준수 |
| **다음** | REFACTOR 또는 다음 Test ID GREEN (사용자 요청 시) |

**응답 첫 줄:** `Phase: GREEN | Layer: entity | Track: Logic | TestID: D-xxx`

---

## RED → GREEN 체인

| 단계 | Skill / Command |
|------|-----------------|
| 설계표 | `/red-test-plan` |
| RED 스켈레톤 | `/red-skeleton` |
| **GREEN 최소** | **`/green-minimal`** ← 이 Skill |
| REFACTOR | 별도 요청 (`unit-converter-tdd` REFACTOR 절) |

---

## 참고

- 헌법: `.cursorrules`
- TDD 전체: [unit-converter-tdd](../unit-converter-tdd/SKILL.md)
- D-* ID: [reference.md](../unit-converter-tdd/reference.md)

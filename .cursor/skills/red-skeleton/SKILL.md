---
name: red-skeleton
description: >-
  UnitConverter_10 RED 스켈레톤만 작성. 확정 설계표 기준 tests/ 파일·pytest.fail
  Then. src/ 구현 금지(GREEN 전). /red-test-plan 다음 단계.
---

# RED Skeleton Skill

`/red-skeleton` — **Phase: RED** 스켈레톤만 `tests/`에 작성한다.  
헌법: `.cursorrules` · 선행: `/red-test-plan` 또는 확정 설계표

---

## 필수 선언

```
Phase: RED | Layer: entity|control|boundary | Track: Logic|UI | TestID: D-xxx
```

---

## 언제 사용

- `/red-test-plan` 완료 후 **테스트 파일 뼈대**만 필요할 때
- `pytest.fail("RED: …")` 로 **의도적 FAIL** 확인할 때
- **GREEN / REFACTOR / src/ 구현** — 이 Skill 범위 **아님**

---

## 절차

1. **설계표 확인** — Test ID, Given/Then, Expected RED Failure
2. **파일** — Logic: `tests/entity/test_d_*.py` · UI: `tests/boundary/test_u_*.py`
3. **conftest** — `tests/conftest.py` 픽스처 (로직 없음, SSOT 상수 import만)
4. **AAA 주석** — `# Given:` / `# When:` / `# Then:` (각 1줄)
5. **Then** — **`pytest.fail("RED: {TestID} — …")` 한 줄만** (assert 본문·skip·xfail·pass 금지)
6. **상수** — `34/16/4` 등 **리터럴 금지** → `src/entity/constants.py` import (픽스처·conftest만)
7. **pytest 실행** — 설계표 명령 · **FAILED** 확인
8. **보고** — Test ID · FAIL 한 줄 · 변경 파일 `tests/`(+ constants SSOT만)

---

## 템플릿 (D-LOC-01)

```python
class TestDLoc01BlankCoords:
    def test_d_loc_01_blank_coords_row_major(self, grid_g1):
        # Given: G1 격자 (0이 2개)
        # When: find_blank_coords(grid_g1) 호출
        # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
        pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
```

---

## 금지

- `src/` **구현** (find_blank_coords, Solver 등) — `constants.py` SSOT **만** 허용
- assert 본문으로 GREEN 우회 · `@pytest.mark.skip` · `@pytest.mark.xfail`
- Logic Track Domain Mock
- git commit/push (사용자 요청 시만)

---

## 완료 보고 형식

| 항목 | 내용 |
|------|------|
| TestID | D-xxx |
| FAIL | pytest 한 줄 |
| 변경 파일 | `tests/` 목록 |

**다음:** `/green-minimal` · ARRR: [unit-converter-tdd](../unit-converter-tdd/SKILL.md)

---

## pytest 예시

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

**RED 완료:** 위 테스트 **FAILED** + 메시지 `RED: D-LOC-01`

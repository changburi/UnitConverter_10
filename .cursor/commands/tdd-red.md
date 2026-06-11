# TDD RED — 실패 테스트 먼저

UnitConverter_10 Dual-Track TDD **RED 단계만** 수행한다.  
헌법: `.cursorrules` · 상세 절차: `.cursor/skills/unit-converter-tdd/SKILL.md` · ID: `reference.md`

---

## 필수 선언

**응답 첫 줄 (고정 형식):**

```
Phase: RED | Layer: entity|control|boundary | Track: Logic|UI | TestID: D-xxx|U-xxx
```

| Track | Layer | TestID | 테스트 파일 |
|-------|-------|--------|-------------|
| Logic | entity, control | `D-*` | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` |
| UI | boundary | `U-*` | `tests/boundary/test_u_*.py` |

---

## 절차

1. **ID 확인** — `D-*` / `U-*`를 `.cursor/skills/unit-converter-tdd/reference.md`(Logic) 또는 사용자 지정 ID와 매핑. 중복 ID 없음 확인.
2. **파일 위치** — Layer·Track에 맞는 `tests/<layer>/test_d_*` 또는 `test_u_*`에만 추가. **`src/` 수정 금지.**
3. **AAA 테스트 작성**
   - **Arrange** — 입력·상수는 README SSOT(`3.28084`, `1.09361`) 또는 `src/entity/constants.py` import(테스트에서 constants만 import 가능).
   - **Act** — 테스트 대상 호출(미구현 시 import 실패·NotImplemented 허용).
   - **Assert** — 기대값 **엄격** assert. skip / xfail / 기대값 완화 금지.
4. **Logic Track** — Solver·UnitRatio **Domain Mock 금지**. UI Track(boundary)만 stdin/stdout Mock 허용.
5. **pytest 실행** — Track별 명령으로 **새 테스트 FAIL** 확인 (ImportError만으로 RED 완료 인정 안 함).
6. **보고** — 아래 보고 형식으로 종료. GREEN·REFACTOR·`src/` 구현은 **하지 않음**.

---

## pytest 예시 (bash)

```bash
# Logic Track (entity + control)
python -m pytest tests/entity tests/control -v -k "D-002"

# UI Track (boundary)
python -m pytest tests/boundary -v -k "U-001"

# Layer 단일
python -m pytest tests/entity -v
python -m pytest tests/control -v
python -m pytest tests/boundary -v
```

**RED 완료 조건:** 대상 TestID 테스트가 **FAILED** (AssertionError / ModuleNotFoundError / NotImplementedError 등 구현 부재로 인한 실패).

---

## 보고

한국어로만 보고한다.

| 항목 | 내용 |
|------|------|
| **TestID** | D-xxx 또는 U-xxx |
| **FAIL 요약** | 실패 테스트 함수명 + pytest 한 줄 (예: `FAILED test_d_feet_to_meter - ImportError`) |
| **변경 파일** | `tests/` 하위 경로만 나열 |
| **다음 단계** | GREEN은 사용자 요청 시 별도 Command |

---

## 금지

- `src/` **어떤 파일도** 수정·생성하지 않는다.
- Logic Track(entity, control)에서 Solver·변환 로직 **Domain Mock** 사용.
- assert 완화, `@pytest.mark.skip`, `@pytest.mark.xfail`, 기대값 임의 변경.
- `3.28084` / `1.09361` 등 MagicConstant **테스트 파일에 리터럴 산재** (constants·README SSOT 사용).
- git commit / push (사용자 명시 요청 시만).
- RED 단계에서 GREEN 구현·REFACTOR.

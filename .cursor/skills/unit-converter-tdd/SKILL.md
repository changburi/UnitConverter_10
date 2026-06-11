---
name: unit-converter-tdd
description: UnitConverter_10 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차
---

# UnitConverter_10 — Dual-Track TDD Skill

`.cursorrules` 헌법을 전제로, entity / control / boundary 개발·테스트 시 이 Skill을 따른다.

---

## 언제 이 Skill을 켜는가

| 트리거 | 예 |
|--------|-----|
| `src/entity`, `src/control`, `src/boundary` 코드·테스트 작성·수정 | Solver, Validator, CLI 출력 |
| `tests/entity/test_d_*`, `tests/control/test_d_*`, `tests/boundary/test_u_*` 추가 | D-001 yard 변환 등 |
| TDD Phase(RED/GREEN/REFACTOR) 진행 요청 | "실패 테스트부터", "GREEN 맞춰줘" |
| ECB 리팩터 후 회귀 확인 | import 방향·오류 책임 점검 |
| **켜지 않음** | Report/Mom Test 문서만, git commit/push, Activity 4(설정·포맷) |

시작 시 **반드시 선언** (매 응답 상단):

`Phase: RED|GREEN|REFACTOR | Layer: entity|control|boundary | Track: Logic|UI | TestID: D-xxx|U-xxx`

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| **Layer** | entity, control | boundary |
| **테스트 ID** | `D-*` | `U-*` |
| **파일** | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` | `tests/boundary/test_u_*.py` |
| **Mock** | Domain Mock **금지** | stdin/stdout·InputHandler Mock **허용** |
| **상수** | `src/entity/constants.py` SSOT만 | SSOT import, 리터럴 산재 금지 |
| **pytest** | `tests/entity` + `tests/control` | `tests/boundary` |

테스트 ID 목록: [reference.md](reference.md)

---

## ECB · Mock · E001~E007

### import (허용 / 금지)

| | 허용 | 금지 |
|---|------|------|
| **entity** | stdlib, typing, `src/entity/*` 내부 | control, boundary, pytest, I/O |
| **control** | entity, stdlib | boundary |
| **boundary** | control | entity **직접** import (control 경유) |

### 오류 코드

| 코드 | 의미 | 검증 | 표시 |
|------|------|------|------|
| E001 | 형식 오류 | control | boundary |
| E002 | 숫자 오류 | control | boundary |
| E003 | 미지원 원본 단위 | control | boundary |
| E004 | 음수 | control | boundary |
| E005 | 빈 입력·빈 값 | control | boundary |
| E006 | 미지원 대상 단위 | control/boundary | boundary |
| E007 | 출력·I/O 실패 | boundary | boundary |

**Entity 금지:** E001~E005 처리·검사·오류 문자열 생성·raise. **유효한 값 객체만** 입력.

### Mock

| Mock 대상 | Logic Track | UI Track |
|-----------|-------------|----------|
| Solver / 변환 로직 | ❌ | — |
| UnitRatio / constants | ❌ (실제 SSOT) | — |
| stdin / stdout / input() | — | ✅ |
| subprocess 전체 Mock | ❌ (Logic) | △ 최소화, 통합는 실 CLI 권장 |

---

## RED (5~7단계)

1. **선언** — Phase=RED, Layer, Track, TestID (`reference.md`에서 선택 또는 신규 ID 제안).
2. **근거 확인** — README·PRD·Report/01의 기대값·Mom Test 증거(S1 yard, S2 SSOT, S3 곱/나눗)와 매핑.
3. **테스트 파일** — Logic→`test_d_*`, UI→`test_u_*`, 해당 `tests/<layer>/`에만 추가.
4. **실패 테스트 1개** — 구현 **없이** assert만. skip/xfail/assert 완화 금지.
5. **SSOT** — 기대값은 `constants.py`(또는 README 상수 import)에서만; `3.28084` 리터럴 산재 금지.
6. **Loop 실행** — Track별 pytest → **FAIL 확인** (RED 완료 조건).
7. **완료 전 금지** — prod 코드 추가, 기대값 낮추기, `@pytest.mark.skip`.

---

## GREEN (5~7단계)

1. **선언** — Phase=GREEN, 동일 Layer/Track/TestID.
2. **범위** — RED 테스트를 green시키는 **최소 코드만** 해당 Layer에 추가.
3. **ECB** — entity=순수 변환, control=검증+Solver, boundary=I/O·E00x 표시.
4. **Entity 규칙** — E001~E005 로직 넣지 않음; Validator가 걸러진 값만 entity에 전달.
5. **Loop 실행** — 대상 Track pytest → **PASS**.
6. **전체 회귀** — `python -m pytest tests/ -v` → 기존 `tests/test_converter.py` 포함 PASS.
7. **완료 전 금지** — REFACTOR성 대규모 이동, 요청 없는 Layer 수정, skip/xfail.

---

## REFACTOR (5~7단계)

1. **선언** — Phase=REFACTOR, Layer, Track.
2. **전제** — GREEN 상태에서만 시작; 동작·테스트 의미 변경 금지.
3. **허용** — 이름 정리, constants SSOT 통합, ECB 파일 분리, 중복 제거.
4. **금지** — assert 완화, 테스트 삭제, MagicConstant 새 리터럴, entity에 검증 추가.
5. **Track Loop** — 해당 Layer pytest → PASS.
6. **전체 Loop** — `python -m pytest tests/ -v` → PASS.
7. **Review Loop (Track 2, 선택)** — Report/01·PRD와 ECB·SSOT 일치 육안 확인 (pytest와 별도).

---

## Test / Review Loop — pytest 실행 시점

| 시점 | 명령 | 통과 기준 |
|------|------|-----------|
| RED 직후 | Logic: `python -m pytest tests/entity tests/control -v`<br>UI: `python -m pytest tests/boundary -v` | **새 테스트 FAIL** (ImportError만으로 RED 인정 안 함) |
| GREEN 직후 | 위 Track pytest | **해당 테스트 PASS** |
| GREEN 회귀 | `python -m pytest tests/ -v` | **전체 PASS** |
| REFACTOR 각 단계 | Track pytest → 전체 pytest | **전체 PASS 유지** |
| ECB 계약만 리뷰 | pytest 생략 가능 | import·E001~E007 표 작성 후 사용자 확인 |

**금지:** 실패를 skip/xfail/approx 완화로 green 처리. Golden Master·snapshot 재생성은 **사용자 명시 승인** 시만.

---

## 완료 보고 항목

작업 종료 시 **한국어**로 아래를 보고한다.

1. **선언 요약** — Phase, Layer, Track, TestID
2. **변경 파일** — 경로 목록
3. **Loop 결과** — 실행한 pytest 명령 + passed/failed/failed 테스트명
4. **ECB 준수** — import 방향, Entity E001~E005 미사용 여부
5. **SSOT** — 상수 출처(`constants.py` / README)
6. **미완료** — 다음 Phase, 블로cker, 사용자 결정 필요 사항
7. **git** — commit/push **하지 않음** (사용자 요청 시만)

---

## 레거시

- `UnitConverter.py`, `tests/test_converter.py` — ECB 이전. 신규는 `src/`·`test_d_*`/`test_u_*` 우선. 레거시 수정 시에도 `.cursorrules` 준수.

---

## 참고

- 헌법: `.cursorrules`
- D-* ID: [reference.md](reference.md)
- PRD: `docs/PRD.md`

# UnitConverter_10 — Product Requirements Document (PRD)

> **문서:** docs/PRD.md  
> **버전:** 0.1 (Draft)  
> **작성일:** 2026-06-11  
> **근거:** [`Report/01.UnitConverter_ProblemDefinition_Report.md`](../Report/01.UnitConverter_ProblemDefinition_Report.md)

---

## 1. 개요

### 1.1 제품 한 줄 설명

사용자가 `단위:값` 형식으로 길이를 입력하면, **meter 기준**으로 정규화한 뒤 **지원하는 모든 길이 단위**로 변환 결과를 출력하는 Python CLI 프로그램.

### 1.2 문제 배경 (Mom Test)

**진짜 문제 (통합):**

> 단위 관계·변환 방향·수치 신뢰를 즉시 판정하지 못해 작업 흐름이 끊기고, 외부 탐색·재확인·도구 선별에 **시간 비용**(10분+, 사이트 4~5개, 계산기 양방향 확인 등)이 발생한다.

**표면 문제 (Non-Goal):**

- ~~"자동 변환 프로그램/UI를 만든다"~~
- ~~"웹 변환기를 완전 대체한다"~~

### 1.3 제품 목표

| # | 목표 | Mom Test 연결 |
|---|------|---------------|
| G1 | **한 번의 입력**으로 meter·feet·yard 동시 확인 | UI/사이트 탐색 비용 감소 |
| G2 | README **단일 상수**로 변환 — 외부 상충 숫자 제거 | 블로그/위키 5분 비교 대체 |
| G3 | **pytest**로 곱/나눗 방향·단위 커버리지 고정 | 계산기 양방향 3분 재확인 대체 |

---

## 2. 사용자 (Personas)

### 2.1 Primary — 프로그래밍 학습자

- Unit Converter 과제·실습을 수행
- meter/feet/yard 관계·코드 방향 혼동 경험
- **Needs:** 신뢰 가능한 변환 규칙, 빠른 판정, 테스트로 재현

### 2.2 Secondary — 영어 문서 독자 (학습자)

- feet·yard가 포함된 자료를 meter 감각으로 읽어야 함
- **Needs:** 즉시 변환·단순 입력, 도구 선별 부담 최소화

---

## 3. 범위

### 3.1 In Scope (Phase 1~3 — README Activities 1~3)

| ID | 기능 | 우선순위 |
|----|------|----------|
| FR-01 | `unit:value` CLI 입력 | P0 |
| FR-02 | meter, feet, yard **전 단위** 출력 | P0 |
| FR-03 | meter 기준 정규화 후 변환 | P0 |
| FR-04 | 입력 형식·숫자·미지 단위 **검증** | P0 |
| FR-05 | 변환·검증 **단위 테스트** | P0 |
| FR-06 | OCP/SRP 준수 설계 (클래스 분리) | P1 |

### 3.2 Out of Scope (Phase 4 — README 추가 요구사항)

| ID | 기능 | 사유 |
|----|------|------|
| — | JSON/YAML 설정 외부화 | Activity 4 |
| — | 동적 단위 등록 (`1 cubit = 0.4572 meter`) | Activity 4 |
| — | JSON / CSV / 표 출력 포맷 | Activity 4 |
| — | 웹 UI·검색·크롤링 | Mom Test 표면 문제 |

---

## 4. 기능 요구사항

### 4.1 입력 (FR-01, FR-04)

**형식:** `{unit}:{value}`

| 케이스 | 입력 예 | 기대 동작 |
|--------|---------|-----------|
| 정상 | `meter:2.5` | 변환 후 출력 |
| 형식 오류 | `meter2.5` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 오류 | `meter:abc` | `Invalid number: abc` |
| 미지 단위 | `cubit:1` | `Unknown unit: cubit` |
| 음수 (품질) | `meter:-1` | 검증 메시지 *(구현 예정 — Activity 2)* |

**지원 단위 (Phase 1):** `meter`, `feet`, `yard`

### 4.2 변환 (FR-02, FR-03)

**비즈니스 규칙 (단일 출처 — README):**

```
1 meter = 3.28084 feet
1 meter = 1.09361 yard
feet ↔ yard: meter 기준 간접 계산
```

**알고리즘:**

1. 입력 단위 → **meter 기준값** (`feet`, `yard`는 **나눗셈**)
2. meter 기준값 → **전 단위 출력** (`feet`, `yard`는 **곱셈**)

**출력 예 (입력 `meter:2.5`):**

```
2.5 meter = 2.5 meter
2.5 meter = 8.2021 feet    # 2.5 × 3.28084 (README 예시는 반올림 8.2)
2.5 meter = 2.734025 yard  # 2.5 × 1.09361 (README 예시는 반올림 2.7)
```

### 4.3 테스트 (FR-05)

**실행:**

```bash
python -m pytest tests/ -v
```

**필수 테스트 케이스:**

| TC | 검증 내용 | Mom Test |
|----|-----------|----------|
| TC-01 | `meter:2.5` → 전 단위 | S1 yard/PDF 공백 |
| TC-02 | `feet:8.2` → meter 역변환 | S3 곱/나눗 방향 |
| TC-03 | `yard:2.7` → meter 역변환 | S1 |
| TC-04 | Invalid format | FR-04 |
| TC-05 | Invalid number | FR-04 |
| TC-06 | Unknown unit | FR-04 |

**현재 상태:** 6 tests, all passed (`tests/test_converter.py`)

---

## 5. 비기능 요구사항

| ID | 요구 | 설명 |
|----|------|------|
| NFR-01 | **OCP** | 새 단위 추가 시 기존 코드 변경 최소 |
| NFR-02 | **SRP** | Validator / Solver / Handler / Display 분리 |
| NFR-03 | **재현성** | README 상수와 테스트 상수 일치 |
| NFR-04 | **실행 환경** | Python 3.x, pytest |

---

## 6. 아키텍처 (ECB)

```
┌─ Boundary ─────────────────────────────┐
│  InputHandler    ResultDisplay         │
└────────────┬───────────────┬───────────┘
             │               │
┌─ Control ──┴───────────────┴───────────┐
│  InputValidator    Solver              │
└────────────┬───────────────────────────┘
             │
┌─ Entity ───┴───────────────────────────┐
│  LengthInput  LengthInMeters           │
│  ConversionResult  UnitRatio           │
└────────────────────────────────────────┘
```

**현재 구현:** `UnitConverter.py` — `main()` 단일 함수 (ECB 분리 **예정**, Activity 2)

---

## 7. 성공 지표 (Acceptance Criteria)

| # | 기준 | 측정 |
|---|------|------|
| AC-1 | meter·feet·yard **3방향** 변환 테스트 통과 | `pytest` green |
| AC-2 | README 상수 **3.28084 / 1.09361** 준수 | TC-01~03 |
| AC-3 | 입력 검증 3종 메시지 출력 | TC-04~06 |
| AC-4 | CLI `meter:2.5` 실행 시 **3줄** 출력 | 수동 스모크 |
| AC-5 | Mom Test **진짜 문제** 문장에 솔루션名 없음 | 문제 정의 보고서 검수 |

---

## 8. 릴리스 계획 (Activities)

| Phase | Activity | 산출물 | 시간 |
|-------|----------|--------|------|
| 1 | 문제·코드 분석 | 문제 정의 보고서, PRD | 0.5h |
| 2 | 기본·품질 구현 | ECB 클래스, 입력 검증 | 2h |
| 3 | TC 구현 | `tests/test_converter.py` | 0.5h ✅ |
| 4 | 추가 요구사항 | 설정·동적등록·포맷 | 2h |
| 5 | 회고·발표 | Mom Test·TC 회고 | 1h |

---

## 9. 리스크 및 가정

| 리스크 | 완화 |
|--------|------|
| README 예시 **반올림**(8.2) vs 코드 **전체 소수** | 테스트는 `pytest.approx` + README 상수; 문서에 명시 |
| 페르소나 A/B **혼합** | 시뮬레이션 라벨·문서 분리 |
| `main()` monolith | Activity 2 ECB 리팩토링 |

**가정:**

- 변환 비율은 README가 **유일한 출처**
- Phase 1~3은 **CLI**만 대상 (GUI 없음)

---

## 10. 참고 문서

- [README.md](../README.md)
- [Report/01.UnitConverter_ProblemDefinition_Report.md](../Report/01.UnitConverter_ProblemDefinition_Report.md)
- [Report/MomTest_Report.md](../Report/MomTest_Report.md)
- [tests/test_converter.py](../tests/test_converter.py)

---

*PRD v0.1 — Mom Test 문제 정의 초안 기반*

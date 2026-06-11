# ECB · 계약 리뷰

UnitConverter_10 **코드 수정 금지**. `src/`, `tests/`를 읽고 **ECB·계약 위반만** 표로 보고한다.  
헌법: `.cursorrules` · 참고: `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 필수 선언

**응답 첫 줄:**

```
Phase: REVIEW | Layer: entity|control|boundary|all | Track: Logic|UI|Review
```

---

## 절차

1. **범위 확인** — 사용자가 지정한 경로(미지정 시 `src/`, `tests/` 전체). `UnitConverter.py` 레거시 포함 여부 명시.
2. **읽기만** — 파일 수정·생성·삭제 **금지**. pytest 실행은 선택(위반 탐지는 정적 리뷰 우선).
3. **체크 5항** — 아래 기준으로 파일·줄 단위 스캔.
4. **위반만 표** — 위반 없으면 `위반 없음` 한 줄. 수정 제안은 **표의 권고 열**에만(코드 패치 금지).
5. **한국어 보고** — git commit/push 금지.

---

## 체크 기준

### 1. import 방향

| 허용 | 금지 |
|------|------|
| boundary → control | control → boundary |
| control → entity | entity → control, entity → boundary |
| entity → stdlib, typing, `src/entity/*` | entity → control, entity → boundary |
| — | entity → pytest, I/O 모듈 |

### 2. entity · E001~E005

- entity/control **Solver** 내부: 형식·숫자·단위·음수·빈값 **검사·raise·오류 문자열 금지**.
- E001~E005 **검증·분류** → control (`InputValidator`).
- E001~E007 **사용자 표시** → boundary (`ResultDisplay`).

### 3. E001~E007 · 1-index · 입출력

> 체크 키: **int[6] 1-index** — 오류 슬롯 **1부터**(E001), E000·0-index enum 금지.

| 코드 | 담당 | Layer |
|------|------|-------|
| E001~E005 | 입력 검증 | control 검증 → boundary 표시 |
| E006 | 미지원 **대상** 단위 | control/boundary |
| E007 | **입·출력** I/O 실패 | boundary only |

- boundary: InputHandler(입력), ResultDisplay(출력) 분리.
- entity에 E006·E007 처리 금지.

### 4. MagicConstant SSOT

- `3.28084`, `1.09361` 등 → **`src/entity/constants.py` 단일 출처**.
- `src/`, `tests/`에 **산재 리터럴** → 위반(테스트는 constants import만 허용).

### 5. Logic Track · Domain Mock

- `tests/entity/`, `tests/control/`(`test_d_*`): Solver·UnitRatio·변환 로직 **Mock 금지**.
- `tests/boundary/`(`test_u_*`): stdin/stdout Mock **허용**.

---

## 위반 보고 표 (필수 형식)

**위반이 있을 때만** 아래 표를 채운다. 없으면: `ECB·계약 위반 없음 (검사 범위: …)`

| # | 체크 | 파일:줄 | 위반 내용 | 계약 (`.cursorrules`) |
|---|------|---------|-----------|------------------------|
| 1 | import | | | boundary→control→entity |
| 2 | E001~E005 | | | entity 검증 금지 |
| 3 | E001~E007 1-index · I/O | | | E001~, E007 boundary I/O |
| 4 | SSOT | | | constants.py only |
| 5 | Logic Mock | | | test_d_* Mock 금지 |

- **#** 열: 위반 건별 순번.
- **체크** 열: `import` / `E001~E005` / `E001~E007 1-index` / `SSOT` / `Logic Mock` 중 하나.
- 코드 블록·패치 **출력 금지**. 표 + 한 줄 요약만.

---

## 요약 (표 아래 3줄)

1. **검사 범위** — 디렉터리·파일 목록  
2. **위반 N건** — 체크별 건수  
3. **다음 액션** — 사용자가 GREEN/TDD로 고칠 항목만 나열 (Agent가 직접 수정하지 않음)

---

## 금지

- `src/`, `tests/`, `.cursorrules` **수정**.
- 위반을 skip·주석 처리·assert 완화로 “해결” 제안.
- 리뷰 없이 기능 구현·REFACTOR.

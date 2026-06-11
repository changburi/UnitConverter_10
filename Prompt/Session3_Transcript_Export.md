# UnitConverter_10 — 세션 3 Transcript Export

> **Export일:** 2026-06-11  
> **범위:** Mom Test ~ Cursor 8계층 · Hook · 세션 3 마무리  
> **형식:** 대화·작업 요약 Transcript (가공)

---

## Part A — Mom Test

### A1. 실인터뷰 (페르소나 A: 학습자 · 영어 문서)

- feet→meter 암산 어려움, meter/feet/yard 차이 모름
- 막히면 **인터넷 단위 변환기 검색**
- **10분+**, 사이트 **4~5개**, UI depth로 포기
- **진짜 문제:** 읽기 중단 + 변환기 탐색·선별 비용
- **표면 문제 (❌):** ~~자동 변환 프로그램~~

→ 저장: `Report/MomTest_Report.md`, `Prompt/MomTest_Interview_Log.md`

### A2. 시뮬레이션 (페르소나 B: 수업 학생 · ⚠️ 가상)

- yard PDF 공백, 블로그/위키 5분, 곱/나눗 3분
- **진짜 문제:** PDF·검색만으로 방향 판정 지연 → 외부 비교·양방향 재확인

### A3. Mom Test 채점 (워크북)

- **8/10** — 실수·수치 검증 내러티브·페르소나 혼합 △
- 보완 질문: 변환 숫자 의심 시 재확인 경험

---

## Part B — 문제 정의 · PRD

- `Report/01.UnitConverter_ProblemDefinition_Report.md` — Mom Test + ECB + 세션 3 Test Loop
- `docs/PRD.md` — FR/NFR, AC, Activity 1~5
- GitHub: https://github.com/changburi/UnitConverter_10

---

## Part C — ECB 개념분석

| ECB | 역할 |
|-----|------|
| Entity | LengthInput, ConversionResult, UnitRatio |
| Control | InputValidator, Solver |
| Boundary | InputHandler, ResultDisplay |

- 의존: boundary → control → entity
- entity E001~E005 금지

---

## Part D — Harness · TDD (세션 3)

### D1. 생성 파일

```
pyproject.toml
src/{entity,control,boundary}/__init__.py
tests/{entity,control,boundary}/__init__.py
tests/test_converter.py  (레거시 6 passed)
```

### D2. `.cursorrules` (Rule)

- Dual-Track, D-*/U-*, test_d_*/test_u_*
- MagicConstant SSOT → `src/entity/constants.py`
- commit/push 사용자 요청 시만

### D3. Skill

- `.cursor/skills/unit-converter-tdd/SKILL.md`
- `reference.md` — D-001~D-011

### D4. Command

- `.cursor/commands/tdd-red.md` — RED only
- `.cursor/commands/review-ecb.md` — ECB 리뷰, 수정 금지

### D5. Mom Test 질문 10개 (✅/❌ + 고친 버전)

- 카테고리: 틀림 / 검증비용 / 포기 / 재발 / 공유

---

## Part E — Tool/MCP · Loop · Hook

### E1. Tool/MCP (세션 3~4)

| Tool | 연결 |
|------|------|
| Shell pytest | Test Loop |
| Read/Write/Grep | Rule·Skill·ECB |
| GitHub MCP | (선택) PR |

### E2. Test/Review Loop SC-1~5

- SC-1 Rule ✅ · SC-2 Skill ✅ · SC-3 tdd-red ✅ · SC-4 review-ecb ✅ · SC-5 RED FAIL ❌

### E3. Hook

| Hook | 파일 |
|------|------|
| sessionStart | `session-init.sh` — MagicSquare_1004, Dual-Track, ECB, `/tdd-red` |
| postToolUse Write | `hint-after-src-test-write.sh` — pytest 힌트, flag touch |

**권고:** `stop` Hook — Loop 미완료 follow-up (구멍)

---

## Part F — 프롬프트 보관 (기존)

| 파일 | 용도 |
|------|------|
| `Prompt/MomTest_Workbook_Prompt.md` | 워크북·STEP1·종료 프롬프트 |
| `Prompt/MomTest_Interview_Log.md` | Q1~Q8 + 종료 정리 |

---

## Part G — 세션 3 마무리 (최종)

| 목표 | 결과 |
|------|------|
| Cursor 설계 산출물 | ✅ |
| Track 1 RED (`test_d_*`) | ❌ |
| ECB `src/` 구현 | ❌ (세션 4) |

**8계층 요약:** Rule·Skill·Command ✅ | Harness·Loop·Hook ⚠️ | RED 미착수 ❌

---

## Part H — Agent 프롬프트 재사용 (복사용)

### H1. Mom Test STEP 1

```
UnitConverter_10 STEP 1 — Mom Test 인터뷰를 진행해.
(규칙: 질문 1개, 과거 사실, 솔루션 → 그건 나중)
```

### H2. TDD RED

```
/tdd-red
TestID: D-002
```

### H3. ECB Review

```
/review-ecb
범위: src/, tests/
```

---

*End of Transcript Export*

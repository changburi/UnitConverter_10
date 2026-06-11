---
name: unit-converter-docs
description: >-
  UnitConverter_10 ARRR·세션 Report·Transcript·Checklist 작성. /export 및 Phase
  완료 시 templates/ 3종. SSOT export.md · docs/PRD.md · .cursorrules.
---

# Unit Converter Docs — ARRR·세션 Export Skill

`/export` 및 Phase 완료 시 **문서만** 작성한다. 코드·pytest·git commit **금지**.

---

## Export Command (SSOT)

`.cursor/commands/export.md` — **`/export`** (`/export-session` 별칭)

| 산출 | 경로 |
|------|------|
| Report | `Report/NN.REPORT.md` |
| Transcript | `Prompting/NN.Export-Transcript.md` |

**번호:** `Report/`·`Prompting/` 최대 `NN` + 1 (2자리). **덮어쓰기 금지.**

---

## 템플릿 (3종)

| 템플릿 | 용도 | 출력 예 |
|--------|------|---------|
| [report-template.md](templates/report-template.md) | `/export` Report | `Report/NN.REPORT.md` |
| [transcript-template.md](templates/transcript-template.md) | `/export` Transcript | `Prompting/NN.Export-Transcript.md` |
| [checklist-template.md](templates/checklist-template.md) | ARRR 누적 | `Prompt/ARRR_Checklist.md` |

---

## 슬래시 단독 입력

`/export` **만** → 현재 채팅에서 주제·Transcript 추출 · **질문 금지**.

---

## 작성 원칙

1. **한국어** · Mom Test: 솔루션名·미래 가정을 문제 정의에 섞지 않음
2. **PRD** — `docs/PRD.md` · 없는 FR은 `⚠️ PRD 미등재 · RED 설계 합의`
3. **pytest** — 실행한 경우만 기록
4. **Git** — 상태 기록만 · commit/push **하지 않음**
5. **int[6] 1-index** — E001~ · golden·오류 문자열 포맷 고정

---

## Report 형식 (`export.md`)

- 제목: `# UnitConverter_10 — {세션 주제}`
- 메타 표: 프로젝트 · 단계 · 작성일 · 목적
- 섹션: 1. 요약 / 2. 핵심 결정·산출물 / 3. 다음 단계
- Transcript 링크: `Prompting/NN.Export-Transcript.md`

---

## Transcript 형식

- `_Exported on {날짜} from Cursor_`
- **User** / **Cursor** 턴 전문
- 생성·변경 파일 표
- Report 링크: `Report/NN.REPORT.md`

---

## Checklist

- `[x]` / `[ ]` — 항목 **삭제 금지**
- ARRR Command · D-LOC · PRD FR-01~06 · Cursor Harness

---

## 완료 보고

| 항목 | 내용 |
|------|------|
| **번호 NN** | 2자리 |
| **생성 파일** | Report · Transcript · (Checklist) |
| **다음** | ARRR 체인 다음 Command |

---

## 금지

- `src/` · `tests/` 수정 · **추가 질문** · git commit

---

## 참고

- TDD: [unit-converter-tdd](../unit-converter-tdd/SKILL.md)
- PRD: `docs/PRD.md`
- Export: `.cursor/commands/export.md`

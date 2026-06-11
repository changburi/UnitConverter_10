# Refactor Smell — ARRR Refine ⑦ 스멜 탐지

UnitConverter_10 **코드 스멜 탐지만** — **`src/`·`tests/` 수정 · commit 금지**.  
헌법: `.cursorrules` · ARRR: `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 슬래시 단독 입력 (고정 컨텍스트)

```
Phase: REFACTOR | Scope: src/ tests/ | Track: Logic+UI | TestID: D-LOC-01
검사: src/entity/loc.py, constants.py, tests/entity/test_d_loc_01.py
전제: python -m pytest tests/ -v 전부 PASS
```

---

## 필수 선언

```
Phase: REFACTOR | Scope: src/ tests/ | Track: Logic+UI | TestID: D-LOC-01
```

---

## 전제 (중단)

```bash
python -m pytest tests/ -v
```

FAIL 1건이라도 → **중단** · GREEN 복구 후 재실행.

---

## 스멜 유형 · 우선순위

| P | 유형 |
|---|------|
| **P0** | ECB 위반 · Magic Number (SSOT 밖) |
| **P1** | Long Method · Duplicated Code · Feature Envy |
| **P2** | Mysterious Name · 경미한 중복 |

---

## Change Budget (`/refactor-safe` 1회)

| 항목 | 한도 |
|------|------|
| 파일 | ≤ 3 |
| 클래스 | ≤ 1 |
| 메서드 | ≤ 3 |

---

## 스멜 표 (필수)

| # | P | 유형 | Track | 파일:줄 | 내용 | Budget | 권고 |
|---|-----|------|-------|---------|------|--------|------|

**0건:** `Refactor smell 없음` + ECB OK.

---

## `/refactor-safe` 후보 1~3개

P0 우선 · Budget ✅ · 패치 **출력 금지**.

---

## 다음 안내

> **P0 1개만** 골라 `/refactor-safe` 실행. P0 없으면 P1 1건 또는 no-op.

---

## 금지

- 코드 수정 · commit · **추가 질문**

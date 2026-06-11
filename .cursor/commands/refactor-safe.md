# Refactor Safe — GREEN 유지 리팩터

UnitConverter_10 **REFACTOR** — pytest **전부 PASS 유지** · 최소 diff.  
헌법: `.cursorrules` · ARRR: `.cursor/skills/unit-converter-tdd/SKILL.md` · 선행: `/refactor-smell`

---

## 슬래시 단독 입력 (고정 컨텍스트)

```
Phase: REFACTOR | Layer: entity | Track: Logic | TestID: D-LOC-01
전제: tests/ -v PASS · smell 표 P0/P1 1건
범위: src/entity/loc.py, constants.py (tests 의미 변경 금지)
Budget: 파일≤3 · 클래스≤1 · 메서드≤3
```

---

## 필수 선언

```
Phase: REFACTOR | Layer: entity | Track: Logic | TestID: D-LOC-01
```

---

## 절차

1. `python -m pytest tests/ -v` **PASS**
2. smell **권고 1건**만 적용 (0건 → no-op)
3. Track → 전체 pytest Loop
4. ECB 재확인
5. 보고 · `/export` 안내

---

## 허용 / 금지

| ✅ | ❌ |
|----|-----|
| private helper · 이름 · SSOT 통합 | assert 완화 · E001~E005 entity · D-LOC-02/03 |

---

## pytest

```bash
python -m pytest tests/entity/test_d_loc_01.py -v
python -m pytest tests/ -v
```

---

## 보고

| **TestID** | D-LOC-01 |
| **리팩터** | 1~2문장 (no-op 가능) |
| **변경 파일** | 목록 또는 "없음" |
| **다음** | `/export` · D-LOC-02 `/red-skeleton` |

---

## 금지

- GREEN 깨짐 상태 계속 · Golden snapshot 무승인 덮어쓰기 · **추가 질문** · git commit

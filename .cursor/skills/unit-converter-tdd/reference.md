# D-* 테스트 ID (Logic Track)

| ID | Layer | 검증 내용 |
|----|-------|-----------|
| D-001 | entity | meter → feet·yard (README SSOT, meter:2.5) |
| D-002 | entity | feet → meter (**나눗셈** 방향, feet:8.2) |
| D-003 | entity | yard → meter (yard PDF 공백 대체, yard:2.7) |
| D-004 | entity | meter 기준 정규화 후 전 단위 출력 |
| D-005 | entity | UnitRatio SSOT — constants 단일 출처 |
| D-006 | control | E001 형식 오류 분류 |
| D-007 | control | E002 숫자 오류 분류 |
| D-008 | control | E003 미지원 원본 단위 |
| D-009 | control | E004 음수 |
| D-010 | control | E005 빈 입력·빈 값 |
| D-011 | control | Solver — Validator 통과 값만 entity 호출 |

파일: `tests/entity/test_d_*.py`, `tests/control/test_d_*.py`

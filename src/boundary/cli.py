from src.control.validation import ValidationError, validate


def process_input_line(line: str) -> str:
    """한 줄 입력을 검증하고 오류 메시지 또는 변환 결과 문자열을 반환한다."""
    result = validate(line)
    if isinstance(result, ValidationError):
        return result.message

    from src.control.solver import solve

    return solve(result)

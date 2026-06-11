from src.boundary.cli import process_input_line


def test_u_in_01_invalid_format_e001():
    # Given: 콜론 없는 입력 meter2.5
    # When: boundary process_input_line 호출
    result = process_input_line("meter2.5")
    # Then: E001 메시지 (FR-04)
    assert result == "Invalid format. Use unit:value (ex: meter:2.5)"


def test_u_in_02_unknown_unit_e003():
    # Given: 미지원 단위 cubit:1
    # When: boundary process_input_line 호출
    result = process_input_line("cubit:1")
    # Then: E003 메시지 (FR-04)
    assert result == "Unknown unit: cubit"

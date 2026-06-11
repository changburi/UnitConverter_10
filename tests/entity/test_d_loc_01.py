from src.entity.constants import (
    METER_TO_FEET,
    METER_TO_YARD,
    UNIT_FEET,
    UNIT_METER,
    UNIT_YARD,
)
from src.entity.conversion import unit_convert


def test_d_loc_01_unit_convert_meter():
    # Given: meter 2.5 (PRD TC-01 / README SSOT)
    value = 2.5
    unit = UNIT_METER
    # When: unit_convert(value, unit) 호출
    result = unit_convert(value, unit)
    # Then: meter·feet·yard 전 단위 변환
    assert result[UNIT_METER] == 2.5
    assert result[UNIT_FEET] == 2.5 * METER_TO_FEET
    assert result[UNIT_YARD] == 2.5 * METER_TO_YARD


def test_d_loc_02_unit_convert_feet():
    # Given: feet 8.2 (PRD TC-02 · 나눗셈 방향)
    value = 8.2
    unit = UNIT_FEET
    # When: unit_convert(value, unit) 호출
    result = unit_convert(value, unit)
    # Then: meter 역변환 · feet 유지
    expected_meters = 8.2 / METER_TO_FEET
    assert result[UNIT_METER] == expected_meters
    assert result[UNIT_FEET] == 8.2


def test_d_loc_03_unit_convert_yard():
    # Given: yard 2.7 (PRD TC-03)
    value = 2.7
    unit = UNIT_YARD
    # When: unit_convert(value, unit) 호출
    result = unit_convert(value, unit)
    # Then: meter 역변환 · yard 유지
    expected_meters = 2.7 / METER_TO_YARD
    assert result[UNIT_METER] == expected_meters
    assert result[UNIT_YARD] == 2.7

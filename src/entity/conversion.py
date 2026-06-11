from src.entity.constants import (
    METER_TO_FEET,
    METER_TO_YARD,
    UNIT_FEET,
    UNIT_METER,
    UNIT_YARD,
)


def unit_convert(value: float, unit: str) -> dict[str, float]:
    """유효한 길이 단위·값을 meter 기준으로 정규화한 뒤 전 단위로 변환한다."""
    meters = _to_meters(value, unit)
    return {
        UNIT_METER: meters,
        UNIT_FEET: meters * METER_TO_FEET,
        UNIT_YARD: meters * METER_TO_YARD,
    }


def _to_meters(value: float, unit: str) -> float:
    if unit == UNIT_METER:
        return value
    if unit == UNIT_FEET:
        return value / METER_TO_FEET
    if unit == UNIT_YARD:
        return value / METER_TO_YARD
    raise ValueError(unit)

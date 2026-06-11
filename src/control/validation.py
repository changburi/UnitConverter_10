from dataclasses import dataclass

from src.entity.constants import SUPPORTED_UNITS


@dataclass(frozen=True)
class ValidInput:
    unit: str
    value: float


@dataclass(frozen=True)
class ValidationError:
    code: str
    message: str


def validate_number(value_str: str) -> float | ValidationError:
    if not value_str.strip():
        return ValidationError("E005", "Empty value")
    try:
        return float(value_str)
    except ValueError:
        return ValidationError("E002", f"Invalid number: {value_str}")


def validate(input_str: str) -> ValidInput | ValidationError:
    if ":" not in input_str:
        return ValidationError(
            "E001",
            "Invalid format. Use unit:value (ex: meter:2.5)",
        )

    unit, value_str = input_str.split(":", 1)

    try:
        value = float(value_str)
    except ValueError:
        return ValidationError("E002", f"Invalid number: {value_str}")

    if unit not in SUPPORTED_UNITS:
        return ValidationError("E003", f"Unknown unit: {unit}")

    return ValidInput(unit=unit, value=value)

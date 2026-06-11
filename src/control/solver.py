from src.control.validation import ValidInput
from src.entity.constants import UNIT_FEET, UNIT_METER, UNIT_YARD
from src.entity.conversion import unit_convert


def solve(valid: ValidInput) -> str:
    converted = unit_convert(valid.value, valid.unit)
    lines = [
        f"{valid.value} {valid.unit} = {converted[UNIT_METER]} meter",
        f"{valid.value} {valid.unit} = {converted[UNIT_FEET]} feet",
        f"{valid.value} {valid.unit} = {converted[UNIT_YARD]} yard",
    ]
    return "\n".join(lines)

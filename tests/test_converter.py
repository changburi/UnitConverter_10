import subprocess
import sys
from pathlib import Path

import pytest

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONVERTER_SCRIPT = PROJECT_ROOT / "UnitConverter.py"


def run_converter(user_input: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CONVERTER_SCRIPT)],
        input=user_input,
        text=True,
        capture_output=True,
        cwd=PROJECT_ROOT,
    )


def parse_output(stdout: str) -> dict[str, float]:
    result: dict[str, float] = {}
    for line in stdout.strip().splitlines():
        if "=" not in line:
            continue
        left, right = line.split("=", 1)
        right_value_str, right_unit = right.strip().split(" ", 1)
        result[right_unit] = float(right_value_str)
    return result


class TestLengthConversion:
    def test_meter_to_all_units(self):
        result = run_converter("meter:2.5")
        assert result.returncode == 0, result.stderr

        out = parse_output(result.stdout)
        assert out["meter"] == pytest.approx(2.5)
        assert out["feet"] == pytest.approx(2.5 * METER_TO_FEET)
        assert out["yard"] == pytest.approx(2.5 * METER_TO_YARD)

    def test_feet_to_meter_bidirectional(self):
        result = run_converter("feet:8.2")
        assert result.returncode == 0, result.stderr

        out = parse_output(result.stdout)
        expected_meters = 8.2 / METER_TO_FEET
        assert out["meter"] == pytest.approx(expected_meters)
        assert out["feet"] == pytest.approx(8.2)

    def test_yard_conversion(self):
        result = run_converter("yard:2.7")
        assert result.returncode == 0, result.stderr

        out = parse_output(result.stdout)
        expected_meters = 2.7 / METER_TO_YARD
        assert out["meter"] == pytest.approx(expected_meters)
        assert out["yard"] == pytest.approx(2.7)


class TestInputValidation:
    def test_invalid_format_no_colon(self):
        result = run_converter("meter2.5")
        assert "Invalid format" in result.stdout

    def test_invalid_number(self):
        result = run_converter("meter:abc")
        assert "Invalid number" in result.stdout

    def test_unknown_unit(self):
        result = run_converter("cubit:1")
        assert "Unknown unit" in result.stdout

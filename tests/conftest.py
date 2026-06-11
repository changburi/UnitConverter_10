import pytest

from src.entity.constants import GRID_COLS, GRID_ROWS, GRID_SUBGRID


@pytest.fixture
def grid_g1():
    """G1 격자 — 0이 2개, row-major. 1-index 빈 칸: (2,2), (3,3)."""
    _ = (GRID_ROWS, GRID_COLS, GRID_SUBGRID)
    return [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]

from src.entity.constants import GRID_BLANK, GRID_INDEX_BASE


def find_blank_coords(grid):
    coords = []
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == GRID_BLANK:
                coords.append((row_idx + GRID_INDEX_BASE, col_idx + GRID_INDEX_BASE))
    return coords

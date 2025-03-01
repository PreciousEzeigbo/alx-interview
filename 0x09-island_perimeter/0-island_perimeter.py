#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list): 2D list of integers containing 0 (water) or 1 (land).

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i <= 0 or grid[i - 1][j] == 0:  # Check top
                    perimeter += 1
                if i >= len(grid) - 1 or grid[i + 1][j] == 0:  # Check bottom
                    perimeter += 1
                if j <= 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j >= len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1
    return perimeter

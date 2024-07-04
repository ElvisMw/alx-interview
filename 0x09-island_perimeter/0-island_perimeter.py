#!/usr/bin/python3
""" Module that contains the island_perimeter function. """


def island_perimeter(grid):
    """Calculate the perimeter of all land cells in a grid.

    Args:
        grid (list[list[int]]): A 2D grid where 1 represents a land cell and 0
                                represents a water cell.

    Returns:
        int: The total perimeter of all land cells.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

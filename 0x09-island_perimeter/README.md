#!/usr/bin/python3
"""
0-main
"""
import sys


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    grid is a list of lists of integers:
        0 represents water
        1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally)
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing)
    The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

    """
    perimeter = 0
    if not grid or not grid[0]:
        return perimeter
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == height - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == width - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter


def main():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

if __name__ == "__main__": <br>
  sys.exit(main() if __name__ == "__main__" else None)


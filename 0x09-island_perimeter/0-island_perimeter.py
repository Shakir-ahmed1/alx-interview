#!/usr/bin/python3
""" calcluates the perimeter of an island in grid"""


def island_perimeter(grid):
    """ calculate island perimeter """
    prm = 0
    length = len(grid)
    if length == 0:
        return 0
    width = len(grid[0])
    for row in range(length):
        for col in range(width):
            if grid[row][col] == 1:
                prm += 0 if row - 1 >= 0 and grid[row-1][col] == 1 else 1
                prm += 0 if col - 1 >= 0 and grid[row][col-1] == 1 else 1
                prm += 0 if row + 1 < length and grid[row+1][col] == 1 else 1
                prm += 0 if col + 1 < width and grid[row][col+1] == 1 else 1
    return prm

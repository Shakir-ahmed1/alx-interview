#!/usr/bin/python3
""" calcluates the perimeter of an island in grid"""


def island_perimeter(grid):
    """ calculate island perimeter """
    perimeter = 0
    length = len(grid)
    if length == 0:
        return 0
    width = len(grid[0])
    for row in range(length):
        for col in range(width):
            if grid[row][col] == 1:
                perimeter += 0 if grid[row-1][col] == 1 else 1
                perimeter += 0 if grid[row][col-1] == 1 else 1
                perimeter += 0 if grid[row+1][col] == 1 else 1
                perimeter += 0 if grid[row][col+1] == 1 else 1
    return perimeter

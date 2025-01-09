#!/usr/bin/python3
"""Calculate the perimeter of the island described in grid"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    :param grid: List of list of integers (0 for water, 1 for land)
    :return: The perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for the current land cell
                perimeter += 4

                # Check for adjacent land cells to reduce the perimeter
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check cell below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter

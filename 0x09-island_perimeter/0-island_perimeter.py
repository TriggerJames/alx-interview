#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    :param grid: List of list of integers where 0
    represents water and 1 represents land.
    :return: The perimeter of the island.
    """
    # Initialize perimeter
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found a land cell
                # Check the top (if i == 0, it's on the edge of the grid)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the bottom
                # (if i == rows - 1, it's on the edge of the grid)
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the left
                # (if j == 0, it's on the edge of the grid)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the right
                # (if j == cols - 1, it's on the edge of the grid)
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

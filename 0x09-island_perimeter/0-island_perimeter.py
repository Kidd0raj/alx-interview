#!/usr/bin/python3
"""
This module provides a function to calculate the perimeter of an island represented by a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island, where 1s represent land and 0s represent water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all sides are land
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract shared edge
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract shared edge
    
    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(island_perimeter(grid))

#!/usr/bin/python3
def island_perimeter(grid):
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

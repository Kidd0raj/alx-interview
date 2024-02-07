#!/usr/bin/python3
'''N-Queens Challenge'''

import sys


def is_safe(placed_queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in placed_queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_n_queens(n):
    """Find solutions for the N-Queens problem."""
    if n < 4:
        print('N must be at least 4')
        return []

    solutions = []
    placed_queens = []  # coordinates format [row, column]

    def backtrack(row):
        """Backtrack to find solutions."""
        if row == n:
            solutions.append(placed_queens[:])
            return
        for col in range(n):
            if is_safe(placed_queens, row, col):
                placed_queens.append((row, col))
                backtrack(row + 1)
                placed_queens.pop()

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    solutions = solve_n_queens(n)
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)


#!/usr/bin/python3
import sys


def solve(n, row, queens):
    if row == n:
        print(queens)
        return

    for col in range(n):
        valid = True

        for queen in queens:
            if queen[1] == col or abs(queen[0] - row) == abs(queen[1] - col):
                valid = False
                break

        if valid:
            solve(n, row + 1, queens + [[row, col]])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve(n, 0, [])

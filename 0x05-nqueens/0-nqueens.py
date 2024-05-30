#!/usr/bin/python3
"""Solve the N Queens problem using backtracking"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if col == board[i] or \
           col - row == board[i] - i or \
           col + row == board[i] + i:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions"""
    def place_queens(row):
        """Backtracking function to solve the NQueens problem"""
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    place_queens(0)
    return solutions


def format_and_print_solutions(solutions):
    """Format and print all solutions in the required format"""
    for solution in solutions:
        result = []
        for row, col in enumerate(solution):
            result.append([row, col])
        print(result)


def main():
    """
    Main function to check command line arguments
    and solve the N Queens problem"""
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

    solutions = solve_nqueens(n)
    format_and_print_solutions(solutions)


if __name__ == "__main__":
    main()

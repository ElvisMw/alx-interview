#!/usr/bin/python3
"""Solve the N Queens problem using backtracking"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == col:
            return False
    # Check if there is a queen in the same diagonal
    for i in range(row):
        if board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions"""
    def backtrack(row):
        """Backtracking function to find all solutions"""
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions


def print_solutions(solutions):
    """Print all solutions in the required format"""
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


def main():
    """Main function to handle command line arguments"""
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
    print_solutions(solutions)

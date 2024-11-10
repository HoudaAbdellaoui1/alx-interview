#!/usr/bin/python3
import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def place_queen(row):
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                place_queen(row + 1)

    board = [-1] * N
    solutions = []
    place_queen(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

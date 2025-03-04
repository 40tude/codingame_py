# https://www.codingame.com/ide/puzzle/sudoku-solver

# A sudoku is a Latin Square which has the numbers 1-9 in each row, column, and 3x3 square.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# import time
# import sys


# def isSafe(mat, i, j, num, row, col, box):
#     if (row[i] & (1 << num)) or (col[j] & (1 << num)) or (box[i // 3 * 3 + j // 3] & (1 << num)):
#         return False
#     return True


# def sudokuSolverRec(mat, i, j, row, col, box):
#     n = len(mat)

#     # base case: Reached nth column of last row
#     if i == n - 1 and j == n:
#         return True

#     # If reached last column of the row go to next row
#     if j == n:
#         i += 1
#         j = 0

#     # If cell is already occupied then move forward
#     if mat[i][j] != 0:
#         return sudokuSolverRec(mat, i, j + 1, row, col, box)

#     for num in range(1, n + 1):
#         # If it is safe to place num at current position
#         if isSafe(mat, i, j, num, row, col, box):
#             mat[i][j] = num

#             # Update masks for the corresponding row, column and box
#             row[i] |= 1 << num
#             col[j] |= 1 << num
#             box[i // 3 * 3 + j // 3] |= 1 << num

#             if sudokuSolverRec(mat, i, j + 1, row, col, box):
#                 return True

#             # Unmask the number num in the corresponding row, column and box masks
#             mat[i][j] = 0
#             row[i] &= ~(1 << num)
#             col[j] &= ~(1 << num)
#             box[i // 3 * 3 + j // 3] &= ~(1 << num)

#     return False


# def solveSudoku(mat):
#     n = len(mat)
#     row = [0] * n
#     col = [0] * n
#     box = [0] * n

#     # Set the bits in bitmasks for values that are initially present
#     for i in range(n):
#         for j in range(n):
#             if mat[i][j] != 0:
#                 row[i] |= 1 << mat[i][j]
#                 col[j] |= 1 << mat[i][j]
#                 box[(i // 3) * 3 + j // 3] |= 1 << mat[i][j]

#     sudokuSolverRec(mat, 0, 0, row, col, box)


# board = [list(map(int, input())) for _ in range(9)]

# start_time = time.perf_counter()
# solveSudoku(board)
# end_time = time.perf_counter()

# # 98049.20 µs with World's Hardest Sudoku Solution
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs\n", file=sys.stderr, flush=True)
# print("\n".join("".join(map(str, row)) for row in board))


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# import time
# import sys


# # -------------------------------------
# def is_valid_move(board: list[list[int]], row: int, col: int, value: int) -> bool:
#     # check if value is in the row
#     if value in board[row]:
#         return False

#     # check if value is in the column
#     if value in [board[i][col] for i in range(9)]:
#         return False

#     # check if value is in the current square
#     square_row = row // 3
#     square_col = col // 3
#     for i in range(3):
#         for j in range(3):
#             if board[square_row * 3 + i][square_col * 3 + j] == value:
#                 return False

#     return True


# # -------------------------------------
# def backtrack(board: list[list[int]], row: int, col: int) -> bool:

#     # Termination condition
#     if row == 8 and col == 9:
#         return True

#     # Explore each possible decision that can be made at current state
#     # last col => move to next row
#     if col == 9:
#         row += 1
#         col = 0

#     # if a value is already set, move to the next column
#     if board[row][col] != 0:
#         return backtrack(board, row, col + 1)

#     # try all possible values
#     for value in range(1, 10):
#         if is_valid_move(board, row, col, value):
#             board[row][col] = value
#             if backtrack(board, row, col + 1):
#                 return True
#             board[row][col] = 0

#     return False


# # -------------------------------------
# def solve(board: list[list[int]]) -> None:
#     backtrack(board, 0, 0)


# # -------------------------------------
# board = [list(map(int, input())) for _ in range(9)]

# start_time = time.perf_counter()
# solve(board)
# end_time = time.perf_counter()

# # 170_009.70 µs with World's Hardest Sudoku Solution
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs\n", file=sys.stderr, flush=True)
# print("\n".join("".join(map(str, row)) for row in board))


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
import time
import sys


class Sudoku_Board:
    def __init__(self, board: list[list[int]]):
        self.board = board

    def __str__(self):
        return "\n".join("".join(map(str, row)) for row in self.board)

    def solve(self):
        self._backtrack(0, 0)

    def _is_valid_move(self, row: int, col: int, value: int) -> bool:
        # check if value is in the row
        if value in self.board[row]:
            return False

        # check if value is in the column
        if value in [self.board[i][col] for i in range(9)]:
            return False

        # check if value is in the current square
        square_row = row // 3
        square_col = col // 3
        for i in range(3):
            for j in range(3):
                if self.board[square_row * 3 + i][square_col * 3 + j] == value:
                    return False

        return True

    def _backtrack(self, row: int, col: int) -> bool:
        # Termination condition
        if row == 8 and col == 9:
            return True

        # Explore each possible decision that can be made at current state
        # last col => move to next row
        if col == 9:
            row += 1
            col = 0

        # if a value is already set, move to the next column
        if self.board[row][col] != 0:
            return self._backtrack(row, col + 1)

        # try all possible values
        for value in range(1, 10):
            if self._is_valid_move(row, col, value):
                self.board[row][col] = value
                if self._backtrack(row, col + 1):
                    return True
                self.board[row][col] = 0

        return False


my_board = Sudoku_Board([list(map(int, input())) for _ in range(9)])

start_time = time.perf_counter()
my_board.solve()
end_time = time.perf_counter()
# 186_611.70 µs with World's Hardest Sudoku Solution
print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs\n", file=sys.stderr, flush=True)
print(my_board)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

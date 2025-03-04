# https://www.codingame.com/ide/puzzle/sum-of-spirals-diagonals

# Given a matrix of shape N×N arranged in a "spiral", with its numbers spiralling from 1 to N² inward
# What is the sum of its diagonals?
# En fait non c'est plutôt : la somme des digits en évitant de compter 2 fois le centre si la matrice est de taille impaire
# En toute logique, on a 2 diag on devrait compter 2 fois le centre... Bref, passons...

#  1    2     3     4
# 12   13    14     5
# 11   16    15     6
# 10    9     8     7

# The sum of the diagonals is:
# 1 + 4 + 7 + 10 + 13 + 14 + 15 + 16 = 80

# Doit bien y a voir une solution analytique
# Construire la matrice
# Faire la somme des m[i][i] et m[i][n-i-1] pour i allant de 0 à n-1 ?


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# ->  v  <-  ^  ->  v  <-  ^  ->  v  <- ...
# 4   3   3  2   2  1   1  0
# 5   4   4  3   3  2   2  1  1


# -----------------------------------------------------------------------------
# Not mine
# import sys
# import math
# import numpy as np

# def spiralSum(firstVal, size) :
#     if size == 0 :
#         return 0
#     elif size == 1 :
#         return firstVal
#     else :
#         size -= 1
#         return 4 * firstVal + 6 * size + spiralSum(firstVal + 4 * size, size - 1)

# n = int(input())

# print(spiralSum(1, n))


# -----------------------------------------------------------------------------
# Not mine
# def compute(n, offset):
#     if n == 1:
#         return offset
#     if n == 2:
#         return 4*offset + 6
#     return 6*n - 6 + 4*offset + compute(n-2, offset + 4*n-4)
# print(compute(int(input()), 1))


# -----------------------------------------------------------------------------
# import time
# import sys

# n = int(input())

# start_time = time.perf_counter()

# board = [[0] * n for _ in range(n)]

# x = y = 0
# dx = dy = 1

# nb_moves = n
# current_val = 1

# while current_val <= n * n:
#     for dir in range(2):  # x=0 y=1
#         for _ in range(nb_moves):
#             board[y][x] = current_val
#             current_val += 1
#             if not dir:
#                 x = x + dx
#             else:
#                 y = y + dy

#         if not dir:
#             dx = -dx
#             nb_moves -= 1
#         else:
#             dy = -dy

#         x += dx
#         y += dy

# end_time = time.perf_counter()
# # Milky Way Execution time: 373_874.60 µs
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs", file=sys.stderr, flush=True)

# total = 0
# for i in range(n):
#     total += board[i][i] + board[i][n - i - 1]
# print(total if n % 2 == 0 else total - n**2)


# -----------------------------------------------------------------------------
import time
import sys

n = int(input())

start_time = time.perf_counter()

board = [[0] * n for _ in range(n)]

x = y = 0
dx = dy = 1

nb_moves = n
current_val = 1

while current_val <= n * n:

    # x moving
    for _ in range(nb_moves):
        board[y][x] = current_val
        current_val += 1
        x = x + dx
    dx = -dx
    x += dx
    y += dy

    nb_moves -= 1

    # y moving
    for _ in range(nb_moves):
        board[y][x] = current_val
        current_val += 1
        y = y + dy
    dy = -dy
    y += dy
    x += dx

end_time = time.perf_counter()
# Milky Way Execution time: 301_722.10 µs
print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs", file=sys.stderr, flush=True)

total = sum(board[i][i] + board[i][n - i - 1] for i in range(n))
if n % 2 == 1:
    total -= board[n // 2][n // 2]  # Remove center value counted twice
print(total)


# # -----------------------------------------------------------------------------
# import time
# import sys

# n = int(input())

# start_time = time.perf_counter()

# board = [[0] * n for _ in range(n)]

# x = y = 0
# dx = dy = 1

# nb_moves = n
# current_val = 1

# while current_val <= n * n:

#     # x moving
#     for _ in range(nb_moves):
#         board[y][x] = current_val
#         current_val += 1
#         x = x + dx
#     dx = -dx
#     x += dx
#     y += dy

#     nb_moves -= 1

#     # y moving
#     for _ in range(nb_moves):
#         board[y][x] = current_val
#         current_val += 1
#         y = y + dy
#     dy = -dy
#     y += dy
#     x += dx

# end_time = time.perf_counter()
# # Milky Way Execution time: 301_722.10 µs
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs", file=sys.stderr, flush=True)

# total = sum(board[i][i] + board[i][n - i - 1] for i in range(n))
# if n % 2 == 1:
#     total -= board[n // 2][n // 2]  # Remove center value counted twice
# print(total)


# # -----------------------------------------------------------------------------

# import time
# import sys

# n = int(input())

# start_time = time.perf_counter()

# board = [[0] * n for _ in range(n)]

# x = y = 0
# dx, dy = 1, 1  # Movement directions

# nb_moves = n
# current_val = 1

# while current_val <= n * n:

#     # x moving (horizontal)
#     for _ in range(nb_moves):
#         board[y][x] = current_val
#         current_val += 1
#         if _ < nb_moves - 1:  # Do not move after last placement
#             x += dx

#     dx = -dx  # Change direction
#     y += dy  # Move downward

#     nb_moves -= 1

#     if current_val > n * n:
#         break  # Stop early if we have filled the board

#     # y moving (vertical)
#     for _ in range(nb_moves):
#         board[y][x] = current_val
#         current_val += 1
#         if _ < nb_moves - 1:  # Do not move after last placement
#             y += dy

#     dy = -dy  # Change direction
#     x += dx  # Move sideways

# end_time = time.perf_counter()

# # Milky Way Execution time: 402_348.10 µs
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs", file=sys.stderr, flush=True)

# # Compute sum of both diagonals
# total = sum(board[i][i] + board[i][n - i - 1] for i in range(n))
# if n % 2 == 1:
#     total -= board[n // 2][n // 2]  # Remove center value counted twice

# print(total)


# # -----------------------------------------------------------------------------

# import time
# import sys

# n = int(input())

# start_time = time.perf_counter()

# # Create an empty NxN board
# board = [[0] * n for _ in range(n)]

# # Directions in order: Right, Down, Left, Up
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dx, dy)
# dir_index = 0  # Start moving right

# x, y = 0, 0  # Start at top-left corner
# current_val = 1

# while current_val <= n * n:
#     board[x][y] = current_val  # Fill the current cell
#     current_val += 1

#     # Compute the next position
#     nx, ny = x + directions[dir_index][0], y + directions[dir_index][1]

#     # If out of bounds or cell already filled, change direction
#     if not (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0):
#         dir_index = (dir_index + 1) % 4  # Change direction
#         nx, ny = x + directions[dir_index][0], y + directions[dir_index][1]  # Recalculate next position

#     # Move to the next position
#     x, y = nx, ny

# end_time = time.perf_counter()

# # Milky Way Execution time: 836_304.00 µs
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :_.2f} µs", file=sys.stderr, flush=True)

# # Compute sum of both diagonals
# total = sum(board[i][i] + board[i][n - i - 1] for i in range(n))
# if n % 2 == 1:
#     total -= board[n // 2][n // 2]  # Remove center value counted twice

# print(total)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))

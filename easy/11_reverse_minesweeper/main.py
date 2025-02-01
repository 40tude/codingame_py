# https://www.codingame.com/ide/puzzle/reverse-minesweeper

# 111.111.11
# 1.211.1.2.
# 12.1222.2.
# .2232.1122
# 12.2.211.1
# .322221122
# 2.1.1.1.1.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_many_mines.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
# import numpy as np
# import time

# w = int(input())
# h = int(input())

# array = np.full((h + 2, w + 2), 0)

# start_time = time.perf_counter()

# for i in range(1, h + 1):
#     line = input()
#     for j, char in enumerate(line, 1):
#         if char == "x":
#             array[i, j] = -10
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     array[i + di, j + dj] += 1

# end_time = time.perf_counter()
# execution_time_microseconds = (end_time - start_time) * 1_000_000
# print(f"Execution time: {execution_time_microseconds:.2f} µs")

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         count = array[i, j]
#         print(end=str(count) if count > 0 else ".")
#     print()


# -----------------------------------------------------------------------------

# w = int(input())
# h = int(input())

# map_in = [list(input()) for _ in range(h)]
# map_out = [[0 for _ in range(w)] for _ in range(h)]


# for y in range(h):
#     min_y = max(y - 1, 0)
#     max_y = min(y + 1, h - 1)
#     for x in range(w):
#         if map_in[y][x] == "x":
#             map_out[y][x] = -1
#             min_x = max(x - 1, 0)
#             max_x = min(x + 1, w - 1)
#             for j in range(min_y, max_y + 1):
#                 for i in range(min_x, max_x + 1):
#                     if map_in[j][i] == -1:
#                         continue
#                     map_out[j][i] = map_out[j][i] + 1 if map_out[j][i] >= 0 else -1
#             continue

# # Replace 0 and -1 with "."
# for y in range(h):
#     msg = "".join("." if map_out[y][x] <= 0 else str(map_out[y][x]) for x in range(w))
#     print(msg)


# # -----------------------------------------------------------------------------
import time

w = int(input())
h = int(input())

map_in = [list(input()) for _ in range(h)]
map_out = [[0 for _ in range(w)] for _ in range(h)]

start_time = time.perf_counter()

for y in range(h):
    min_y = max(y - 1, 0)
    max_y = min(y + 1, h - 1)
    for x in range(w):
        if map_in[y][x] == "x":
            map_out[y][x] = -1
            min_x = max(x - 1, 0)
            max_x = min(x + 1, w - 1)
            for j in range(min_y, max_y + 1):
                for i in range(min_x, max_x + 1):
                    if map_in[j][i] == -1:
                        continue
                    map_out[j][i] = map_out[j][i] + 1 if map_out[j][i] >= 0 else -1
            continue

end_time = time.perf_counter()
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Execution time: {execution_time_microseconds:.2f} µs")

# Replace 0 and -1 with "."
for y in range(h):
    msg = "".join("." if map_out[y][x] <= 0 else str(map_out[y][x]) for x in range(w))
    print(msg)


# -----------------------------------------------------------------------------
# import time

# w = int(input())
# h = int(input())

# map_in = [list(input()) for _ in range(h)]
# map_out = [["."] * w for _ in range(h)]

# start_time = time.perf_counter()

# for y in range(h):
#     min_y = max(y - 1, 0)
#     max_y = min(y + 1, h - 1)
#     for x in range(w):
#         if map_in[y][x] == "x":
#             map_out[y][x] = "."
#             min_x = max(x - 1, 0)
#             max_x = min(x + 1, w - 1)
#             for j in range(min_y, max_y + 1):
#                 for i in range(min_x, max_x + 1):
#                     if map_in[j][i] == "x":
#                         continue
#                     val = int(map_out[j][i]) if map_out[j][i].isdigit() else 0
#                     map_out[j][i] = str(val + 1)
#             continue

# end_time = time.perf_counter()
# execution_time_microseconds = (end_time - start_time) * 1_000_000
# print(f"Execution time: {execution_time_microseconds:.2f} µs")

# for y in range(h):
#     print("".join(map_out[y]))


# -----------------------------------------------------------------------------
# import time

# w = int(input())
# h = int(input())

# map_in = [list(input()) for _ in range(h)]
# map_out = [["."] * w for _ in range(h)]

# start_time = time.perf_counter()

# for y in range(h):
#     min_y = max(y - 1, 0)
#     max_y = min(y + 1, h - 1)
#     for x in range(w):
#         if map_in[y][x] == "x":
#             map_out[y][x] = "."
#             continue
#         min_x = max(x - 1, 0)
#         max_x = min(x + 1, w - 1)
#         count = 0
#         for j in range(min_y, max_y + 1):
#             for i in range(min_x, max_x + 1):
#                 if map_in[j][i] == "x":
#                     count += 1
#         map_out[y][x] = str(count) if count > 0 else "."

# end_time = time.perf_counter()
# execution_time_microseconds = (end_time - start_time) * 1_000_000
# print(f"Execution time: {execution_time_microseconds:.2f} µs")

# for y in range(h):
#     print("".join(map_out[y]))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/custom-game-of-life

# First line: h & w, height and width of the grid, n the number of turns you have to simulate before output.
# Second line: 9 not space separated binary integers, the condition of surviving of a living cell (0: dies, 1: stays alive).
# Third line: 9 not space separated binary integers, the condition of birth of a dead cell (0: stays dead, 1: birth).
# Next h lines: w-length string for cells
# . : dead
# O : alive


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


# -----------------------------------------------------------------------------
def sum_around(m, y, x):
    sum = -m[y][x]

    for j in range(max(0, y - 1), min(len(m), y + 2)):
        for i in range(max(0, x - 1), min(len(m[0]), x + 2)):
            sum += m[j][i]
    return sum


# -------------------------------------
# c2i = lambda c: 1 if c == "O" else 0
# i2c = lambda i: "O" if i == 1 else "."

h, w, n = map(int, input().split())
life2death_cond = list(map(int, input()))
death2life_cond = list(map(int, input()))
map_in = [list(map((lambda c: 1 if c == "O" else 0), input())) for _ in range(h)]

map_out = [[0] * w for _ in range(h)]

for _ in range(n):
    for y, row in enumerate(map_in):
        for x, value in enumerate(row):
            neighbors = sum_around(map_in, y, x)
            map_out[y][x] = life2death_cond[neighbors] if value == 1 else death2life_cond[neighbors]
    map_in, map_out = map_out, map_in

for row in map_in:
    print("".join((lambda i: "O" if i == 1 else ".")(value) for value in row))


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
# def sum_around(m, y, x):
#     sum = -m[y][x]

#     for j in range(max(0, y - 1), min(len(m), y + 2)):
#         for i in range(max(0, x - 1), min(len(m[0]), x + 2)):
#             sum += m[j][i]
#     return sum


# # -------------------------------------
# c2i = lambda c: 1 if c == "O" else 0
# i2c = lambda i: "O" if i == 1 else "."

# h, w, n = map(int, input().split())
# life2death_cond = list(map(int, input()))
# death2life_cond = list(map(int, input()))
# map_in = [list(map(c2i, input())) for _ in range(h)]

# map_out = [[0] * w for _ in range(h)]

# for _ in range(n):
#     for y, row in enumerate(map_in):
#         for x, value in enumerate(row):
#             neighbors = sum_around(map_in, y, x)
#             map_out[y][x] = life2death_cond[neighbors] if value == 1 else death2life_cond[neighbors]
#     map_in, map_out = map_out, map_in

# for row in map_in:
#     print("".join(i2c(value) for value in row))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/gravity-tumbler

# rotating count times counterclockwise 90°

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
# Not mine

# import time
# import sys

# _width, height = map(int, input().split())
# count = int(input())
# grid = [input().rstrip() for _ in range(height)]

# start_time = time.perf_counter()
# for _ in range(count):
#     grid = ["".join(row) for row in zip(*grid)]
#     grid.sort(reverse=True)
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)

# for row in grid:
#     print(row)


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# import time
# import sys

# _width, height = map(int, input().split())
# count = int(input())
# grid = [input().rstrip() for _ in range(height)]

# start_time = time.perf_counter()
# for _ in range(2 + count % 2):
#     grid = ["".join(row) for row in zip(*grid)]
#     grid.sort(reverse=True)
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)

# for row in grid:
#     print(row)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# import time
# import sys

# width, height = [int(i) for i in input().split()]
# count = int(input())
# grid = [input() for i in range(height)]

# start_time = time.perf_counter()
# for rotate in range(2 + count % 2):
#     sortright = [sorted(g, reverse=True) for g in grid]
#     # * est utilisé pour "déréférencer" une liste ou un itérable, ce qui revient à passer chaque élément de la liste en argument séparé à une fonction.
#     # zip() combine plusieurs itérables élément par élément. Elle crée des tuples où chaque élément provient de la même position dans chaque itérable.
#     # list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) => [(1, 4, 7), (2, 5, 8), (3, 6, 9)] on a transposé la matrice
#     grid = zip(*sortright)
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)

# for row in grid:
#     print(*row, sep="")


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------


def rotate(m):
    m = [sorted(row, reverse=True) for row in m]
    return zip(*m)


w, h = map(int, input().split())
count = int(input())
map = [list(input()) for _ in range(h)]

for _ in range(2 + count % 2):
    map = rotate(map)

print("\n".join("".join(row) for row in map))


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys

# # start_time = time.perf_counter()
# # end_time = time.perf_counter()
# # print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


# # 80 µs with CodingGame 1
# def rotate(m, h, w):
#     m_out = [list(" " * h) for _ in range(w)]
#     for j in range(h):
#         m[j].sort(reverse=True)
#         for i in range(w):
#             m_out[i][j] = m[j][i]
#     return m_out


# # # 90 µs with CodingGame 1
# # def rotate2(m, h, w):
# #     m_out = [[" "] * h for _ in range(w)]
# #     for j, row in enumerate(m):
# #         for i, value in enumerate(sorted(row, reverse=True)):
# #             m_out[i][j] = value
# #     return m_out


# # -----------------------------------------------------------------------------
# w, h = map(int, input().split())
# count = int(input())
# map_in = [list(input()) for _ in range(h)]

# start_time = time.perf_counter()

# if count % 2:
#     map_out = rotate(map_in, h, w)
# else:
#     map_out = rotate(map_in, h, w)
#     map_out = rotate(map_out, w, h)

# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)

# print("\n".join("".join(row) for row in map_out))


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

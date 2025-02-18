# https://www.codingame.com/ide/puzzle/porcupine-fever

# Simulate to find the total amount of surviving porcupines after every year. Stop if all the porcupines are dead (do not repeat "0"s after the first time).
# Line 1: Integer N, the amount of cages.
# Line 2: Integer Y, the number of years.
# Next N lines: Three space-separated integers S, H and A, the amounts of sick, healthy and alive porcupines in the cage respectively.

# Output
# Y or fewer lines of integers of porcupines alive.
# Line 1 is year 1, not year 0. Any sick porcupines die first.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_04.txt"
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
# Sick Healthy Alive
k_Sick, k_Healthy, k_Alive = range(3)

cages = int(input())
years = int(input())
map_in = [list(map(int, input().split())) for _ in range(cages)]

for y in range(years):
    Total = 0
    for cage in range(cages):
        map_in[cage][k_Sick] = min(map_in[cage][k_Healthy], 2 * map_in[cage][k_Sick])
        map_in[cage][k_Healthy] = max(0, map_in[cage][k_Healthy] - map_in[cage][k_Sick])
        Total += map_in[cage][k_Sick] + map_in[cage][k_Healthy]
    print(Total)
    if Total == 0:
        break


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# # Sick Healthy Alive Dead
# k_Sick = 0
# k_Healthy = 1
# k_Alive = 2
# # k_Dead = 3

# cages = int(input())
# years = int(input())
# # map_in = [list(map(int, input().split())) + [0] for _ in range(cages)]
# map_in = [list(map(int, input().split())) for _ in range(cages)]

# # for y in range(years):
# #     Total = 0
# #     for cage in range(cages):
# #         map_in[cage][k_Dead] = map_in[cage][k_Sick]
# #         map_in[cage][k_Sick] = min(map_in[cage][k_Healthy], map_in[cage][k_Sick] * 2)
# #         map_in[cage][k_Healthy] = max(0, map_in[cage][k_Healthy] - map_in[cage][k_Sick])
# #         map_in[cage][k_Alive] = map_in[cage][k_Sick] + map_in[cage][k_Healthy]
# #         Total += map_in[cage][k_Alive]
# #     print(Total)
# #     if Total == 0:
# #         break


# for y in range(years):
#     Total = 0
#     for cage in range(cages):
#         # map_in[cage][k_Dead] = map_in[cage][k_Sick]
#         map_in[cage][k_Sick] = min(map_in[cage][k_Healthy], map_in[cage][k_Sick] * 2)
#         map_in[cage][k_Healthy] = max(0, map_in[cage][k_Healthy] - map_in[cage][k_Sick])
#         Total += map_in[cage][k_Sick] + map_in[cage][k_Healthy]
#     print(Total)
#     if Total == 0:
#         break
# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

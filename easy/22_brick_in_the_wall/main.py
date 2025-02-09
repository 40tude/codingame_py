# https://www.codingame.com/ide/puzzle/brick-in-the-wall

# The most bottom row ist the 1st one.
# W = ((L-1) * 6.5 / 100) * g * m
# L = L th row
# g = 10
# m mass of the brick
# (L-1) * 6.5 / 100 measures the distance the brick needs to be lift in meters.

# Calculate the minimal work Master Mason can build all the bricks into a (not necessarily rectangular) wall.

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
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -----------------------------------------------------------------------------
# Not mine
# x = int(input())
# n = int(input())
# m = sorted([int(i) for i in input().split()], reverse=True)
# print('{:.3f}'.format(sum(i*sum(m[i:i+x]) for i in range(0, n, x))*0.65/x))


# -----------------------------------------------------------------------------
bricks_per_row = int(input())
nb_brick = int(input())
# brick_weights = [int(i) for i in input().split()]
# brick_weights.sort(reverse=True)
brick_weights = sorted([int(i) for i in input().split()], reverse=True)

# def process(trio, L):
#     return ((L - 1) * 6.5 / 100) * 10 * sum(trio)

# process = lambda trio, L: ((L - 1) * 6.5 / 100) * 10 * sum(trio)
process = lambda trio, L: (L - 1) * 0.65 * sum(trio)


total_weight = 0
# [
#     total_weight := total_weight + process(brick_weights[i : i + bricks_per_row], 1 + i / bricks_per_row)
#     for i in range(0, len(brick_weights), bricks_per_row)
# ]


[
    total_weight := total_weight + process(brick_weights[i : i + bricks_per_row], 1 + i / bricks_per_row)
    for i in range(0, len(brick_weights), bricks_per_row)
]


print(f"{total_weight:.3f}")


# # -----------------------------------------------------------------------------
# bricks_per_row = int(input())
# nb_brick = int(input())
# brick_weights = [int(i) for i in input().split()]
# brick_weights.sort(reverse=True)

# current_brick = 0
# total_weight = 0.0
# L = 1
# while current_brick < nb_brick:
#     bricks_in_row = 0
#     while bricks_in_row < bricks_per_row and current_brick < nb_brick:
#         total_weight += ((L - 1) * 6.5 / 100) * 10 * brick_weights[current_brick]
#         bricks_in_row += 1
#         current_brick += 1
#     L += 1

# print(f"{total_weight:.3f}")

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

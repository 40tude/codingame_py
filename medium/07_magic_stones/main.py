# https://www.codingame.com/training/medium/magic-stones


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
# Not mine
input()
levels = sum(2 ** int(x) for x in input().split())
print("{:b}".format(levels).count("1"))

# -----------------------------------------------------------------------------
# input()  # number of stones is not needed
# stones = list(map(int, input().split()))

# b_mod = True
# while b_mod:
#     stones.sort()
#     b_mod = False
#     i = 0
#     while i < len(stones) - 1:
#         if stones[i] == stones[i + 1]:
#             stones[i] += 1
#             stones.pop(i + 1)
#             b_mod = True
#         else:
#             i += 1

# print(len(set(stones)))


# # -----------------------------------------------------------------------------
# input() # number of stones is not needed
# stones = sorted(list(map(int, input().split())))

# while True:
#     b_mod = False
#     # go thru the stones
#     # if 2 adjacent stones have the same value, increase by 1 the first one, pop out the other
#     i = 0
#     while i < len(stones) - 1:
#         if stones[i] == stones[i + 1]:
#             stones[i] += 1
#             stones.pop(i + 1)
#             b_mod = True
#         else:
#             i += 1
#     if not b_mod:
#         break
#     else:
#         stones.sort()


# print(len(set(stones)))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/robot-show

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
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))


# -----------------------------------------------------------------------------
# l = int(input())
# input()
# print(max(max(int(x),  l - int(x)) for x in input().split()))

# -----------------------------------------------------------------------------

length = int(input())
input()
bots = list(map(int, input().split()))
bots.sort()
half_len = length / 2
while len(bots) != 1:
    bots.pop(0) if abs(bots[0] - half_len) < abs(bots[1] - half_len) else bots.pop(1)
print(round(half_len + abs(bots[0] - half_len)))


# length = int(input())
# n = int(input())
# bots = list(map(int, input().split()))
# bots.sort()

# half_len = length / 2
# while len(bots) != 1:
#     d1 = half_len + abs(bots[0] - half_len)
#     d2 = half_len + abs(bots[1] - half_len)
#     if d1 < d2:
#         bots.pop(0)
#     else:
#         bots.pop(1)
# print(round(half_len + abs(bots[0] - half_len)))


# length = int(input())
# n = int(input())
# bots = list(map(int, input().split()))
# bots.sort()

# half_len = length / 2
# while len(bots) != 1:
#     i = 0
#     while i < len(bots) - 1:
#         d1 = half_len + abs(bots[i] - half_len)
#         d2 = half_len + abs(bots[i + 1] - half_len)

#         if d1 < d2:
#             bots.pop(i)
#         else:
#             bots.pop(i + 1)
# print(round(half_len + abs(bots[0] - half_len)))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

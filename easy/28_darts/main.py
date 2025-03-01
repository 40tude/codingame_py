# https://www.codingame.com/ide/puzzle/darts-checkout-routes

# The goal is to calculate the number of routes to checkout a given score with a given number of darts.
# In order to checkout, the total sum of the darts thrown MUST equal score and use LESS THAN OR EQUAL TO darts number of darts.
# The final dart in any checkout route MUST land in the double segment.

# Singles: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25
# Doubles: D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D25
# Trebles: T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20


# Line 1: Integer score representing the remaining score.
# Line 2: Integer darts representing the number of darts remaining to throw.
# Integer of number of possible routes to reach score using at most darts number of darts.

# T5 D10 D10 - D10 T5 D10                   are two valid paths
# 10 D25 D25 - Swapping dart 2 and 3        is considered the same route

# 1 ≤ score ≤ 170
# 0 ≤ darts ≤ 5

# The final dart in any checkout route MUST land in the double segment.
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
# from collections import deque

score = int(input())
darts = int(input())

count = 0
targets = [score]
new_targets = []
while darts > 0:
    for target in targets:
        # The final dart in any checkout route MUST land in the double segment.
        for i in range(1, 25 + 1):
            if target - 2 * i >= 0:
                new_targets.append(target - 2 * i)
            else:
                break
    count += new_targets.count(0)
    new_targets = [x for x in new_targets if x != 0]
    darts -= 1
    print(count, new_targets)

print(count)

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

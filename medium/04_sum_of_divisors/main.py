# https://www.codingame.com/ide/puzzle/sum-of-divisors

# the sum of divisors of all the numbers from 1 to n.


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
n = int(input())
s = 0
[s := s + n // i * i for i in range(n, 0, -1)]
print(s)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/detective-pikaptcha-ep2


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_one_based.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -----------------------------------------------------------------------------


width, height = [int(i) for i in input().split()]
for i in range(height):
    line = input()

side = input()

for i in range(height):

    print("#####")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

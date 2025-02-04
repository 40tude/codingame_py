# https://www.codingame.com/ide/puzzle/1d-bush-fire

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_basic.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


n = int(input())
for _ in range(n):
    line = input().strip(".")
    count = 0
    while len(line):
        head = line[:3]  # up to 3 characters
        line = line[len(head) :].strip(".")
        count += 1  # there is always at least a fire thanks to the .strip(".")

    print(count)

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

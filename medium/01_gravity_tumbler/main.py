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

# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))


# -----------------------------------------------------------------------------
w, h = map(int, input().split())
count = int(input())
map_in = [list(input()) for _ in range(h)]


print("\n".join("".join(row) for row in map_in))


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

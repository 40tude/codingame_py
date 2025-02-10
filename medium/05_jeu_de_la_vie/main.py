# https://www.codingame.com/training/medium/game-of-life

# 1 => 0 if voisin = 0 ou 1
# 1 => 1 if voisin = 2 ou 3
# 1 => 0 if voisin > 3
# 0 => 1 if voisin== 3

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
w, h = map(int, input().split())
map = [list(input()) for _ in range(h)]


for row in map:
    print(*row, sep="")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

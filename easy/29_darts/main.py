# https://www.codingame.com/ide/puzzle/darts

# Line 1: SIZE of square as integer.
# Line 2: The number of competitors in name list, N.
# Next N lines: name of a single competitor in name list.
# Next line (N+3): Number of throws, T.
# Next T lines: Name of competitor, integer x-coordinate and integer y-coordinate of throw, each separated by a space, name X Y.

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
size = int(input())
R = size >> 1
n = int(input())
scores = {input(): 0 for _ in range(n)}

nb_throws = int(input())
for _ in range(nb_throws):
    inputs = input().split()
    x = abs(int(inputs[1]))
    y = abs(int(inputs[2]))
    if y <= R - x:
        scores[inputs[0]] += 15
    elif x**2 + y**2 <= R**2:
        scores[inputs[0]] += 10
    elif x <= R and y <= R:
        scores[inputs[0]] += 5

sorted_items = sorted(scores.items(), key=lambda x: (-x[1], list(scores.keys()).index(x[0])))
scores = dict(sorted_items)
for name, score in scores.items():
    print(f"{name} {score}")

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

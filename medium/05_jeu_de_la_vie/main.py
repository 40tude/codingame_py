# https://www.codingame.com/training/medium/game-of-life

# 1 => 0 if voisin =  0 ou 1
# 1 => 1 if voisin =  2 ou 3
# 1 => 0 if voisin >  3
# 0 => 1 if voisin == 3

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
def sum_around(m, y, x):
    sum = -m[y][x]

    for j in range(max(0, y - 1), min(len(m), y + 2)):
        for i in range(max(0, x - 1), min(len(m[0]), x + 2)):
            sum += m[j][i]
    return sum


# -------------------------------------
str_out = ""
w, h = map(int, input().split())
map_in = [list(map(int, input())) for _ in range(h)]


for y, row in enumerate(map_in):
    for x, value in enumerate(row):
        neighbors = sum_around(map_in, y, x)
        match value:
            case 0:
                cell = "1" if neighbors == 3 else "0"
            case 1:
                cell = "0" if neighbors <= 1 else "1" if 2 <= neighbors <= 3 else "0"
        str_out += cell
    str_out += "\n"

print(str_out)

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

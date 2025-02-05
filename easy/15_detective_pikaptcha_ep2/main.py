# https://www.codingame.com/ide/puzzle/detective-pikaptcha-ep2
# see https://bradleycarey.com/posts/2012-08-15-maze-solving-algorithms-wall-follower/

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
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -------------------------------------
def walk(y, x, dir):
    # Get the priorities according the current direction
    prios = priorities[direction_indices.get(dir)]
    for dir in prios:
        match (dir):
            case ">":
                if x + 1 < w and map[y][x + 1] != "#":
                    map[y][x] = str(int(map[y][x]) + 1)  # if speed becomes an issue keep int in the map
                    x += 1
                    break  # the for loop
            case "v":
                if y + 1 < h and map[y + 1][x] != "#":
                    map[y][x] = str(int(map[y][x]) + 1)  # if speed becomes an issue keep int in the map
                    y += 1
                    break
            case "<":
                if x - 1 >= 0 and map[y][x - 1] != "#":
                    map[y][x] = str(int(map[y][x]) + 1)  # if speed becomes an issue keep int in the map
                    x -= 1
                    break
            case "^":
                if y - 1 >= 0 and map[y - 1][x] != "#":
                    map[y][x] = str(int(map[y][x]) + 1)  # if speed becomes an issue keep int in the map
                    y -= 1
                    break
    return y, x, dir


# -------------------------------------
k_North = "^"
k_South = "v"
k_East = ">"
k_West = "<"

# direction_mapping = {"^": k_North, "v": k_South, ">": k_East, "<": k_West}
direction_indices = {"^": 0, "v": 1, ">": 2, "<": 3}

# According the current direction, the priorities are different
# 0: North, 1: East, 2: South, 3: West
priorities = []
priorities.append([k_West, k_North, k_East, k_South])
priorities.append([k_East, k_South, k_West, k_North])
priorities.append([k_North, k_East, k_South, k_West])
priorities.append([k_South, k_West, k_North, k_East])

w, h = [int(i) for i in input().split()]

# fill the map, update insertion point and initial direction
map = []
for y in range(h):
    line = list(input())
    map.append(line)
    for x, c in enumerate(line):
        if c in ("^", "v", ">", "<"):
            dir = c
            x0 = x
            y0 = y
            map[y][x] = "0"

side = input()
# if side is R, exchange columns 0 and 2 in priorities
if side == "R":
    for l in priorities:
        l[0], l[2] = l[2], l[0]


x = x0
y = y0
while True:
    y, x, dir = walk(y, x, dir)
    # print(f"{y} {x} {dir}")
    if x == x0 and y == y0:
        break

for y in range(h):
    print("".join(map[y]))


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

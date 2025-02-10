# https://www.codingame.com/ide/puzzle/dungeons-and-maps

# You are given N maps for a dungeon. Each map may contain a path to a treasure T, from starting position [ startRow; startCol ].
# Determine the index of the map which holds the shortest path from the starting position to T, but be careful a map may lead you to a TRAP.
# A path is marked on the map with ^, v, <, > symbols, each corresponding to UP, DOWN, LEFT, RIGHT directions respectively, i.e. each symbol shows you the next cell to move on.
# A valid path must start from [ startRow; startCol ] and end on T.
# The path length is the count of direction symbols plus 1, for the T cell.

# W = 4 H = 4
# startRow = 1 startCol = 1
# N = 3

# Maps:
# 0
# .>>v
# .^#v
# ..#v
# ...T

# 1
# ....
# .v#.
# .v#.
# .>>T

# 2
# ....
# v<#.
# v.#.
# ..>T

# In the above example map 2 does not contain a valid path from [1; 1] to T, map 0 contains a valid path with length 7 (the count of the direction symbols + T) and map 1 contains a valid path with length 5, so the answer is 1.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_trap.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
k_Big = 2**63 - 1
# w, h = [int(i) for i in input().split()]
w, h = map(int, input().split())

# start_row, start_col = [int(i) for i in input().split()]
start_row, start_col = map(int, input().split())

n = int(input())
# maps = [[list(input().strip()) for _ in range(h)] for _ in range(n)]
maps = [[list(input()) for _ in range(h)] for _ in range(n)]

lengths = []
for map in maps:
    len = 0
    row = start_row
    col = start_col
    while True:
        if (len > w * h) or (row not in range(h)) or (col not in range(w)):
            lengths.append(k_Big)
            break
        c = (map[row])[col]
        len += 1
        match c:
            case "^":
                row -= 1
            case "v":
                row += 1
            case "<":
                col -= 1
            case ">":
                col += 1
            case "T":
                lengths.append(len)
                break
            case ".":
                lengths.append(k_Big)
                break  # no path
            case "#":
                lengths.append(k_Big)
                break  # trap

print(lengths.index(min(lengths))) if min(lengths) != k_Big else print("TRAP")

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

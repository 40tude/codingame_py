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

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    for j in range(h):
        map_row = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("mapIndex")

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

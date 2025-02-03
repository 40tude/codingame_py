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


# ffff.ff.fff..fff...fffffff       8
#            ..   ...      f       8

# ffff.f.ffffff..ffff.f.ffffffff.  9


# f.ffff.ffff..ff.ffffff.fff.f.ff. 10


# -----------------------------------------------------------------------------
# pour chaque ligne
# Tant qu'il y a des f dans la ligne
# retrouver le nombre de groupes de 3 lettres dont 3f, remplacer les f par des ., count+1=1
# retrouver le nombre de groupes de 3 lettres dont 2f, remplacer les f par des ., count+1=1
# retrouver le nombre de groupes de 3 lettres dont 1f, remplacer les f par des ., count+1=1
# Afficher count

import re

# Replacements = [
#     ("fff", "..."),
#     ("ff.", "..."),
#     ("f.f", "..."),
#     (".ff", "..."),
#     ("f..", "..."),
#     (".f.", "..."),
#     ("..f", "..."),
# ]
Replacements = ["fff", "ff.", "f.f", ".ff", "f..", ".f.", "..f"]

n = int(input())
for i in range(n):
    line = input()
    count = 0
    for pattern in Replacements:
        t = re.subn(pattern, "...", line)
        line = t[0]
        count += t[1]
    print(count)

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

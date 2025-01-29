# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    sys.stdin = open("input.txt", "r")


# -----------------------------------------------------------------------------
w, h, t1, t2, t3 = [int(i) for i in input().split()]
for i in range(h):
    first_picture_row, second_picture_row = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/sudoku-solver


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
if RedirectIOtoFile:
    sys.stdin.close()

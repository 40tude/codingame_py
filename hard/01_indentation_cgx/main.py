# https://www.codingame.com/ide/puzzle/what-the-brainfuck
# https://fr.wikipedia.org/wiki/Brainfuck

# > increment the pointer position.
# < decrement the pointer position.
# + increment the value of the cell the pointer is pointing to.
# - decrement the value of the cell the pointer is pointing to.
# . output the value of the pointed cell, interpreting it as an ASCII value.
# , accept a positive one byte integer as input and store it in the pointed cell.
# [ jump to the instruction after the corresponding ] if the pointed cell's value is 0. Can be NESTED
# ] go back to the instruction after the corresponding [ if the pointed cell's value is different from 0.
#
# # Any other character is a comment and should be ignored.
#
# Error messages:
# "SYNTAX ERROR" if a [ appears to have no ] to jump to, or vice versa. Note that this error must be raised before the execution of the program, no matter its position in the Brainfuck code.
# "POINTER OUT OF BOUNDS" if the pointer position goes below 0 or above S - 1.
# "INCORRECT VALUE" if after an operation the value of a cell becomes negative or higher than 255.
#
# The output must be the characters sequence printed (.)


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


n = int(input())
for i in range(n):
    cgxline = input()

print("answer")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

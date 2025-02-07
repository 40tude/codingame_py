# https://www.codingame.com/ide/puzzle/bulk-email-generator

# Not a line based problem
# for the ith choice, pick the ith clause (modulo the number of clauses)


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_edge.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -----------------------------------------------------------------------------
import re

lines = ""

for _ in range(int(input())):
    lines += input()
    lines += "\n"

print(lines)

print()
match = re.search(r".*(\(.*\)).*", lines, re.DOTALL)
print(match.group(1))
# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

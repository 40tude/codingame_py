# https://www.codingame.com/ide/puzzle/folding-paper

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_many_mines.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# # -----------------------------------------------------------------------------
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# execution_time_microseconds = (end_time - start_time) * 1_000_000
# print(f"Execution time: {execution_time_microseconds:.2f} µs")


# -----------------------------------------------------------------------------
order = input()
side = input()


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

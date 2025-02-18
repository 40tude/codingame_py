# https://www.codingame.com/ide/puzzle/these-romans-are-crazy!

# convertir en decimal, faire la somme, puis reconvertir en romain ?
# https://www.rapidtables.com/convert/number/how-roman-numerals-to-number.html

# I has a value of 1 (maximum 3 in a row)
# V has a value of 5 (maximum 1 in a row)
# X has a value of 10 (maximum 3 in a row)
# L has a value of 50 (maximum 1 in a row)
# C has a value of 100 (maximum 3 in a row)
# D has a value of 500 (maximum 1 in a row)
# M has a value of 1000 (maximum 4 in a row)
#
# The character I just before an V or X has a value of -1 (example IX equals 9)
# The character X just before an L or C has a value of -10 (example XL equals 40)
# The character C just before an D or M has a value of -100 (example CM equals 900)

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


rom_1 = list(input())
rom_2 = list(input())


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

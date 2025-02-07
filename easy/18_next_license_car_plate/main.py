# https://www.codingame.com/training/easy/next-car-license-plate
# dig from 001 to 999 => 999

"""
AA-001-AA, AA-002-AA, AA-003-AA, ..., AA-999-AA,
AA-001-AB, AA-002-AB, AA-003-AB, ..., AA-999-AB,
...,
AA-001-ZZ, AA-002-ZZ, AA-003-ZZ, ..., AA-999-ZZ,
AB-001-AA, AB-002-AA, AB-003-AA, ..., AB-999-AA,
...,
ZY-001-ZZ, ZY-002-ZZ, ZY-003-ZZ, ..., ZY-999-ZZ,
ZZ-001-AA, ZZ-002-AA, ZZ-003-AA, ..., ZZ-999-ZZ
"""


# faut compter de 001 à 999 sans passer par 000
# faut compter de 000 à 998 en passant par 000 puis en ajoutant 1?


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


# -----------------------------------------------------------------------------
plate = input()
n = int(input())

k_alphabet = 26
k_Max_2Chars = k_alphabet**2
k_MaxUnits = 999

a2d = lambda a: ord(a) - ord("A")
d2a = lambda d: chr(d + ord("A"))

hundreds, units, tenths = plate.split("-")
units = int(units) - 1

tenths = a2d(tenths[0]) * k_alphabet + a2d(tenths[1])
hundreds = a2d(hundreds[0]) * k_alphabet + a2d(hundreds[1])
carry, units = divmod(units + n, k_MaxUnits)
units += 1

carry, tenths = divmod(tenths + carry, k_Max_2Chars)
t1, t2 = divmod(tenths, k_alphabet)
carry, hundreds = divmod(hundreds + carry, k_Max_2Chars)
h1, h2 = divmod(hundreds, k_alphabet)
print(f"{d2a(h1)}{d2a(h2)}-{units:03}-{d2a(t1)}{d2a(t2)}")

# # -----------------------------------------------------------------------------
# import re

# a2d = lambda a: ord(a) - ord("A")
# d2a = lambda d: chr(d + ord("A"))

# plate = input()
# n = int(input())


# match = re.search(r"^([A-Z]{2})-(\d{3})-([A-Z]{2})$", plate)
# Hundreds = match.group(1)
# Units = int(match.group(2))
# Tenths = match.group(3)

# Tenths = a2d(Tenths[0]) * 26**1 + a2d(Tenths[1]) * 26**0

# Hundreds = a2d(Hundreds[0]) * 26**1 + a2d(Hundreds[1]) * 26**0

# k_MaxUnits = 999
# Carry, Units = divmod(Units + n, k_MaxUnits)

# k_Max_Tenths = 26**2
# Carry, Tenths = divmod(Tenths + Carry, k_Max_Tenths)
# t1, t2 = divmod(Tenths, 26)

# k_Max_Hundreds = 26**2
# Carry, Hundreds = divmod(Hundreds + Carry, k_Max_Hundreds)
# h1, h2 = divmod(Hundreds, 26)

# print(f"{d2a(h1)}{d2a(h2)}-{Units:03}-{d2a(t1)}{d2a(t2)}")


# # -----------------------------------------------------------------------------
# import re

# a2d = lambda a: ord(a) - ord("A")
# d2a = lambda d: chr(d + ord("A"))

# plate = input()
# n = int(input())


# match = re.search(r"^([A-Z]{2})-(\d{3})-([A-Z]{2})$", plate)
# Hundreds = match.group(1)
# Units = int(match.group(2))
# Tenths = match.group(3)

# print(plate)
# print(f"Units    : {Units:03}")

# Tenths = a2d(Tenths[0]) * 26**1 + a2d(Tenths[1]) * 26**0
# print(f"Tenths   : {Tenths}")

# Hundreds = a2d(Hundreds[0]) * 26**1 + a2d(Hundreds[1]) * 26**0
# print(f"Hundreds : {Hundreds}")

# k_MaxUnits = 999
# Carry, Units = divmod(Units + n, k_MaxUnits)
# print(f"Units    : {Units:03} + {Carry}")

# k_Max_Tenths = 26**2
# Carry, Tenths = divmod(Tenths + Carry, k_Max_Tenths)
# print(f"Tenths   : {Tenths} + {Carry}")
# t1, t2 = divmod(Tenths, 26)
# print(d2a(t1), d2a(t2))

# k_Max_Hundreds = 26**2
# Carry, Hundreds = divmod(Hundreds + Carry, k_Max_Hundreds)
# print(f"Hundreds : {Hundreds} + {Carry}")
# h1, h2 = divmod(Hundreds, 26)
# print(d2a(h1), d2a(h2))

# print()
# print(f"{d2a(h1)}{d2a(h2)}-{Units:03}-{d2a(t1)}{d2a(t2)}")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

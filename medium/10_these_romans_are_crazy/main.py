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

# # -----------------------------------------------------------------------------
# Not mine
#
# romanNumeralMap = (('M',  1000),
#                    ('CM', 900),
#                    ('D',  500),
#                    ('CD', 400),
#                    ('C',  100),
#                    ('XC', 90),
#                    ('L',  50),
#                    ('XL', 40),
#                    ('X',  10),
#                    ('IX', 9),
#                    ('V',  5),
#                    ('IV', 4),
#                    ('I',  1))

# def toRoman(n):
#     result = ""
#     for numeral, integer in romanNumeralMap:
#         while n >= integer:
#             result += numeral
#             n -= integer
#     return result


# def fromRoman(s):
#     result = 0
#     index = 0
#     for numeral, integer in romanNumeralMap:
#         while s[index:index+len(numeral)] == numeral:
#             result += integer
#             index += len(numeral)
#     return result

# rom_1 = input()
# rom_2 = input()
# print(toRoman(fromRoman(rom_1)+fromRoman(rom_2)))


# -----------------------------------------------------------------------------
def int_to_roman(number: int) -> str:
    value_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    roman = ""
    for value, symbol in value_map:
        while number >= value:
            roman += symbol
            number -= value
    return roman


# -----------------------------------------------------------------------------
def roman_to_int(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):  # Iterate from right to left
        value = roman_dict[char]
        if value < prev_value:
            total -= value  # Subtractive notation (e.g., IV = 4)
        else:
            total += value
        prev_value = value

    return total


str_rom1 = input()
rom1 = roman_to_int(str_rom1)

str_rom2 = input()
rom2 = roman_to_int(str_rom2)
rom = rom1 + rom2
print(int_to_roman(rom))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

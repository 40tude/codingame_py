# https://www.codingame.com/ide/puzzle/recurring-decimals

# Given an input integer N
# Output 1/N in decimal form, with brackets () around any part of the fraction that repeats indefinitely

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_01.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
cache = []
str_result = "0."

N = 1
D = int(input())
R = N % D

while R and R not in cache:
    cache.append(R)
    N = R * 10
    R = N % D
    str_result += str(N // D)

if R != 0:
    length_of_repetitive_pattern = len(cache) - cache.index(R)
    insert_id = len(str_result) - length_of_repetitive_pattern
    str_result = str_result[:insert_id] + "(" + str_result[insert_id:] + ")"

print(str_result)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

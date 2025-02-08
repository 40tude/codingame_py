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
# Not mine
# import re

# n = int(input())
# txt = '\n'.join(input() for _ in range(n))
# pattern = '\(((?:(?:[^(\|)]*)\|?)*)\)'

# for pos, match in enumerate(re.findall(pattern, txt)):
#     choices = match.split('|')
#     txt = txt.replace('(%s)' % match, choices[pos % len(choices)], 1)

# print(txt)


# -----------------------------------------------------------------------------
# def make_choice(str_in):
#     choices = str_in.split("|")
#     return choices[curr_choice % len(choices)]

# make_choice = lambda str_in: str_in.split("|")[curr_choice % len(str_in.split("|"))]
make_choice = lambda str_in: (choices := str_in.split("|"))[curr_choice % len(choices)]

str_in = str_out = ""
curr_choice = cursor = 0

# for _ in range(int(input())):
#     str_in += input()
#     str_in += "\n"
str_in = "\n".join(input() for _ in range(int(input())))

while cursor < len(str_in):
    c = str_in[cursor]
    if c == "(":
        sub = ""
        cursor += 1
        while str_in[cursor] != ")":
            sub += str_in[cursor]
            cursor += 1
        str_out += make_choice(sub)
        curr_choice += 1
    else:
        str_out += c
    cursor += 1

print(str_out)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/van-ecks-sequence
# memoization

# The rule here is that you start with an element A1
#       - you get to a number you have     seen before, the following term is the number of occurences
#       - you get to a number you have not seen before, the following term is a 0.

# 0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, …
# Term 1: The first term is 0.
# Term 2: Since we haven’t seen 0 before, the second term is 0.
# Term 3: Since we had seen a 0 before, one step back, the third term is 1
# Term 4: Since we haven’t seen a 1 before, the fourth term is 0
# Term 5: Since we had seen a 0 before, two steps back, the fifth term is 2.

# ! C'est PAS le nb d’occurrence mais le nombre de termes avant de le revoir
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
# set_val = set()
# id_tracker: dict[int, int] = {}

# a = int(input())
# n = int(input())

# for i in range(0, n - 1):
#     if a in set_val:
#         # tmp = i - id_tracker[a]
#         # id_tracker[a] = i
#         # a = tmp
#         tmp = id_tracker[a]
#         id_tracker[a] = i
#         a = i - tmp
#     else:
#         set_val.add(a)
#         id_tracker[a] = i
#         tmp = id_tracker[a]
#         a = i - tmp
# print(a)

# -----------------------------------------------------------------------------
# Not mine
# a = int(input())
# n = int(input())

# seen = dict()

# for i in range(n-1):
#     (seen[a], a) = (i, i-seen[a] if a in seen else 0)

# print(a)

# -----------------------------------------------------------------------------
set_val = set()
id_tracker: dict[int, int] = {}

a = int(input())
n = int(input())

for i in range(0, n - 1):
    if a in set_val:
        tmp = i - id_tracker[a]
        id_tracker[a] = i
        a = tmp
    else:
        set_val.add(a)
        id_tracker[a] = i
        a = 0
print(a)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))

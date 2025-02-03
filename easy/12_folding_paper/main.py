# https://www.codingame.com/ide/puzzle/folding-paper

# L =>    R = L+R, U<<1, D<<1, L=1
# R =>    L = L+R, U<<1, D<<1, R=1
# U =>    D = D+U, L<<1, R<<1, U=1
# D =>    U = D+U, L<<1, R<<1, D=1

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input4.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")

# -----------------------------------------------------------------------------
D, L, R, U = 1, 1, 1, 1

operations = {
    "L": lambda D, L, R, U: (D << 1, 1, L + R, U << 1),
    "R": lambda D, L, R, U: (D << 1, L + R, 1, U << 1),
    "U": lambda D, L, R, U: (D + U, L << 1, R << 1, 1),
    "D": lambda D, L, R, U: (1, L << 1, R << 1, D + U),
}

for op in input():
    D, L, R, U = operations[op](D, L, R, U)
print(globals().get(input()))


# # -----------------------------------------------------------------------------
# D, L, R, U = 1, 1, 1, 1

# ops = input()
# for op in ops:
#     match op:
#         case "L":
#             R = L + R
#             U = U << 1
#             D = D << 1
#             L = 1
#         case "R":
#             L = L + R
#             U = U << 1
#             D = D << 1
#             R = 1
#         case "U":
#             D = D + U
#             L = L << 1
#             R = R << 1
#             U = 1
#         case "D":
#             U = D + U
#             L = L << 1
#             R = R << 1
#             D = 1

# # side = input()
# # print(globals().get(side, "Variable not found!"))
# # print(globals().get(side))
# print(globals().get(input()))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

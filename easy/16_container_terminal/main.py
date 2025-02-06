# https://www.codingame.com/ide/puzzle/container-terminal

# Ship A will come earlier than Ship B. Ship B will come earlier than Ship C
# Note that we do not sort the containers before stacking them up. Sorting is an option too slow and costly to put into practice.

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

# Not Mine
# for _ in range(int(input())):
#     stack = []
#     for char in input():
#         k = 0
#         while k < len(stack) and char > stack[k]: k += 1
#         if k == len(stack): stack += char,
#         stack[k] = char
#     print(len(stack))

# -------------------------------------
for i in range(int(input())):
    stack = []
    for char in input():
        # char_max = max(stack, key=lambda x: ord(x), default="@")
        # if char > char_max:
        if char > max(stack, key=lambda x: ord(x), default="@"):
            stack += char
        else:
            for j, id2 in enumerate(stack):
                if id2 >= char:  # ! >= not > 😁
                    stack[j] = char
                    break
    print(len(stack))


# -------------------------------------
# n = int(input())
# for i in range(n):
#     top_Of_Stack: list[int] = []
#     line = input()
#     for char in line:
#         id = ord(char)
#         if id > max(top_Of_Stack, default=0):
#             top_Of_Stack.append(id)
#         else:
#             for j, id2 in enumerate(top_Of_Stack):
#                 if id2 >= id:  # ! >= not > 😁
#                     top_Of_Stack[j] = id
#                     break
#     print(len(top_Of_Stack))


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

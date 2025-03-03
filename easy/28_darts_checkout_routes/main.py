# https://www.codingame.com/ide/puzzle/darts-checkout-routes

# The goal is to calculate the number of routes to checkout a given score with a given number of darts.
# In order to checkout, the total sum of the darts thrown MUST equal score and use LESS THAN OR EQUAL TO darts number of darts.
# The final dart in any checkout route MUST land in the double segment.

# Singles: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,                        25
# Doubles: D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20,   D25
# Trebles: T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20


# Line 1: Integer score representing the remaining score.
# Line 2: Integer darts representing the number of darts remaining to throw.
# Integer of number of possible routes to reach score using at most darts number of darts.

# T5 D10 D10 - D10 T5 D10                   are two valid paths
# 10 D25 D25 - Swapping dart 2 and 3        is considered the same route => We can have 2 consecutive darts from the same segment (S, D, T) only once

# 1 ≤ score ≤ 170
# 0 ≤ darts ≤ 5

# The final dart in any checkout route MUST land in the double segment.
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
# # Not mine

# # from functools import cache
# import time
# import sys


# # @cache  => speedup 960 µs vs 1300 µs
# def ways(score, darts):
#     if darts < 0:
#         return 0
#     if score == 0:
#         return 1
#     if score < 0 or darts == 0:
#         return 0
#     return sum(ways(score - n, darts - 1) for values in (singles, doubles, trebles) for n in values)


# singles = list(range(1, 21)) + [25]
# doubles = [2 * n for n in singles]
# trebles = [3 * n for n in singles if n != 25]

# score, darts = int(input()), int(input())
# start_time = time.perf_counter()
# bob = sum(ways(score - d, darts - 1) for d in doubles)
# end_time = time.perf_counter()
# print(bob)
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

import time

segments = {
    "S": [i for i in range(1, 21)] + [25],  # Single values 1-20 + Bullseye
    "D": [2 * i for i in range(1, 21)] + [50],  # Doubles 2-40 + Bullseye
    "T": [3 * i for i in range(1, 21)],  # Trebles 3-60
}

targets = [int(input())]  # Target score to reach
darts = nb_darts = int(input())  # Number of darts available

start_time = time.perf_counter()

nb_routes = 0
while darts > 0:
    new_targets = []
    valid_segments = ["D"] if darts == nb_darts else segments.keys()  # Last dart must be a double

    for target in targets:
        for segment in valid_segments:
            new_targets.extend([target - i for i in segments[segment] if target - i >= 0])

    nb_routes += new_targets.count(0)  # Count successful finishes
    targets = [x for x in new_targets if x > 0]  # Keep only positive targets
    darts -= 1

end_time = time.perf_counter()
print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)
print(nb_routes)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Singles = [1 * i for i in range(1, 20 + 1)] + [25]
# Doubles = [2 * i for i in range(1, 20 + 1)] + [50]
# Trebles = [3 * i for i in range(1, 20 + 1)]

# segments = {"S": Singles, "D": Doubles, "T": Trebles}

# count = 0
# targets = [int(input())]
# darts = int(input())

# if darts > 0:
#     new_targets = []
#     for target in targets:
#         for segment in "D":
#             for i in segments[segment]:
#                 if target - i >= 0:
#                     new_targets.append(target - i)
#                 else:
#                     break

#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1

# while darts > 0:
#     new_targets = []
#     for target in targets:
#         for segment in segments:
#             for i in segments[segment]:
#                 if target - i >= 0:
#                     new_targets.append(target - i)
#                 else:
#                     break
#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1

# print(count)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# import time
# import sys

# Singles = [1 * i for i in range(1, 20 + 1)] + [25]
# Doubles = [2 * i for i in range(1, 20 + 1)] + [50]
# Trebles = [3 * i for i in range(1, 20 + 1)]

# segments = {"S": Singles, "D": Doubles, "T": Trebles}

# count = 0
# targets = [int(input())]
# darts = int(input())

# start_time = time.perf_counter()
# if darts > 0:
#     segment = "D"
#     new_targets = []
#     for target in targets:
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#                 # if (target - i) == 0:
#                 #     print(f"{target}, {i}")
#             else:
#                 break

#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1
#     # print(count, targets)
#     # print()

# # Throw order. We can have 2 consecutive darts from the same segment (S, D, T) only once
# while darts > 0:
#     new_targets = []
#     for target in targets:
#         for segment in segments:
#             for i in segments[segment]:
#                 if target - i >= 0:
#                     new_targets.append(target - i)
#                     # if (target - i) == 0:
#                     #     print(f"{target}, {segment}{i}")
#                 else:
#                     break
#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1

# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)
# print(count)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Singles = [1 * i for i in range(1, 20 + 1)] + [25]
# Doubles = [2 * i for i in range(1, 20 + 1)] + [50]
# Trebles = [3 * i for i in range(1, 20 + 1)]

# segments = {"S": Singles, "D": Doubles, "T": Trebles}

# count = 0
# targets = [int(input())]
# darts = int(input())

# if darts > 0:
#     segment = "D"
#     new_targets = []
#     for target in targets:
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#                 if (target - i) == 0:
#                     print(f"{target}, {i}")
#             else:
#                 break

#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1
#     print(count, targets)
#     print()

# # Throw order. We can have 2 consecutive darts from the same segment (S, D, T) only once
# while darts > 0:
#     new_targets = []
#     for target in targets:
#         for segment in segments:
#             for i in segments[segment]:
#                 if target - i >= 0:
#                     new_targets.append(target - i)
#                     if (target - i) == 0:
#                         print(f"{target}, {segment}{i}")
#                 else:
#                     break
#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1

# print(count)


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------

# Singles = [1 * i for i in range(1, 20 + 1)] + [25]
# Doubles = [2 * i for i in range(1, 20 + 1)] + [50]
# Trebles = [3 * i for i in range(1, 20 + 1)]

# segments = {"S": Singles, "D": Doubles, "T": Trebles}
# # segments2 = list(segments.keys() - {"D"})
# # segments2 = {cle: valeur for cle, valeur in segments.items() if cle != "D"}

# count = 0
# targets = [int(input())]
# darts = int(input())

# if darts > 0:
#     # The final dart in any checkout route MUST land in the double segment.
#     segment = "D"
#     new_targets = []
#     for target in targets:
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#                 if (target - i) == 0:
#                     print(f"{target}, {i}")
#             else:
#                 break

#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1
#     print(count, targets)
#     print()

# # Throw order. We can have 2 consecutive darts from the same segment (S, D, T) only once
# while darts > 0:
#     new_targets = []
#     for target in targets:
#         for segment in segments:
#             for i in segments[segment]:
#                 if target - i >= 0:
#                     new_targets.append(target - i)
#                     if (target - i) == 0:
#                         print(f"{target}, {segment}{i}")
#                 else:
#                     break
#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1

# print(count)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Singles = [1 * i for i in range(1, 20 + 1)] + [25]
# Doubles = [2 * i for i in range(1, 20 + 1)] + [50]
# Trebles = [3 * i for i in range(1, 20 + 1)]

# segments = {"S": Singles, "D": Doubles, "T": Trebles}

# count = 0
# targets = [int(input())]
# darts = int(input())

# if darts > 0:
#     segment = "D"
#     new_targets = []
#     for target in targets:
#         # The final dart in any checkout route MUST land in the double segment.
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#             else:
#                 break

#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1
#     print(count, targets)
#     print()

# # Throw order. We cannot have 2 consecutive darts from the same segment (S, D, T)
# new_targets = []
# while darts > 0:
#     for target in targets:
#         segment = "S"
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#                 if (target - i) == 0:
#                     print(f"{target}, {i}")
#             else:
#                 break
#         # for i in Doubles:
#         #     if target - i >= 0:
#         #         new_targets.append(target - i)
#         #         if (target - i) == 0:
#         #             print(f"{target}, {i}")
#         #     else:
#         #         break
#         segment = "T"
#         for i in segments[segment]:
#             if target - i >= 0:
#                 new_targets.append(target - i)
#                 if (target - i) == 0:
#                     print(f"{target}, T{i}")
#             else:
#                 break
#     count += new_targets.count(0)
#     targets = [x for x in new_targets if x != 0]
#     darts -= 1
#     print(count, targets)


# print(count)

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

# https://www.codingame.com/training/easy/111-rubiks-cube-movements


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


for c in "xyz":
    rotate[c + "'"] = {v: k for k, v in rotate[c].items()}

# -----------------------------------------------------------------------------
# LUT
#    L  R  U  D  F  B
# x  L  R  B  F  U  D
# x' L  R  F  B  D  U
# y  B  F  U  D  L  R
# y' F  B  U  D  R  L
# z  U  D  R  L  F  B
# z' D  U  L  R  F  B

LUT = {
    "x": {"L": "L", "R": "R", "U": "B", "D": "F", "F": "U", "B": "D"},
    "x'": {"L": "L", "R": "R", "U": "F", "D": "B", "F": "D", "B": "U"},
    "y": {"L": "B", "R": "F", "U": "U", "D": "D", "F": "L", "B": "R"},
    "y'": {"L": "F", "R": "B", "U": "U", "D": "D", "F": "R", "B": "L"},
    "z": {"L": "U", "R": "D", "U": "R", "D": "L", "F": "F", "B": "B"},
    "z'": {"L": "D", "R": "U", "U": "L", "D": "R", "F": "F", "B": "B"},
}

rotations = input().split()
face1 = input()
face2 = input()

for r in rotations:
    face1, face2 = LUT[r][face1], LUT[r][face2]

print(f"{face1}\n{face2}")


# # -----------------------------------------------------------------------------
# # LUT
# #    L  R  U  D  F  B
# # x  L  R  B  F  U  D
# # x' L  R  F  B  D  U
# # y  B  F  U  D  L  R
# # y' F  B  U  D  R  L
# # z  U  D  R  L  F  B
# # z' D  U  L  R  F  B

# LUT = {
#     "x": {
#         "L": "L",
#         "R": "R",
#         "U": "B",
#         "D": "F",
#         "F": "U",
#         "B": "D",
#     },
#     "x'": {
#         "L": "L",
#         "R": "R",
#         "U": "F",
#         "D": "B",
#         "F": "D",
#         "B": "U",
#     },
#     "y": {
#         "L": "B",
#         "R": "F",
#         "U": "U",
#         "D": "D",
#         "F": "L",
#         "B": "R",
#     },
#     "y'": {
#         "L": "F",
#         "R": "B",
#         "U": "U",
#         "D": "D",
#         "F": "R",
#         "B": "L",
#     },
#     "z": {
#         "L": "U",
#         "R": "D",
#         "U": "R",
#         "D": "L",
#         "F": "F",
#         "B": "B",
#     },
#     "z'": {
#         "L": "D",
#         "R": "U",
#         "U": "L",
#         "D": "R",
#         "F": "F",
#         "B": "B",
#     },
# }


# rotations = input().split()
# face1 = input()
# face2 = input()

# for r in rotations:
#     face1, face2 = LUT[r][face1], LUT[r][face2]

# print(f"{face1}\n{face2}")

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

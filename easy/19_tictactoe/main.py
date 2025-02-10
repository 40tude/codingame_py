# https://www.codingame.com/ide/puzzle/tictactoe
# no win condition => false

# trouver 2 o hor, vert ou diag
#   completer la ligne, la colonne ou la diag
#       print map
#       exit
# sinon
#   print false

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
# Note mine
# b = ''
# for i in range(3):
#     b += input()
# b = list(b)
# for x,y,z in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
#     if sorted([b[x], b[y], b[z]]) == ['.', 'O', 'O']:
#         b[x], b[y], b[z] = 'O', 'O', 'O'
#         print('{}{}{}\n{}{}{}\n{}{}{}'.format(*b))
#         quit(0)
# print("false")


# -----------------------------------------------------------------------------
def transpose(M):

    # return [[M[j][i] for j in range(3)] for i in range(3)]
    # I want to modify the original matrix in-place
    for i in range(3):
        for j in range(i + 1, 3):
            M[i][j], M[j][i] = M[j][i], M[i][j]


# --------------------------------------
def move_O_hori(M):
    for y in range(3):
        count_0 = map[y].count("O")
        count_X = map[y].count("X")
        if count_0 == 2 and count_X == 0:
            map[y][map[y].index(".")] = "O"
            return True

    return False


# --------------------------------------
def move_O_diags(M):
    # Check main diagonal
    d = M[0][0] + M[1][1] + M[2][2]
    count_0 = d.count("O")
    count_X = d.count("X")
    if count_0 == 2 and count_X == 0:
        i = d.index(".")
        map[i][i] = "O"
        return True

    # Check secondary diagonal
    d = M[2][0] + M[1][1] + M[0][2]
    count_0 = d.count("O")
    count_X = d.count("X")
    if count_0 == 2 and count_X == 0:
        i = d.index(".")
        map[2 - i][i] = "O"
        return True


# --------------------------------------
map = [list(input()) for i in range(3)]

modified = move_O_hori(map)
if not modified:
    transpose(map)
    modified = move_O_hori(map)
    transpose(map)
if not modified:
    modified = move_O_diags(map)
if not modified:
    print("false")
else:
    # for y in range(3):
    #     print("".join(map[y]))
    print("\n".join("".join(row) for row in map))


# -----------------------------------------------------------------------------
# str = "".join([input() for i in range(3)])
# l1 = str[0:3]
# l2 = str[3:6]
# l3 = str[6:9]

# c1 = str[0] + str[3] + str[6]
# c2 = str[1] + str[4] + str[7]
# c3 = str[2] + str[5] + str[8]

# d1 = str[0] + str[4] + str[8]
# d2 = str[2] + str[4] + str[6]

# if l1.count("O") == 2 and l1.count("X") == 0:
#     l1 = l1.replace(".", "O")
# elif l2.count("O") == 2 and l2.count("X") == 0:
#     l2 = l2.replace(".", "O")
# elif l3.count("O") == 2 and l3.count("X") == 0:
#     l3 = l3.replace(".", "O")
# elif c1.count("O") == 2 and c1.count("X") == 0:
#     c1 = c1.replace(".", "O")
# elif c2.count("O") == 2 and c2.count("X") == 0:
#     c2 = c2.replace(".", "O")
# elif c3.count("O") == 2 and c3.count("X") == 0:
#     c3 = c3.replace(".", "O")
# elif d1.count("O") == 2 and d1.count("X") == 0:
#     d1 = d1.replace(".", "O")
# elif d2.count("O") == 2 and d2.count("X") == 0:
#     d2 = d2.replace(".", "O")

# ??????????????

# for y in range(3):
#     print(str[y * 3 : y * 3 + 3])

# -----------------------------------------------------------------------------
# map = [list(input()) for i in range(3)]

# for y in range(3):
#     count_0 = map[y].count("O")
#     count_X = map[y].count("X")
#     if count_0 == 2 and count_X == 0:
#         map[y][map[y].index(".")] = "O"
#         break

# for x in range(3):
#     count_0 = map[0][x].count("O") + map[1][x].count("O") + map[2][x].count("O")
#     count_X = map[0][x].count("X") + map[1][x].count("X") + map[2][x].count("X")
#     if count_0 == 2 and count_X == 0:
#         # ??????????????
#         break

# for i in range(3):
#     count_0 = map[0][0].count("O") + map[1][1].count("O") + map[2][2].count("O")
#     count_X = map[0][0].count("X") + map[1][1].count("X") + map[2][2].count("X")
#     if count_0 == 2 and count_X == 0:
#         # ??????????????
#         break


# for i in range(3):
#     count_0 = map[2][0].count("O") + map[1][1].count("O") + map[0][2].count("O")
#     count_X = map[2][0].count("X") + map[1][1].count("X") + map[0][2].count("X")
#     if count_0 == 2 and count_X == 0:
#         # ??????????????
#         break


# for y in range(3):
#     print("".join(map[y]))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

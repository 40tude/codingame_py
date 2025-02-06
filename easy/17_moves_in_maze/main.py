# https://www.codingame.com/ide/puzzle/moves-in-maze
# Read https://en.wikipedia.org/wiki/Breadth-first_search

# 4 directions only


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_space.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -----------------------------------------------------------------------------
from collections import deque

k_DMAX = 35


class Node:
    def __init__(self, x, y):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.x = x
        self.y = y
        self.d = 0


def bfs(root):
    i2a = lambda i: str(i) if i < 10 else chr(55 + i)
    a2i = lambda a: int(a) if a.isdigit() else ord(a) - 55

    # if root is None:
    #     return

    # Initialize a queue for BFS
    queue = deque([root])

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()

        # Visit the node : update the distance if shorter
        tmp = map[node.y][node.x]
        tmp = k_DMAX if tmp == "." else a2i(tmp)
        if node.d < tmp:
            map[node.y][node.x] = i2a(node.d)

        # Enqueue the north child if not yet initialized
        # h = 5   0 -> 4
        # si y+1 = 5 => y+1%h = 1
        # si y-1 = -1 => (y - 1 + h)%h = 4
        if map[(node.y - 1 + h) % h][node.x] == ".":
            node.north = Node(node.x, (node.y - 1 + h) % h)
            node.north.d = node.d + 1
            queue.append(node.north)

        if map[(node.y + 1) % h][node.x] == ".":
            node.south = Node(node.x, (node.y + 1) % h)
            node.south.d = node.d + 1
            queue.append(node.south)

        if map[node.y][(node.x + 1) % w] == ".":
            node.east = Node((node.x + 1) % w, node.y)
            node.east.d = node.d + 1
            queue.append(node.east)

        if map[node.y][(node.x - 1 + w) % w] == ".":
            node.west = Node((node.x - 1 + w) % w, node.y)
            node.west.d = node.d + 1
            queue.append(node.west)


# -------------------------------------
w, h = [int(i) for i in input().split()]

map = []
for j in range(h):
    line = list(input())
    map.append(line)
    for i, c in enumerate(line):
        if c == "S":
            x0, y0 = i, j

# On crée un arbre
# On se place en Start y0, x0
# On probe les 4 directions
#   Si la cellule est accessible on crée un enfant et on stocke  d = 1 + parent
# On recommence pour chacun des enfants jusqu'à ce
root = Node(x0, y0)
bfs(root)

for y in range(h):
    print("".join(map[y]))


# # -----------------------------------------------------------------------------
# from collections import deque


# class Node:
#     def __init__(self, x, y):
#         self.north = None
#         self.south = None
#         self.east = None
#         self.west = None
#         self.x = x
#         self.y = y
#         self.d = 0


# i2a = lambda i: str(i) if i < 10 else chr(55 + i)
# a2i = lambda a: int(a) if a.isdigit() else ord(a) - 55


# def bfs(root):
#     if root is None:
#         return

#     # Initialize a queue for BFS
#     queue = deque([root])

#     while queue:
#         # Dequeue a node from the front of the queue
#         node = queue.popleft()

#         # Visit the node : update the distance if shorter
#         tmp = map_out[node.y][node.x]
#         tmp = 35 if a2i(tmp) < 0 else a2i(tmp)
#         if node.d < tmp:
#             # map_out[node.y][node.x] = str(node.d) if node.d < 10 else chr(55 + node.d)
#             tmp = i2a(node.d)
#             map_out[node.y][node.x] = tmp

#         # Enqueue the north child if not yet initialized
#         # h = 5   0 -> 4
#         # si y+1 = 5 => y+1%h = 1
#         # si y-1 = -1 => (y - 1 + h)%h = 4
#         if map_out[(node.y - 1 + h) % h][node.x] == ".":
#             node.north = Node(node.x, (node.y - 1 + h) % h)
#             node.north.d = node.d + 1
#             queue.append(node.north)

#         if map_out[(node.y + 1) % h][node.x] == ".":
#             node.south = Node(node.x, (node.y + 1) % h)
#             node.south.d = node.d + 1
#             queue.append(node.south)

#         if map_out[node.y][(node.x + 1) % w] == ".":
#             node.east = Node((node.x + 1) % w, node.y)
#             node.east.d = node.d + 1
#             queue.append(node.east)

#         if map_out[node.y][(node.x - 1 + w) % w] == ".":
#             node.west = Node((node.x - 1 + w) % w, node.y)
#             node.west.d = node.d + 1
#             queue.append(node.west)


# # -------------------------------------
# w, h = [int(i) for i in input().split()]

# map = []
# for j in range(h):
#     line = list(input())
#     map.append(line)
#     for i, c in enumerate(line):
#         if c == "S":
#             x0, y0 = i, j

# map_out = map.copy()
# map_out[y0][x0] = "0"
# # On crée un arbre
# # On se place en Start y0, x0
# # On probe les 4 directions
# #   Si la cellule est accessible on crée un enfant et on stocke  d = 1 + parent
# # On recommence pour chacun des enfants jusqu'à ce
# root = Node(x0, y0)
# bfs(root)

# for y in range(h):
#     print("".join(map_out[y]))


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


""""
Trouvé  : 23456789A876543
Attendu : 234567899876543

Solution
234567899876543
345678#AA987654
456789ABBA98765
56789ABCCBA9876
456789ABBA98765
3456789AA987#54
234567899876#43
123456788765432
012345677654321
1#3456788765432

Proposition
23456789A876543
345678#BA987654
456789ABCA98765
56789ABCDBA9876
456789ABCA98765
3456789AB987#54
23456789A876#43
123456789765432
012345678654321
1#3456798765432

15 10
...............
......#........
...............
...............
...............
............#..
............#..
...............
S..............
.#.............
23456789A876543

"""


"""
# #########
# 01234567#
# #2#####8#
# #3#DCBA9#
# #########

"""

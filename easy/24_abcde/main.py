# https://www.codingame.com/training/easy/abcdefghijklmnopqrstuvwxyz
# On peut pas traverser les limites du tableau et passer de la droite à la gauche

# recursive ?

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
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))


# -----------------------------------------------------------------------------
from collections import deque


class Node:
    def __init__(self, y, x, id):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.x = x
        self.y = y
        self.char_id = id


def bfs(root):
    seq_len = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()

        map_out[node.y][node.x] = k_alphabet[node.char_id]
        seq_len += 1

        if map_in[new_y := max(0, node.y - 1)][node.x] == k_alphabet[node.char_id + 1]:
            node.north = Node(new_y, node.x, node.char_id + 1)
            queue.append(node.north)

        if map_in[new_y := min(n - 1, node.y + 1)][node.x] == k_alphabet[node.char_id + 1]:
            node.south = Node(new_y, node.x, node.char_id + 1)
            queue.append(node.south)

        if map_in[node.y][new_x := min(n - 1, node.x + 1)] == k_alphabet[node.char_id + 1]:
            node.east = Node(node.y, new_x, node.char_id + 1)
            queue.append(node.east)

        if map_in[node.y][new_x := max(0, node.x - 1)] == k_alphabet[node.char_id + 1]:
            node.west = Node(node.y, new_x, node.char_id + 1)
            queue.append(node.west)
    return seq_len == 26


k_alphabet = "abcdefghijklmnopqrstuvwxyz."  # !there is a dot at the end
char_id = 0
n = int(input())
map_in = [list(input()) for _ in range(n)]

multiple_starts = [
    Node(y, x, char_id) for y, row in enumerate(map_in) for x, value in enumerate(row) if value == k_alphabet[char_id]
]

Done = False
while not Done:
    map_out = [list("-" * n) for _ in range(n)]
    Done = bfs(multiple_starts.pop())

print("\n".join("".join(row) for row in map_out))


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
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# import sys
# import time
# from collections import deque


# # -------------------------------------
# class Node:
#     def __init__(self, y, x, id):
#         self.north = None
#         self.south = None
#         self.east = None
#         self.west = None
#         self.x = x
#         self.y = y
#         self.char_id = id


# # -------------------------------------
# def bfs(root):

#     # if root is None:
#     #     return

#     # Initialize a queue for BFS
#     queue = deque([root])
#     seq_len = 0

#     while queue:
#         # Dequeue a node from the front of the queue
#         node = queue.popleft()

#         # Visit node
#         map_out[node.y][node.x] = k_alphabet[node.char_id]
#         seq_len += 1

#         if map_in[new_y := max(0, node.y - 1)][node.x] == k_alphabet[node.char_id + 1]:
#             node.north = Node(new_y, node.x, node.char_id + 1)
#             queue.append(node.north)

#         if map_in[new_y := min(n - 1, node.y + 1)][node.x] == k_alphabet[node.char_id + 1]:
#             node.south = Node(new_y, node.x, node.char_id + 1)
#             queue.append(node.south)

#         if map_in[node.y][new_x := min(n - 1, node.x + 1)] == k_alphabet[node.char_id + 1]:
#             node.east = Node(node.y, new_x, node.char_id + 1)
#             queue.append(node.east)

#         if map_in[node.y][new_x := max(0, node.x - 1)] == k_alphabet[node.char_id + 1]:
#             node.west = Node(node.y, new_x, node.char_id + 1)
#             queue.append(node.west)

#     return seq_len == 26 # all letters of the alphabet


# # -------------------------------------
# k_alphabet = "abcdefghijklmnopqrstuvwxyz."  # !there is a dot at the end
# char_id = 0
# n = int(input())
# map_in = [list(input()) for _ in range(n)]


# multiple_starts = [
#     Node(y, x, char_id) for y, row in enumerate(map_in) for x, value in enumerate(row) if value == k_alphabet[char_id]
# ]


# start_time = time.perf_counter()

# Done = False
# while not Done:
#     map_out = [list("-" * n) for _ in range(n)]
#     Done = bfs(multiple_starts.pop())

# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


# print("\n".join("".join(row) for row in map_out))
# # for y in range(n):
# #     print("".join(map_out[y]))


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
# import time
# from collections import deque


# # -------------------------------------
# class Node:
#     def __init__(self, y, x, id):
#         self.north = None
#         self.south = None
#         self.east = None
#         self.west = None
#         self.x = x
#         self.y = y
#         self.char_id = id


# # -------------------------------------
# def bfs(root):

#     # if root is None:
#     #     return

#     # Initialize a queue for BFS
#     queue = deque([root])
#     length = 0
#     while queue:
#         # Dequeue a node from the front of the queue
#         node = queue.popleft()

#         # Visit node
#         map_out[node.y][node.x] = k_alphabet[node.char_id]
#         length += 1

#         if map_in[new_y := max(0, node.y - 1)][node.x] == k_alphabet[node.char_id + 1]:
#             node.north = Node(new_y, node.x, node.char_id + 1)
#             queue.append(node.north)

#         if map_in[new_y := min(n - 1, node.y + 1)][node.x] == k_alphabet[node.char_id + 1]:
#             node.south = Node(new_y, node.x, node.char_id + 1)
#             queue.append(node.south)

#         if map_in[node.y][new_x := min(n - 1, node.x + 1)] == k_alphabet[node.char_id + 1]:
#             node.east = Node(node.y, new_x, node.char_id + 1)
#             queue.append(node.east)

#         if map_in[node.y][new_x := max(0, node.x - 1)] == k_alphabet[node.char_id + 1]:
#             node.west = Node(node.y, new_x, node.char_id + 1)
#             queue.append(node.west)
#     return length


# # -------------------------------------
# k_alphabet = "abcdefghijklmnopqrstuvwxyz."  # !there is a doc at the end
# char_id = 0
# n = int(input())
# map_in = [list(input()) for _ in range(n)]


# # 139 µs
# # multiple_starts = []
# # for y in range(n):
# #     for x in range(n):
# #         if map_in[y][x] == k_alphabet[char_id]:
# #             multiple_starts.append(Node(y, x, char_id))

# # 90 µs
# multiple_starts = [
#     Node(y, x, char_id) for y, row in enumerate(map_in) for x, value in enumerate(row) if value == k_alphabet[char_id]
# ]


# start_time = time.perf_counter()

# length = 0
# while multiple_starts and length != 26:
#     map_out = [list("-" * n) for _ in range(n)]
#     length = bfs(multiple_starts.pop())

# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# # for y in range(n):
# #     print("".join(map_out[y]))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

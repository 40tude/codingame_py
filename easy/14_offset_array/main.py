# https://www.codingame.com/ide/puzzle/offset-arrays
#  the indexing operations may be nested
# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_one_based.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# Not mine
# offset_arrays = {}

# def parse_definition(line):
#     lhs, rhs = line.split("=")
#     id, offset = lhs.split("[")
#     offset = int(offset.split("..")[0])
#     data = [int(x) for x in rhs.split()]
#     offset_arrays[id] = (offset, data)

# def lookup(line):
#     stack = line.split("[")
#     idx = int(stack.pop().split("]")[0])
#     while len(stack):
#         id = stack.pop()
#         a = offset_arrays[id]
#         idx = a[1][idx - a[0]]
#     return idx

# n = int(input())
# for _ in range(n): parse_definition(input())
# print (lookup(input()))


# Not mine
# import sys
# import math

# offsets = {}
# vals = {}

# n = int(input())
# for i in range(n):
#     left, right = list(map(str.strip, input().split('=')))
#     name, indexes = left.split('[')
#     offsets[name] = int(indexes.split('.')[0])
#     vals[name] = right.split()

# calls = input().replace(']', '').split('[')
# calls.reverse()
# n, *calls = calls

# for call in calls:
#     n = vals[call][int(n)-offsets[call]]

# print(n)


# -----------------------------------------------------------------------------
import re


class OffsetArray:
    def __init__(self, low, high, lst):
        self.low_idx = low
        self.high_idx = high
        self.lst = lst.copy()

    def __getitem__(self, idx):
        resolved_idx = resolve_expression(idx)
        return self.lst[int(resolved_idx) - self.low_idx]


# Brings a level of indirection which makes recursion possible
def resolve_expression(expr):
    is_int = lambda s: s[1:].isdigit() if s[0] in ("-", "+") else s.isdigit()

    if is_int(expr):
        return int(expr)

    match = re.search(r"^([A-Z]+)\[(.+)\]$", expr)
    var_name = match.group(1)
    inner_idx = match.group(2)
    # resolve_expression gets called recursively
    return globals()[var_name][inner_idx]


n = int(input())
for _ in range(n):
    assignment = input()
    match = re.search(r"^([A-Z]+)\[(-*\d+)\.\.(-*\d+)\]\s*=\s*(.+)$", assignment)
    globals()[match.group(1)] = OffsetArray(
        int(match.group(2)), int(match.group(3)), list(map(int, match.group(4).split(" ")))
    )

value = input()
match = re.search(r"^([A-Z]+)\[(.+)\]$", value)
print(globals()[match.group(1)][match.group(2)])


# # -----------------------------------------------------------------------------
# import re


# class OffsetArray:
#     def __init__(self, low, high, lst):
#         self.low_idx = low
#         self.high_idx = high
#         self.lst = lst.copy()

#     def __getitem__(self, idx):
#         resolved_idx = resolve_expression(idx)
#         return self.lst[int(resolved_idx) - self.low_idx]


# # Brings a level of indirection which makes recursion possible
# def resolve_expression(expr):
#     is_int = lambda s: s[1:].isdigit() if s[0] in ("-", "+") else s.isdigit()

#     if is_int(expr):
#         return int(expr)

#     match = re.search(r"^([A-Z]+)\[(.+)\]$", expr)
#     # if match:
#     var_name = match.group(1)
#     inner_idx = match.group(2)
#     # resolve_expression gets called recursively
#     return globals()[var_name][inner_idx]
#     # else:
#     # raise ValueError(f"Invalid expression: {expr}")


# n = int(input())
# for _ in range(n):
#     assignment = input()
#     match = re.search(r"^([A-Z]+)\[(-*\d+)\.\.(-*\d+)\]\s*=\s*(.+)$", assignment)
#     if match:
#         name = match.group(1)
#         low = int(match.group(2))
#         high = int(match.group(3))
#         lst = list(map(int, match.group(4).split(" ")))
#         globals()[name] = OffsetArray(low, high, lst)

# value = input()
# match = re.search(r"^([A-Z]+)\[(.+)\]$", value)
# print(globals()[match.group(1)][match.group(2)])

# var_name = match.group(1)
# idx = match.group(2)
# print(globals()[var_name][idx])


# -----------------------------------------------------------------------------
# import re

# # def is_int(s):
# #     return s[1:].isdigit() if s[0] in ("-", "+") else s.isdigit()

# is_int = lambda s: s[1:].isdigit() if s[0] in ("-", "+") else s.isdigit()


# class OffsetArray:
#     def __init__(self, low, high, lst):
#         self.low_idx = low
#         self.high_idx = high
#         self.lst = lst.copy()

#     def __getitem__(self, idx):
#         if isinstance(idx, int):
#             return self.lst[idx - self.low_idx]
#         else:
#             match = re.search(r"^([A-Z]+)\[(.+)\]$", idx)
#             var_name = match.group(1)
#             idx = match.group(2)
#             return globals()[var_name][int(idx)] if is_int(idx) else globals()[var_name][idx]


# n = int(input())
# for _ in range(n):
#     assignment = input()
#     match = re.search(r"^([A-Z]+)\[(-*\d+)\.\.(-*\d+)\]\s*=\s*(.+)$", assignment)
#     if match:
#         name = match.group(1)
#         low = int(match.group(2))
#         high = int(match.group(3))
#         lst = list(map(int, match.group(4).split(" ")))
#         globals()[name] = OffsetArray(low, high, lst)


# # bob = B[4]
# # marcel = C[0]

# value = input()
# match = re.search(r"^([A-Z]+)\[(.+)\]$", value)
# var_name = match.group(1)
# idx = match.group(2)
# zoubida = globals()[var_name][int(idx)] if is_int(idx) else globals()[var_name][idx]
# print(zoubida)


# -----------------------------------------------------------------------------

# import re


# class OffsetArray:
#     def __init__(self, low, high, lst):
#         self.low_idx = low
#         self.high_idx = high
#         self.lst = lst.copy()

#     def __getitem__(self, i):
#         return self.lst[i - self.low_idx]


# n = int(input())
# offset_arrays = {}
# for _ in range(n):
#     assignment = input()
#     match = re.search(r"^(\w+)\[(-*\d+)\.\.(-*\d+)\]\s*=\s*(.+)$", assignment)
#     if match:
#         # print(match.group(1))  # Name
#         # print(match.group(2))  # Lower index
#         # print(match.group(3))  # Upper index
#         # print(match.group(4))  # values
#         name = match.group(1)
#         low = int(match.group(2))
#         high = int(match.group(3))
#         length = high - low + 1
#         lst = list(map(int, match.group(4).split(" ")))
#         print(lst)
#         offset_arrays[name] = OffsetArray(low, high, lst)


# bob = offset_arrays["B"].lst[2]
# marcel = offset_arrays["C"][0]


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

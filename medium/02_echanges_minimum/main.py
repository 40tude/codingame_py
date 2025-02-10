# https://www.codingame.com/ide/puzzle/minimal-number-of-swaps

# les 1 au debut en un minimum de swap
# Est ce qu'il faut vraiment faire le swap ou juste compter le nombre de swaps

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
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


# -----------------------------------------------------------------------------
# Not mine
input()
x = input().split()
nb_ones = x.count("1")
# Il y a nb_ones 1
# bob = x[:nb_ones] slicind pour extraire les nb_ones premiers element
swaps = x[:nb_ones].count("0")  # ensuite on compte juste les 0
print(swaps)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
n = int(input())
lst = list(map(int, input().split()))

head = count = 0
tail = n - 1

while head < tail:
    if lst[head] == 1:
        head += 1
        continue  # on repasse au while head<tail

    if lst[tail] == 0:
        tail -= 1
        continue

    count += 1
    head += 1
    tail -= 1

print(count)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# def swap(lst, i, j):
#     lst[i], lst[j] = lst[j], lst[i]


# n = int(input())
# lst = list(map(int, input().split()))

# head = 0
# tail = n - 1
# count = 0

# while True:
#     while lst[head] == 1 and head < n - 1:
#         head += 1
#     while lst[tail] == 0 and tail >= 0:
#         tail -= 1
#     if tail <= head:
#         break
#     # swap(lst, head, tail)
#     count += 1
#     head += 1
#     tail -= 1
# print(count)

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

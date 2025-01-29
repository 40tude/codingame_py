import sys

RedirectIOtoFile = True
if RedirectIOtoFile :
  sys.stdin = open("input.txt", "r")

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())
 
Maps = []
for i in range(n):
    CurrentMap = [['' for x in range(w)] for y in range(h)]
    for j in range(h):
        CurrentMap[j] = list(input())
    Maps.append(map)

if RedirectIOtoFile :
    sys.stdin.close()


# 1sp 1/ 1bS 1_ 1/ 1bS nl 1( 1sp 1o 1. 1o 1sp 1) nl 1sp 1> 1sp 1^ 1sp 1< nl 2sp 3|

# Abbreviation is one of : sp, bS, sQ, nl
# sp = space
# bS = backSlash \
# sQ = singleQuote '
# nl = NewLine
# If a chunk is composed only of numbers, the character is the last digit

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    from pathlib import Path
    import os

    os.chdir(Path(__file__).parent)
    sys.stdin = open("input.txt", "r")


# -----------------------------------------------------------------------------
import re

surprise = ""
for chunk in input().split(" "):
    chunk = chunk.replace("sp", " ").replace("bS", "\\").replace("sQ", "'").replace("nl", "\n")
    x = re.findall(r"^(\d+)(.)$", chunk)
    n, char = x[0] if x else (1, "\n")
    surprise += int(n) * f"{char}"

print(surprise)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

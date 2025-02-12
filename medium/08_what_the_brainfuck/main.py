# https://www.codingame.com/ide/puzzle/what-the-brainfuck

# > increment the pointer position.
# < decrement the pointer position.
# + increment the value of the cell the pointer is pointing to.
# - decrement the value of the cell the pointer is pointing to.
# . output the value of the pointed cell, interpreting it as an ASCII value.
# , accept a positive one byte integer as input and store it in the pointed cell.
# [ jump to the instruction after the corresponding ] if the pointed cell's value is 0. Can be NESTED
# ] go back to the instruction after the corresponding [ if the pointed cell's value is different from 0.
#
# # Any other character is a comment and should be ignored.
#
# Error messages:
# "SYNTAX ERROR" if a [ appears to have no ] to jump to, or vice versa. Note that this error must be raised before the execution of the program, no matter its position in the Brainfuck code.
# "POINTER OUT OF BOUNDS" if the pointer position goes below 0 or above S - 1.
# "INCORRECT VALUE" if after an operation the value of a cell becomes negative or higher than 255.
#
# The output must be the characters sequence printed (.)


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
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
import sys


# -------------------------------------
def preprocessor():
    line_out = ""
    for line in prog_lines:
        for op_code in line:
            if op_code in ops:
                line_out += op_code
    return line_out


# -------------------------------------
def parser(line):
    stack = []
    for op_code in line:
        if op_code == "[":
            stack.append(op_code)
        elif op_code == "]":
            if not stack:
                return
            stack.pop()
    if stack:
        print("SYNTAX ERROR")
        sys.exit()


# -------------------------------------
def ptr_check(addr):
    if addr < 0 or addr > ram_size - 1:
        print("POINTER OUT OF BOUNDS")
        sys.exit()


def val_check(addr):
    if addr < 0 or addr > 255:
        print("INCORRECT VALUE")
        sys.exit()


# -------------------------------------
def val_inc(addr, ip):
    ram[addr] = ram[addr] + 1
    val_check(ram[addr])
    return addr, (ip := ip + 1)


def val_dec(addr, ip):
    ram[addr] = ram[addr] - 1
    val_check(ram[addr])
    return addr, (ip := ip + 1)


# -------------------------------------
def addr_inc(addr, ip):
    # addr += 1
    ptr_check(addr := addr + 1)
    return addr, (ip := ip + 1)


def addr_dec(addr, ip):
    # addr -= 1
    ptr_check(addr := addr - 1)
    return addr, (ip := ip + 1)


# -------------------------------------
def STO(addr, ip):
    ram[addr] = params.pop(0)
    val_check(ram[addr])
    return addr, (ip := ip + 1)


# -------------------------------------
def output(addr, ip):
    print(chr(ram[addr]), end="")
    return addr, (ip := ip + 1)


# -------------------------------------
def jump_fwd(addr, ip):
    stack.append(ip)
    if ram[addr] == 0:
        ip = stack.pop()
    return addr, (ip := ip + 1)


# -------------------------------------
def jump_bck(addr, ip):
    if ram[addr] != 0:
        ip = stack[-1]
    return addr, (ip := ip + 1)


# > increment the pointer position.
# < decrement the pointer position.
# + increment the value of the cell the pointer is pointing to.
# - decrement the value of the cell the pointer is pointing to.
# . output the value of the pointed cell, interpreting it as an ASCII value.
# , accept a positive one byte integer as input and store it in the pointed cell.
# [ jump to the instruction after the corresponding ] if the pointed cell's value is 0. Can be NESTED
# ] go back to the instruction after the corresponding [ if the pointed cell's value is different from 0.
ops = {
    ">": addr_inc,
    "<": addr_dec,
    "+": val_inc,
    "-": val_dec,
    ".": output,
    ",": STO,
    "[": jump_fwd,
    "]": jump_bck,
}

# -------------------------------------
line_count, ram_size, n_inputs = map(int, input().split())
prog_lines = [input() for _ in range(line_count)]
params = [int(input()) for _ in range(n_inputs)]

line = preprocessor()  # Remove comments... Flatten the source code on a single line
parser(line)  # Check for syntax errors

ip = 0  # Instruction Pointer
addr = 0  # Pointer to the current cell in the RAM
ram = [0] * ram_size
stack: list[int] = []

while ip < len(line):
    op_code = line[ip]
    if op_code in ops:
        addr, ip = ops[op_code](addr, ip)
    else:
        ip += 1

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

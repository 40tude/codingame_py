# AND : performs a logical AND operation.
# OR : performs a logical OR operation.
# XOR : performs a logical exclusive OR operation.
# NAND : performs a logical inverted AND operation.
# NOR : performs a logical inverted OR operation.
# NXOR : performs a logical inverted exclusive OR operation.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    sys.stdin = open("input.txt", "r")


# -----------------------------------------------------------------------------
n = int(input())  # 1 ≤ n ≤ 4
m = int(input())  # 1 ≤ m ≤ 16
inputs = {}
for i in range(n):
    input_name, str_signal = input().split()
    lst_signal = [0 if char == "_" else 1 for char in str_signal]
    inputs[input_name] = lst_signal

for i in range(m):
    output_name, op, input_name_1, input_name_2 = input().split()

    match op:
        case "AND":
            lst_signal = [bit1 & bit2 for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]
        case "OR":
            lst_signal = [bit1 | bit2 for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]
        case "XOR":
            lst_signal = [bit1 ^ bit2 for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]
        case "NAND":
            lst_signal = [not (bit1 & bit2) for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]
        case "NOR":
            lst_signal = [not (bit1 | bit2) for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]
        case "NXOR":
            lst_signal = [not (bit1 ^ bit2) for bit1, bit2 in zip(inputs[input_name_1], inputs[input_name_2])]

    str_signal = "".join(["_" if bit == 0 else "-" for bit in lst_signal])
    print(f"{output_name} {str_signal}")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


# outputs = {}
# for i in range(m):
#     output_name, op, input_name_1, input_name_2 = input().split()
#     outputs[output_name] = [a & b for a, b in zip(inputs[input_name_1], inputs[input_name_2])]

#     match op:
#         case "AND":
#             outputs[output_name] = [a & b for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case "OR":
#             outputs[output_name] = [a | b for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case "XOR":  # bool(a) != bool(b)
#             outputs[output_name] = [a ^ b for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case "NAND":
#             outputs[output_name] = [not (a & b) for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case "NOR":
#             outputs[output_name] = [not (a | b) for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case "NXOR":
#             outputs[output_name] = [not (a ^ b) for a, b in zip(inputs[input_name_1], inputs[input_name_2])]
#         case _:
#             assert False

# for name, lst_signal in outputs.items():
#     str_signal = "".join(["_" if bit == 0 else "-" for bit in lst_signal])
#     print(f"{name} {str_signal}")

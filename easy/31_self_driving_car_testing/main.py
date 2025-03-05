# https://www.codingame.com/ide/puzzle/self-driving-car-testing

# Line 1: The number N of lines describing the road pattern
# Line 2: The position X (starting from 1) of the car at the beginning, then a list of command separated by a semi-colon ;
# N next lines: The number R of similar consecutive patterns, then, separated with a semi-colon ; the pattern of the road to be repeated R times.

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# -----------------------------------------------------------------------------
# Last version using generators
# The main function is 3 lines : get_road, get_car, print

import sys
import re
from typing import Generator, Iterator

# Read all lines at once otherwise the code works locally but NOT one CodinGame
lines: list[str] = sys.stdin.read().splitlines()
lines_iter: Iterator[str] = iter(lines)  # Lines iterator (think lines_iter as input())


# -------------------------------------
def get_car_position(car_commands: list[str]) -> Generator[int, None, None]:
    """Generator that yields the car's position based on movement commands."""
    car_x: int = int(car_commands.pop(0)) - 1  # 0-based position of the car
    pattern: re.Pattern = re.compile(r"^(\d+)([LSR]+)$")

    for expr in car_commands:
        a_match = pattern.match(expr)
        if a_match:
            nb_move: int = int(a_match.group(1))
            move: str = a_match.group(2)
            match move:
                case "S":
                    dx = 0
                case "L":
                    dx = -1
                case "R":
                    dx = 1
            for _ in range(nb_move):
                car_x += dx
                yield car_x


# -------------------------------------
def get_car_position_init() -> Generator[int, None, None]:
    """Initialize the car position generator from input commands."""
    car_commands: list[str] = next(lines_iter).split(";")  # Get the logs for the car
    return get_car_position(car_commands)


# -------------------------------------
def get_road_section() -> Generator[list[str], None, None]:
    """Generator that yields each road segment as a list of characters."""
    for user_input in lines_iter:
        if not user_input:
            yield None
        else:
            road_segment_len, road_pattern = user_input.split(";")
            for _ in range(int(road_segment_len)):
                yield list(road_pattern)


# -------------------------------------
_ = next(lines_iter)  # Not used explicitly
car_position = get_car_position_init()
road_section = get_road_section()

try:
    while True:
        road: list[str] = next(road_section)
        road[next(car_position)] = "#"
        print("".join(road))
except StopIteration:
    pass

# # -----------------------------------------------------------------------------
# # Fonctionne en LOCAL et sur CodinGame
# # Bien voir qu'on lit toutes les entrées d'un coup
# # Ensuite on utilise un itérateur pour lire les lignes une à une*

# import sys
# import re

# lines = sys.stdin.read().splitlines()  # Read all lines at once
# lines_iter = iter(lines)  # Lines iterator (think lines_iter as input())


# # -------------------------------------
# def get_car_position(car_commands):
#     car_x = int(car_commands.pop(0)) - 1  # 0-based position of the car
#     pattern = re.compile(r"^(\d+)([LSR]+)$")

#     for expr in car_commands:
#         a_match = pattern.match(expr)
#         if a_match:
#             nb_move = int(a_match.group(1))
#             move = a_match.group(2)
#             match move:
#                 case "S":
#                     dx = 0
#                 case "L":
#                     dx = -1
#                 case "R":
#                     dx = 1
#             for _ in range(nb_move):
#                 car_x += dx
#                 yield car_x


# # -------------------------------------
# def get_car_position_init():
#     car_commands = next(lines_iter).split(";")  # Get the logs for the car
#     return get_car_position(car_commands)


# # -------------------------------------
# def get_road_section():
#     for user_input in lines_iter:
#         if not user_input:
#             yield None
#         else:
#             road_segment_len, road_pattern = user_input.split(";")
#             for _ in range(int(road_segment_len)):
#                 yield list(road_pattern)


# # -------------------------------------
# _ = next(lines_iter)
# car_position = get_car_position_init()
# road_section = get_road_section()

# try:
#     while True:
#         road = next(road_section)
#         road[next(car_position)] = "#"
#         print("".join(road))
# except StopIteration:
#     pass


# # -----------------------------------------------------------------------------
# # Fonctionne en LOCAL et sur CodinGame
# # Bien voir qu'on lit toutes les entrées d'un coup
# # Ensuite on utilise un itérateur pour lire les lignes une à une*

# import sys
# import re

# # Lire toutes les entrées d'un coup
# lines = sys.stdin.read().splitlines()
# lines_iter = iter(lines)  # Création d'un itérateur sur les lignes


# # -------------------------------------
# def get_car_pattern(car_commands):
#     car_x = int(car_commands.pop(0)) - 1  # Position initiale de la voiture
#     pattern = re.compile(r"^(\d+)([LSR]+)$")  # 1S, 2L, 3R

#     for expr in car_commands:
#         a_match = pattern.match(expr)
#         if a_match:
#             nb_move = int(a_match.group(1))
#             move = a_match.group(2)
#             match move:
#                 case "S":
#                     dx = 0
#                 case "L":
#                     dx = -1
#                 case "R":
#                     dx = 1
#             for _ in range(nb_move):
#                 car_x += dx
#                 yield car_x


# # -------------------------------------
# def get_car_pattern_init():
#     car_commands = next(lines_iter).split(";")  # Lire la ligne suivante de l'itérateur
#     return get_car_pattern(car_commands)


# # -------------------------------------
# def get_road_pattern():
#     for user_input in lines_iter:  # On itère sur les lignes restantes
#         if not user_input:  # Vérifier si l'entrée est vide pour sortir
#             yield None
#         else:
#             road_segment_len, road_pattern = user_input.split(";")
#             for _ in range(int(road_segment_len)):  # Répéter le motif le bon nombre de fois
#                 yield list(road_pattern)


# road_log = []
# nb_road_segments = int(next(lines_iter))  # Lire le premier élément de l'itérateur
# gen_car = get_car_pattern_init()
# gen_road = get_road_pattern()

# try:
#     while True:
#         road_pattern = next(gen_road)
#         car_x = next(gen_car)
#         road_pattern[car_x] = "#"
#         road_log.append(road_pattern)
# except StopIteration:
#     pass  # Sortie propre de la boucle quand le générateur est épuisé

# print("\n".join("".join(row) for row in road_log))


# -----------------------------------------------------------------------------
# On essaie de ne plus avoir qu'une seule boucle pour dessiner la route
# et positionner la voiture
#
# On va maintenir 2 pointeurs : un pour la route et un pour la voiture
# Chaque pointeur avance dans un segment : road_segment ou car_segment
# Quand un pointeur arrive au bout de son segment il passe au debut du suivant

# On verra ensuite si il est possible d'afficher au fil de l'eau

# ! Le code ci-dessous ne fonctionne QUE EN LOCAL

# import re


# # -------------------------------------
# def get_car_pattern(car_commands):
#     car_x = int(car_commands.pop(0)) - 1  # Position initiale de la voiture
#     pattern = re.compile(r"^(\d+)([LSR]+)$")  # 1S, 2L, 3R

#     for expr in car_commands:
#         a_match = pattern.match(expr)
#         if a_match:
#             nb_move = int(a_match.group(1))
#             move = a_match.group(2)
#             match move:
#                 case "S":
#                     dx = 0
#                 case "L":
#                     dx = -1
#                 case "R":
#                     dx = 1
#             for _ in range(nb_move):
#                 car_x += dx
#                 yield car_x


# # -------------------------------------
# def get_car_pattern_init():
#     car_commands = input().split(";")  # Liste des commandes
#     return get_car_pattern(car_commands)


# # -------------------------------------
# def get_road_pattern():
#     while user_input := input():
#         if not user_input:  # Vérifier si l'entrée est vide pour sortir
#             yield None
#         else:
#             road_segment_len, road_pattern = user_input.split(";")
#             for _ in range(int(road_segment_len)):  # Répéter le motif le bon nombre de fois
#                 yield list(road_pattern)


# road_log = []
# nb_road_segments = int(input())
# gen_car = get_car_pattern_init()
# gen_road = get_road_pattern()

# try:
#     while True:
#         road_pattern = next(gen_road)
#         car_x = next(gen_car)
#         road_pattern[car_x] = "#"
#         road_log.append(road_pattern)
# except StopIteration:
#     pass  # Sortie propre de la boucle quand le générateur est épuisé


# print("\n".join("".join(row) for row in road_log))


# # -----------------------------------------------------------------------------
# import re

# pattern = re.compile(r"^(\d+)([LSR]+)$")  # 1S, 2L, 3R

# road_log: list[list[str]] = []

# n = int(input())
# commands = input().split(";")

# for _ in range(n):
#     repetition, road_pattern = input().split(";")
#     for _ in range(int(repetition)):
#         road_log.append(list(road_pattern))

# pos = int(commands.pop(0)) - 1
# dx = 0
# index = 0

# for expr in commands:
#     a_match = pattern.match(expr)
#     if a_match:
#         nb_move = int(a_match.group(1))
#         move = a_match.group(2)
#         match move:
#             case "S":
#                 dx = 0
#             case "L":
#                 dx = -1
#             case "R":
#                 dx = 1
#         for _ in range(nb_move):
#             pos += dx
#             road_log[index][pos] = "#"
#             index += 1

# print("\n".join("".join(map(str, row)) for row in road_log))


# -----------------------------------------------------------------------------
# import sys
# print(f"{sys.version}", file=sys.stderr, flush=True)

# import re

# n = int(input())
# commands = input().split(";")

# road_log: list[list[str]] = []
# for _ in range(n):
#     repetition, road_pattern = input().split(";")
#     n_repetition = int(repetition)
#     for _ in range(n_repetition):
#         # Créer et ajouter une liste à chaque fois sinon pb de référence
#         road_log.append(list(road_pattern))

# pos = int(commands.pop(0)) - 1
# dx = 0
# index = 0

# for expr in commands:
#     a_match = re.search(r"^(\d+)([LSR]+)$", expr)
#     if a_match:
#         nb_move = int(a_match.group(1))
#         move = a_match.group(2)
#         match move:
#             case "S":
#                 dx = 0
#             case "L":
#                 dx = -1
#             case "R":
#                 dx = 1
#         for _ in range(nb_move):
#             pos += dx
#             road_log[index][pos] = "#"
#             index += 1

# print("\n".join("".join(map(str, row)) for row in road_log))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))

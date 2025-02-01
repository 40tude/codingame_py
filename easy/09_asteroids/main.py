# You are given two pictures of the night sky of dimensions W*H, taken at two different times t1 and t2
# For your convenience, asteroids have been marked with capital letters A to Z
# The rest is empty space represented by a dot (.)
#
# Using the information contained in those two pictures, determine the position of the asteroids at t3, and output a picture of the same region of the sky.
#
# If necessary, the final coordinates are to be rounded-down (floor).
# Asteroids travel at different altitudes (with A being the closest and Z the farthest from your observation point) and therefore cannot collide with each other during their transit.
# If two or more asteroids have the same final coordinates, output only the closest one.
# It is guaranteed that all asteroids at t1 will still be present at t2, that no asteroids are hidden in the given pictures, and that there is only one asteroid per altitude.
#
# NB: Because of the flooring operation, it is important that you choose a coordinate system with the origin at the top left corner and the y-axis increasing in the downward direction.
#

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_out_of_bounds.txt"  # "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# Les astéroides sont dans un dictionnaire
# Repérés par leur nom : A...Z
# Chaque astéroïdes est un dictionnaire avec des champs x1, y1, x2, y2, x3, y3

# L'origine est en haut à gauche
# Pour chaque ligne des 2 images
#  Pour chaque caractère
#    Si c'est une lettre
#      On ajoute le caractère au dictionnaire des astéroïdes
#      Si on est dans l'image 1, on met à jour x1 et y1
#      Sinon, si on est est dans l'image 2 on met à jour x2 et y2
# Fin

# Pour chaque astéroïde du dictionnaire
#  On calcule vx et vy
#  On calcule x3 et y3 (floor)
# Fin

# Pour chaque astéroïde du dictionnaire
#   On met à jour l'image de sortie
#   Gérer les cas où il y a plusieurs astéroïdes à la même position
# Fin

# Afficher l'image de sortie


# Un astéroïde c'est une liste
#   une position à t1 (x1,y1)
#   une position à t2 (x2,y2)
#   une position à t3 (x3,y3)

# vx = (x2-x1)/(t2-t1)
# vy = (y2-y1)/(t2-t1)
# x3 = x1 + dx = x1 + vx * (t3-t2)
# y3 = y1 + dy = y1 + vy * (t3-t2)


# for y in range(h):
#     first_picture_row, second_picture_row = input().split()
# image1.append(list(first_picture_row))
# image2.append(list(second_picture_row))

# -----------------------------------------------------------------------------
import math

w, h, t1, t2, t3 = [int(i) for i in input().split()]

# dict_asteroids: dict[int, int, int, int, int, int] = {}
dict_asteroids = {}

for y in range(h):
    first_picture_row, second_picture_row = input().split()

    for x in range(w):
        char = first_picture_row[x]
        if char.isalpha():
            # setdefault permet de créer un dictionnaire vide si la clé n'existe pas
            asteroid = dict_asteroids.setdefault(char, {})
            asteroid["x1"] = x
            asteroid["y1"] = y

        char = second_picture_row[x]
        if char.isalpha():
            asteroid = dict_asteroids.setdefault(char, {})
            asteroid["x2"] = x
            asteroid["y2"] = y


for asteroid in dict_asteroids:
    vx = (dict_asteroids[asteroid]["x2"] - dict_asteroids[asteroid]["x1"]) / (t2 - t1)
    vy = (dict_asteroids[asteroid]["y2"] - dict_asteroids[asteroid]["y1"]) / (t2 - t1)
    dict_asteroids[asteroid]["x3"] = dict_asteroids[asteroid]["x2"] + math.floor((vx * (t3 - t2)))
    dict_asteroids[asteroid]["y3"] = dict_asteroids[asteroid]["y2"] + math.floor(vy * (t3 - t2))

img_out = [["." for _ in range(w)] for _ in range(h)]

for asteroid in dict_asteroids:
    x3, y3 = dict_asteroids[asteroid]["x3"], dict_asteroids[asteroid]["y3"]
    if x3 in range(w) and y3 in range(h):
        if img_out[y3][x3] == ".":
            img_out[y3][x3] = asteroid
        else:
            img_out[y3][x3] = asteroid if ord(asteroid) < ord(img_out[y3][x3]) else img_out[y3][x3]

for row in img_out:
    print("".join(row))

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

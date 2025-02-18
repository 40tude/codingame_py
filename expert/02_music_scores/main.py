# https://www.codingame.com/ide/puzzle/music-scores
# https://files.codingame.com/pub/dw/dw2-allimages_fr.html


# Ligne 1 : la largeur W et la hauteur H de l'image en pixels.
# Ligne 2 : l'image encodée de haut en bas en utilisant l'algorithme DWE Doctor Who Encoding
# Plusieurs couples "C L" séparés par des espaces.
# "C" est la couleur du pixel (soit B pour noir ou W pour blanc)
# "L" est le nombre de pixels contigus de la même couleur (! potentiellement sur plusieurs lignes de l'image).

# SORTIE :
# Les notes lues de gauche à droite séparées par des espaces.
# Chaque note est composée de deux caractères.
# Premier caractère     la note elle-même   : A B C D E F or G.
# Deuxième caractère    son type            : H pour une blanche (Half) ou Q pour une noire (Quarter).
# Il n'y a pas de distinction entre le premier C et le second C (idem pour D, E, F, G). Gamme du dessus


# C     D   E   F   G   A   B
# do    ré  mi  fa  sol la  si

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_05.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
w, h = [int(i) for i in input().split()]
image = input()


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

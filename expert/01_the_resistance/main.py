# https://www.codingame.com/ide/puzzle/the-resistance

# Pas d'espace
# Votre programme devra déterminer le nombre de messages différents qu'il est possible d'obtenir à partir d'une séquence en Morse et d'un dictionnaire donné.

# -....--.-. peut correspondre : BAC, BANN, DUC, DU TETE etc.

#
# E  .	    F  ..-.	 G  --.	 H  ....
# I  ..	    J  .---	 K  -.-	 L  .-..
# M  --	    N  -.	 O  ---	 P  .--.
# Q  --.-	R  .-.	 S  ...	 T  -
# U  ..-	V  ...-	 W  .--	 X  -..-
# Y  -.--	Z  --..

# Ligne 1 : une séquence Morse de longueur maximale L
# Ligne 2 : un entier N correspondant au nombre de mots du dictionnaire
# Les N Lignes suivantes : un mot du dictionnaire par ligne. Chaque mot a une longueur maximale M et n’apparaît qu'une seule fois dans le dictionnaire.

# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_05.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


DICO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


# --------------------------------------
# Approche recursive
# On a une chaîne, on choisit un mot qui commence comme la chaîne
# Si on a trouvé un mot, on supprime de la chaîne les lettres du mot et on rappelle
#       Quand la chaîne a une longueur nulle on compte +1
#       Sinon on recommence et on passe en revue tous les mots du vocabulaire
def check_if_in(voc, morse_str):
    if morse_str == "":
        return 1

    count = 0
    for translated in voc.values():
        if morse_str.startswith(translated):
            count += check_if_in(voc, morse_str[len(translated) :])
    return count


# --------------------------------------
morse_input = input()
voc_size = int(input())
vocabulary = {
    word: "".join(DICO_MORSE[letter] for letter in word) for word in (input().strip() for _ in range(voc_size))
}
result = check_if_in(vocabulary, morse_input)
print(result)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

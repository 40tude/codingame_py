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
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


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


# ! “cache” provides memoization.
# As a default argument, it is shared between calls and therefore behaves like a static variable.
def build_messages(voc, morse_str, cache={}):
    if morse_str == "":
        return 1

    if morse_str in cache:
        return cache[morse_str]

    count = 0
    for translated in voc.values():
        if morse_str.startswith(translated):
            count += build_messages(voc, morse_str[len(translated) :], cache)

    cache[morse_str] = count
    return count


# --------------------------------------
morse_input = input()
voc_size = int(input())
vocabulary = {
    word: "".join(DICO_MORSE[letter] for letter in word) for word in (input().strip() for _ in range(voc_size))
}
# memo: dict[str, int] = {}
# print(build_messages(vocabulary, morse_input, memo))
print(build_messages(vocabulary, morse_input))


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
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# DICO_MORSE = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
# }


# # --------------------------------------
# # Recursive approach
# # We have a string, we choose a word that starts like the string
# # If we found a word, we remove the letters of the word from the string and call again
# #       When the string has a length of zero, we count +1 (meaning we have a set of valid words)
# #       Otherwise, we start over and go through all the words in the vocabulary
# def check_if_in1(voc, morse_str):
#     if morse_str == "":
#         return 1

#     count = 0
#     # for translated in voc.values():
#     for word, translated in voc.items():
#         if morse_str.startswith(translated):
#             print(f"Look for {word}\t ({translated})\tat beginning of {morse_str}")
#             count += check_if_in1(voc, morse_str[len(translated) :])
#             print(count)
#     return count


# # # Recursive, starts with the end of the string
# # def check_if_in2(voc, morse_str):
# #     if morse_str == "":
# #         return 1

# #     count = 0
# #     # for translated in voc.values():
# #     for word, translated in voc.items():
# #         if morse_str.endswith(translated):
# #             print(f"Look for {word}\t ({translated})\tat end of {morse_str}")
# #             count += check_if_in2(voc, morse_str[: -len(translated)])
# #     return count


# # --------------------------------------
# morse_input = input()
# voc_size = int(input())
# vocabulary = {
#     word: "".join(DICO_MORSE[letter] for letter in word) for word in (input().strip() for _ in range(voc_size))
# }
# result = check_if_in1(vocabulary, morse_input)
# print(result)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

# https://www.codingame.com/ide/puzzle/cgx-formatter
# Créer son AST (Abstract Syntax Tree) pour formatter un code CGX.?
# Créer son Tokenizer pour parser un code CGX ?
# Voir lib lark avec Lark et Transformer pour parser et formatter un code CGX ?


# Un ELEMENT peut être de type
#   BLOC
#   TYPE_PRIMITIF
#   CLE_VALEUR.

# BLOC
# Suite d'ELEMENTs séparés par le caractère ';' et entourés par les marqueurs '(' et ')'.

# TYPE_PRIMITIF
#       Un nombre
#       un booléen,
#       null,
#       chaîne de caractères (entourée par le marqueur ' et ')

# CLE_VALEUR
#       Une chaîne de caractères séparée = un BLOC ou un TYPE_PRIMITIF

# CGX : ELEMENT*;
# ELEMENT : BLOC | PRIMITIVE_TYPE | KEY_VALUE
# BLOC : '(' ELEMENT* ')'
# PRIMITIVE_TYPE : NUMBER | BOOLEAN | NULL | STRING
# KEY_VALUE : STRING '=' (BLOC | TYPE_PRIMITIF)
# NUMBER : [0-9]+
# BOOLEAN : true | false
# NULL : ''
# STRING : '\s*[a-zA-Z0-9_ ]+\s*'


# CGX           : ELEMENT* ;
# ELEMENT       : BLOC | PRIMITIVE_TYPE | KEY_VALUE ;

# BLOC          : '(' (ELEMENT (';' ELEMENT)*)? ')' ;     # 0 ou plusieurs ELEMENT
#                                                           S'il y a plusieurs ELEMENT, ils sont séparés par ;
#                                                           ? signifie que la partie ELEMENT (';' ELEMENT)* est optionnelle (un bloc peut être vide).
# PRIMITIVE_TYPE: NUMBER | BOOLEAN | NULL | STRING ;
# KEY_VALUE     : STRING "=" (BLOC | PRIMITIVE_TYPE) ;
# NUMBER        : [0-9]+ ;
# BOOLEAN       : "true" | "false" ;
# NULL          : ;
# STRING        : "'\s*[a-zA-Z0-9_ \-.,]*\s*'"            # attention à l'espace dans les crochets
#                 '[^']*'                                 # une apostrophe ouvrante + une séquence de caractères quelconques, sauf ' (et ce 0 ou plrs fois) + une apostrophe fermante '


# -----------------------------------------------------------------------------
# Not mine
#
# result, quotes, indentation = [''], False, 0
# cgx_lines = "".join([input() for _ in range(int(input()))])
# for idx, char in enumerate(cgx_lines):
#     if idx and cgx_lines[idx-1] == "'":
#         quotes = not quotes
#     if not quotes and char in " \t":
#         continue
#     if not quotes:
#         if char == ')':
#             indentation -= 4
#         if (idx and char in "()") or result[-1] in ['(', ';']:
#             result.append('\n'.ljust(indentation + 1))
#         if char == '(':
#             indentation += 4
#     result.append(char)
# print(''.join(result))

# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_10.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True)


import re


# -----------------------------------------------------------------------------
def tokenizer(cgx):
    # une chaine entre ' OU    une valeur : true | false ||un entier       OU  un séparateur
    # '[^']*' = une apostrophe ouvrante + une séquence de caractères quelconques, sauf ' (et ce 0 ou plrs fois) + une apostrophe fermante '

    # \b → Assure qu'on capture des mots entiers ("true" et non "truevalue").
    # (?: ... ) → Groupe non capturant (pour éviter de stocker dans re.findall).
    # true|false → Détecte exactement "true" ou "false".
    # \d+ → Capture un entier positif (chiffres uniquement, sans signe + ou -).
    # \b → Fin de mot pour éviter des faux positifs.

    # [=;()] = les séparateurs
    token_pattern = r"'[^']*'|\b(?:true|false|\d+)\b|[();=]"

    tokens = re.findall(token_pattern, cgx)
    return [t.encode().decode("unicode_escape") if t.startswith("'") else t for t in tokens]


def parser(tokens):
    stack = [[]]  # Stack to track nested levels
    i = 0

    while i < len(tokens):
        token = tokens[i]

        match token:
            case "(":
                # Début d'un nouveau bloc
                new_block = []
                if stack:
                    # Vérifier si le parent est une clé qui attend un bloc
                    if stack[-1] and isinstance(stack[-1][-1], tuple) and stack[-1][-1][1] == []:
                        stack[-1][-1] = (stack[-1][-1][0], new_block)  # Remplace le bloc vide par le bon
                    else:
                        stack[-1].append(new_block)  # Ajoute au parent
                stack.append(new_block)  # Empiler ce bloc

            case ")":
                if len(stack) > 1:
                    stack.pop()  # Fermer le bloc courant

            case ";":
                stack[-1].append(None)

            case "=":
                # Associer la clé et la valeur
                key = stack[-1].pop()  # Retirer la clé de la pile
                value = tokens[i + 1]  # La valeur suit le "="
                if value == "(":
                    # Si la valeur est un bloc, on l'initialise et le rattache correctement
                    new_block = []
                    stack[-1].append((key, new_block))
                    stack.append(new_block)  # On entre dans le bloc
                else:
                    stack[-1].append((key, value))  # on fait pas .strip(), on garde bien les ' autour
                i += 1  # Avancer d'un token après "="

            case _:
                stack[-1].append(token)  # on fait pas .strip(), on garde bien les ' autour
        i += 1
    return stack[0]  # Retourne l'élément racine


# -----------------------------------------------------------------------------
def formatter(tree, indent=0):

    formatted = []
    spacing = "    " * indent  # Indentation avec 4 espaces

    for element in tree:
        if element is None:  # Correspond à un `;`
            formatted[-1] += ";"  # Ajouter le `;` à la ligne précédente
        elif isinstance(element, tuple):
            key, value = element
            if isinstance(value, list):  # Bloc
                formatted.append(f"{spacing}{key}=")
                formatted.append(f"{spacing}(")
                formatted.append(formatter(value, indent + 1))
                formatted.append(f"{spacing})")
            else:  # Valeur primitive
                formatted.append(f"{spacing}{key}={value}")
        elif isinstance(element, list):  # Bloc sans clé
            formatted.append(f"{spacing}(")
            if len(element):
                formatted.append(formatter(element, indent + 1))
            formatted.append(f"{spacing})")
        else:  # Valeur isolée
            formatted.append(f"{spacing}{element}")

    return "\n".join(formatted)


# -------------------------------------
n = int(input())
cgx = "".join(input() for _ in range(n))
tokens = tokenizer(cgx)
tree = parser(tokens)
formated_cgx = formatter(tree)
print(formated_cgx)


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------

# import re


# # -----------------------------------------------------------------------------
# def tokenizer(cgx):
#     # unechaine entre ', un identifiant, un séparateur
#     # '[^']*' = une apostrophe ouvrante + une séquence de caractères quelconques, sauf ' (et ce 0 ou plrs fois) + une apostrophe fermante '
#     # [a-zA-Z0-9_]+ = une séquence de lettres, de chiffres ou de tirets du bas (au moins 1)
#     # [=;()] = les séparateurs
#     # TODO: faire un test juste avec [0-9] au lieu de [a-zA-Z0-9_]
#     # token_pattern = r"'[^']*'|[a-zA-Z0-9_]+|[();=]"
#     # \b → Assure qu'on capture des mots entiers ("true" et non "truevalue").
#     # (?: ... ) → Groupe non capturant (pour éviter de stocker dans re.findall).
#     # true|false → Détecte exactement "true" ou "false".
#     # \d+ → Capture un entier positif (chiffres uniquement, sans signe + ou -).
#     # \b → Fin de mot pour éviter des faux positifs.
#     token_pattern = r"'[^']*'|\b(?:true|false|\d+)\b|[();=]"

#     tokens = re.findall(token_pattern, cgx)
#     return [t.encode().decode("unicode_escape") if t.startswith("'") else t for t in tokens]


# def parser(tokens):
#     stack = [[]]  # Stack to track nested levels
#     i = 0

#     while i < len(tokens):
#         token = tokens[i]

#         # TODO : mettre un match et des cases
#         # On gère les différents séparateurs possibles

#         if token == "(":
#             # Début d'un nouveau bloc
#             new_block = []
#             if stack:
#                 # Vérifier si le parent est une clé qui attend un bloc
#                 if stack[-1] and isinstance(stack[-1][-1], tuple) and stack[-1][-1][1] == []:
#                     stack[-1][-1] = (stack[-1][-1][0], new_block)  # Remplace le bloc vide par le bon
#                 else:
#                     stack[-1].append(new_block)  # Ajoute au parent
#             stack.append(new_block)  # Empiler ce bloc

#         elif token == ")":
#             if len(stack) > 1:
#                 stack.pop()  # Fermer le bloc courant
#             # The cgx file is supposed to be well formed
#             # else:
#             # raise SyntaxError("Unexpected ')' without matching '('")

#         elif token == ";":
#             # Ajouter un séparateur explicite (None) pour conserver le ;
#             stack[-1].append(None)

#         elif token == "=":
#             # The cgx file is supposed to be well formed
#             # if not stack[-1]:
#             # raise SyntaxError("Unexpected '=' without a preceding key")

#             # Associer la clé et la valeur
#             key = stack[-1].pop()  # Retirer la clé de la pile

#             # The cgx file is supposed to be well formed
#             # if i + 1 >= len(tokens):
#             # raise SyntaxError("Unexpected end of input after '='")

#             value = tokens[i + 1]  # La valeur suit le "="

#             if value == "(":
#                 # Si la valeur est un bloc, on l'initialise et le rattache correctement
#                 new_block = []
#                 stack[-1].append((key, new_block))
#                 stack.append(new_block)  # On entre dans le bloc
#             else:
#                 stack[-1].append((key, value))  # on fait pas .strip(), on garde bien les ' autour

#             i += 1  # Avancer d'un token après "="

#         else:
#             # C'est soit une clé, soit une valeur isolée
#             # stack[-1].append(token.strip("'"))  # Nettoyage des strings
#             stack[-1].append(token)  # on fait pas .strip(), on garde bien les ' autour

#         i += 1

#     # The cgx file is supposed to be well formed
#     # if len(stack) > 1:
#     #     raise SyntaxError("Missing closing ')' at the end of the file")

#     return stack[0]  # Retourne l'élément racine


# # -----------------------------------------------------------------------------
# def formatter(tree, indent=0):
#     """Pretty-print CGX from a nested list structure preserving ';'"""
#     formatted = []
#     spacing = "    " * indent  # Indentation avec 4 espaces

#     for element in tree:
#         if element is None:  # Correspond à un `;`
#             formatted[-1] += ";"  # Ajouter le `;` à la ligne précédente
#         elif isinstance(element, tuple):
#             key, value = element
#             if isinstance(value, list):  # Bloc
#                 # formatted.append(f"{spacing}{key}=(")
#                 formatted.append(f"{spacing}{key}=")
#                 formatted.append(f"{spacing}(")
#                 formatted.append(formatter(value, indent + 1))
#                 formatted.append(f"{spacing})")
#             else:  # Valeur primitive
#                 formatted.append(f"{spacing}{key}={value}")
#         elif isinstance(element, list):  # Bloc sans clé
#             formatted.append(f"{spacing}(")
#             if len(element):
#                 formatted.append(formatter(element, indent + 1))
#             formatted.append(f"{spacing})")
#         else:  # Valeur isolée
#             formatted.append(f"{spacing}{element}")

#     return "\n".join(formatted)


# # -------------------------------------
# n = int(input())
# cgx = "".join(input() for _ in range(n))
# tokens = tokenizer(cgx)
# tree = parser(tokens)
# formated_cgx = formatter(tree)
# print(formated_cgx)

# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

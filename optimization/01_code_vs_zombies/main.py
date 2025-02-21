# https://www.codingame.com/ide/puzzle/code-vs-zombies

# 16_000 x 9_000
# 0,0 is top left
# Ash +1000 every turn
# Zombies +400 every turn go to target including Ash
# Targets are static
# All Zombies closer to 2000 to Ash will die
#

# The zombies move towards their targets.
# Ash moves towards his target.
# Any zombie within a radius of 2000 units is destroyed.
# If a zombie is on a human, it eats him.

# Points:
# Points = 10 * (H-1)^2             . The value of a killed zombie is equal to the number of humans still alive squared and multiplied by 10, not including Ash.
# Points = Sum (Fibo)(N+2)(10 * (H-1)^2) .If several zombies are destroyed in a single turn, the value of the nth zombie killed is multiplied by the (n+2)th term of the Fibonacci sequence (1, 2, 3, 5, 8, etc). So it's in your interest to kill as many zombies as possible in a single turn!

# Round  to the inferior integer

# Ligne 1 : deux entiers x et y séparés par un espace : les coordonnées de votre personnage.
# Ligne 2 : un entier humanCount, le nombre d'humains encore en vie.
#       Les humanCount lignes suivantes : trois entiers séparés par un espace humanId, humanX et humanY, l'identifiant unique et les coordonnées d'un humain.
# Ligne suivante : Un entier zombieCount, le nombre de zombies restant à détruire.
#       Les zombieCount lignes suivantes : cinq entiers séparés par un espace zombieId, zombieX, zombieY, zombieXNext et zombieYNext, l'identifiant unique, les coordonnées courantes et les coordonnées futures d'un zombie.


# Comment décider des sacrifices ?
# Faut utiliser le fait qu'on sait comment fonctionnent les zombies.
# Il vont toujours vers l'humain le plus proche (ash inclus)
# On peut donc les attirer vers Ash si il devient l'humain le plus proche
# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input_01.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")


# -----------------------------------------------------------------------------
import sys

k_Width = 16_000
k_Height = 9_000
k_HashStep = 1_000
k_ZombiesStep = 400
k_DeathRadius = 2_000  # cousin of the Death Ray

while True:
    x, y = [int(i) for i in input().split()]
    humans_count = int(input())
    humans = [list(map(int, input().split())) for _ in range(humans_count)]
    zombies_count = int(input())
    zombies = [list(map(int, input().split())) for _ in range(zombies_count)]

    print(f"Humans : {humans}", file=sys.stderr, flush=True)
    print(f"Zombies : {zombies}", file=sys.stderr, flush=True)
    print("0 0")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()

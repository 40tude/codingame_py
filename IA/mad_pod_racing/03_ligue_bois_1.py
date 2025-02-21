# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.


# # game loop
# while True:
#     # next_checkpoint_x: x position of the next check point
#     # next_checkpoint_y: y position of the next check point
#     # next_checkpoint_dist: distance to the next checkpoint
#     # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
#     x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
#     opponent_x, opponent_y = [int(i) for i in input().split()]

#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#     if next_checkpoint_angle>90 or next_checkpoint_angle<-90:
#         thrust=0
#     else:
#         thrust=100

#     # You have to output the target position
#     # followed by the power (0 <= thrust <= 100)
#     # i.e.: "x y thrust"
#     # print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
#     print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")

# # On peut utiliser le boost une seule fois pendant la course
# # Attention à limite de temps lap 1 = 1000 ms, sinon 75 ms
# #

# import math

# cp_x = -1
# cp_y = -1
# bfirst_lap = True
# cp_set = set()
# cp_list = []
# nb_cp = -1
# bBoost_Used = False
# current_cp=-1
# id_max = -1

# while True:

#     x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
#         int(i) for i in input().split()
#     ]
#     opponent_x, opponent_y = [int(i) for i in input().split()]

#     # Pendant le 1er tour on enregistre les check-points pour pouvoir identifier la plus grande distance entre 2 check-points
#     if bfirst_lap and (next_checkpoint_x != cp_x) and (next_checkpoint_y != cp_y):
#         if ((next_checkpoint_x, next_checkpoint_y)) not in cp_set:
#             cp_set.add((next_checkpoint_x, next_checkpoint_y))
#             cp_list.append([next_checkpoint_x, next_checkpoint_y, 0.0]) # x, y, distance to next cp
#             cp_x = next_checkpoint_x
#             cp_y = next_checkpoint_y
#         else:
#             bfirst_lap = False
#             nb_cp = len(cp_list)  # find the number of cp
#             cp_list = cp_list[-1:] + cp_list[:-1]  # Rotate cp_list by 1 to the right so that start cp becomes first
#             for i in range(nb_cp): # calculate the distance to the next cp
#                 cp_list[i][2] = math.sqrt(
#                     (cp_list[i][0] - cp_list[(i + 1) % nb_cp][0]) ** 2
#                     + (cp_list[i][1] - cp_list[(i + 1) % nb_cp][1]) ** 2
#                 )
#             dmax=-1.0
#             for i in range(nb_cp):
#                 if cp_list[i][2]>dmax:
#                     dmax = cp_list[i][2]
#                     id_max = i

#             # At this point we know the longest distance is between id_max and id_max+1%nb_cp
#             # Since we just finish first lap, we know we go from Start (cp_0) to cp_1
#             current_cp = 0

#     # Mettre le boost si :
#     #       pas encore utilisé
#     #       on est dans l'axe next_checkpoint_angle==0
#     #       la distance est grande (?)
#     #       si on a pas encore atteint 1/2 de la distance
#     if not bBoost_Used and not bfirst_lap:
#         if (current_cp==id_max) and (next_checkpoint_angle == 0) and (next_checkpoint_dist > dmax/2):
#             print(f"{next_checkpoint_x} {next_checkpoint_y} BOOST")
#             bBoost_Used = True
#     else:
#         if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
#             thrust = 0
#         else:
#             thrust = 100
#         print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")


#     if current_cp > -1:
#         current_cp = (current_cp + 1) % nb_cp


# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # On peut utiliser le boost une seule fois pendant la course
# # Attention à limite de temps lap 1 = 1000 ms, sinon 75 ms
# # Y a un gros bug dans le code (detection du 1er tout) mais bizarrement ça marche et j'ai été classé 1er sur le leaderboard devant le Boss

# import sys

# cp_list = set()
# dmax = -1.0
# bFirstLap = True

# while True:

#     x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
#         int(i) for i in input().split()
#     ]
#     opponent_x, opponent_y = [int(i) for i in input().split()]

#     # Pendant le 1er tour on enregistre les check-points pour pouvoir identifier la plus grande distance entre 2 check-points
#     if (next_checkpoint_x, next_checkpoint_y) not in cp_set:
#         cp_set.add((next_checkpoint_x, next_checkpoint_y))
#         if next_checkpoint_dist > dmax:
#             dmax = next_checkpoint_dist
#     else:
#         # On a fini de parcourir les check-points
#         print(f"Next checkpoint    : {next_checkpoint_x} {next_checkpoint_y}", file=sys.stderr, flush=True)
#         print(f"Set of checkpoints : {cp_set}", file=sys.stderr, flush=True)
#         bFirstLap = False

#     if not bFirstLap and next_checkpoint_dist > dmax and next_checkpoint_angle == 0:
#         print(f"{next_checkpoint_x} {next_checkpoint_y} BOOST")
#     else:
#         if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
#             thrust = 0
#         else:
#             thrust = 100
#         print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# On peut utiliser le boost une seule fois pendant la course
# Attention à limite de temps lap 1 = 1000 ms, sinon 75 ms
# BUG fixé : Y a un gros bug dans le code (detection du 1er tout) mais bizarrement ça marche et j'ai été classé 1er sur le leaderboard devant le Boss
# C'est le code que j'aurai dû passer en ligue bois

import sys

cp_list = []
dmax = -1.0
bFirstLap = True

while True:

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()
    ]
    # Un seul opposant
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Pendant le 1er tour on enregistre les check-points pour pouvoir identifier la plus grande distance entre 2 check-points
    if bFirstLap:
        if (next_checkpoint_x, next_checkpoint_y) not in cp_list:
            cp_list.append((next_checkpoint_x, next_checkpoint_y))
            if next_checkpoint_dist > dmax:
                dmax = next_checkpoint_dist
        else:
            # Le check-point est déjà enregistré, on regarde si c'est le premier dans la liste car alors ca veut dire qu'on a fait un tour
            if bFirstLap and len(cp_list) > 1 and cp_list.index((next_checkpoint_x, next_checkpoint_y)) == 0:
                bFirstLap = False
                print(f"Next checkpoint    : {next_checkpoint_x} {next_checkpoint_y}", file=sys.stderr, flush=True)
                print(f"Set of checkpoints : {cp_list}", file=sys.stderr, flush=True)
                print(f"Dist Max           : {dmax}", file=sys.stderr, flush=True)

    if not bFirstLap and next_checkpoint_dist > dmax and next_checkpoint_angle == 0:
        print(f"{next_checkpoint_x} {next_checkpoint_y} BOOST")
        print(f"Dist : {next_checkpoint_dist}", file=sys.stderr, flush=True)
    else:
        if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
            thrust = 0
        else:
            thrust = 100
        print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
        print(f"Dist : {next_checkpoint_dist}", file=sys.stderr, flush=True)

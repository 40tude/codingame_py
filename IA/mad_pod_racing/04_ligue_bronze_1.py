# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # -----------------------------------------------------------------------------
# # On peut utiliser le boost une seule fois pendant la course
# # Attention à limite de temps lap 1 = 1000 ms, sinon 75 ms
# # J'essaie de diminuer la vitesse à l'approche du checkpoint pour eviter l'overshoot
# import sys
# import math

# k_Angle = 90
# k_MinThrottle = 0
# k_FullThrottle = 100

# cp_list = []
# dmax = -1.0
# bFirstLap = True

# while True:
#     x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
#         int(i) for i in input().split()
#     ]
#     opponent_x, opponent_y = [int(i) for i in input().split()]

#     # Pendant le 1er tour on enregistre les check-points pour pouvoir identifier la plus grande distance entre 2 check-points
#     if bFirstLap :
#         if (next_checkpoint_x, next_checkpoint_y) not in cp_list:
#             cp_list.append((next_checkpoint_x, next_checkpoint_y))
#             if next_checkpoint_dist > dmax:
#                 dmax = next_checkpoint_dist
#         else:
#             # Le check-point est déjà enregistré, on regarde si c'est le premier dans la liste car alors ca veut dire qu'on a fait un tour
#             if bFirstLap and len(cp_list)>1 and cp_list.index((next_checkpoint_x, next_checkpoint_y))==0:
#                 bFirstLap = False
#                 print(f"Next checkpoint    : {next_checkpoint_x} {next_checkpoint_y}", file=sys.stderr, flush=True)
#                 print(f"Set of checkpoints : {cp_list}", file=sys.stderr, flush=True)
#                 print(f"Dist Max           : {dmax}", file=sys.stderr, flush=True)


#     if not bFirstLap and next_checkpoint_dist > dmax and next_checkpoint_angle == 0:
#         print(f"{next_checkpoint_x} {next_checkpoint_y} BOOST")
#         print(f"Dist : {next_checkpoint_dist}", file=sys.stderr, flush=True)
#     else:
#         if next_checkpoint_angle > k_Angle or next_checkpoint_angle < -k_Angle:
#             angle = k_Angle
#         else:
#             angle = abs(next_checkpoint_angle)
#             angle = angle % k_Angle

#         angle = angle/180*math.pi
#         thrust = int((k_FullThrottle-k_MinThrottle)*math.cos(angle)+k_MinThrottle)

#         print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
#         print(f"Dist : {next_checkpoint_dist}", file=sys.stderr, flush=True)
#         print(f"Thrust : {thrust}", file=sys.stderr, flush=True)
#         print(f"Angle : {next_checkpoint_angle}", file=sys.stderr, flush=True)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# On peut utiliser le boost une seule fois pendant la course
# Attention à limite de temps lap 1 = 1000 ms, sinon 75 ms
# Version PID
# J'essaie de diminuer la vitesse à l'approche du checkpoint pour eviter l'overshoot

# PID
# Augmenter légèrement kp de dist_pid pour que le bot accélère plus rapidement.
# Diminuer ki si le bot accumule trop d'erreur dans le temps et devient instable.
# Augmenter kd pour éviter une sur-correction et réduire les oscillations.

# Méthode Ziegler-Nichols
# ki et kd à 0, ajuste kp jusqu'à ce que le bot commence à osciller.
# Note cette valeur critique Kp_crit et la période T_crit de l'oscillation.
# Applique ces formules :
# Kp = 0.6 * Kp_crit
# Ki = 1.2 * Kp_crit / T_crit
# Kd = 0.075 * Kp_crit * T_crit

# Si le bot est trop lent → Augmenter Kp et Kd du dist_pid
# Si le bot oscille trop ou tourne trop brusquement → Réduire Kp et augmenter Kd du angle_pid
# Si le bot reste trop longtemps à vitesse faible → Augmenter Ki du dist_pid

import sys
import time

bStart = True


class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # Proportional coefficient
        self.ki = ki  # Integral coefficient
        self.kd = kd  # Derivative coefficient

        self.previous_error = 0
        self.integral = 0
        self.last_time = time.time()

    def compute(self, error):
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        self.integral += error * delta_time
        derivative = (error - self.previous_error) / delta_time if delta_time > 0 else 0
        self.previous_error = error

        return self.kp * error + self.ki * self.integral + self.kd * derivative


# PID controller parameters
angle_pid = PIDController(kp=2.0, ki=0.01, kd=0.5)

# dist_pid = PIDController(kp=0.1, ki=0.005, kd=0.02)
dist_pid = PIDController(kp=0.6, ki=0.002, kd=0.05)

while True:
    # Read inputs
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()
    ]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # dynamic_kp = 0.2 + (0.8 * (1 - abs(next_checkpoint_angle) / 180))
    # dist_pid.kp = dynamic_kp

    # Compute PID output for angle correction
    angle_correction = angle_pid.compute(next_checkpoint_angle)

    # Compute PID output for distance correction
    distance_correction = dist_pid.compute(next_checkpoint_dist)

    # Ajuster le thrust en fonction :
    # De l'erreur angulaire (angle_correction) : plus le virage est serré, plus la puissance doit être réduite pour éviter des mouvements brusques.
    # De l'erreur de distance (distance_correction) : plus la cible est loin, plus la puissance peut être augmentée pour accélérer.
    # Si bot trop lent :
    #       diminuer le facteur de abs(angle_correction) : 0.5 initial
    #       augmenter le facteur de distance_correction  : 0.1 initial
    thrust = int(max(30, min(100, 100 - abs(angle_correction) * 0.4 + distance_correction * 0.2)))

    # Print the command for the game
    if bStart:
        print(f"{next_checkpoint_x} {next_checkpoint_y} BOOST")
        bStart = False
    else:
        print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")

    print(f"Dist : {next_checkpoint_dist}", file=sys.stderr, flush=True)
    print(f"Thrust : {thrust}", file=sys.stderr, flush=True)
    print(f"Angle : {next_checkpoint_angle}", file=sys.stderr, flush=True)

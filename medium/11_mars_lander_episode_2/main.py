# https://www.codingame.com/training/medium/mars-lander-episode-2

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
# J'ai déjà une solution en C++ je refait le puzzle avec un PID en Python pour le fun
# Pour le PID voir IA\mad_pod_racing\04_ligue_bronze_1.py

# Le jeu modélise une chute libre sans atmosphère.
# La gravité sur Mars est de 3,711 m/s².
# Pour une puissance des fusées de X, on génère une poussée équivalente à X m/s² et on consomme X litres de fuel.
# Il faut donc une poussée de 4 quasi verticale pour compenser la gravité de Mars.

# Pour qu’un atterrissage soit réussi, la capsule doit :
#       atterrir sur un sol plat
#       atterrir dans une position verticale (angle = 0°)
#       la vitesse verticale doit être limitée ( ≤ 40 m/s en valeur absolue)
#       la vitesse horizontale doit être limitée ( ≤ 20 m/s en valeur absolue)


# La zone fait 7000m de large et 3000m de haut.
# Pour ce niveau, Mars Lander
#       se situe AU DESSUS de la zone d’atterrissage,
#       en position verticale,
#       avec aucune vitesse initiale.
# Il existe une unique zone d'atterrissage plane sur la surface de Mars et elle mesure au moins 1000 mètres de large.


import sys
import time
import math

def clamp(value, min_val, max_val):
    return round(max(min_val, min(value, max_val)))

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
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


kTarget_VSpeed = -40  # Target vertical speed for landing

N = int(input())  # Read surface points
surfaces = [tuple(map(int, input().split())) for _ in range(N)]

# Find landing zone
landing_x, landing_y = 0, 0
for i in range(N - 1):
    if surfaces[i][1] == surfaces[i + 1][1]:  # The flat surface found
        landing_x = (surfaces[i][0] + surfaces[i + 1][0]) // 2
        landing_y = surfaces[i][1]
        break

vertical_speed_pid = PIDController(kp=1, ki=0, kd=0.5)  
rot_pid = PIDController(kp=-1.2, ki=0, kd=0.6)  

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Phase 1 : Correct horizontally, set the lander over the landing spot
    # Thrust set to 4 and angle small
    vertical=False
    while not vertical:
        dx = landing_x - x 
        print(f"dx = {dx}", file=sys.stderr, flush=True)

        dx_correction = rot_pid.compute(dx)
        print(f"dx_correction = {dx_correction}", file=sys.stderr, flush=True)

        rotation_angle = clamp(dx_correction, -10, 10)
        print(f"Rotation = {rotation_angle}", file=sys.stderr, flush=True)
    
        print(f"{rotation_angle} {4}")
        if (dx=0 and abs(vx)<20):
            vertical=True


    # Phase 2 : Correct vertically, land the lander
    # See mars lander 1

    # print(f"v_speed = {v_speed}", file=sys.stderr, flush=True)
    # v_error = kTarget_VSpeed - v_speed
    # v_speed_correction = vertical_speed_pid.compute(v_error)

    # dx = landing_x - x 
    # print(f"dx = {dx}", file=sys.stderr, flush=True)

    # dx_correction = rot_pid.compute(dx)
    # print(f"dx_correction = {dx_correction}", file=sys.stderr, flush=True)

    # rotation_angle = clamp(dx_correction, -5, 5)
    # print(f"Rotation = {rotation_angle}", file=sys.stderr, flush=True)
    
    # thrust = clamp(v_speed_correction / math.cos(math.radians(rotation_angle)), 0, 4)
    # print(f"{rotation_angle} {thrust}")




# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# import sys
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs", file=sys.stderr, flush=True))

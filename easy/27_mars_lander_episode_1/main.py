# https://www.codingame.com/ide/puzzle/mars-lander-episode-1

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

# import sys
# import time

# class PIDController:
#     def __init__(self, kp, ki, kd):
#         self.kp = kp  # Proportional coefficient
#         self.ki = ki  # Integral coefficient
#         self.kd = kd  # Derivative coefficient

#         self.previous_error = 0
#         self.integral = 0
#         self.last_time = time.time()

#     def compute(self, error):
#         current_time = time.time()
#         delta_time = current_time - self.last_time
#         self.last_time = current_time

#         self.integral += error * delta_time
#         derivative = (error - self.previous_error) / delta_time if delta_time > 0 else 0
#         self.previous_error = error

#         return self.kp * error + self.ki * self.integral + self.kd * derivative

# clamp = lambda x: int(max(0.0, min(x, 4.0)))

# N = int(input()) # number of segments in the surface of Mars
# surfaces = [tuple(map(int, input().split())) for _ in range(N)]
# print(surfaces, file=sys.stderr, flush=True)

# # kp = 2.0 : Réaction plus douce.
# # ki = 0.0 : On ne veut pas d'effet mémoire qui pourrait déséquilibrer la descente.
# # kd = 4.0 : Toujours un effet dérivé fort pour une réaction rapide aux variations.
# # vspeed_pid = PIDController(kp=3.5, ki=-0.03, kd=4.5)
# vspeed_pid = PIDController(kp=4.0, ki=0.0, kd=3.0)

# while True:
#     # h_speed: the horizontal speed (in m/s), can be negative.
#     # v_speed: the vertical speed (in m/s), can be negative.
#     # fuel: the quantity of remaining fuel in liters.
#     # rotate: the rotation angle in degrees (-90 to 90).
#     # power: the thrust power (0 to 4).
#     x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

#     target_speed = -39
#     vspeed_correction = vspeed_pid.compute(target_speed-v_speed)
#     cmd = clamp(vspeed_correction)

#     # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
#     print(f"0 {cmd}")


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

# import sys
# import time

# class PIDController:
#     def __init__(self, kp, ki, kd):
#         self.kp = kp
#         self.ki = ki
#         self.kd = kd
#         self.previous_error = 0
#         self.integral = 0
#         self.last_time = time.time()

#     def compute(self, error):
#         current_time = time.time()
#         delta_time = current_time - self.last_time
#         self.last_time = current_time

#         self.integral += error * delta_time
#         derivative = (error - self.previous_error) / delta_time if delta_time > 0 else 0
#         self.previous_error = error

#         return self.kp * error + self.ki * self.integral + self.kd * derivative

# def clamp(x):
#     return int(max(0.0, min(x, 4.0)))

# # Read Mars surface
# N = int(input())
# surfaces = [tuple(map(int, input().split())) for _ in range(N)]
# print(surfaces, file=sys.stderr, flush=True)

# # Find the flat landing zone
# landing_y = 0
# flat_start, flat_end = 0, 0
# for i in range(N - 1):
#     if surfaces[i][1] == surfaces[i + 1][1]:  # Same Y => flat area
#         flat_start, flat_end = surfaces[i][0], surfaces[i + 1][0]
#         landing_y = surfaces[i][1]
#         break
# print(f"Landing y = {landing_y}", file=sys.stderr, flush=True)

# vspeed_pid = PIDController(kp=3.0, ki=0.0, kd=4.0)  # Adjusted PID values

# while True:
#     x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

#     distance_to_ground = y - landing_y  # Remaining altitude

#     # Define dynamic speed target based on altitude
#     if distance_to_ground > 1000:
#         target_speed = -60
#     elif distance_to_ground > 500:
#         target_speed = -55
#     elif distance_to_ground > 250:
#         target_speed = -50
#     elif distance_to_ground > 125:
#         target_speed = -45
#     else:
#         target_speed = -35  # Smooth final landing

#     vspeed_correction = vspeed_pid.compute(target_speed - v_speed)
#     cmd = clamp(vspeed_correction)

#     print(f"0 {cmd}")


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

# import sys
# import time

# class PIDController:
#     def __init__(self, kp, ki, kd):
#         self.kp = kp
#         self.ki = ki
#         self.kd = kd
#         self.previous_error = 0
#         self.integral = 0
#         self.last_time = time.time()

#     def compute(self, error):
#         current_time = time.time()
#         delta_time = current_time - self.last_time
#         self.last_time = current_time

#         self.integral += error * delta_time
#         derivative = (error - self.previous_error) / delta_time if delta_time > 0 else 0
#         self.previous_error = error

#         return self.kp * error + self.ki * self.integral + self.kd * derivative

# def clamp(x):
#     return int(max(0.0, min(x, 4.0)))

# N = int(input())
# surfaces = [tuple(map(int, input().split())) for _ in range(N)]
# print(surfaces, file=sys.stderr, flush=True)

# # Find the flat landing zone altitude.
# # Keep in mind the landing zone is unique and under the lander
# flat_start, flat_end = 0, 0
# landing_y = 0

# for i in range(N - 1):
#     if surfaces[i][1] == surfaces[i + 1][1]:  # Flat area
#         flat_start, flat_end = surfaces[i][0], surfaces[i + 1][0]
#         landing_y = surfaces[i][1]
#         break

# # vspeed_pid = PIDController(kp=2.5, ki=0.0, kd=4.0)  # PID to maintain -40 m/s
# vspeed_pid = PIDController(kp=4.0, ki=0, kd=0.0)  # PID to maintain -40 m/s

# while True:
#     x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

#     distance_to_ground = y - landing_y  # Remaining altitude
#     target_speed = -39  # We want to reach and maintain -40 m/s

#     if v_speed > target_speed:
#         # If the lander is falling too slowly, disable thrust to speed up
#         cmd = 0
#     else:
#         # Use PID to maintain -40 m/s
#         vspeed_correction = vspeed_pid.compute(target_speed - v_speed)
#         cmd = clamp(vspeed_correction)

#     # Smooth landing adjustment
#     # # Time 6:05 and Fuel = 295
#     # vspeed_pid = PIDController(kp=4.0, ki=0.0, kd=2.0)  # PID to maintain -40 m/s
#     # if distance_to_ground < 500:
#     #     target_speed = max(-40, -20 + (distance_to_ground / 25))  # Gradually slow down
#     #     vspeed_correction = vspeed_pid.compute(target_speed - v_speed)
#     #     cmd = clamp(vspeed_correction)

#     # Time 6:04 and Fuel = 302
#     print(f"0 {cmd}")


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

# import sys
# import time

# class PIDController:
#     def __init__(self, kp, ki, kd):
#         self.kp = kp
#         self.ki = ki
#         self.kd = kd
#         self.previous_error = 0
#         self.integral = 0
#         self.last_time = time.time()

#     def compute(self, error):
#         current_time = time.time()
#         delta_time = current_time - self.last_time
#         self.last_time = current_time

#         self.integral += error * delta_time
#         derivative = (error - self.previous_error) / delta_time if delta_time > 0 else 0
#         self.previous_error = error

#         return self.kp * error + self.ki * self.integral + self.kd * derivative

# def clamp(x):
#     return int(max(0.0, min(x, 4.0)))

# N = int(input())
# surfaces = [tuple(map(int, input().split())) for _ in range(N)]
# print(surfaces, file=sys.stderr, flush=True)

# # Find the flat landing zone altitude.
# # The landing zone is unique and under the lander
# flat_start, flat_end = 0, 0
# landing_y = 0

# for i in range(N - 1):
#     if surfaces[i][1] == surfaces[i + 1][1]:  # Flat area
#         # flat_start, flat_end = surfaces[i][0], surfaces[i + 1][0]
#         landing_y = surfaces[i][1]
#         break

# vspeed_pid = PIDController(kp=4.0, ki=0, kd=0.0)  # PID to maintain -40 m/s
# target_speed = -39  # We want to reach and maintain -40 m/s

# while True:
#     x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

#     # distance_to_ground = y - landing_y  # Remaining altitude

#     if v_speed > target_speed:
#         # If the lander is falling too slowly, disable thrust to speed up
#         cmd = 0
#     else:
#         # Use PID to maintain speed -40 m/s
#         vspeed_correction = vspeed_pid.compute(target_speed - v_speed)
#         cmd = clamp(vspeed_correction)

#     # Time 6:04 and Fuel = 302
#     print(f"0 {cmd}")


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


import time


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


kTarget_Speed = -39  # We want to reach and maintain -40 m/s
N = int(input())
surfaces = [tuple(map(int, input().split())) for _ in range(N)]
vspeed_pid = PIDController(kp=4.0, ki=0, kd=0.0)  # PID to maintain -40 m/s
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if v_speed > kTarget_Speed:
        cmd = 0
    else:
        vspeed_correction = vspeed_pid.compute(kTarget_Speed - v_speed)
        cmd = (lambda x: round(max(0.0, min(x, 4.0))))(vspeed_correction)
    print(f"0 {cmd}")  # Time 6:04 and Fuel = 302


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

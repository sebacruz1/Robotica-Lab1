"""controlador_test_automaticos controller."""
import math
from controller import Robot, AnsiCodes

robot    = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor  = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Parámetros (medidas en metros, velocidad en rad/s)
L        = 0.052    # distancia entre ruedas
r        = 0.0205   # radio de rueda
MAX_SPEED = 6.28    # velocidad máxima

# Colores de terminal
RED = AnsiCodes.RED_FOREGROUND
RESET  = AnsiCodes.RESET

# v = (vr + vl) / 2 -> velocidad lineal  [m/s]
# ω = (vr − vl) / L -> velocidad angular [rad/s]

def v_robot(vl, vr):
    # Velocidad lineal del robot
    return ((vr + vl) / 2) * r

def omega_robot(vl, vr):
    # Velocidad angular del robot
    return ((vr - vl) * r) / L

def ms_avanzar(vl, vr, distancia_m):
    # Tiempo en ms para recorrer una distancia
    v = v_robot(vl, vr)
    return int(abs(distancia_m / v) * 1000) if v != 0 else 0

def ms_rotar(vl, vr, angulo_rad):
    # Tiempo en ms para rotar un ángulo exacto
    w = omega_robot(vl, vr)
    return int(abs(angulo_rad / w) * 1000) if w != 0 else 0

# Velocidades base
V  = 4.0   # velocidad recta
VG = 3.0   # velocidad de rotación en el lugar
PAUSA = (0.0, 0.0, 800, "pausa")

sequence = [

    # Experimento 1: vr == vl -> línea recta
    (V, V,
     ms_avanzar(V, V, 0.30),
     "Exp 1, Línea recta (vr == vl)"),
    PAUSA,

    # Experimento 2: vr != vl -> trayectoria curva
    (2.0, 5.0,
     2500,
     "Exp 2, Curva (vr != vl)"),
    PAUSA,

    # Experimento 3: vr == -vl -> rotación en el lugar
    (VG, -VG,
     ms_rotar(VG, -VG, math.pi),
     "Exp 3, Rotación 180° (vr == -vl)"),
    PAUSA,

    # Desafío 1: línea recta
    (V, V,
     ms_avanzar(V, V, 0.40),
     "Desafío, Línea recta 40 cm"),
    PAUSA,

    # Desafío 2: curva
    (2.0, 5.0,
     3500,
     "Desafío, Curva pronunciada"),
    PAUSA,

    # Desafío 3: círculo completo
    (2.0, 4.0,
     ms_rotar(2.0, 4.0, 2 * math.pi),
     "Desafío, Círculo completo"),
    PAUSA,

    # Desafío 4: cuadrado
    (V,  V,   ms_avanzar(V,  V,   0.20), "Cuadrado, lado 1"),
    (VG, -VG, ms_rotar(VG, -VG, math.pi / 2), "Cuadrado, giro 90°"),
    (V,  V,   ms_avanzar(V,  V,   0.20), "Cuadrado, lado 2"),
    (VG, -VG, ms_rotar(VG, -VG, math.pi / 2), "Cuadrado, giro 90°"),
    (V,  V,   ms_avanzar(V,  V,   0.20), "Cuadrado, lado 3"),
    (VG, -VG, ms_rotar(VG, -VG, math.pi / 2), "Cuadrado, giro 90°"),
    (V,  V,   ms_avanzar(V,  V,   0.20), "Cuadrado, lado 4"),
    (VG, -VG, ms_rotar(VG, -VG, math.pi / 2), "Cuadrado, giro 90°"),
    PAUSA,

    (0.0, 0.0, 500, "Todos los experimentos completados"),
]

# Loop principal
step_index = 0
elapsed_ms = 0

print("E-PUCK Secuencias automáticas")

while robot.step(timestep) != -1:

    if step_index >= len(sequence):
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        break

    vl, vr, duration, label = sequence[step_index]

    if elapsed_ms == 0:
        left_motor.setVelocity(vl)
        right_motor.setVelocity(vr)

        v = v_robot(vl, vr)
        w = omega_robot(vl, vr)

        print(f"{RED}[{step_index + 1}/{len(sequence)}] {label}")
        print(f"  vl = {vl:+.2f} rad/s  |  vr = {vr:+.2f} rad/s")
        print(f"  v  = {v:+.4f} m/s    |  ω  = {w:+.4f} rad/s")
        print(f"  duración = {duration / 1000} s{RESET}")

    elapsed_ms += timestep
    if elapsed_ms >= duration:
        elapsed_ms = 0
        step_index += 1

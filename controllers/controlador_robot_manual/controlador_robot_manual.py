"""controlador_robot_manual controller."""
from controller import Robot, Keyboard

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Leer desde el teclado
kb = robot.getKeyboard()
kb.enable(timestep)

left_motor  = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Velocidad máxima del epuck
MAX_SPEED    = 6.28
LINEAR_STEP  = 1.0 # Cambio en la velocidad por presion en la flecha UP o DOWN
ANGULAR_STEP = 0.5 # Cambio en la velocidad hacia los lados por presion en LEFT o RIGHT

# Prender leds para diferenciar los epucks
leds = [robot.getDevice(f'led{i}') for i in range(8)]
for led in leds:
    led.set(1)

linear  = 0.0
angular = 0.0
prev_keys   = set()
prev_speeds = (0.0, 0.0)

while robot.step(timestep) != -1:
    # leer teclas
    keys = set()
    key = kb.getKey()
    while key != -1:
        keys.add(key)
        key = kb.getKey()

    just_pressed = keys - prev_keys # para evitar errores al mantener apretado

    if Keyboard.UP in just_pressed:
        linear = min(linear + LINEAR_STEP, MAX_SPEED)
    if Keyboard.DOWN in just_pressed:
        linear = max(linear - LINEAR_STEP, -MAX_SPEED)
    if Keyboard.LEFT in just_pressed:
        angular = min(angular + ANGULAR_STEP, MAX_SPEED)
    if Keyboard.RIGHT in just_pressed:
        angular = max(angular - ANGULAR_STEP, -MAX_SPEED)

    # Tecla espacio para frenar todo
    if ord(' ') in just_pressed:
        linear  = 0.0
        angular = 0.0

    prev_keys = keys

    # Calcular velocidades
    left_speed  = linear - angular
    right_speed = linear + angular
    left_speed  = max(-MAX_SPEED, min(MAX_SPEED, left_speed))
    right_speed = max(-MAX_SPEED, min(MAX_SPEED, right_speed))

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    if (left_speed, right_speed) != prev_speeds:
        print(f"Left:   {left_speed:+.2f}  |  Right:   {right_speed:+.2f}")
        print("Flecha Up / Flecha Down = velocidad  |  Flecha Left / Right = giro  |  SPACE freno \n")
        prev_speeds = (left_speed, right_speed)

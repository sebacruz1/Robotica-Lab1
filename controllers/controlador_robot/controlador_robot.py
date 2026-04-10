"""controlador_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# manejar por teclado
kb = robot.getKeyboard()
kb.enable(timestep)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

prev_speeds = (0, 0)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    linear = 0.0   # adelante/atras
    angular = 0.0  # izquierda/derecha

    keys = set()
    key = kb.getKey()
    while key != -1:
        keys.add(key)
        key = kb.getKey()

    if Keyboard.UP in keys:
        linear += 5.0
    if Keyboard.DOWN in keys:
        linear -= 5.0
    if Keyboard.LEFT in keys:
        angular += 2.0
    if Keyboard.RIGHT in keys:
        angular -= 2.0

    left_speed  = linear - angular
    right_speed = linear + angular

    max_speed = 5.0
    left_speed  = max(-max_speed, min(max_speed, left_speed))
    right_speed = max(-max_speed, min(max_speed, right_speed))

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    if (left_speed, right_speed) != prev_speeds:
        print("\033c", end="")
        print(f"Left: {left_speed:+.2f}  |  Right: {right_speed:+.2f}")
        prev_speeds = (left_speed, right_speed)

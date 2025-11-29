import time
import math
import os

car_x = 0        # Car position
car_y = 0        # Car height on hill
speed = 1        # Car speed
jump = 0         # Jump force
gravity = -0.2   # Gravity value

def hill(x):
    return int(5 * math.sin(x * 0.3))   # Hill pattern

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Hill height
    ground = hill(car_x)

    # Apply jump
    if jump != 0:
        car_y += jump
        jump += gravity
        if car_y <= ground:
            car_y = ground
            jump = 0

    # Car draw line
    print("\n" * (10 - int(car_y)))

    print(" " * car_x + "🚗")   # Car

    print("\n" * (10)) 

    # Controls info
    print("Controls: A = Left | D = Right | SPACE = Jump | Q = Quit")
    cmd = input("Enter: ").lower()

    if cmd == "a":
        car_x = max(0, car_x - speed)
    elif cmd == "d":
        car_x += speed
    elif cmd == " ":
        if jump == 0:      # Only jump if on ground
            jump = 3
    elif cmd == "q":
        break

    time.sleep(0.1)

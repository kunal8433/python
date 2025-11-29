import pygame
import sys
import math

pygame.init()

# Window setup
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Hill & Climb Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (200, 30, 30)
BLACK = (0, 0, 0)

# Car settings
car_x = 100
car_y = 300
car_speed = 0
gravity = 0.3
jump_force = -8
on_ground = False

# Hill function
def hill_y(x):
    return 250 + 80 * math.sin(x * 0.01)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Car movement left-right
    if keys[pygame.K_RIGHT]:
        car_x += 3
    if keys[pygame.K_LEFT]:
        car_x -= 3

    # Jump
    if keys[pygame.K_SPACE] and on_ground:
        car_speed = jump_force

    # Apply gravity
    car_speed += gravity
    car_y += car_speed

    # Hill collision
    ground_y = hill_y(car_x)
    if car_y > ground_y - 20:
        car_y = ground_y - 20
        car_speed = 0
        on_ground = True
    else:
        on_ground = False

    # Drawing
    screen.fill(WHITE)

    # Draw hill
    points = []
    for x in range(0, WIDTH):
        points.append((x, hill_y(x)))
    pygame.draw.lines(screen, GREEN, False, points, 5)

    # Draw car (circle)
    pygame.draw.circle(screen, RED, (int(car_x), int(car_y)), 20)

    # Text
    font = pygame.font.SysFont(None, 30)
    txt = font.render("Press ← → to move, SPACE to jump", True, BLACK)
    screen.blit(txt, (20, 20))

    pygame.display.update()
    clock.tick(60)

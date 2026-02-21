# ONE CAR + ROAD + COIN + SCORE + keyboard + real joystick
# pip install pygame

import pygame
import random
import sys

pygame.init()
pygame.joystick.init()

# --------------------
# Window
# --------------------
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One Car Road Game - Coin & Score")

clock = pygame.time.Clock()

# --------------------
# Joystick
# --------------------
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# --------------------
# Colors
# --------------------
ROAD  = (60, 60, 60)
GRASS = (20, 120, 20)
WHITE = (255, 255, 255)
RED   = (200, 0, 0)
YELLOW = (255, 215, 0)

# --------------------
# Road
# --------------------
road_x = 90
road_w = WIDTH - 180

line_w = 10
line_h = 40
line_gap = 30

lines = []
y = 0
while y < HEIGHT:
    lines.append(pygame.Rect(WIDTH//2 - line_w//2, y, line_w, line_h))
    y += line_h + line_gap

road_speed = 6

# --------------------
# Car (only one)
# --------------------
car_w, car_h = 50, 80
car = pygame.Rect(WIDTH//2 - car_w//2, HEIGHT - 120, car_w, car_h)
speed = 10

# --------------------
# Coin
# --------------------
coin_size = 25
coin = pygame.Rect(
    random.randint(road_x + 5, road_x + road_w - coin_size - 5),
    random.randint(-300, -50),
    coin_size,
    coin_size
)

coin_speed = 8

# --------------------
# Score
# --------------------
score = 0
font = pygame.font.SysFont(None, 32)

# --------------------
# Game loop
# --------------------
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx = 0
    dy = 0

    # keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx -= speed
    if keys[pygame.K_RIGHT]:
        dx += speed
    if keys[pygame.K_UP]:
        dy -= speed
    if keys[pygame.K_DOWN]:
        dy += speed

    # joystick
    if joystick:
        ax = joystick.get_axis(0)
        ay = joystick.get_axis(1)

        if abs(ax) > 0.2:
            dx += int(ax * speed)
        if abs(ay) > 0.2:
            dy += int(ay * speed)

    car.x += dx
    car.y += dy

    # stay inside road
    if car.left < road_x:
        car.left = road_x
    if car.right > road_x + road_w:
        car.right = road_x + road_w
    if car.top < 0:
        car.top = 0
    if car.bottom > HEIGHT:
        car.bottom = HEIGHT

    # move road lines
    for l in lines:
        l.y += road_speed
        if l.top > HEIGHT:
            l.y = -line_h

    # move coin
    coin.y += coin_speed
    if coin.top > HEIGHT:
        coin.x = random.randint(road_x + 10, road_x + road_w - coin_size - 10)
        coin.y = random.randint(-200, -40)

    # collect coin
    if car.colliderect(coin):
        score += 1
        coin.x = random.randint(road_x + 10, road_x + road_w - coin_size - 10)
        coin.y = random.randint(-200, -40)

    # --------------------
    # Draw
    # --------------------
    screen.fill(GRASS)

    # road
    pygame.draw.rect(screen, ROAD, (road_x, 0, road_w, HEIGHT))

    # borders
    pygame.draw.line(screen, WHITE, (road_x, 0), (road_x, HEIGHT), 4)
    pygame.draw.line(screen, WHITE, (road_x + road_w, 0), (road_x + road_w, HEIGHT), 4)

    # center lines
    for l in lines:
        pygame.draw.rect(screen, WHITE, l)

    # coin
    pygame.draw.ellipse(screen, YELLOW, coin)

    # car
    pygame.draw.rect(screen, RED, car)

    # score
    text = font.render(f"Score : {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()
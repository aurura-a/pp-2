import pygame
import sys
import random
import time

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 10
FramePerSec = pygame.time.Clock()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and Food initialization
snake_pos = [[100, 100], [80, 100], [60, 100]]
snake_direction = "RIGHT"
snake_speed = CELL_SIZE

food_pos = [random.randrange(0, SCREEN_WIDTH, CELL_SIZE), random.randrange(
    0, SCREEN_HEIGHT, CELL_SIZE)]
food_weight = random.choice([1, 2, 3])
food_timer = time.time()
food_lifespan = 5  # Food disappears after 5 seconds

score = 0


def spawn_food():
    global food_pos, food_weight, food_timer
    food_pos = [random.randrange(0, SCREEN_WIDTH, CELL_SIZE), random.randrange(
        0, SCREEN_HEIGHT, CELL_SIZE)]
    food_weight = random.choice([1, 2, 3])
    food_timer = time.time()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    head_x, head_y = snake_pos[0]
    if snake_direction == "UP":
        head_y -= snake_speed
    elif snake_direction == "DOWN":
        head_y += snake_speed
    elif snake_direction == "LEFT":
        head_x -= snake_speed
    elif snake_direction == "RIGHT":
        head_x += snake_speed

    # Insert new head and remove tail if no food is eaten
    new_head = [head_x, head_y]
    if new_head == food_pos:
        score += food_weight  # Increase score by food weight
        spawn_food()
    else:
        snake_pos.pop()

    # Check for collisions
    if new_head in snake_pos or head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        running = False

    snake_pos.insert(0, new_head)

    # Check if food should disappear
    if time.time() - food_timer > food_lifespan:
        spawn_food()

    # Drawing
    DISPLAYSURF.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(DISPLAYSURF, GREEN, pygame.Rect(
            pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(
        food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()

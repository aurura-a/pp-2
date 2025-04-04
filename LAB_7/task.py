import pygame
import sys

# Initializing pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
BALL_RADIUS = 25
BALL_X = SCREEN_WIDTH // 2
BALL_Y = SCREEN_HEIGHT // 2
BALL_SPEED = 20

# Screen setup
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and BALL_Y - BALL_SPEED >= BALL_RADIUS:
                BALL_Y -= BALL_SPEED
            elif event.key == pygame.K_DOWN and BALL_Y + BALL_SPEED <= SCREEN_HEIGHT - BALL_RADIUS:
                BALL_Y += BALL_SPEED
            elif event.key == pygame.K_LEFT and BALL_X - BALL_SPEED >= BALL_RADIUS:
                BALL_X -= BALL_SPEED
            elif event.key == pygame.K_RIGHT and BALL_X + BALL_SPEED <= SCREEN_WIDTH - BALL_RADIUS:
                BALL_X += BALL_SPEED

    # Drawing
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, RED, (BALL_X, BALL_Y), BALL_RADIUS)

    pygame.display.flip()

pygame.quit()
sys.exit()

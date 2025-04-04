import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLUE = (255, 255, 255), (0, 255,
                                            0), (255, 0, 0), (0, 0, 255)
SNAKE_SPEED = 10

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and food initialization
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Game variables
score = 0
level = 1
speed = SNAKE_SPEED
running = True

# Function to generate new food position


def generate_food():
    while True:
        new_food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if new_food not in snake:
            return new_food


# Game loop
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions with walls
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
        break

    # Check for collisions with itself
    if new_head in snake:
        running = False
        break

    snake.insert(0, new_head)

    # Check for food collision
    if new_head == food:
        score += 1
        if score % 4 == 0:
            level += 1
            speed += 2  # Increase speed every level
        food = generate_food()
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Draw score and level
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

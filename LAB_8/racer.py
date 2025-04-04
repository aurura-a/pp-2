import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coins_collected = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("racer_folder/AnimatedStreet.png")

# Create a screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Creating sprite groups
enemies_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()


def is_position_valid(rect, group):
    return not any(rect.colliderect(sprite.rect) for sprite in group)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_folder/Enemy.png")
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if is_position_valid(self.rect, coins_group):
                break

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("racer_folder/Coin.png")
        self.image = pygame.transform.scale(self.original_image, (30, 30))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        while True:
            self.rect.center = (random.randint(
                40, SCREEN_WIDTH - 40), random.randint(50, SCREEN_HEIGHT // 2))
            if is_position_valid(self.rect, enemies_group):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_folder/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# Initializing sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Adding to groups
enemies_group.add(E1)
coins_group.add(C1)

# Creating sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_counter = font_small.render(
        "Coins: " + str(coins_collected), True, BLACK)
    DISPLAYSURF.blit(coin_counter, (SCREEN_WIDTH -
                     coin_counter.get_width() - 10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies_group):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    coin_collision = pygame.sprite.spritecollide(P1, coins_group, True)
    if coin_collision:
        pygame.mixer.Sound('gotcoin.wav').play()
        coins_collected += len(coin_collision)
        new_coin = Coin()
        coins_group.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)

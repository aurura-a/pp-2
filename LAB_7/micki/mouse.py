import pygame
import sys
from datetime import datetime  # Используем правильный импорт
import math

pygame.init()

def run():
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Мики макс")
    bg_color = (0,0,0)

    # Загрузка изображения часов
    ground = pygame.image.load("main-clock.png")
    groundrect = ground.get_rect()

    # Загрузка изображения "left-hand.png"
    left_hand = pygame.image.load("left-hand.png")
    left_hand_rect = left_hand.get_rect()
    left_hand_rect.center = screen.get_rect().center
    # Устанавливаем координаты для левой руки
    left_hand_rect.centerx = screen.get_rect().centerx  
    left_hand_rect.centery = screen.get_rect().centery

    # Загрузка изображения правой маленькой руки(минутной)
    right_hand = pygame.image.load("right-hand.png")
    right_hand_rect = right_hand.get_rect()
    right_hand_rect.center = screen.get_rect().center
    # Устанавливаем координаты правой
    right_hand_rect.centerx = screen.get_rect().centerx ##
    right_hand_rect.centery = screen.get_rect().centery

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение фона
        screen.fill(bg_color)
        screen.blit(ground, groundrect)
        groundrect.center = screen.get_rect().center


        # Получение текущего времени и плюс должны синхронизировать секунды с углом это 6 и минуту с углом это 6*60 = 360
        now = datetime.now()
        minute = int(now.strftime('%M')) 
        sec = int(now.strftime('%S'))
        secAngle = 90 - (sec * 6)
        minAngle = 90 - (minute * 6)

        #Терь поворачиваем руки на задданый угол
        rotated_left_hand = pygame.transform.rotate(left_hand, secAngle)
        rotated_left_hand_rect = rotated_left_hand.get_rect(center=left_hand_rect.center)
        
        rotated_right_hand = pygame.transform.rotate(right_hand,minAngle)
        rotated_right_hand_rect = rotated_right_hand.get_rect(center = right_hand_rect.center)


        # Отображение рук
        screen.blit(rotated_left_hand, rotated_left_hand_rect)
        screen.blit(rotated_right_hand, rotated_right_hand_rect)




        # Обновление экрана
        pygame.display.flip()

run()

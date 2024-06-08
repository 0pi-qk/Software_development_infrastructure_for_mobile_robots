import pygame

# Задаем размеры экрана
horizontalSizeWindow = 500
verticalSizeWindow = 500

# Инициализация Pygame
pygame.init()

# Создание окна с заданными размерами
display = pygame.display.set_mode((horizontalSizeWindow, verticalSizeWindow))
pygame.display.set_caption('Turtle stalker')  # Заголовок окна

from window import horizontalSizeWindow, verticalSizeWindow, pygame, display
from dds import TurtlePublisher, KeyboardKey
from random import random
from Turtle import Turtle

import sys


if __name__ == "__main__":
    # Получаем входной параметр - количество черепашек-преследователей
    turtleStalkerCount = int(sys.argv[1])

    # Создание объекта для отслеживания времени
    clock = pygame.time.Clock()

    # Создание целевой черепашки
    targetTurtle = Turtle(name="Target",
                          x=random() * horizontalSizeWindow,
                          y=random() * verticalSizeWindow,
                          color=(180, 200, 200)
                          )

    print("Spawn target turtle \"" + targetTurtle.name + "\" on [" + str(targetTurtle.x) + ", " + str(
        targetTurtle.y) + "]")

    stalkerTurtles = []  # Список для хранения черепашек-преследователей

    # Создание черепашек-преследователей и добавление их в список
    for i in range(turtleStalkerCount):
        stalkerTurtles.append(
            Turtle(name="Stalker" + str(i),
                   x=random() * horizontalSizeWindow,
                   y=random() * verticalSizeWindow,
                   color=(random() * 255, random() * 255, random() * 255),
                   targetRect=targetTurtle if i == 0 else stalkerTurtles[i - 1]
                   )
        )
        print("Spawn stalker turtle \"" + stalkerTurtles[i].name + "\" on [" + str(stalkerTurtles[i].x) + ", " + str(
            stalkerTurtles[i].y) + "]")

    while True:
        for event in pygame.event.get():
            # Обработка события закрытия окна
            if event.type == pygame.QUIT:
                pygame.quit()  # Завершение работы Pygame
                break
            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]:
                    TurtlePublisher.write(KeyboardKey(key=event.key))
            # Обработка отпускания клавиш
            if event.type == pygame.KEYUP:
                TurtlePublisher.write(KeyboardKey(key=-10))

        display.fill((0, 40, 96))  # Заливка фона цветом

        # Обновление позиции целевой черепашки
        targetTurtle.new_position()
        # Перемещение целевой черепашки и ее отрисовка
        targetTurtle.move_publish()
        targetTurtle.draw_turtle()

        # Аналогичные операции для черепашек-преследователей
        for stalker in stalkerTurtles:
            stalker.new_position()
            stalker.move_publish()
            stalker.draw_turtle()

        pygame.display.update()  # Обновление экрана
        clock.tick(30)  # Установка FPS

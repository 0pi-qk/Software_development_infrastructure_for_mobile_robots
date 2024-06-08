from dds import Topic, Pose, KeyboardKey, Publisher, Subscriber, dp, KeyTopic
from window import pygame, display, horizontalSizeWindow, verticalSizeWindow
from math import sqrt

# Задание размера черепашки
turtleSize = 25


# Класс черепаха
class Turtle:
    def __init__(self, name, x, y, color, targetRect=None):
        # Инициализация черепахи с заданными параметрами
        self.name = name  # Имя черепахи
        self.x = x  # Позиция по оси X
        self.y = y  # Позиция по оси Y
        self.color = color  # Цвет черепахи

        # Переменные для хранения расстояний по горизонтали и вертикали
        self.horizontalDistance = 0
        self.verticalDistance = 0

        # Базовая скорость черепахи
        self.basicSpeed = 5

        # Создание топика для черепахи и подписка на топик черепахи-цели
        self.topic = Topic(dp, self.name, Pose)
        self.publisher = Publisher(dp, self.topic)
        if not targetRect:
            self.subscriber = Subscriber(dp, KeyTopic)
        else:
            self.subscriber = Subscriber(dp, targetRect.topic)

    # Метод для определения новой позиции черепахи
    def new_position(self):
        msg = self.subscriber.read()
        if len(msg) > 0:
            if self.name == "Target":
                self.read_keyboard_key(msg)
            else:
                self.calculate_move(msg)

    # Метод для обработки ввода с клавиатуры для целевой черепахи
    def read_keyboard_key(self, msg: KeyboardKey):
        key = msg[0].key

        # Словарь сопоставления клавишам и изменениям позиции
        key_mappings = {
            97: (-self.basicSpeed, 0),  # Клавиша 'a'
            100: (self.basicSpeed, 0),  # Клавиша 'd'
            119: (0, -self.basicSpeed),  # Клавиша 'w'
            115: (0, self.basicSpeed)  # Клавиша 's'
        }

        # Получение изменений позиции в соответствии с нажатой клавишей
        self.horizontalDistance, self.verticalDistance = key_mappings.get(key, (0, 0))

    # Метод для вычисления движения преследователей к целевой черепахе
    def calculate_move(self, msg: Pose):
        dx = msg[0].x - self.x
        dy = msg[0].y - self.y

        distance = sqrt(dx * dx + dy * dy)

        cf = 1 / distance * (self.basicSpeed - 0.5) if distance > turtleSize else 0

        self.horizontalDistance = dx * cf
        self.verticalDistance = dy * cf

    # Метод для перемещения черепахи и публикации новой позиции
    def move_publish(self):
        # Перемещение черепахи на заданные расстояния
        self.x += self.horizontalDistance
        self.y += self.verticalDistance

        # Ограничение координат, чтобы черепаха не выходила за границы окна
        self.x = max(0, min(horizontalSizeWindow - turtleSize, self.x))
        self.y = max(0, min(verticalSizeWindow - turtleSize, self.y))

        # Публикация новой позиции черепахи
        self.publisher.write(Pose(x=self.x, y=self.y))

    # Метод для отрисовки черепахи на экране
    def draw_turtle(self):
        pygame.draw.rect(display, self.color, [self.x, self.y, turtleSize, turtleSize])

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Human Stats Bars")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Шрифт
font = pygame.font.Font(None, 24)  # Шрифт для подписей

class Human:
    def __init__(self):
        self.eat = 100
        self.health = 100
        self.energy = 100
        self.money = 100
        self.sanity = 100

    def edit_stats(self, stat, amount):
        if hasattr(self, stat):
            current_value = getattr(self, stat)
            new_value = 0 if current_value + amount < 0 else 100 if current_value + amount > 100 else current_value + amount
            setattr(self, stat, new_value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{stat}'")

    def display_stats(self, screen):
        # Параметры для отрисовки полосок
        bar_width = 200  # Ширина полоски
        bar_height = 20  # Высота полоски
        start_x = SCREEN_WIDTH - bar_width - 20  # Начальная позиция по X (отступ 20 пикселей от правого края)
        start_y = 20  # Начальная позиция по Y (отступ 20 пикселей от верхнего края)
        gap = 30  # Расстояние между полосками

        # Статы и их цвета
        stats = [
            ("Eat", self.eat, GREEN),
            ("Health", self.health, RED),
            ("Energy", self.energy, YELLOW),
            ("Money", self.money, BLUE),
            ("Sanity", self.sanity, PURPLE),
        ]

        # Отрисовка каждой полоски
        for i, (name, value, color) in enumerate(stats):
            # Позиция полоски
            y = start_y + i * gap

            # Отрисовка фона полоски (серый прямоугольник)
            pygame.draw.rect(screen, (128, 128, 128), (start_x, y, bar_width, bar_height))

            # Отрисовка заполненной части полоски
            filled_width = (value / 100) * bar_width
            pygame.draw.rect(screen, color, (start_x, y, filled_width, bar_height))

            # Отрисовка текста с названием стата и значением
            text = f"{name}: {value}"
            text_surface = font.render(text, True, WHITE)
            screen.blit(text_surface, (start_x - 120, y))  # Текст слева от полоски

# Создаем объект Human
human = Human()

# Основной цикл Pygame
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Изменяем статы для примера
    human.edit_stats('eat', -0.1)
    human.edit_stats('health', -0.05)
    human.edit_stats('energy', -0.2)
    human.edit_stats('money', 0.1)
    human.edit_stats('sanity', -0.1)

    # Очищаем экран
    screen.fill(BLACK)

    # Отображаем статы в виде полосок
    human.display_stats(screen)

    # Обновляем экран
    pygame.display.flip()

    # Ограничиваем FPS
    clock.tick(30)

# Завершение работы Pygame
pygame.quit()
sys.exit()
import pygame
import sys
from prolog import prolog
from game import test

# Инициализация PyGame
pygame.init()


# Настройки окна (полноэкранный режим)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифт
font = pygame.font.Font(None, 36)  # Используем стандартный шрифт

# Тексты для слайдов
slides = [
    "Наконец, то я съехал от родителей...",
    "Теперь моя жизнь полностью в моих руках",
    "Почти все деньги я потратил на квартиру",
    "Надо подзаработать денег и доказать что я могу жить самостоятельно",
    "Было бы славно жить и вообще не работать..."
]


# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    prolog(screen)
    test(screen)
    break



# Завершение работы PyGame
pygame.quit()
sys.exit()
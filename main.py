import pygame
import sys
from prolog import prolog
from game import test

# Инициализация PyGame
pygame.init()


# Настройки окна (полноэкранный режим)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    test(screen)
    break


# Завершение работы PyGame
pygame.quit()
sys.exit()
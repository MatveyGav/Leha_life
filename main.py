import pygame
import sys
from prolog import prolog
from game import game
from scenes import bank_1, bank_1_1, home_1
from clases import Human

# Инициализация PyGame
pygame.init()


# Настройки окна (полноэкранный режим)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

Leha = Human()
actions = 0

# Основной цикл программы
running = True
current_scene = "game"
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(Leha.eat)
    func = globals()[current_scene]
    current_scene = func(screen, actions, Leha)


# Завершение работы PyGame
pygame.quit()
sys.exit()
import pygame
import sys
from clases import Rectangle, Bar, Human

# Инициализация Pygame
pygame.init()


def game(screen, actions, Leha):
    # Размеры окна
    WIDTH, HEIGHT = screen.get_size()  # Получаем размеры экрана

    # Цвета
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Создание окна
    pygame.display.set_caption("Кликабельные прямоугольники")

    # Создание списка прямоугольников
    rectangles = [
        Rectangle(100, 100, 150, 100, BLUE, 1, "bank_1"),
        Rectangle(400, 300, 200, 150, RED, 2, "home_1"),
        Rectangle(50, 400, 100, 50, BLUE, 3)
    ]

    health_bar = Bar(740, 25, 500, 20, 100, RED, WIDTH, BLACK)

    # Основной цикл программы
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Получаем позицию клика
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Проверяем, попал ли клик в какой-либо прямоугольник
                for rect in rectangles:
                    if rect.check_click((mouse_x, mouse_y)):
                        return rect.scene

        # Отрисовка фона
        screen.fill(WHITE)

        # Отрисовка всех прямоугольников
        for rect in rectangles:
            rect.draw(screen)

        health_bar.draw(screen)

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы Pygame
    return
import pygame
import sys
from clases import Rectangle, Button

# Инициализация Pygame
pygame.init()

def test(screen):
# Полноэкранный режим
    WIDTH, HEIGHT = screen.get_size()  # Получаем размеры экрана
    pygame.display.set_caption("Кликабельные прямоугольники с меню")

    # Цвета
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # Разделение экрана на левую и правую части
    map_width = WIDTH // 2  # Левая половина экрана
    map_height = HEIGHT



    # Создаем список прямоугольников в левой части
    rectangles = [
        Rectangle(100, 100, 150, 100, RED, 1),
        Rectangle(300, 200, 120, 80, RED, 2),
        Rectangle(500, 300, 200, 150, RED, 3)
    ]

    # Словарь с вариантами для каждого прямоугольника
    options_dict = {
        1: [Button(map_width + 50, 100, 200, 50, "Вариант 1.1", BLUE),
            Button(map_width + 50, 200, 200, 50, "Вариант 1.2", BLUE)],
        2: [Button(map_width + 50, 100, 200, 50, "Вариант 2.1", BLUE),
            Button(map_width + 50, 200, 200, 50, "Вариант 2.2", BLUE),
            Button(map_width + 50, 300, 200, 50, "Вариант 2.3", BLUE)],
        3: [Button(map_width + 50, 100, 200, 50, "Вариант 3.1", BLUE)]
    }

    # Основной цикл программы
    running = True
    selected_rectangle = None  # Выделенный прямоугольник
    show_options = False  # Показывать ли варианты в правой части
    current_options = []  # Текущие варианты для выбранного прямоугольника

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход по нажатию Esc
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    # Проверяем клик в левой части
                    for rect in rectangles:
                        if rect.check_click(event.pos):
                            # Сбрасываем цвет всех прямоугольников
                            for r in rectangles:
                                r.color = RED
                            # Выделяем выбранный прямоугольник
                            rect.color = GREEN
                            selected_rectangle = rect
                            show_options = True  # Показываем варианты в правой части
                            current_options = options_dict.get(rect.id, [])  # Загружаем варианты для этого прямоугольника

                    # Проверяем клик в правой части (если варианты отображаются)
                    if show_options:
                        for option in current_options:
                            if option.check_click(event.pos):
                                print(f"Выбран прямоугольник {selected_rectangle.id} с вариантом: {option.text}")

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка всех прямоугольников в левой части
        for rect in rectangles:
            rect.draw(screen)

        # Отрисовка разделительной линии между картой и правой частью
        pygame.draw.line(screen, BLACK, (map_width, 0), (map_width, HEIGHT), 2)

        # Отрисовка вариантов в правой части (если нужно)
        if show_options:
            for option in current_options:
                option.draw(screen)

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы
    return
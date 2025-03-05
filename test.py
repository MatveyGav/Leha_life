import pygame
import sys

# Инициализация Pygame
pygame.init()

# Полноэкранный режим
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Кликабельные прямоугольники с меню")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Разделение экрана на левую и правую части
map_width = screen_width // 2  # Левая половина экрана
map_height = screen_height

# Класс для прямоугольников
class Rectangle:
    def __init__(self, x, y, width, height, color, id):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.clicked = False
        self.id = id

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

# Класс для кнопок в правой части
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

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
    pygame.draw.line(screen, BLACK, (map_width, 0), (map_width, screen_height), 2)

    # Отрисовка вариантов в правой части (если нужно)
    if show_options:
        for option in current_options:
            option.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()
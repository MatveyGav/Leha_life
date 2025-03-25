import pygame
import sys

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (245, 136, 46)
GREEN = pygame.Color("#00BB00")

# Шрифт
font = pygame.font.Font(None, 24)  # Шрифт для подписей

class Rectangle:
    def __init__(self, x, y, width, height, color, id, scene=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.clicked = False
        self.id = id
        self.scene = scene

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False


class Button:
    def __init__(self, x, y, width, height, text, color, scene=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.scene = scene

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, pygame.Color("black"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False


class Human:
    def __init__(self, screen):
        self.eat = 100
        self.health = 100
        self.energy = 100
        self.money = 100
        self.sanity = 100
        self.screen = screen
        info = pygame.display.Info()
        self.WIDTH, self.HEIGHT = info.current_w, info.current_h

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
        start_x = self.WIDTH - bar_width - 20  # Начальная позиция по X (отступ 20 пикселей от правого края)
        start_y = 20  # Начальная позиция по Y (отступ 20 пикселей от верхнего края)
        gap = 30  # Расстояние между полосками

        # Статы и их цвета
        stats = [
            ("Голод", self.eat, BLUE),
            ("Здоровье", self.health, GREEN),
            ("Энергия", self.energy, ORANGE),
            ("Деньги", self.money, YELLOW),
            ("Рассудок", self.sanity, PURPLE),
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


class Bar:
    def __init__(self, x, y, width, height, max_value, color, bg_color, outline_color, outline_thickness=2):
        """
        Инициализация шкалы.

        :param x: Координата X шкалы.
        :param y: Координата Y шкалы.
        :param width: Ширина шкалы.
        :param height: Высота шкалы.
        :param max_value: Максимальное значение шкалы.
        :param color: Цвет заполненной части шкалы.
        :param bg_color: Цвет фона шкалы.
        :param outline_color: Цвет обводки.
        :param outline_thickness: Толщина обводки.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = max_value
        self.color = color
        self.bg_color = bg_color
        self.outline_color = outline_color
        self.outline_thickness = outline_thickness

    def set_value(self, value):
        """
        Устанавливает текущее значение шкалы.

        :param value: Новое значение шкалы.
        """
        self.current_value = max(0, min(value, self.max_value))  # Ограничение значения в пределах [0, max_value]

    def draw(self, screen):
        """
        Отрисовывает шкалу на экране.

        :param screen: Экран PyGame, на котором будет отрисована шкала.
        """
        # Отрисовка обводки
        pygame.draw.rect(
            screen,
            self.outline_color,
            (self.x - self.outline_thickness, self.y - self.outline_thickness,
             self.width + 2 * self.outline_thickness, self.height + 2 * self.outline_thickness),
            self.outline_thickness
        )

        # Отрисовка фона шкалы
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))

        # Отрисовка заполненной части шкалы
        filled_width = (self.current_value / self.max_value) * self.width
        pygame.draw.rect(screen, self.color, (self.x, self.y, filled_width, self.height))


class Scene:
    def __init__(self, screen, background_image, buttons, actions, Leha):
        self.screen = screen
        # Масштабируем фоновое изображение под размеры экрана
        self.background = pygame.transform.scale(pygame.image.load(background_image), (screen.get_width(), screen.get_height()))
        self.actions = actions
        self.buttons = buttons
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200, 128)
        self.TRANSPARENT = (0, 0, 0, 128)  # Полупрозрачный черный
        self.font = pygame.font.Font(None, 36)
        self.panel_height = screen.get_height() // 4
        self.Leha = Leha
        # Создаем полупрозрачную панель
        self.panel = pygame.Surface((screen.get_width(), self.panel_height), pygame.SRCALPHA)
        self.panel.fill(self.TRANSPARENT)  # Заливаем полупрозрачным цветом

    def draw(self):
        # Отрисовка фона
        self.screen.blit(self.background, (0, 0))
        # Отрисовка полупрозрачной панели
        self.screen.blit(self.panel, (0, self.screen.get_height() - self.panel_height))
        # Отрисовка кнопок
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.color = self.WHITE
            else:
                button.color = self.GRAY
            button.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.check_click(mouse_pos):
                        return button.scene
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if running != True:
                return running, self.actions, self.Leha
            self.draw()
            self.Leha.display_stats(self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def fade_out(self, duration=3):
        fade_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        fade_surface.fill((0, 0, 0))
        for alpha in range(0, 255, 5):
            fade_surface.set_alpha(alpha)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(50)

    def fade_in(self, duration=3):
        fade_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        fade_surface.fill((0, 0, 0))
        for alpha in range(255, 0, -5):
            fade_surface.set_alpha(alpha)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(50)
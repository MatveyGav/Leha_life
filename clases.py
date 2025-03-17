import pygame


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
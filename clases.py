# Класс для прямоугольников
import pygame


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
        text_surface = font.render(self.text, True, pygame.Color("black"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

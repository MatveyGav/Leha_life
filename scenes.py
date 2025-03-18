import pygame
import sys
from clases import Button, Human, Scene

# Инициализация Pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)  # Полупрозрачный серый
BLUE = (0, 0, 255, 128)  # Полупрозрачный синий
TRANSPARENT = (0, 0, 0, 128)  # Полупрозрачный черный



def bank_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    # Создание кнопок
    button_width = 300
    button_height = 50
    enter_button = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 50, button_width, button_height,
                          "Зайти", GRAY, "bank_1_1")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 190, button_width, button_height, "Уйти",
                      GRAY, "game")
    buttons = [enter_button, exit_btn]

    # Создание сцены
    scene = Scene(screen, "data/bank_1.png", buttons, Leha=Leha)
    return scene.run()


def bank_1_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    # Создание кнопок
    button_width = 300
    button_height = 50
    credit_button = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 50, button_width, button_height,
                           "Взять кредит", GRAY, "bank_1_1_1")
    deposit_button = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 120, button_width, button_height,
                            "Оформить вклад", GRAY, "bank_1_1_2")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 190, button_width, button_height, "Уйти",
                      GRAY, "game")
    buttons = [credit_button, deposit_button, exit_btn]

    # Создание сцены
    scene = Scene(screen, "data/bank_1_1.png", buttons, Leha=Leha)
    return scene.run()


def home_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    # Создание кнопок
    button_width = 300
    button_height = 50
    sleep_btn = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 50, button_width, button_height, "Поспать",
                       GRAY, "home_sleep")
    laptoop_button = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 120, button_width, button_height,
                            "Запустить ноутбук", GRAY, "game")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - (HEIGHT // 4) + 190, button_width, button_height,
                      "Выйти на улицу", GRAY, "game")
    buttons = [sleep_btn, laptoop_button, exit_btn]

    # Создание сцены
    scene = Scene(screen, "data/home_1.png", buttons, Leha=Leha)
    return scene.run()


def home_sleep(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    scene = Scene(screen, "data/home_1.png")
    scene.fade_out()
    pygame.time.delay(3000)  # 3 секунды
    actions += 5
    Leha.edit_stats("energy", 50)
    Leha.edit_stats("eat", -25)
    print(Leha.eat)
    scene.fade_in()
    return "home_1"
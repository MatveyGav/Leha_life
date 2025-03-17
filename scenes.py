import pygame
import sys
from clases import Button, Human


# Инициализация Pygame
pygame.init()


def bank_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200, 128)  # Полупрозрачный серый
    BLUE = (0, 0, 255, 128)  # Полупрозрачный синий
    TRANSPARENT = (0, 0, 0, 128)  # Полупрозрачный черный

    # Шрифт
    font = pygame.font.Font(None, 36)

    # Загрузка фонового изображения
    background = pygame.image.load("data/bank_1.png")  # Убедитесь, что файл background.jpg находится в той же папке
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Создание окна в полноэкранном режиме
    pygame.display.set_caption("Визуальная новелла")

    # Создание полупрозрачной панели для кнопок
    panel_height = HEIGHT // 4  # Высота панели
    panel = pygame.Surface((WIDTH, panel_height), pygame.SRCALPHA)  # Полупрозрачная поверхность
    panel.fill(TRANSPARENT)  # Заливка полупрозрачным цветом

    # Создание кнопок
    button_width = 300
    button_height = 50
    enter_button = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 50, button_width, button_height, "Зайти", GRAY, "bank_1_1")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 190, button_width, button_height, "Уйти", GRAY, "game")
    buttons = [enter_button, exit_btn]

    # Основной цикл программы
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход по нажатию ESC
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка клика по кнопкам
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.check_click(mouse_pos):
                        return button.scene

        # Получение позиции мыши
        mouse_pos = pygame.mouse.get_pos()

        # Отрисовка фона
        screen.blit(background, (0, 0))

        # Отрисовка полупрозрачной панели
        screen.blit(panel, (0, HEIGHT - panel_height))

        # Отрисовка кнопок на панели
        for button in buttons:
            # Изменение цвета кнопки при наведении
            if button.rect.collidepoint(mouse_pos):
                button.color = WHITE  # Цвет при наведении
            else:
                button.color = GRAY  # Обычный цвет
            button.draw(screen)  # Рисуем кнопки на экране

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()


def bank_1_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200, 128)  # Полупрозрачный серый
    BLUE = (0, 0, 255, 128)  # Полупрозрачный синий
    TRANSPARENT = (0, 0, 0, 128)  # Полупрозрачный черный

    # Шрифт
    font = pygame.font.Font(None, 36)

    # Загрузка фонового изображения
    background = pygame.image.load("data/bank_1_1.png")  # Убедитесь, что файл background.jpg находится в той же папке
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Создание окна в полноэкранном режиме
    pygame.display.set_caption("Визуальная новелла")

    # Создание полупрозрачной панели для кнопок
    panel_height = HEIGHT // 4  # Высота панели
    panel = pygame.Surface((WIDTH, panel_height), pygame.SRCALPHA)  # Полупрозрачная поверхность
    panel.fill(TRANSPARENT)  # Заливка полупрозрачным цветом

    # Создание кнопок
    button_width = 300
    button_height = 50
    credit_button = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 50, button_width, button_height, "Взять кредит", GRAY, "bank_1_1_1")
    deposit_button = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 120, button_width, button_height, "Оформить вклад", GRAY, "bank_1_1_2")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 190, button_width, button_height, "Уйти", GRAY, "game")
    buttons = [credit_button, deposit_button, exit_btn]

    # Основной цикл программы
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход по нажатию ESC
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка клика по кнопкам
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.check_click(mouse_pos):
                        return button.scene

        # Получение позиции мыши
        mouse_pos = pygame.mouse.get_pos()

        # Отрисовка фона
        screen.blit(background, (0, 0))

        # Отрисовка полупрозрачной панели
        screen.blit(panel, (0, HEIGHT - panel_height))

        # Отрисовка кнопок на панели
        for button in buttons:
            # Изменение цвета кнопки при наведении
            if button.rect.collidepoint(mouse_pos):
                button.color = WHITE  # Цвет при наведении
            else:
                button.color = GRAY  # Обычный цвет
            button.draw(screen)  # Рисуем кнопки на экране

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()


def home_1(screen, actions, Leha):
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200, 128)  # Полупрозрачный серый
    BLUE = (0, 0, 255, 128)  # Полупрозрачный синий
    TRANSPARENT = (0, 0, 0, 128)  # Полупрозрачный черный

    # Шрифт
    font = pygame.font.Font(None, 36)

    # Загрузка фонового изображения
    background = pygame.image.load("data/home_1.png")  # Убедитесь, что файл background.jpg находится в той же папке
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Создание окна в полноэкранном режиме
    pygame.display.set_caption("Визуальная новелла")

    # Создание полупрозрачной панели для кнопок
    panel_height = HEIGHT // 4  # Высота панели
    panel = pygame.Surface((WIDTH, panel_height), pygame.SRCALPHA)  # Полупрозрачная поверхность
    panel.fill(TRANSPARENT)  # Заливка полупрозрачным цветом

    # Создание кнопок
    button_width = 300
    button_height = 50
    sleep_btn = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 50, button_width, button_height,"Поспать", GRAY)
    laptoop_button = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 120, button_width, button_height,"Запустить ноутбук", GRAY, "game")
    exit_btn = Button((WIDTH - button_width) // 2, HEIGHT - panel_height + 190, button_width, button_height, "Выйти на улицу",GRAY, "game")
    buttons = [sleep_btn, laptoop_button, exit_btn]

    def fade_out(duration=3):
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        for alpha in range(0, 255, 5):  # Постепенно увеличиваем прозрачность
            fade_surface.set_alpha(alpha)
            screen.blit(background, (0, 0))  # Отрисовываем фон
            screen.blit(fade_surface, (0, 0))  # Накладываем затемнение
            pygame.display.flip()
            pygame.time.delay(50)  # Задержка для плавности

    # Функция проявления экрана
    def fade_in(duration=3):
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        for alpha in range(255, 0, -5):  # Постепенно уменьшаем прозрачность
            fade_surface.set_alpha(alpha)
            screen.blit(background, (0, 0))  # Отрисовываем фон
            screen.blit(fade_surface, (0, 0))  # Накладываем затемнение
            pygame.display.flip()
            pygame.time.delay(50)  # Задержка для плавности

    # Основной цикл программы
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход по нажатию ESC
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка клика по кнопкам
                mouse_pos = pygame.mouse.get_pos()
                if sleep_btn.check_click(mouse_pos):
                    fade_out()
                    pygame.time.delay(3000)  # 3 секунды
                    actions += 5
                    Leha.edit_stats("energy", 50)
                    Leha.edit_stats("eat", -25)
                    print(Leha.eat)
                    fade_in()
                else:
                    for button in buttons:
                        if button.check_click(mouse_pos):
                            return button.scene

        # Получение позиции мыши
        mouse_pos = pygame.mouse.get_pos()

        # Отрисовка фона
        screen.blit(background, (0, 0))

        # Отрисовка полупрозрачной панели
        screen.blit(panel, (0, HEIGHT - panel_height))

        # Отрисовка кнопок на панели
        for button in buttons:
            # Изменение цвета кнопки при наведении
            if button.rect.collidepoint(mouse_pos):
                button.color = WHITE  # Цвет при наведении
            else:
                button.color = GRAY  # Обычный цвет
            button.draw(screen)  # Рисуем кнопки на экране

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()
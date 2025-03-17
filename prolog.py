import pygame
import sys

# Инициализация PyGame
pygame.init()


def prolog(screen):
    # Настройки окна (полноэкранный режим)
    WIDTH, HEIGHT = screen.get_size()  # Получаем размеры экрана
    pygame.display.set_caption("ПРОЛОГ")

    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Шрифт
    font = pygame.font.Font(None, 36)  # Используем стандартный шрифт

    # Тексты для слайдов
    slides = [
        "Наконец, то я съехал от родителей...",
        "Теперь моя жизнь полностью в моих руках",
        "Почти все деньги я потратил на квартиру",
        "Надо подзаработать денег и доказать что я могу жить самостоятельно",
        "Было бы славно жить и вообще не работать..."
    ]

    # Переменные для анимации текста
    current_slide = 0
    text = ""
    char_index = 0
    animation_speed = 0.05  # Скорость появления текста (секунды на символ)
    skip_animation = False

    # Таймер для анимации
    clock = pygame.time.Clock()
    last_char_time = 0

    # Основной цикл программы
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if pygame.time.get_ticks() - last_char_time < 300:  # Двойной клик
                        skip_animation = True
                    else:
                        # Переход к следующему слайду
                        if current_slide < len(slides) - 1:
                            current_slide += 1
                            text = ""
                            char_index = 0
                            skip_animation = False
                        else:
                            running = False  # Завершение после последнего слайда
                    last_char_time = pygame.time.get_ticks()

        # Очистка экрана
        screen.fill(BLACK)

        # Анимация текста
        if char_index < len(slides[current_slide]):
            if skip_animation:
                text = slides[current_slide]
                char_index = len(slides[current_slide])
            else:
                current_time = pygame.time.get_ticks()
                if current_time - last_char_time > animation_speed * 1000:
                    text += slides[current_slide][char_index]
                    char_index += 1
                    last_char_time = current_time

        # Отрисовка текста
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(60)

    # Завершение работы PyGame
    return "game"
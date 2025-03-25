import pygame
import sys
import numpy as np


def point_in_polygon(point, polygon):
    """Проверяет, находится ли точка внутри многоугольника"""
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def map(screen, actions, Leha):
    pygame.init()

    zones = [
        [(300, 0), (316, 176), (383, 280), (780, 260), (790, 0)],
        [(0, 60), (313, 322), (374, 633), (153, 790), (0, 640)],
        [(794, 656), (783, 420), (1152, 127), (1233, 145), (1311, 236), (1287, 508), (969, 785)],
        [(1331, 230), (1338, 128), (1430, 0), (1557, 0), (1626, 70), (1620, 194), (1444, 314)],
        [(100, 1170), (57, 1000), (220, 866), (195, 779), (384, 639), (600, 680), (635, 1000), (484, 1116), (426, 1096), (256, 1220)]
    ]

    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Выберите зону")

    original_image = pygame.image.load("data/map.png")
    # Масштабируем изображение под экран (с сохранением пропорций)
    img_width, img_height = original_image.get_size()
    scale = min(screen_width / img_width, screen_height / img_height)
    scaled_width = int(img_width * scale)
    scaled_height = int(img_height * scale)
    image = pygame.transform.scale(original_image, (scaled_width, scaled_height))

    # Позиция изображения по центру экрана
    img_x = (screen_width - scaled_width) // 2
    img_y = (screen_height - scaled_height) // 2

    # Масштабируем зоны для нового размера изображения
    scaled_zones = []
    for zone in zones:
        scaled_zone = []
        for point in zone:
            x, y = point
            scaled_point = (
                int(x * scale) + img_x,
                int(y * scale) + img_y
            )
            scaled_zone.append(scaled_point)
        scaled_zones.append(scaled_zone)

    # Основной цикл
    selected_zone = None
    running = True

    locations = {1:"bank_1", 3:"home_1"}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    mouse_pos = pygame.mouse.get_pos()
                    for i, zone in enumerate(scaled_zones):
                        if point_in_polygon(mouse_pos, zone):
                            selected_zone = locations[i + 1]
                            running = False
                            break

        # Отрисовка
        screen.fill((0, 0, 0))  # Черный фон
        screen.blit(image, (img_x, img_y))

        # Отрисовка зон (полупрозрачные)
        for i, zone in enumerate(scaled_zones):
            if len(zone) >= 3:  # Рисуем только если есть хотя бы 3 точки
                zone_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                pygame.draw.polygon(zone_surface, (0, 255, 0, 128), zone)
                screen.blit(zone_surface, (0, 0))

                # Вычисляем центр многоугольника для номера
                center_x = sum(p[0] for p in zone) / len(zone)
                center_y = sum(p[1] for p in zone) / len(zone)

                # Номер зоны
                font = pygame.font.Font(None, 36)
                text = font.render(str(i + 1), True, (255, 255, 255))
                text_rect = text.get_rect(center=(center_x, center_y))
                screen.blit(text, text_rect)

        pygame.display.flip()

    return selected_zone, actions, Leha
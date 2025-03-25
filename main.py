import pygame
import sys
from prolog import prolog
from game import map
from scenes import bank_1, bank_1_1, home_1, home_sleep
from clases import Human

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

Leha = Human(screen)
actions = 0

running = True
current_scene = "map"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    func = globals()[current_scene]
    current_scene, actions, Leha = func(screen, actions, Leha)


pygame.quit()
sys.exit()
import pygame
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False

# PyGame

RES = WIDTH, HEIGHT = 900, 720
FPS = 60

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

while True:
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(FPS)

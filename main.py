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

# PyMunk variables

space = pymunk.Space()
space.gravity = 0, 8000

# PyMunk constants

E = 1.602 * 10 ** -19  # electic charge
M0 = 9.109 * 10 ** -31  # electron's mass
C = 3 * 10 ** 8  # light speed
EC0 = 8.854 * 10 ** -12  # dielectric constant
PI = 3.14

# Electron

e_shape = pymunk.shapes.Circle(E**2/(4*PI*EC0*M0*C**2))

# Drawing

while True:
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(FPS)

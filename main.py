from random import randrange

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
R = E**2/(4*PI*EC0*M0*C**2)


segment_shape = pymunk.Segment(space.static_body, (2, HEIGHT), (WIDTH,HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.8
segment_shape.friction = 1.0


# Electron

body = pymunk.Body()
def create_circle(space, pos):
    circle_mass = M0
    circle_size = (R, R)
    circle_moment = pymunk.moment_for_circle(20, 30, 30)
    circle_body = pymunk.Body(circle_mass, circle_moment)
    circle_body.position = pos
    circle_shape = pymunk.shapes.Circle(circle_body, 30)
    circle_shape.elasticity = 0.4
    circle_shape.friction = 1.0
    circle_shape.color = [randrange(256) for i in range(4)]
    space.add(circle_body, circle_shape)


# Drawing

while True:
    surface.fill(pygame.Color('black'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_circle(space, i.pos)
                print(i.pos)

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(FPS)

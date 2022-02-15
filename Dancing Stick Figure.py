import random

import pygame

pygame.init()

window = pygame.display.set_mode([300, 500])

frames = 0

while frames < 100:

    frames += 1

    window.fill((255, 255, 255))

    pygame.draw.circle(window, (0, 0, 0), (150, 75), 50, 1)

    pygame.draw.line(window, (0, 0, 0), (150, 125), (150, 275))

    left_leg = random.randint(25, 100)

    right_leg = random.randint(200, 275)

    pygame.draw.line(window, (0, 0, 0), (150, 275), (left_leg, 475))

    pygame.draw.line(window, (0, 0, 0), (150, 275), (right_leg, 475))

    left_arm = random.randint(100, 250)

    right_arm = random.randint(100, 250)

    pygame.draw.line(window, (0, 0, 0), (25, left_arm), (150, 175))

    pygame.draw.line(window, (0, 0, 0), (275, right_arm), (150, 175))

    pygame.display.flip()

    pygame.time.wait(100)

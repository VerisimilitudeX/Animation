"""
LESSON: 3.3 - Animation
TECHNIQUE 4: Backgrounds and Trails
DEMO
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

bg_color = (0, 0, 0)

offset = 0

frames = 0
while frames < 100:

    offset += 4

    window.fill(bg_color)

    pygame.draw.circle(window, (200, 0, 0), (offset, 200), 50)
    pygame.draw.circle(window, (0, 200, 0), (200, offset), 50)
    pygame.draw.circle(window, (0, 0, 200), (offset, offset), 50)

    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1

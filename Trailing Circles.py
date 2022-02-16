import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])

bg_color = (0, 0, 0)

x_offset = 0
y_offset = 0

frames = 0
while frames < 110:

    y_offset += 25
    if y_offset > 400:
        x_offset += 80
        y_offset = 0

    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    color = (r, g, b)
    
    pygame.draw.circle(window, color, (x_offset, y_offset), 50)

    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1

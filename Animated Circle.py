import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
circle_color = (140, 140, 220)
triangle_color = (230, 220, 120)

left = (0, 400)
right = (400, 400)
circle_y = 280
top_y = 300

circle_offset = 0
x = 50
y = 50

frames = 0
while frames < 400:

    circle_offset += 1
    center = (x + circle_offset, y)
    window.fill((255, 255, 255))

    pygame.draw.circle(window, circle_color, center, 10)

    pygame.display.flip() 
    pygame.time.wait(1)

    frames += 1

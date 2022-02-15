import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

ground_color = (150, 100, 60)
gray = (200, 200, 200)

r_x_start = 50
r_y_start = 0

e_x_start = 0
e_y_start = 50

offset = 0

frames = 0
while frames < 100:

    offset += 1

    r_x_start += offset
    r_y_start += offset
    e_x_start += offset
    e_y_start += offset

    rectangle = pygame.Rect(r_x_start, r_y_start, 60, 50)
    ellipse = pygame.Rect(e_x_start, e_y_start, 50, 70)

    window.fill(ground_color)

    pygame.draw.rect(window, gray, rectangle)
    pygame.draw.ellipse(window, gray, ellipse)

    pygame.display.flip()
    pygame.time.wait(10)
    
    frames += 1

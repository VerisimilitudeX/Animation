import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])
window.fill((255, 255, 255))

offset = 0
frames = 0
while frames < 50:
    pygame.draw.circle(window, (123, 41, 213), (offset, 20), 20)
    offset += 5
    pygame.display.flip()
    window.fill((255, 255, 255))

window = pygame.display.set_mode([500, 500])
window.fill((255, 255, 255))

circle_x = 0
while circle_x < 500:

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), (circle_x, 250), 25)
    circle_x += 5

    pygame.display.flip()
input()

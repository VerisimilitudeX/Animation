import pygame
pygame.init()

window = pygame.display.set_mode([200, 400])
b = (0, 0, 0)
r = pygame.Rect(90, 0, 20, 25)
offset = 0

while r.y < 400:
    r.y += offset
    offset += 1
    window.fill((255, 255, 255))
    pygame.draw.rect(window, b, r)

    pygame.display.flip()
    pygame.time.wait(20)

input("Hit enter to close window")

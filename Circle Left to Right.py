import pygame
pygame.init()
x = 0
window = pygame.display.set_mode([400, 200])
b = (0, 0, 0)
offset = 0
while offset < 400:
    window.fill((255, 255, 255))
    pygame.draw.circle(window, b, (0 + offset, 100), 20)
    offset += 1
    pygame.display.flip()
    pygame.time.wait(20)

input("Press enter to close window")

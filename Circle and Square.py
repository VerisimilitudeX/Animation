import pygame
pygame.init()

window = pygame.display.set_mode([600, 400])
window.fill((255, 255, 255))

b = (0, 0, 0)

# Draw shapes here
pygame.draw.circle(window, b, (50, 200), 20)
r = pygame.Rect(300, 150, 25, 25)
pygame.draw.rect(window, (0, 0, 0), r)

pygame.display.flip()

input("Hit enter to close window")

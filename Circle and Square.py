import pygame
pygame.init()

window = pygame.display.set_mode([600, 400])
window.fill((255, 255, 255))

b = (0, 0, 0)

# Draw shapes here
pygame.draw.circle(window, b, (50, 100), 20)
pygame.draw.polygon(window, b, [(350, 200), (350, 230), (380, 230), (380, 200)])


pygame.display.flip()

input("Hit enter to close window")

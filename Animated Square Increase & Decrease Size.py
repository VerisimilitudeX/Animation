import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))
color = (100, 130, 80)

left = 0
right = 400
top = 0
bottom = 400

offset = 0

frames = 0
while frames <= 250:

    offset += 0.03

    left += offset
    right -= offset
    top += offset
    bottom -= offset
    
    window.fill((0, 0, 0))

    pygame.draw.polygon(window, color, [(left, top), (right, top), (right, bottom), (left, bottom)])

    pygame.display.flip()
    pygame.time.wait(0)

    frames += 1

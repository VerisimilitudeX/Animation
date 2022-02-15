import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

string_color = (240, 240, 240)
yoyo_color = (140, 40, 50)

string_start = (0, 0)
yoyo_x = 200
yoyo_y = 0

offset = 0

frames = 0
while frames < 500:

    offset += 1

    center = (yoyo_x + offset - 50, yoyo_y + offset + 100)

    window.fill((0, 0, 0))

    pygame.draw.line(window, string_color, string_start, center, 3)
    pygame.draw.circle(window, yoyo_color, center, 50)

    pygame.display.flip()
    pygame.time.wait(20)

    frames += 1

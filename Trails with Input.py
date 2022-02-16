import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

bg_color = (0, 0, 0)

offset = 0

trails = input("Do you want to have trails in this animation? y/n\n")


frames = 0
while frames < 100:

    offset += 1

    if trails == "n":
        window.fill((0, 0, 0))

    circles = 11
    while circles > 0:
        circles -= 1
        pygame.draw.circle(window, (200, 0, circles * 20), (offset * circles, circles * 40), 25)

    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1

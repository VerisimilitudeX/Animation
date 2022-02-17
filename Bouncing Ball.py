import pygame

pygame.init()

window = pygame.display.set_mode([800, 300])

x_speed = 2

y_speed = 3

ball_x = 0

ball_y = 0

ceiling_y = 0

floor_y = 285

ceiling_increment = 100

while ball_x < 800:

    ball_x += x_speed

    ball_y += y_speed

    if ball_y > floor_y:

        y_speed = y_speed * -1

        ceiling_y += ceiling_increment
        ceiling_y = int(ceiling_y)

        ceiling_increment = ceiling_increment * 0.5

    if ball_y < ceiling_y:

        y_speed = y_speed * -1

    window.fill((255, 255, 255))

    pygame.draw.circle(window, (142, 42, 242), (ball_x, ball_y), 15)

    pygame.display.flip()

    pygame.time.wait(10)

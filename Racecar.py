import pygame
pygame.init()

window = pygame.display.set_mode([600, 400])

grass_color = (120, 240, 100)
car_color = (160, 20, 20)
road_color = (55, 50, 50)

car_x = 5

car_rect = pygame.Rect(car_x, 150, 50, 30)
road_rect = pygame.Rect(0, 120, 600, 160)

car_offset = 0

speed = 0

frames = 0
while frames < 200:

    car_offset += speed + 1

    car_rect.x = car_x + car_offset

    window.fill(grass_color)
    pygame.draw.rect(window, road_color, road_rect)
    pygame.draw.ellipse(window, car_color, car_rect)

    pygame.display.flip()
    pygame.time.wait(0)

    frames += 1

    if speed % 5 == 0:
        speed += 2

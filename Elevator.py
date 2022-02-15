import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

sky_color = (180, 200, 240)
ground_color = (100, 150, 100)
building_color = (50, 50, 50)
elevator_color = (100, 100, 100)

ground_rect = pygame.Rect(0, 300, 400, 100)
building_rect = pygame.Rect(250, 20, 100, 280)

elevator_start = 240
elevator_rect = pygame.Rect(240, elevator_start, 40, 60)

# Declare an offset for the elevator
offset = 2

frames = 0
while frames < 22:

    # Subtract from offset
    offset -= 1

    # Use the offset to set the elevator rect's y
    elevator_rect.y += offset

    window.fill(sky_color)
    pygame.draw.rect(window, ground_color, ground_rect)
    pygame.draw.rect(window, building_color, building_rect)

    # Draw the elevator
    pygame.draw.rect(window, elevator_color, elevator_rect)

    # Flip and wait every frame
    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1

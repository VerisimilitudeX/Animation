import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

bg_color = (160, 180, 240)
rock_color = (60, 45, 30)
feather_color = (240, 240, 240)

rock_y = 0
feather_y = 0

rock_rect = pygame.Rect(30, rock_y, 60, 60)
feather_rect = pygame.Rect(330, feather_y, 40, 80)

feather_offset = 0
rock_offset = 0

# Declare variable for frame delay
frame_delay = 40

# Declare variables for speed
rock_speed = 2


frames = 0
while frames < 100:

    # Change offset by using speed
    rock_offset += 6
    feather_offset += 2

    rock_rect.y = rock_y + rock_offset
    feather_rect.y = feather_y + feather_offset

    window.fill(bg_color)
    pygame.draw.ellipse(window, rock_color, rock_rect)
    pygame.draw.ellipse(window, feather_color, feather_rect)

    pygame.display.flip()
    pygame.time.wait(frame_delay)

    frames += 1

    # Slow motion
    if frames == 50:
        frame_delay = 100


    # Speed up rock
if frames % 5 == 0:
    rock_speed += 1

import pygame
pygame.init()

window = pygame.display.set_mode([600, 400])

bg_color = (80, 80, 80)
black = (0, 0, 0)

jumper_y = 260
arrow_x = 0

jumper_rect = pygame.Rect(310, jumper_y, 60, 90)
arrow_rect = pygame.Rect(arrow_x, 270, 20, 10)
floor_rect = pygame.Rect(0, 350, 600, 50)
ceiling_rect = pygame.Rect(0, 0, 600, 50)

jumper_offset = 0
arrow_offset = 0
jump_speed = 0

# Declare variable for frame delay
frame_delay = 40

frames = 0
while frames < 100:

    arrow_offset += 8
    jumper_offset += jump_speed

    arrow_rect.x = arrow_x + arrow_offset
    jumper_rect.y = jumper_y + jumper_offset

    window.fill(bg_color)
    pygame.draw.rect(window, black, floor_rect)
    pygame.draw.rect(window, black, ceiling_rect)
    pygame.draw.rect(window, black, arrow_rect)
    pygame.draw.rect(window, black, jumper_rect)

    pygame.display.flip()

    # Change to use the frame delay variable
    pygame.time.wait(frame_delay)

    frames += 1

    if frames == 20:
        jump_speed = -6
    if frames == 40:
        jump_speed = 0
    if frames == 45:
        jump_speed = 8
    if frames == 60:
        jump_speed = 0

    # Turn on slow motion on frame 30
    if frames / 30 == 1:
        frame_delay = 200

    # Turn off slow motion on frame 50
    if frames / 50 == 1:
        frame_delay = 20

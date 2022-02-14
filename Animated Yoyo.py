"""
LESSON: 3.3 - Animation
TECHNIQUE 1: Animating Shapes
PRACTICE 1
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

string_color = (240, 240, 240)
yoyo_color = (140, 40, 50)

string_start = (0, 0)
yoyo_x = 200
yoyo_y = 0

# Declare an offset for the yoyo
offset = 0

frames = 0
while frames < 500:

    # Add to the offset
    offset += 1

    # Use yoyo_x, yoyo_y, and yoyo_offset in a point
    center = (yoyo_x + offset - 50, yoyo_y + offset + 100)

    window.fill((0, 0, 0))

    # Draw a line, then a circle with a radius of
    # your choice to make a yoyo
    pygame.draw.line(window, string_color, string_start, center, 3)
    pygame.draw.circle(window, yoyo_color, center, 50)

    # Flip and wait every frame
    pygame.display.flip()
    pygame.time.wait(20)

    frames += 1


# Turn in your Coding Exercise.

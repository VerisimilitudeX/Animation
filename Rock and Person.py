import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

bg_color = (120, 80, 40)
rock_color = (70, 60, 50)
ground_color = (60, 50, 40)
person_color = (150, 140, 80)

rock_y = -200
person_x = 50

ground_rect = pygame.Rect(0, 340, 400, 60)
rock_rect = pygame.Rect(20, rock_y, 150, 340)
person_rect = pygame.Rect(person_x, 300, 30, 40)

# Declare an offset for the rock and person
rock_offset = 0
person_offset = 0

frames = 0
while frames < 100:

    # Increase the rock offset
    rock_offset += 1

    # If the rock offset is higher than 80,
    # increase the person offset
    if rock_offset > 5:
        person_offset += 2

    # Use the offsets to set the rock rect's y
    # and person rect's x
    rock_rect.y += rock_offset
    person_rect.x += person_offset

    window.fill(bg_color)
    pygame.draw.rect(window, ground_color, ground_rect)

    # Draw the rock rectangle and person ellipse
    pygame.draw.rect(window, rock_color, rock_rect)
    pygame.draw.ellipse(window, person_color, person_rect)

    # Flip and wait every frame
    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1

"""
LESSON: TechSmart Studio Project
EXERCISE: Click Finder
"""

#### ---- SETUP ---- ####

# Libraries
import pygame
pygame.init()

# Variables
total_width = 600
colors = [(0, 0, 0), (255, 0, 0), (255, 130, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255)]

# Create color position list
color_width = int(total_width / len(colors))
color_positions = []
for i in range(len(colors)):
    color_positions.append(i * color_width)

# Window
w = pygame.display.set_mode([total_width, 30])
w.fill((255, 255, 255))


#### ---- MAIN LOOP ---- ####

done = False
while not done:

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        #### ---- CLICK HANDLING ---- ####

        # On click
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Get edge of each rectangle
            for i in range(len(color_positions)):
                edge = color_positions[i]

                # Check if the click is in current rect
                if edge < x and x < edge + color_width:
                    print("Position " + str(i) + ": " + str(colors[i]))
                    break


    #### ---- DRAWING ---- ####

    # For each color rect
    for i in range(len(colors)):

        # Get position
        position = color_positions[i]

        # Draw rectangle
        r = pygame.Rect(position, 0, color_width, 30)
        pygame.draw.rect(w, colors[i], r)

    pygame.display.flip()

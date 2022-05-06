import pygame
pygame.init()

total_width = 600
colors = [(0, 0, 0), (255, 0, 0), (255, 130, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255)]

color_width = int(total_width / len(colors))
color_positions = []
for i in range(len(colors)):
    color_positions.append(i * color_width)

w = pygame.display.set_mode([total_width, 30])
w.fill((255, 255, 255))

done = False
while not done:

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for i in range(len(color_positions)):
                edge = color_positions[i]

                if edge < x and x < edge + color_width:
                    print("Position " + str(i) + ": " + str(colors[i]))
                    break

    for i in range(len(colors)):

        position = color_positions[i]

        r = pygame.Rect(position, 0, color_width, 30)
        pygame.draw.rect(w, colors[i], r)

    pygame.display.flip()

#### ---- SETUP ---- ####

import pygame
pygame.init()
window = pygame.display.set_mode([800, 500])


#### ---- ANIMATION VARIABLES ---- ####

# Draw ship
ship_saucer = pygame.Rect(0, 10, 150, 40)
ship_cabin = pygame.Rect(40, 0, 70, 60)
ship_color = (150, 150, 150)
saucer_y = 130
cabin_y = 120
saucer_start_x = -150
cabin_start_x = -110
ship_speed = 5

# Draw package
package = pygame.Rect(0, 0, 30, 30)
package_x = 385
package_start_y = 145
package_speed = 7

# Animation variables
ship_saucer.y = saucer_y
ship_cabin.y = cabin_y
package.x = package_x
package.y = package_start_y

# Start the animating objects where they begin on screen
ship_offset = 0
package_offset = 510  # the package starts off-screen the first time
packages_delivered = 0


#### ---- ANIMATION LOOP ---- ####

while packages_delivered < 3:

    #### ---- UPDATE POSITIONS ---- ####

    # Move ship
    ship_offset += ship_speed
    ship_saucer.x = saucer_start_x + ship_offset
    ship_cabin.x = cabin_start_x + ship_offset

    ## Move package
    package_offset += package_speed
    package.y = package_start_y + package_offset

    # Reset ship if off-screen
    if ship_saucer.x >= 950:
        ship_offset = 0
        packages_delivered += 1

    # Reset package if ship is halfway across (x is 325)
    if ship_saucer.x == 325:
        package_offset = 0


    #### ---- DRAW ---- ####

    # Draw background
    window.fill((15, 5, 70))
    pygame.draw.circle(window, (45, 185, 225), (400, 900), 500)

    # Make a package using a rectangle
    pygame.draw.rect(window, (50, 175, 35), package)

    # Make a spaceship using two ellipses
    pygame.draw.ellipse(window, ship_color, ship_saucer)
    pygame.draw.ellipse(window, ship_color, ship_cabin)

    # Finish drawing
    pygame.display.flip()
    pygame.time.wait(15)

import random
import pygame
pygame.init()
window = pygame.display.set_mode([300, 500])
frames = 0

l_leg_start = 25

r_leg_start = 150

leg_offset = 0

leg_speed = 4

l_arm_start = 100

r_arm_start = 250

arm_offset = 0

arm_speed = 3

while frames < 250:

    frames += 1
    window.fill((255, 255, 255))

    pygame.draw.circle(window, (0, 0, 0), (150, 75), 50, 1)
    pygame.draw.line(window, (0, 0, 0), (150, 125), (150, 275))

    left_leg = l_leg_start + leg_offset

    right_leg = random.randint(200, 275)

    leg_offset += leg_speed

    if leg_offset > 125 or leg_offset < 0:

        leg_speed = leg_speed * -1.2

    pygame.draw.line(window, (0, 0, 0), (150, 275), (left_leg, 475))
    pygame.draw.line(window, (0, 0, 0), (150, 275), (right_leg, 475))

    left_arm = l_arm_start + arm_offset

    right_arm = r_arm_start - arm_offset

    arm_offset += arm_speed

    if arm_offset > 200:

        arm_offset = 200

        arm_speed = arm_speed * -1.2

    elif arm_offset < 25:

        arm_offset = 25

        arm_speed = arm_speed * -1.2

    pygame.draw.line(window, (0, 0, 0), (25, left_arm), (150, 175))
    pygame.draw.line(window, (0, 0, 0), (275, right_arm), (150, 175))

    pygame.display.flip()

    pygame.time.wait(80)

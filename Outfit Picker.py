import pygame

pygame.init()

shirt_r = int(input("What is the r value for the shirt? "))

shirt_g = int(input("What is the g value for the shirt? "))

shirt_b = int(input("What is the b value for the shirt? "))

pants_r = int(input("What is the r value for the pant? "))

pants_g = int(input("What is the g value for the pant? "))

pants_b = int(input("What is the b value for the pant? "))

shirt_color = (shirt_r, shirt_g, shirt_b)

pants_color = (pants_r, pants_g, pants_b)

window = pygame.display.set_mode([300, 500])

window.fill((255, 255, 255))

black = (0, 0, 0)
pygame.draw.circle(window, black, (150, 125), 50, 1)

pygame.draw.line(window, black, (150, 175), (150, 350))

pygame.draw.line(window, black, (150, 350), (100, 450))

pygame.draw.line(window, black, (150, 350), (200, 450))

pygame.draw.line(window, black, (50, 225), (250, 225))

pygame.draw.polygon(window, shirt_color, [(60, 200), (240, 200), (240, 250), (190, 250), (190, 345), (110, 345), (110, 250), (60, 250)])

pygame.draw.polygon(window, pants_color, [(110, 350), (190, 350), (225, 440), (175, 440), (150, 375), (125, 440), (75, 440)])

pygame.display.flip()

input()


import pygame
pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill((221, 31, 121))
count = 0
animating = True
while count <= 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    frames = 0
    radius = 5
    print("Breathe in...")
    while frames < 300:
        radius += 1
        frames += 1
        pygame.draw.circle(window, (255, 155, 0), (200, 200), radius)
        pygame.display.flip()
        window.fill((221, 31, 121))
        pygame.time.wait(10)
    frames = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    print("Breathe out...")
    while frames < 300:
        radius -= 1
        frames += 1
        pygame.draw.circle(window, (255, 155, 0), (200, 200), radius)
        pygame.display.flip()
        window.fill((221, 31, 121))
        pygame.time.wait(10)

    pygame.time.wait(100)

    frames1 = 2
    radius1 = 5
    print("Breathe in...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames1 < 300:
        radius1 += 1
        frames1 += 1
        pygame.draw.circle(window, (221, 31, 121), (200, 200), radius1)
        pygame.display.flip()
        window.fill((255, 155, 0))
        pygame.time.wait(10)
    frames1 = 0
    print("Breathe out...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames1 < 300:
        radius1 -= 1
        frames1 += 1
        pygame.draw.circle(window, (221, 31, 121), (200, 200), radius1)
        pygame.display.flip()
        window.fill((255, 155, 0))
        pygame.time.wait(10)

    pygame.time.wait(100)

    frames2 = 2
    radius2 = 5
    print("Breathe in...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames2 < 300:
        radius2 += 1
        frames2 += 1
        pygame.draw.circle(window, (21, 31, 121), (200, 200), radius2)
        pygame.display.flip()
        window.fill((221, 31, 121))
        pygame.time.wait(10)
    frames2 = 0
    print("Breathe out...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames2 < 300:
        radius2 -= 1
        frames2 += 1
        pygame.draw.circle(window, (21, 31, 121), (200, 200), radius2)
        pygame.display.flip()
        window.fill((221, 31, 121))
        pygame.time.wait(10)

    pygame.time.wait(100)

    frames3 = 2
    radius3 = 5
    print("Breathe in...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames3 < 300:
        radius3 += 1
        frames3 += 1
        pygame.draw.circle(window, (21, 231, 21), (200, 200), radius3)
        pygame.display.flip()
        window.fill((21, 31, 121))
        pygame.time.wait(10)
    frames3 = 0
    print("Breathe out...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    while frames3 < 300:
        radius3 -= 1
        frames3 += 1
        pygame.draw.circle(window, (21, 231, 21), (200, 200), radius3)
        pygame.display.flip()
        window.fill((21, 31, 121))
        pygame.time.wait(10)

    pygame.time.wait(100)
    count += 1
pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill((221, 31, 121))
frames = 0
radius = 5

while frames < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    radius += 4
    frames += 1
    pygame.draw.circle(window, (255, 155, 0), (200, 200), radius)
    pygame.display.flip()
    window.fill((221, 31, 121))
    pygame.time.wait(10)
frames1 = 2
radius1 = 5
while frames1 < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    radius1 += 4
    frames1 += 1
    pygame.draw.circle(window, (221, 31, 121), (200, 200), radius1)
    pygame.display.flip()
    window.fill((255, 155, 0))
    pygame.time.wait(10)
frames2 = 2
radius2 = 5
while frames2 < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    radius2 += 4
    frames2 += 1
    pygame.draw.circle(window, (21, 31, 121), (200, 200), radius2)
    pygame.display.flip()
    window.fill((221, 31, 121))
    pygame.time.wait(10)
frames3 = 2
radius3 = 5
while frames3 < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    radius3 += 4
    frames3 += 1
    pygame.draw.circle(window, (21, 231, 21), (200, 200), radius3)
    pygame.display.flip()
    window.fill((21, 31, 121))
    pygame.time.wait(10)

b = (0, 0, 0)
r = pygame.Rect(90, 0, 20, 25)
offset = 0
while r.y < 400:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
    r.y += 3
    offset += 2
    window.fill((21, 231, 21))
    pygame.draw.rect(window, b, r)

    pygame.display.flip()
    pygame.time.wait(20)
frames = 0

input("Please press enter to end the program. ")

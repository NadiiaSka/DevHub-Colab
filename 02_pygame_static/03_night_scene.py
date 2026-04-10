# 03_night_scene.py
# A peaceful night scene: moon, house, and rolling hills!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Scene")

# Colors
SKY    = ( 10,  10,  40)
GROUND = ( 30,  80,  30)
HILL   = ( 20,  60,  20)
WHITE  = (255, 255, 255)
YELLOW = (255, 240, 100)
BROWN  = (100,  60,  20)
ORANGE = (220, 120,  40)
GRAY   = (150, 150, 160)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)

    # Hills (drawn as large circles peeking above the ground line)
    pygame.draw.circle(screen, HILL, (150, 520), 200)
    pygame.draw.circle(screen, HILL, (500, 540), 220)
    pygame.draw.circle(screen, HILL, (750, 510), 180)

    # Ground
    pygame.draw.rect(screen, GROUND, (0, 520, WIDTH, HEIGHT - 520))

    # Moon
    pygame.draw.circle(screen, YELLOW, (650, 100), 60)
    pygame.draw.circle(screen, SKY, (675, 85), 50)   # crescent cutout

    # Stars
    star_positions = [(100, 60), (200, 40), (350, 80), (450, 30),
                      (550, 70), (720, 50), (760, 130), (300, 120)]
    for sx, sy in star_positions:
        pygame.draw.circle(screen, WHITE, (sx, sy), 3)

    # House body
    pygame.draw.rect(screen, BROWN, (300, 380, 200, 140))

    # Roof
    pygame.draw.polygon(screen, GRAY, [(280, 385), (520, 385), (400, 270)])

    # Door
    pygame.draw.rect(screen, ORANGE, (375, 460, 50, 60))

    # Windows
    pygame.draw.rect(screen, YELLOW, (320, 410, 50, 40))
    pygame.draw.rect(screen, YELLOW, (430, 410, 50, 40))

    pygame.display.flip()

pygame.quit()

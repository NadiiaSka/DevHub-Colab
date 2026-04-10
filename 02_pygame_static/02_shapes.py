# 02_shapes.py
# Draw circles, squares, and lines with pygame!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes!")

# Colors (R, G, B)
WHITE  = (255, 255, 255)
RED    = (220,  50,  50)
GREEN  = ( 50, 200,  50)
BLUE   = ( 50, 100, 220)
YELLOW = (255, 220,   0)
BG     = ( 20,  20,  40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # Rectangle: (surface, color, (x, y, width, height))
    pygame.draw.rect(screen, RED, (50, 50, 150, 100))

    # Circle: (surface, color, (center_x, center_y), radius)
    pygame.draw.circle(screen, GREEN, (400, 150), 80)

    # Filled circle
    pygame.draw.circle(screen, YELLOW, (650, 150), 60)

    # Line: (surface, color, start_point, end_point, thickness)
    pygame.draw.line(screen, WHITE, (50, 400), (750, 400), 5)

    # Triangle using polygon
    pygame.draw.polygon(screen, BLUE, [(400, 250), (300, 450), (500, 450)])

    pygame.display.flip()

pygame.quit()

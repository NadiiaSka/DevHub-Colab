# 02_keyboard.py
# Move a shape around with the arrow keys!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move with Arrow Keys")

clock = pygame.time.Clock()

# Player square
square_x = WIDTH // 2
square_y = HEIGHT // 2
square_size = 50
square_color = pygame.Color("deepskyblue")
SPEED = 5

BG = pygame.Color("midnightblue")

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read which keys are held down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        square_x -= SPEED
    if keys[pygame.K_RIGHT]:
        square_x += SPEED
    if keys[pygame.K_UP]:
        square_y -= SPEED
    if keys[pygame.K_DOWN]:
        square_y += SPEED

    # Keep player inside the window
    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    screen.fill(BG)
    pygame.draw.rect(screen, square_color,
                     (square_x, square_y, square_size, square_size),
                     border_radius=8)
    pygame.display.flip()

pygame.quit()

# 03_drawing_app.py
# A simple drawing app!
# - Hold left mouse button to draw
# - Press C to clear the canvas
# - Press 1-7 to change color
# - Press +/- to change brush size

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

PALETTE = [
    (255, 255, 255),   # 1 white
    (255,  80,  80),   # 2 red
    (255, 180,  50),   # 3 orange
    (255, 240,  50),   # 4 yellow
    ( 80, 220,  80),   # 5 green
    ( 80, 150, 255),   # 6 blue
    (200,  80, 255),   # 7 purple
]

BG = (30, 30, 30)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG)

current_color = PALETTE[0]
brush_size = 8

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                canvas.fill(BG)   # Clear
            # Number keys 1-7 change color
            for i, key in enumerate([pygame.K_1, pygame.K_2, pygame.K_3,
                                      pygame.K_4, pygame.K_5, pygame.K_6,
                                      pygame.K_7]):
                if event.key == key:
                    current_color = PALETTE[i]
            if event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                brush_size = min(60, brush_size + 2)
            if event.key == pygame.K_MINUS:
                brush_size = max(2, brush_size - 2)

    # Draw while mouse button is held
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, current_color, (mx, my), brush_size)

    screen.blit(canvas, (0, 0))

    # HUD
    tip = font.render(
        f"Color: 1-7 | Size: {brush_size} (+/-) | Clear: C",
        True, (180, 180, 180)
    )
    screen.blit(tip, (10, 10))

    # Color swatches
    for i, col in enumerate(PALETTE):
        rect = pygame.Rect(10 + i * 36, HEIGHT - 44, 30, 30)
        pygame.draw.rect(screen, col, rect, border_radius=5)
        if col == current_color:
            pygame.draw.rect(screen, (255, 255, 255), rect, 3, border_radius=5)

    pygame.display.flip()

pygame.quit()

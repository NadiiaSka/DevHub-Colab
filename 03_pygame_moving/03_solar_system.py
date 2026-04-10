# 03_solar_system.py
# Planets orbiting the Sun using math.sin and math.cos!

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

clock = pygame.time.Clock()

SUN_X = WIDTH // 2
SUN_Y = HEIGHT // 2

# Each planet: (color, orbit_radius, size, speed, start_angle)
planets = [
    {"color": (180, 140, 100), "orbit": 80,  "size": 10, "speed": 0.04, "angle": 0.0},   # Mercury
    {"color": (220, 180,  80), "orbit": 130, "size": 14, "speed": 0.025,"angle": 1.0},   # Venus
    {"color": ( 60, 120, 220), "orbit": 185, "size": 15, "speed": 0.018,"angle": 2.0},   # Earth
    {"color": (200,  80,  50), "orbit": 245, "size": 12, "speed": 0.012,"angle": 0.5},   # Mars
]

BG = (5, 5, 20)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # Draw orbit rings
    for p in planets:
        pygame.draw.circle(screen, (40, 40, 60), (SUN_X, SUN_Y), p["orbit"], 1)

    # Sun
    pygame.draw.circle(screen, (255, 220, 50), (SUN_X, SUN_Y), 35)

    # Draw and update each planet
    for p in planets:
        px = SUN_X + int(math.cos(p["angle"]) * p["orbit"])
        py = SUN_Y + int(math.sin(p["angle"]) * p["orbit"])
        pygame.draw.circle(screen, p["color"], (px, py), p["size"])
        p["angle"] += p["speed"]   # advance the orbit angle

    pygame.display.flip()

pygame.quit()

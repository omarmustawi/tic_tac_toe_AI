from constants import *
import pygame
# Draw the O (circle)
def draw_circle(row, col, screen):
    x = col * WIDTH // 3 + WIDTH // 6
    y = row * HEIGHT // 3 + HEIGHT // 6
    pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS, LINE_WIDTH)

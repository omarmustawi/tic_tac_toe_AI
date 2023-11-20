import pygame
from constants import *
# Draw the X (cross)


def draw_cross(row, col, screen):
    x = col * WIDTH // 3 + WIDTH // 6
    y = row * HEIGHT // 3 + HEIGHT // 6
    # print("x:", x, " ,y: ", y)
    # print("row:", row, " ,col: ", col)
    # print("(x - CROSS_WIDTH, y - CROSS_WIDTH):", (x - CROSS_WIDTH, y - CROSS_WIDTH),
    #       " ,(x + CROSS_WIDTH, y + CROSS_WIDTH): ", (x + CROSS_WIDTH, y + CROSS_WIDTH))
    pygame.draw.line(screen, CROSS_COLOR, (x - CROSS_WIDTH, y -
                     CROSS_WIDTH), (x + CROSS_WIDTH, y + CROSS_WIDTH), LINE_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (x + CROSS_WIDTH, y -
                     CROSS_WIDTH), (x - CROSS_WIDTH, y + CROSS_WIDTH), LINE_WIDTH)

import pygame
import sys
import copy
from constants import *
from game_logic import *
from draw_circle import draw_circle
from draw_cross import draw_cross
from draw_grid import draw_grid
from minmax import minimax
from pygame.font import Font


# Initialize Pygame
pygame.init()

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)


# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Main game loop
running = True
player_turn = True  # True for player X, False for player O
while running:
    draw_grid(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            # Player's turn
            col = event.pos[0] // (WIDTH // 3)
            row = event.pos[1] // (HEIGHT // 3)
            # print("event.pos[0]: ", event.pos[0] , " event.pos[1]: " , event.pos[1] )
            if board[row][col] == ' ':
                board[row][col] = 'X'
                draw_cross(row, col, screen)
                player_turn = not player_turn

    # AI's turn (O)
    if not player_turn:
        best_move = None
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = 'O'
                    score = minimax(new_board, 0, False)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            row, col = best_move
            board[row][col] = 'O'
            draw_circle(row, col, screen)
            player_turn = not player_turn

    # Check for a winner or tie
    if check_winner(board, 'X'):
        text_alert = "X is winner "
        running = False
    elif check_winner(board, 'O'):
        text_alert = "O is winner "
        running = False
    elif check_tie(board):
        text_alert = "It's a tie!"
        running = False

    # Update the display
    pygame.display.flip()

    font = Font(None, 150)

    # Display the alert text
    if not running:
        text_surface = font.render( text_alert, True, (255, 150, 150))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

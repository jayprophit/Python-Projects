# Connect 4 Game by @JayProphit

# Import required packages
import numpy as np
import pygame
import sys
import math

# Global settings (constants)
BLUE = (0, 0, 255)      # Background color for the board
BLACK = (0, 0, 0)       # Empty cell color
RED = (255, 0, 0)       # Player 1 piece color
YELLOW = (255, 255, 0)  # Player 2 piece color

ROW_COUNT = 6           # Number of rows in the board
COLUMN_COUNT = 7        # Number of columns in the board
SQUARESIZE = 100        # Size of each square in pixels
RADIUS = int(SQUARESIZE / 2 - 5)  # Radius of the pieces

# Screen dimensions
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

# Create the game board (2D array initialized with zeros)
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

# Drop a piece in the specified row and column
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if the selected column is valid for a move
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Find the next open row in the specified column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Print the board in terminal (flipped for proper orientation)
def print_board(board):
    print(np.flip(board, 0))

# Check if the current player has a winning move
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (board[r][c] == piece and board[r][c + 1] == piece and
                board[r][c + 2] == piece and board[r][c + 3] == piece):
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and board[r + 1][c] == piece and
                board[r + 2][c] == piece and board[r + 3][c] == piece):
                return True

    # Check positively sloped diagonals for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and board[r + 1][c + 1] == piece and
                board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece):
                return True

    # Check negatively sloped diagonals for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (board[r][c] == piece and board[r - 1][c + 1] == piece and
                board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True

# Draw the game board and pieces
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Draw the board (blue background)
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # Draw the black circles (empty cells)
            pygame.draw.circle(screen, BLACK, 
                               (int(c * SQUARESIZE + SQUARESIZE / 2), 
                                int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), 
                               RADIUS)
    
    # Draw the pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, 
                                   (int(c * SQUARESIZE + SQUARESIZE / 2), 
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), 
                                   RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, 
                                   (int(c * SQUARESIZE + SQUARESIZE / 2), 
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), 
                                   RADIUS)
    pygame.display.update()

# Initialize the game
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
board = create_board()
draw_board(board)
pygame.display.update()
font = pygame.font.SysFont("monospace", 75)

game_over = False
turn = 0  # Alternates between 0 (Player 1) and 1 (Player 2)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Show the piece above the board as the player hovers
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        # Handle mouse click for a move
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                piece = 1 if turn == 0 else 2
                drop_piece(board, row, col, piece)

                if winning_move(board, piece):
                    label = font.render(f"Player {piece} Wins!!", 1, RED if piece == 1 else YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                draw_board(board)
                turn = (turn + 1) % 2

                if game_over:
                    pygame.time.wait(3000)
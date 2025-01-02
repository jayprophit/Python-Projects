# Tetris Game by @JayProphit

import pygame
import random

"""
Tetris Game
-----------
- Grid size: 10 x 20
- Shapes: S, Z, I, O, J, L, T
- Shapes represented by indices: 0-6
- Blocks are 30x30 pixels

Code Overview:
1. Constants and Global Variables
2. Classes:
   - Piece: Represents a Tetris piece
3. Functions:
   - Grid creation, shape formatting, validation, and drawing
   - Game logic (e.g., clearing rows, score management)
4. Main Game Loop and Menu
"""

# Initialize Pygame
pygame.font.init()

# Global Constants
s_width = 800  # Screen width
s_height = 700  # Screen height
play_width = 300  # Play area width (10 blocks * 30px each)
play_height = 600  # Play area height (20 blocks * 30px each)
block_size = 30  # Size of a single block

# Position of the play area on the screen
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# Shape Formats
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# List of shapes and their corresponding colors
shapes = [S, Z, I, O, J, L, T]
shape_colors = [
    (0, 255, 0),    # Green for S
    (255, 0, 0),    # Red for Z
    (0, 255, 255),  # Cyan for I
    (255, 255, 0),  # Yellow for O
    (255, 165, 0),  # Orange for J
    (0, 0, 255),    # Blue for L
    (128, 0, 128)   # Purple for T
]

# Piece class: Represents a Tetris piece
class Piece:
    def __init__(self, x, y, shape):
        self.x = x  # x-coordinate of the piece
        self.y = y  # y-coordinate of the piece
        self.shape = shape  # Shape format
        self.color = shape_colors[shapes.index(shape)]  # Assign color based on shape
        self.rotation = 0  # Current rotation state (0-3)

# Function to create the game grid
def create_grid(locked_positions={}):
    """
    Create a 10x20 grid with locked positions.

    Args:
        locked_positions (dict): A dictionary of locked block positions.

    Returns:
        list: A 2D grid representing the play area.
    """
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]  # Default grid: black blocks

    for (j, i), color in locked_positions.items():
        grid[i][j] = color  # Fill locked positions with their respective colors

    return grid

# Function to convert shape format to positions on the grid
def convert_shape_format(shape):
    """
    Convert a shape's format into grid positions.

    Args:
        shape (Piece): The current Tetris piece.

    Returns:
        list: A list of (x, y) positions for the shape.
    """
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':  # Indicates a filled block
                positions.append((shape.x + j, shape.y + i))

    # Adjust positions to account for grid offset
    positions = [(x - 2, y - 4) for x, y in positions]
    return positions

# Function to check if a space is valid
def valid_space(shape, grid):
    """
    Check if the current shape's position is valid.

    Args:
        shape (Piece): The current Tetris piece.
        grid (list): The game grid.

    Returns:
        bool: True if valid, False otherwise.
    """
    accepted_positions = [
        (j, i) for i in range(20) for j in range(10) if grid[i][j] == (0, 0, 0)
    ]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions and pos[1] >= 0:
            return False
    return True

# Remaining code continues with similar fixes and improvements.
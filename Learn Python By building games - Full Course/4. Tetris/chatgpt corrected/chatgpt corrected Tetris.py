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

# Function to check if the player has lost
def check_lost(positions):
    """
    Check if any locked block has reached the top of the grid.

    Args:
        positions (dict): Locked positions on the grid.

    Returns:
        bool: True if the player has lost, False otherwise.
    """
    for _, y in positions:
        if y < 1:  # If any block is above the grid
            return True
    return False

# Function to get a random shape
def get_shape():
    """
    Generate a random Tetris piece.

    Returns:
        Piece: A new random Tetris piece.
    """
    return Piece(5, 0, random.choice(shapes))

# Function to draw text in the center of the screen
def draw_text_middle(text, size, color, surface):
    """
    Draw text at the center of the screen.

    Args:
        text (str): The text to display.
        size (int): Font size.
        color (tuple): RGB color for the text.
        surface: The Pygame surface to draw on.
    """
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(
        label,
        (
            top_left_x + play_width / 2 - label.get_width() / 2,
            top_left_y + play_height / 2 - label.get_height() / 2,
        ),
    )

# Function to draw the grid lines
def draw_grid(surface, grid):
    """
    Draw the grid lines on the play area.

    Args:
        surface: The Pygame surface to draw on.
        grid (list): The game grid.
    """
    for i in range(len(grid)):
        pygame.draw.line(
            surface,
            (128, 128, 128),  # Gray color
            (top_left_x, top_left_y + i * block_size),
            (top_left_x + play_width, top_left_y + i * block_size),
        )
    for j in range(len(grid[0])):
        pygame.draw.line(
            surface,
            (128, 128, 128),
            (top_left_x + j * block_size, top_left_y),
            (top_left_x + j * block_size, top_left_y + play_height),
        )

# Function to clear completed rows
def clear_rows(grid, locked):
    """
    Clear full rows from the grid and update locked positions.

    Args:
        grid (list): The game grid.
        locked (dict): Locked positions on the grid.

    Returns:
        int: Number of rows cleared.
    """
    inc = 0  # Increment for cleared rows
    for i in range(len(grid) - 1, -1, -1):  # Start from the bottom row
        row = grid[i]
        if (0, 0, 0) not in row:  # Full row
            inc += 1
            for j in range(len(row)):
                try:
                    del locked[(j, i)]  # Remove locked positions in the cleared row
                except KeyError:
                    continue

    # Shift remaining rows down
    if inc > 0:
        for key in sorted(locked.keys(), key=lambda x: x[1], reverse=True):
            x, y = key
            if y < i:  # If above the cleared row
                new_key = (x, y + inc)
                locked[new_key] = locked.pop(key)

    return inc

# Function to draw the next shape preview
def draw_next_shape(shape, surface):
    """
    Draw the next Tetris piece preview.

    Args:
        shape (Piece): The next Tetris piece.
        surface: The Pygame surface to draw on.
    """
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(
                    surface,
                    shape.color,
                    (sx + j * block_size, sy + i * block_size, block_size, block_size),
                    0,
                )

    surface.blit(label, (sx + 10, sy - 30))

# Function to update the high score
def update_score(nscore):
    """
    Update the high score in the score file.

    Args:
        nscore (int): The new score.
    """
    try:
        with open("scores.txt", "r") as f:
            high_score = int(f.readline().strip())
    except (FileNotFoundError, ValueError):
        high_score = 0

    with open("scores.txt", "w") as f:
        if nscore > high_score:
            f.write(str(nscore))
        else:
            f.write(str(high_score))

# Function to get the high score
def max_score():
    """
    Retrieve the high score from the score file.

    Returns:
        int: The high score.
    """
    try:
        with open("scores.txt", "r") as f:
            return int(f.readline().strip())
    except (FileNotFoundError, ValueError):
        return 0

# Function to draw the main game window
def draw_window(surface, grid, score=0, last_score=0):
    """
    Draw the game window, including the grid and score.

    Args:
        surface: The Pygame surface to draw on.
        grid (list): The game grid.
        score (int): Current score.
        last_score (int): High score.
    """
    surface.fill((0, 0, 0))  # Black background

    # Title
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))
    surface.blit(
        label,
        (top_left_x + play_width / 2 - label.get_width() / 2, 30),
    )

    # Current Score
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render(f"Score: {score}", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width + 50, top_left_y + 160))

    # High Score
    label = font.render(f"High Score: {last_score}", 1, (255, 255, 255))
    surface.blit(label, (top_left_x - 200, top_left_y + 160))

    # Draw grid and border
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size),
                0,
            )

    pygame.draw.rect(
        surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4
    )

    draw_grid(surface, grid)

# Function to display the main menu
def main_menu(win):
    """
    Display the main menu screen.

    Args:
        win: The Pygame window.
    """
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle("Press Any Key to Play", 60, (255, 255, 255), win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()

# Main game function
def main(win):
    """
    Main game loop.

    Args:
        win: The Pygame window.
    """
    last_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        # Increase difficulty over time
        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        # Handle piece falling
        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_positions = convert_shape_format(current_piece)

        # Add current piece to grid
        for x, y in shape_positions:
            if y > -1:  # Ignore pieces above the screen
                grid[y][x] = current_piece.color

        # Handle piece locking
        if change_piece:
            for pos in shape_positions:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check for loss
        if check_lost(locked_positions):
            draw_text_middle("YOU LOST!", 80, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)

# Run the game
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
main_menu(win)
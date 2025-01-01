# by @jayprophit
# Snake Game in Pygame

# Import necessary libraries
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Cube class to represent each block of the snake and the snack
class Cube:
    rows = 20  # Number of rows in the grid
    w = 500  # Width of the game window

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        """
        Initialize a cube.
        :param start: Starting position of the cube (x, y).
        :param dirnx: Direction of movement in the x-axis.
        :param dirny: Direction of movement in the y-axis.
        :param color: Color of the cube.
        """
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        """
        Update the cube's direction and position.
        """
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        """
        Draw the cube on the screen.
        :param surface: Pygame surface to draw on.
        :param eyes: Whether to draw eyes (for the snake's head).
        """
        dis = self.w // self.rows
        i, j = self.pos

        # Draw the cube
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        # Draw eyes if it's the snake's head
        if eyes:
            center = dis // 2
            radius = 3
            circle_middle1 = (i * dis + center - radius, j * dis + 8)
            circle_middle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle1, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


# Snake class to represent the player-controlled snake
class Snake:
    def __init__(self, color, pos):
        """
        Initialize the snake.
        :param color: Color of the snake.
        :param pos: Starting position of the snake's head.
        """
        self.color = color
        self.head = Cube(pos)  # Snake's head is a cube
        self.body = [self.head]  # List of cubes making up the snake
        self.turns = {}  # Dictionary to track turns
        self.dirnx = 0  # Direction in the x-axis
        self.dirny = 1  # Direction in the y-axis

    def move(self):
        """
        Handle snake movement and user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            pos = c.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                # Wrap around the edges of the screen
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        """
        Reset the snake to its initial state.
        """
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        """
        Add a new cube to the snake.
        """
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        """
        Draw the snake on the screen.
        """
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # Draw eyes for the head
            else:
                c.draw(surface)


# Helper functions
def draw_grid(w, rows, surface):
    """
    Draw the grid on the screen.
    """
    size_btwn = w // rows

    for i in range(rows):
        x = i * size_btwn
        y = i * size_btwn
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    """
    Update the game window.
    """
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, snake):
    """
    Generate a random position for the snack.
    """
    positions = [cube.pos for cube in snake.body]

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if (x, y) not in positions:
            break

    return x, y


def message_box(subject, content):
    """
    Display a message box.
    """
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    """
    Main function to run the game.
    """
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, s), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        # Check if the snake eats the snack
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(0, 255, 0))

        # Check if the snake collides with itself
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score:', len(s.body))
                message_box('You Lost', 'Play again...')
                s.reset((10, 10))
                break

        redraw_window(win)


# Run the game
main()
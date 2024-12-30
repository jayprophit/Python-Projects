# by @JayProphit
# part 3

'''
game name: connect 4

index:-
np = numpy
col = column
'''



# imports numpy package, set numpy to be defined as np
import numpy as np
import pygame
import sys


# global
BLUE = (0,0,255)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT =7



# defines the board specifications
def create_board(
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))):
    return board



# drops the player 1 or player 2 piece in the correct row and column
def drop_piece(board, row, col, piece):
    boared[row][col] = piece



# defines if its the valid location
def is_valid_location(board, col):
    # check to see if the 5th col is available without an input
    return board[ROW_COUNT-1][col] == 0



# gets the next open row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        # if the row is equal to 0 (empty), return the 1st instance of an empty row and column
        if board[r][col] == 0:
            return r



# change the orientation of the board, flips board to right side up
def print_board(board):
    print(np.flip(board, 0))



# this is for all winning directions
# shows who's the winner
def winning_move(board, piece):
    # check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check virtical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # check positively sloped diaganol locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check neatively sloped diaganol locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c-2] == piece and board[r-3][c+3] == piece:
                return True



# draw board with pygame graphics
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # draws a blue screen
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draws black circles
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)



# creates board
board = create_board()

# prints board
print_boaard(board)

# defines if the game is over on in play
game_over = False

#defines turn amount
turn = 0



# initialize pygame
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()



# defines what happens if the game is not over 
while not game_over:

    # this allows the screen event to continue and not close
    for event in pygame.event.get():
        if event type == pygame.QUIT:
            sys.exit()

        # this allows the use of a mouse to be detected
        if event.type == pygame.MOUSEBUTTONDOWN:
            continue


            # ask for player 1 input
            if turn == 0:
                # col = colunm
                col = int(input("Player 1 make your Selection (0-6):"))

                # checks if its a valid location on the board
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # checks for winning move
                    if winning_move(board, 1):
                        print("Player 1 Wins!!! Congrats!!!")
                        game_over = True

            # askfor player 2 input
            else:
                col = int(input("Player 2 make your Selection (0-6):"))

                # checks if its a valid location on the board
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    # checks for winning move
                    if winning_move(board, 2):
                        print("Player 2 Wins!!! Congrats!!!")
                        game_over = True
                        '''break'''



            # prints board
            print_board(board)

            # increase turn by 1
            turn += 1
            # turns its to odd even, meaning take what ever our turn is and divides it by 2 (alternating between player 1 and 2)
            turn = turn % 2

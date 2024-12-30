# by @JayProphit
# part 3

'''
game name: connect four

index:-
np = numpy
col = column
'''

# global
ROW_COUNT = 6
COLUMN_COUNT =7

# imports numpy package, set numpy to be defined as np
import numpy as np

# defines the board specifications
def create_board(
    board = np.zeros((6,7)))
    return board

# drops the player 1 or player 2 piece in the correct row and column
def drop_piece(board, row, col, piece):
    boared[row][col] = piece

# defines if its the valid location
def is_valid_location(board, col):
    # check to see if the 5th col is available without an input
    return board[5][col] == 0

# gets the next open row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        # if the row is equal to 0 (empty), return the 1st instance of an empty row and column
        if board[r][col] == 0:
            return r

# change the orientation of the board, flips board to right side up
def print_board(board):
    print(np.flip(board, 0))

# creates board
board = create_board()
# prints board
print_boaard(board)

# defines if the game is over on in play
game_over = False

#defines turn amount
turn = 0

# defines what happens if the game is not over 
while not game_over:
    # ask for player 1 input
    if turn == 0:
        # col = colunm
        col = int(input("Player 1 make your Selection (0-6):"))

        # checks if its a valid location on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    # askfor player 2 input
    else:
        col = int(input("Player 2 make your Selection (0-6):"))

        # checks if its a valid location on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    # prints board
    print_board(board)

    # increase turn by 1
    turn += 1
    # turns its to odd even, meaning take what ever our turn is and divides it by 2 (alternating between player 1 and 2)
    turn = turn % 2
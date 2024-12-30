'''
connect four
'''
# imports numpy package, set numpy to be defined as np
import numpy as np

# defines the board specifications
def create_board(
    board = np.zeros((6,7)))
    return board

# drops the player 1 or player 2 piece
def drop_piece()
    pass

# defines if its the valid location
def is_valid_location():
    pass

# gets the next open row
def get_next_open_row():
    pass

# creates board
board = create_board()

# defines if the game is over on in play
game_over = False

#defines turn amount
turn = 0

# defines what happens if the game is not over 
while not game_over:
    # ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1 make your Selection (0-6):"))

        '''
        print(selection)
        print(type(selectiojn))
        '''
    # askfor player 2 input
    else:
        selection = int(input("Player 2 make your Selection (0-6):"))

    # increase turn by 1
    turn += 1
    # turns its to odd even, meaning take what ever our turn is and divide it by 2 (alternating between player 1 and 2)
    turn = turn % 2
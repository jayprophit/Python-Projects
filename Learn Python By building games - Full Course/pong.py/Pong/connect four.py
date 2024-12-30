'''
connect four
'''
# imports numpy function, set numpy to be defined as np
import numpy as np

# defines the board specifications
def create_board(
    board = np.zeros((6,7)))
    return board

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
        selection = input("Player 1 make your Selection (0-6):")

    # askfor player 2 input
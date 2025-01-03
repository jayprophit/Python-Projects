# by @JayProphit
# part 3

'''
game name: Connect 4

index:-
np = numpy
col = column
'''


'''these are importated packages with functions'''
# imports numpy package, set numpy to be defined as np
import numpy as np
import pygame
import sys
import math



'''these are set global settings that can not be changed'''
# global - set specification by definition that can not be changed
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT =7



'''defines board specifications'''
# defines the board specifications
def create_board(
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))):
    return board



''' drops players piece'''
# drops the player 1 or player 2 piece in the correct row and column
def drop_piece(board, row, col, piece):
    board[row][col] = piece



'''defines if the piece is in the correct location'''
# defines if its the valid location
def is_valid_location(board, col):
    # check to see if the 5th col is available without an input
    return board[ROW_COUNT-1][col] == 0



'''looks for the next available space'''
# gets the next open row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        # if the row is equal to 0 (empty), return the 1st instance of an empty row and column
        if board[r][col] == 0:
            return r



'''flip the orientation of th bord 180 degress'''
# change the orientation of the board, flips board to right side up
def print_board(board):
    print(np.flip(board, 0))



'''cheecks for a 4 count in four directions:- horizontal, vertical, positive diaganal, negative diaganal'''
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



'''draws graphics with pygame package'''
# draw board with pygame graphics
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # draws a blue screen
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draws black circles
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)


    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                # draws red circles
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                # draws yellow circles
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


'''generates board'''
# creates board
board = create_board()

'''prints board to screen'''
# prints board
print_board(board)

'''defines if the game is still active or has reached a result'''
# defines if the game is over on in play
game_over = False

'''defines how many turns are available'''
#defines turn amount
turn = 0



'''initiates pygame package'''
# initialize pygame
pygame.init()

'''defines the size and shape of board'''
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

'''defines grahical display of pygame package'''
screen = pygame.display.set_mode(size)
draw_board(board)

'''updates display'''
pygame.display.update()

# screen font
myfont = pygame.font.SysF("monospace", 75)


'''defines what happens, (whilst game is in loop) if the game has not reached a result'''
# defines what happens if the game is not over 
while not game_over:


    # this allows the screen event to continue and not close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        # this detects when the mouse button is pressed
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            pos = event.pos[o]
            if turn == o:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()


        # this allows the use of a mouse to be detected
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            '''int(input("Player 1 make your Selection (0-6):"))'''


            # checks if its a valid location on the board
            if is_valid_location(board, col):

                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))

                # print(event.pos)
                # ask for player 1 input

                if turn == 0:
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)


                    # checks for winning move
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 Wins!!", 1, RED)
                        '''print("Player 1 Wins!!! Congrats!!!")'''
                        # updates that specific part of the screen 
                        screen.blit(label, (40, 10))
                        game_over = True


            # askfor player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE)) 
                '''int(input("Player 2 make your Selection (0-6):"))'''


                # checks if its a valid location on the board
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)


                    # checks for winning move
                    if winning_move(board, 2):
                        label = myfont.render("Player 2 Wins!!", 1, YELLOW)
                        '''print("Player 2 Wins!!! Congrats!!!")'''
                        # updates that specific part of the screen 
                        screen.blit(label, (40, 10))
                        game_over = True
                        #break



            # prints board
            print_board(board)

            # draw board
            draw_board(board)

            # increase turn by 1
            turn += 1
            # turns its to odd even, meaning take what ever our turn is and divides it by 2 (alternating between player 1 and 2)
            turn = turn % 2

            # wait function
            if game_over:
                pygame.timer.wait(3000)
# by @JayProphit
# part 4

'''
game name: Tetris

index:-

'''


import pygame
import random



# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main



"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""



pygame.font.init()



# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300    # meaning 300 // 10 = 30 width per block
play_height = 600   # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height



'''defines shapes'''
# SHAPE FORMATS

S = [[\'.....\',
    \'.....\',
    \'..00.\',
    \'.00..\',
    \'.....\'],
    \'.....\',
    \'..0..\',
    \'..00.\',
    \'...0.\',
    \'.....\']]

Z = [[\'.....\',
    \'.....\',
    \'.00..\',
    \'..00.\',
    \'.....\'],
    [\'.....\',
    \'..0..\',
    \'.00..\',
    \'.0...\',
    \'.....\']]

I = [[\'..0..\',
    \'..0..\',
    \'..0..\',
    \'..0..\',
    \'.....\'],
    [\'.....\',
    \'0000.\',
    \'.....\',
    \'.....\',
    \'.....\']]

O = [[\'.....\',
    \'.....\',
    \'.00..\',
    \'.00..\',
    \'.....\']]

J = [[\'.....\',
    \'.0...\',
    \'.000.\',
    \'.....\',
    \'.....\'],
    [\'.....\',
    \'..00.\',
    \'..0..\',
    \'..0..\',
    \'.....\'],
    [\'.....\',
    \'.....\',
    \'.000.\',
    \'...0.\',
    \'.....\'],
    [\'.....\',
    \'..0..\',
    \'..0..\',
    \'.00..\',
    \'.....\']]

L = [[\'.....\',
    \'...0.\',
    \'.000.\',
    \'.....\',
    \'.....\'],
    [\'.....\',
    \'..0..\',
    \'..0..\',
    \'..00.\',
    \'.....\'],
    [\'.....\',
    \'.....\',
    \'.000.\',
    \'.0...\',
    \'.....\'],
    [\'.....\',
    \'.00..\',
    \'..0..\',
    \'..0..\',
    \'.....\']]

T = [[\'.....\',
    \'..0..\',
    \'.000.\',
    \'.....\',
    \'.....\'],
    [\'.....\',
    \'..0..\',
    \'..00.\',
    \'..0..\',
    \'.....\'],
    [\'.....\',
    \'.....\',
    \'.000.\',
    \'..0..\',
    \'.....\'],
    [\'.....\',
    \'..0..\',
    \'.00..\',
    \'..0..\',
    \'.....\']]


'''sets shape colors'''
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0,255,0), (255,0,0), (0,255,255), (255,255,0), (255,165,0), (0,0,255), (128,0,128)]
# index 0-6 represent shape



'''class objects'''
class Piece(object):
    pass



'''creates grid'''
def create_grid(locked_positions={}):
    pass



'''converts shape'''
def convert_shape_format(shape):
    pass



'''validates space'''
def valid_space(shape, grid):
    pass



'''checks for lost'''
def check_lost(positions):
    pass



'''gets shape'''
def get_shape():
    pass



'''draws text'''
def draw_text_middle(text, size, color, surface):
    pass



'''draws grid'''
def draw_grid(surface, row, col):
    pass



'''clears rows'''
def clear_rows(grid, locked):



'''draws next shape'''
def draw_next_shape(shape, surface):



'''draws window'''
def draw_window(surface):
    pass



'''defines main'''
def main():
    pass



'''defines main menu'''
def main_menu():
    pass



main_menu() # start game
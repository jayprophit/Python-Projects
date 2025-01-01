# by @JayProphit
# part 4

'''
game name: Tetris

index:-

'''

import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0-6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300 # meaning 300 // 10 = 30 width per block
play_height = 600 # meaing 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height 



'''tetris object shapes'''
# SHAPE FORMATS

S = [[
    '.....',
    '.....',
    '..00.',
    '.00..',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....',]]
    
Z = [[
    '.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....',]]
    
I = [[
    '..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '0000.',
    '.....',
    '.....',
    '.....',]]

O = [[
    '.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]

J = [[
    '.....',
    '.....',
    '.0...',
    '.000.',
    '.....'],
    ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....',]
    ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....',]
    ['.....',
    '..0..',
    '..0..',
    '.00..',
    '.....',]]

L = [[
    '.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '..00.',
    '.....',]
    ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....',]
    ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....',]]
    

T = [[
    '.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '..0..',
    '.....',]
    ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....',]
    ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....',]]

'''tetris shape colors'''
shapes = [S, Z, I, O, J, L, T]
SHAPE_COLORS = [(0,255,0), (255,0,0), (0,255,255), (255,255,0), (255,165,0), (0,0,255), (128,0,128)]
# index 0-6 represent shape


'''piece'''
class piece(object):    # *
    pass



'''creates grid'''
def create_grid(locked_pos = {}):   # *
    pass



'''coverts shapes'''
def convert_shape_format():
    pass



'''defines valid space'''
def valid_space():
    pass



'''checks lost'''
def check_lost():
    pass



'''get shape'''
def get_shape():    # *
    pass



'''draw text middle'''
def draw_text_middle():
    pass



'''draws grid'''
def draw_grid():    # *
    pass



'''clears row'''
def clear_rows():
    pass



'''draws next shape'''
def draw_next_shape():
    pass



'''draws window'''
def draw_window():  # *
    pass


'''runs main game'''
def main(): # *
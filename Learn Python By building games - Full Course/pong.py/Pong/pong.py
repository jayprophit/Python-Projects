# by @JayProphit
# part 1 : Getting started

'''
Pong
'''
# import tutrle function
import turtle

# window screen
win = turtle.Screen()
# window title
win.tittle(" Pong by @JayProphit")
# background color
win.bgcolor("black")
# widows dimensions, width and height in pixels
win.setup(width=800, height=600)
# stops the window from updating, which means you have to manually update, this also lets us speed up the game
win.tracer(0)


# Main game loop
while True:
    # every time the loop runs, it updates the screen
    win.date()

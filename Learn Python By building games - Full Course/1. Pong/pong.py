# by @JayProphit
# part 1 : Getting started

'''
game name: Pong

index:-
win= window
'''


# import tutrle function
import turtle
import os
'''
# microsoft windows sound import
import winsound
'''



# window screen
win = turtle.Screen()
# window title
win.title(" Pong by @JayProphit")
# background color
win.bgcolor("black")
# widows dimensions, width and height in pixels
win.setup(width=800, height=600)
# stops the window from updating, which means you have to manually update, this also lets us speed up the game,  0,0 is at the center 800 is split into +400, -400 and 600 is split into +300, -300, from the center
win.tracer(0)



# Score
score_a = 0
score_b = 0


# Paddle A - Left
# name of Object 1
paddle_a = turtle.Turtle()
# sets the speed of animation the the speed the object moves on screen
paddle_a.speed(0)
# gives it a shape
paddle_a.shape("square")
# specifies the color
paddle_a.color("white")
# default shape size is 20 pixels wide by 20 pixels high, 1 pixel = 20, 5 = 100 which is 5*20
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# turns of the ability to draw a line, as the turtle program by default draws a line as its moving
paddle_a.penup()
# sets tthe location
paddle_a.goto(-350, 0)


# Paddle B - Right
# name of Object 2
paddle_b = turtle.Turtle()
# sets the speed of animation the the speed the object moves on screen
paddle_b.speed(0)
# gives it a shape
paddle_b.shape("square")
# specifies the color
paddle_b.color("white")
# default shape size is 20 pixels wide by 20 pixels high, 1 pixel = 20, 5 = 100 which is 5*20
paddle_b.shapesize(stretch_wid=5, strectch_len=1)
# turns of the ability to draw a line, as the turtle program by default draws a line as its moving
paddle_b.penup()
# sets tthe location
paddle_b.goto(350, 0)


# Ball
# name of Object 3
ball = turtle.Turtle()
# sets the speed of animation the the speed the object moves on screen
ball.speed(0)
# gives it a shape
ball.shape("square")
# specifies the color
ball.color("white")
# turns of the ability to draw a line, as the turtle program by default draws a line as its moving
ball.penup()
# sets tthe location
ball.goto(0, 0)
# x movement and a y movement by pixels
ball.dx = 2
ball.dy = 2


# Pen
# score board
pen = turtle.Turtle()
# sets the speed of animation the the speed the object moves on screen
pen.speed(0)
# specifies the color
pen.color("white")
# turns of the ability to draw a line, as the turtle program by default draws a line as its moving
pen.penup()
# hide the turtle
pen.hideturtle()
# sets hight of score location display
pen.goto(0, 260)
# writes the score
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))



# Function
# paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    # sets y to new y
    padddle_a.sety(y)

# paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    # sets y to new y
    padddle_a.sety(y)

# paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    # sets y to new y
    padddle_b.sety(y)

# paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    # sets y to new y
    padddle_b.sety(y)



# Keybooard binding
#listen for keyboard input
win.listen()
# when w is pressed call the function paddle_a_up
win.onkeypress(paddle_a_up, "w")
# when w is pressed call the function paddle_a_down
win.onkeypress(paddle_a_down, "s")
# when w is pressed call the function paddle_b_up
win.onkeypress(paddle_b_up, "UP")
# when w is pressed call the function paddle_b_down
win.onkeypress(paddle_b_down, "DOWN")



# Main game loop
while True:
    # every time the loop runs, it updates the screen
    win.date()


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    # top border
    if ball.ycor() > 290:
        ball.set(290)
        ball.dy *= -1
        # mac operating systems, & stops the delay
        os.system("afplay bounce.wav&")
        
        '''
        # linux operating systems
        os.system("aplay bounce.wav&")

        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        '''

    # bottom border
    if ball.ycor() < -290:
        ball.set(-290)
        ball.dy *= -1
        # mac operating systems, & stops the delay
        os.system("afplay bounce.wav&")

    # right border
    if ball.xcor() > 390:
        # if the ball gose of the screen it will go back to center
        ball.goto(0, 0)
        # reverse direction
        ball.dx *= -1
        # awards score point
        score_a += 1
        # clears whats on the screen
        pen.clear()
        # writes the score on the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
    # left border
    if ball.xcor() > -390:
        # if the ball gose of the screen it will go back to center
        ball.goto(0, 0)
        # reverse direction
        ball.dx *= -1
        # awards score point
        score_b += 1
        # clears whats on the screen
        pen.clear()
        # writes the score on the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


    # Paddle and Ball collisions
    # right paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        # mac operating systems, & stops the delay
        os.system("afplay bounce.wav&")

    # left paddle and ball
    if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        # mac operating systems, & stops the delay
        os.system("afplay bounce.wav&")

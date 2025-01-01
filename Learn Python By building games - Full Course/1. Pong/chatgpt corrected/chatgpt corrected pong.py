# Pong Game by @JayProphit
# Part 1: Getting Started

import turtle
import os

# Uncomment for Windows sound functionality
# import winsound


# Window Setup
win = turtle.Screen()
win.title("Pong by @JayProphit")  # Fixed typo: `tittle` to `title`
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Disables auto-update for better control of rendering speed

# Scores
score_a = 0
score_b = 0

# Paddle A (Left Paddle)
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Corrected `strectch_len` to `stretch_len`
paddle_a.penup()  # Prevents drawing
paddle_a.goto(-350, 0)  # Starting position

# Paddle B (Right Paddle)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # Starting position
ball.dx = 2  # Ball movement in x direction
ball.dy = 2  # Ball movement in y direction

# Pen (Scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions for Paddle Movement
def paddle_a_up():
    y = paddle_a.ycor()  # Get current y-coordinate
    if y < 250:  # Prevent paddle from moving out of bounds
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:  # Prevent paddle from moving out of bounds
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)

# Keyboard Binding
win.listen()  # Listen for keyboard input
win.onkeypress(paddle_a_up, "w")  # 'w' to move Paddle A up
win.onkeypress(paddle_a_down, "s")  # 's' to move Paddle A down
win.onkeypress(paddle_b_up, "Up")  # Arrow Up to move Paddle B up
win.onkeypress(paddle_b_down, "Down")  # Arrow Down to move Paddle B down

# Main Game Loop
while True:
    win.update()  # Updates the screen each iteration

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Collision
    if ball.ycor() > 290:  # Top border
        ball.sety(290)
        ball.dy *= -1  # Reverse direction
        os.system("afplay bounce.wav&")  # Play sound (MacOS)
    
    if ball.ycor() < -290:  # Bottom border
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:  # Right border
        ball.goto(0, 0)  # Reset position
        ball.dx *= -1
        score_a += 1  # Player A scores
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # Left border
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  # Player B scores
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

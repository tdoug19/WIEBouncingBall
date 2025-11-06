#This runs in trinket on the web.  It has three different size balls
#bouncing.

import turtle
import time

# --- Setup screen ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0)

# --- Create Ball Function ---
def create_ball(color, size, start_x, start_y):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color(color)
    ball.penup()
    ball.goto(start_x, start_y)
    ball.dy = 0  # vertical velocity
    ball.size = size
    ball.hideturtle()  # hide turtle cursor
    return ball

# --- Draw Ball Function ---
def draw_ball(ball):
    ball.clear()
    ball.penup()
    ball.goto(ball.xcor(), ball.ycor() - ball.size)  # move down by radius
    ball.pendown()
    ball.begin_fill()
    ball.circle(ball.size)
    ball.end_fill()
    ball.penup()
    ball.goto(ball.xcor(), ball.ycor() + ball.size)  # return to center

# Create 3 balls of different sizes beside each other
ball1 = create_ball("red", 10, -325, 200)
ball2 = create_ball("blue", 20, -175, 200)
ball3 = create_ball("green", 60, 50, 200)

balls = [ball1, ball2, ball3]

# Physics constants
g = -1.0   # gravity (negative = down)
floor = -250
restitution = 0.95  # how much bounce energy is kept

running = False  # start paused

# --- Simulation Function ---
def simulate():
    global running
    if not running:
        return
    for ball in balls:
        # Apply gravity
        ball.dy += g
        y = ball.ycor() + ball.dy

        # Bounce on floor
        if y <= floor:
            y = floor
            ball.dy = -ball.dy * restitution

        ball.goto(ball.xcor(), y)
        draw_ball(ball)

    screen.update()
    screen.ontimer(simulate, 20)  # loop every 20 ms

# --- Start Function ---
def start_simulation():
    global running
    if not running:
        running = True
        simulate()

# --- Bind Spacebar ---
screen.listen()
screen.onkey (start_simulation, "space")

# Draw initial balls
for b in balls:
    draw_ball(b)
screen.update()

# --- Keep window open ---
turtle.done()  
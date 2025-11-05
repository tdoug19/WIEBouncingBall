# You can also write comments for your students to read like this.
# When you're done, add this to your website using the embed code.
import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.setworldcoordinates(0, 0, 600, 400)

ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(300, 390)

ballPositionY = 390         # starting height
deltaYPosition = 1.0  

def fall():
  global ballPositionY
  
  while ballPositionY > 0.0:
    ballPositionY = ballPositionY - deltaYPosition
    
    ball.goto(300 , ballPositionY)
    screen.update()
    
screen.tracer(0)

screen.listen()
screen.onkey(fall, "space")
turtle.done()
  
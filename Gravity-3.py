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

# Physics parameters
gravity = -9.8        # gravity (m/s^2)
ballPositionY = 390.0         # starting height
deltaYPosition = 0.0
yVelocity = 0.0          # velocity
dt = 0.1 #50ms
running = True
absorb = 0.8

def fall():
    global ballPositionY, deltaYPosition, yVelocity, running

    while running == True:
        
        # Update physics
        deltaYPosition = (yVelocity * dt) + (0.5 * gravity * dt *dt)
        yVelocity += gravity * dt
        ballPositionY += deltaYPosition
   
        # Bounce check
        if ballPositionY <= 0.0:
            ballPositionY = 0.0
            yVelocity = -yVelocity * absorb
            if abs(yVelocity) < 1:  # stop when motion is small
                running = False
                
        ball.goto(300, ballPositionY)
        screen.update()
    
screen.tracer(0)
screen.listen()
screen.onkey(fall, "space")
turtle.done()
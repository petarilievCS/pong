import turtle

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
MARGIN = 10
X = 350
Y = 0

BALL_WIDTH = 20
BOUNCE_DISTANCE = 80

# Screen setup 
screen = turtle.Screen()    
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddles 
paddle_a = Paddle(X, Y)
paddle_b = Paddle(-X - 10, Y)
ball = Ball()
scoreboard = Scoreboard()

screen.update()

# Event listeners
screen.listen()
screen.onkeypress(paddle_a.move_up, "Up")
screen.onkeypress(paddle_a.move_down, "Down")
screen.onkeypress(paddle_b.move_up, "w")   
screen.onkeypress(paddle_b.move_down, "s")

# Main game loop
while True:
    # Collision detection with wall
    if ball.ycor() >= HEIGHT / 2 - MARGIN or ball.ycor() <= -HEIGHT / 2 + MARGIN:
        ball.bounce_y()
    # Collision detection with paddles
    elif paddle_a.xcor() - BALL_WIDTH <= ball.xcor() and paddle_a.distance(ball) < BOUNCE_DISTANCE:
        ball.bounce_x()
    # Collision detection with paddles
    elif paddle_b.xcor() + BALL_WIDTH >= ball.xcor() and paddle_b.distance(ball) < BOUNCE_DISTANCE:
        ball.bounce_x()
    # Out of bounds detection
    elif ball.xcor() == WIDTH / 2:
        scoreboard.increase_score_a()
        ball.reset()
    elif ball.xcor() == -WIDTH / 2:
        scoreboard.increase_score_b()
        ball.reset()

    ball.move()
    screen.update()
    

screen.exitonclick()


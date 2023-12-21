import turtle
import random

class Ball(turtle.Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.speed = 1
        self.x_move = self.speed
        self.y_move = self.speed
    
    # Move the ball
    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x_move, y + self.y_move)

    # Bounce 
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move += 0.1 if self.x_move > 0 else -0.1

    # Reset
    def reset(self):
        self.goto(0, 0)
        self.move_x = random.choice([-1, 1])
        self.move_y = random.choice([-1, 1])
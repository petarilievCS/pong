import turtle

# Constants
WIDTH = 1
HEIGHT = 5
UP = 90

class Paddle(turtle.Turtle):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(x, y)
        self.setheading(UP)
        self.shapesize(WIDTH, HEIGHT)

    # Move up
    def move_up(self):
        self.forward(20)

    # Move down
    def move_down(self):
        self.backward(20)
import turtle

FONT = ("Courier", 70, "normal")
ALIGN = "center"
X_POSITION = 0
Y_POSITION = 200

class Scoreboard(turtle.Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_a = 0
        self.score_b = 0
        self.update()

    # Update
    def update(self):
        self.clear()
        self.goto(X_POSITION, Y_POSITION)
        self.write(f"{self.score_a} {self.score_b}", align=ALIGN, font=FONT)

    # Increase score
    def increase_score_a(self):
        self.score_a += 1
        self.update()
    
    def increase_score_b(self):
        self.score_b += 1
        self.update()
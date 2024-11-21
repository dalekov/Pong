from turtle import Turtle

class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0,y=300)
        self.hideturtle()
        self.color("white")
        self.setheading(270)
        self.appear()

    def appear(self):
        """Creates a dashed line in the middle so to split the area in two equal halves."""
        while self.ycor() > -300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()



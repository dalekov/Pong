from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.x_move = 20
        self.y_move = 20

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def increase_speed(self):
        """The ball increases its speed when hit by a paddle. The game gets progressively harder."""
        self.x_move *= 1.1
        self.y_move *= 1.1

    def bounce_x(self):
        """Inverts the x-axis, effectively creating a bouncing animation when the upper wall is hit."""
        self.x_move *= -1

    def bounce_y(self):
        """Inverts the y-axis, effectively creating a bouncing animation when the lower wall is hit."""
        self.y_move *= -1

    def reset_pos(self):
        """The ball resets its position once a goal is scored and is thrown to the player that scored
        in a random direction. Resets the ball speed back to default.
        """
        self.goto(x=0, y=0)
        self.x_move = 20
        self.y_move = 20
        self.bounce_x()
        self.randomize_y()

    def randomize_y(self):
        # We randomize the direction in which the ball will go:
        rng = random.randint(1, 2)
        if rng == 1:
            self.bounce_y()
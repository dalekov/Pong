from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        """Updates scoreboard. Old score is cleared, new one is written."""
        self.clear()
        self.goto(-200, 250)
        self.write(arg=f"{self.l_score}", move=False, align="center", font=("Courier", 30, "bold"))
        self.goto(200, 250)
        self.write(arg=f"{self.r_score}", move=False, align="center", font=("Courier", 30, "bold"))

    def game_over(self):
        """Displays a game over message and the winner."""
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=0)
        if self.l_score == 10:
            self.write(arg="  GAME OVER\nPLAYER 1 WINS!", move=False, align="center", font=("Courier", 72, "bold"))
        elif self.r_score == 10:
            self.write(arg="  GAME OVER!\nPLAYER 2 WINS!", move=False, align="center", font=("Courier", 72, "bold"))


from turtle import Screen
from paddle import Paddle
from dashed_line import DashedLine
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen object
screen = Screen()

# We setup the screen with the relevant properties:
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(n=0)

# We create the objects - 2 paddles to the left and right, the dashed line in the middle, as well as the ball
# and scoreboard
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((370, 0))
dashed_line = DashedLine()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # Detect collision with upper and lower wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles:
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        ball.increase_speed()
        ball.randomize_y()

    # Detect when a goal has been scored. First we check for the right side and then for the left side
    # so the score is incremented separately
    if ball.xcor() > 390:
        scoreboard.l_score += 1
        scoreboard.update()
        ball.reset_pos()

    if ball.xcor() < -390:
        scoreboard.r_score += 1
        scoreboard.update()
        ball.reset_pos()

    # If either player reaches 10 points, game ends.
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        ball.reset_pos()
        game_is_on = False


screen.mainloop()

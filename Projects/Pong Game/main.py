import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def exit_game():
    screen.bye()


screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
screen.onkey(exit_game, "Escape")

game_is_on = True


while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Right
    if ball.xcor() > 360:
        scoreboard.update_score_l()
        ball.reset()
    # Left
    elif ball.xcor() < -360:
        scoreboard.update_score_r()
        ball.reset()
    if scoreboard.right_player_score < scoreboard.left_player_score == 5:
        winner = "Left"
        scoreboard.game_over(winner)
        game_is_on = False
    if scoreboard.left_player_score < scoreboard.right_player_score == 5:
        winner = "Right"
        scoreboard.game_over(winner)
        game_is_on = False

screen.exitonclick()


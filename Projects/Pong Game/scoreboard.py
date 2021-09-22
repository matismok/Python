import time
from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_player_score = 0
        self.right_player_score = 0
        self.left_player()
        self.right_player()

    def left_player(self):
        self.goto(-300, 260)
        self.write(f"Left Player Score: {self.left_player_score}", move=False, align="left", font=FONT)

    def right_player(self):
        self.goto(300, 260)
        self.write(f"Right Player Score: {self.right_player_score}", move=False, align="right", font=FONT)

    def update_score_r(self):
        self.right_player_score += 1
        self.clear()
        self.right_player()
        self.left_player()

    def update_score_l(self):
        self.left_player_score += 1
        self.clear()
        self.left_player()
        self.right_player()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER. The winner is {winner} Player", align="center", font=FONT)


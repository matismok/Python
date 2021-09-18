from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setx(-15)
        self.sety(260)
        self.hideturtle()
        self.write(f"My score is: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"My score is: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)





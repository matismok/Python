from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(5, 1)
        self.goto(position)

    def move_up(self):
        my_y = self.ycor()
        my_x = self.xcor()
        self.goto(my_x, my_y + 20)

    def move_down(self):
        my_y = self.ycor()
        my_x = self.xcor()
        self.goto(my_x, my_y - 20)

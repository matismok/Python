from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.change_x = 10
        self.change_y = 10
        self.move_speed = 0.1

    def move(self):
        self.penup()
        my_x = self.xcor() + self.change_x
        my_y = self.ycor() + self.change_y
        self.goto(my_x, my_y)
        self.speed(0)

    def bounce_y(self):
        self.change_y *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.change_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1





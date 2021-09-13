import random
import turtle
from turtle import Turtle, Screen
from random import Random


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim = Turtle()
tim.shape("arrow")
turtle.colormode(255)
# side = 3
# angle = 360 / side
# while side <= 10:
#     tim.color(random.choice(colours))
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(angle)
#     side += 1
#     angle = 360 / side


end = True
angles = [90, 180]
distance = 20
my_choices = ["left", "right"]
tim.speed(0)


# while end:
#     tim.pensize(10)
#     tim.color(random_colors())
#     if random.choice(my_choices) == "left":
#         tim.left(random.choice(angles))
#         tim.forward(distance)
#     elif random.choice(my_choices) == "right":
#         tim.right(random.choice(angles))
#         tim.forward(distance)

draw_spirograph(10)

screen = Screen()
screen.exitonclick()

import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
turtles = []

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("cyan")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
my_x = -230
my_y = -125

for i in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(i)
    my_turtle.penup()
    my_turtle.goto(x=my_x, y=my_y)
    my_y += 50
    turtles.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winner is {winning_color} turtle.")
            else:
                print(f"You lose. The winner is {winning_color} turtle.")



# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()

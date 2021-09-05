# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City Name", ["Madrid","Lisbon", "Warsaw", "Krakow", "Zakopane"])
table.add_column("Country", ["Spain", "Portugal", "Poland", "Poland", "Poland"])
table.align = "l"
print(table)

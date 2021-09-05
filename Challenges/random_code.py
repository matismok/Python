import random

random_side = random.randint(1, 10)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Delaware", "Pencilvania", "New Jersey"]
states_of_america[1] = "Pennsylvania"

states_of_america.append("Georgia")

# names_string = input("Give me everybody's names, seperated by a comma. ")
# # Angela, Ben, Jenny, Jack, Matt
# names = names_string.split(", ")
#
# random_name = random.randint(0, len(names) - 1)
# random_to_list = names[random_name]
# print(f"{random_to_list} is going to buy the meal!")

row1 = ["🥲", "🥲", "🥲"]
row2 = ["🥲", "🥲", "🥲"]
row3 = ["🥲", "🥲", "🥲"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("It's 3x3 map .Where do you want to put your treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[int(vertical) - 1][int(horizontal) - 1] = "x"
print(f"\n{row1}\n{row2}\n{row3}\n")


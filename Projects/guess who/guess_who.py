import random
from game_data import data
from art import vs, logo


def create_and_compare(first, second):
    global copied
    global first_one, second_one
    global score, endGame
    first_name = first["name"]
    first_followers = first["follower_count"]
    first_description = first["description"]
    first_country = first["country"]
    second_name = second["name"]
    second_followers = second["follower_count"]
    second_description = second["description"]
    second_country = second["country"]
    print(f"Compare A: {first_name}, {first_description} from {first_country}. ")
    print(vs)
    print(f"Compare B: {second_name}, {second_description} from {second_country}. ")
    a_or_b = input("Who have more followers? Type 'A' or 'B' ")
    if a_or_b == "A" and first_followers > second_followers:
        score += 1
        print(f"You are right! Current score: {score} ")
        copied.remove(second_one)
        second_one = random.choice(copied)
    elif a_or_b == "A" and first_followers < second_followers:
        print(f"Sorry that's wrong! Final score: {score}")
        endGame = False
    elif a_or_b == "B" and first_followers > second_followers:
        print(f"Sorry that's wrong! Final score: {score}")
        endGame = False
    elif a_or_b == "B" and first_followers < second_followers:
        score += 1
        copied.remove(first_one)
        first_one = second_one
        second_one = random.choice(copied)
        print(f"You are right! Current score: {score} ")
    elif a_or_b == "A" or a_or_b == "B" and first_followers == second_followers:
        print("They are the same. Here goes next one.")
        second_one = random.choice(copied)


copied = data
first_one = random.choice(copied)
second_one = random.choice(copied)
score = 0
endGame = True
print(logo)
while endGame:
    create_and_compare(first_one, second_one)





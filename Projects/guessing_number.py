# Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random


def check(number_input):
    global endGame
    global attempts
    if number_input == number:
        endGame = False
        print("You guessed the number.\n You win!")
    elif number_input > number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attemtps remaining to geuss the number.")
    elif number_input < number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attemtps remaining to geuss the number.")
    if attempts == 0:
        print(f"The number was {number} .")
        print("You lose!")
        endGame = False


def check_level(level_input):
    global attempts
    if level_input == "easy":
        attempts = 10
        print(f"You have {attempts} attemtps remaining to geuss the number.")
    elif level_input == "hard":
        attempts = 5
        print(f"You have {attempts} attemtps remaining to geuss the number.")
    else:
        print("Wrong level!")
        exit(-1)


def game():
    level = input("Chose level difficulty. Type 'easy' or 'hard': ").lower()
    check_level(level)
    while endGame:
        guess_number = int(input("Make a guess: "))
        check(guess_number)
    choice = input("Do you want try again? Type 'y' or 'n' ").lower()
    again(choice)


def again(choice):
    global number
    global endGame
    if choice == "y":
        number = int(random.randint(1, 100))
        endGame = True
        game()
    elif choice == "n":
        print("Bye bye :)")
    else:
        print("Wrong answer! ")
        exit(-1)


print("Welcome to the Number Geussing Game!")
print("I'm thinking of number between 1 and 100.")
number = int(random.randint(1, 100))
endGame = True
game()





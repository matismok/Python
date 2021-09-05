import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

choices = [rock, paper, scissors]
if choice == 0:
    print(choices[choice])
elif choice == 1:
    print(choices[choice])
elif choice == 2:
    print(choices[choice])
else:
    print("Wrong number! Try again")
    exit(-1)

random_choice = int(random.randint(0, len(choices) - 1))

print("Computer chose:")
print(choices[random_choice])

if choice == 0 and random_choice == 0 or choice == 1 and random_choice == 1 or choice == 2 and random_choice == 2:
    print("It's draw.")
elif choice == 1 and random_choice == 0 or choice == 2 and random_choice == 1 or choice == 0 and random_choice == 2:
    print("You won")
elif choice == 2 and random_choice == 0 or choice == 0 and random_choice == 1 or choice == 1 and random_choice == 2:
    print("You lose")



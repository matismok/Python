import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
print(f"{logo}\n")
lives = 6
blank_list = []
# chosen_word_to_list = []
end_of_game = False
list_of_letters = []

# for i in chosen_word:
#     if i == letter:
#         print("right")
#     else:
#         print("wrong")

for i in range(len(chosen_word)):
    blank_list.append("_")
print(f"{blank_list}\n")
# for i in range(len(chosen_word)):
#     if letter == chosen_word[i]:
#         blank_list[i] = letter
#
# print(f"{blank_list}")
# blank = ""
# for i in range(0, len(blank_list)):
#     blank += str(blank_list[i])

# for i in range(len(chosen_word)):
#     chosen_word_to_list.append(chosen_word[i])
# print(f"Chosen word to list: {chosen_word_to_list}")

# while blank_list != chosen_word_to_list:
while not end_of_game:
    letter = input("Guess a letter: ").lower()
    if len(letter) > 1:
        print("Your letter is too long\n")
    else:
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                blank_list[i] = letter
        print(f"{blank_list}\n")
        if len(list_of_letters) > 0:
            print(f"Used letters: {list_of_letters}\n")
        if letter not in blank_list:
            if letter in list_of_letters:
                print(f"You already used  letter {letter}! You're losing another life.\n")
            lives -= 1
            print(f"lives: {lives}")
            print(stages[lives])
        if "_" not in blank_list:
            end_of_game = True
            print("You win!")
        if lives == 0:
            print("You lose!")
            end_of_game = True
            print(f"The word was: {chosen_word}")
    list_of_letters.append(letter)

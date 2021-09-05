import random


def sum_in_deck(deck_list):
    sum_deck = 0
    for i in deck_list:
        sum_deck += i
    return sum_deck


def checking(pds, pd, dds, dd):
    if pds > 21:
        print(f"Your cards are: {pd}\nSum of your deck: {pds}\n")
        print(f"Dealer cards are: {dd}\nSum of dealer deck: {dds}\n")
        print("You lose!")
    elif dds < pds <= 21:
        print(f"Your cards are: {pd}\nSum of your deck: {pds}\n")
        print(f"Dealer cards are: {dd}\nSum of dealer deck: {dds}\n")
        print("You win!")
    elif pds < dds:
        print(f"Your cards are: {pd}\nSum of your deck: {pds}\n")
        print(f"Dealer cards are: {dd}\nSum of dealer deck: {dds}\n")
        print("You lose!")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

ace = cards[0]

dealer_deck = [random.choice(cards), random.choice(cards)]
player_deck = [random.choice(cards), random.choice(cards)]

player_deck_sum = int(sum_in_deck(player_deck))
dealer_deck_sum = int(sum_in_deck(dealer_deck))

print(f"Your cards are: {player_deck}\nSum of your deck: {player_deck_sum}")
print(f"Dealer first card is {dealer_deck[0]}")

end = True

while end:
    choice = input("Do you want to take next card? Type 'y' or 'n \n").lower()
    if choice == "y":
        next_card = random.choice(cards)
        tmp = player_deck_sum + next_card
        if next_card == ace and tmp > 21:
            next_card = 1
            player_deck.append(next_card)
        else:
            player_deck.append(next_card)
        player_deck_sum = sum_in_deck(player_deck)
        print(f"Your cards are: {player_deck}\nSum of your deck: {player_deck_sum}")
        print(f"Dealer first card is {dealer_deck[0]}")
        if player_deck_sum > 21:
            print("You lose!")
            end = False
    elif choice == "n":
        end = False
        checking(player_deck_sum, player_deck, dealer_deck_sum, dealer_deck)
    else:
        print("Wrong input!")
        exit(-1)




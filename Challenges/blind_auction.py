
def find_highest(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"Highest bid was {highest_bid} and the winner is {winner}.\n")


is_other = True
empty_dict = {}
while is_other:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    empty_dict[name] = bid
    other = input("Is there any other bidder? Type 'yes' or 'no' ").lower()
    if other == "no":
        is_other = False
        find_highest(empty_dict)








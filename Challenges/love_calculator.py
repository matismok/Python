print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

score = 0
total = 0
total2 = 0

# long version
if lower_name1.count("t") >= 0 or lower_name2.count("t") >= 0:
    score += lower_name1.count("t") + lower_name2.count("t")
    total += score
    if score == 0 or score > 1:
        print(f"T occurs {score} times")
    else:
        print(f"T occurs {score} time")
    score = 0


if lower_name1.count("r") >= 0 or lower_name2.count("r") >= 0:
    score += lower_name1.count("r") + lower_name2.count("r")
    total += score
    if score == 0 or score > 1:
        print(f"R occurs {score} times")
    else:
        print(f"R occurs {score} time")
    score = 0

if lower_name1.count("u") >= 0 or lower_name2.count("u") >= 0:
    score += lower_name1.count("u") + lower_name2.count("u")
    total += score
    if score == 0 or score > 1:
        print(f"U occurs {score} times")
    else:
        print(f"U occurs {score} time")
    score = 0

if lower_name1.count("e") >= 0 or lower_name2.count("e") >= 0:
    score += lower_name1.count("e") + lower_name2.count("e")
    total += score
    if score == 0 or score > 1:
        print(f"E occurs {score} times")
    else:
        print(f"E occurs {score} time")
    score = 0

print(f"Total = {total} \n")

if lower_name1.count("l") >= 0 or lower_name2.count("l") >= 0:
    score += lower_name1.count("l") + lower_name2.count("l")
    total2 += score
    if score == 0 or score > 1:
        print(f"L occurs {score} times")
    else:
        print(f"L occurs {score} time")
    score = 0

if lower_name1.count("o") >= 0 or lower_name2.count("o") >= 0:
    score += lower_name1.count("o") + lower_name2.count("o")
    total2 += score
    if score == 0 or score > 1:
        print(f"O occurs {score} times")
    else:
        print(f"O occurs {score} time")
    score = 0

if lower_name1.count("v") >= 0 or lower_name2.count("v") >= 0:
    score += lower_name1.count("v") + lower_name2.count("v")
    total2 += score
    if score == 0 or score > 1:
        print(f"V occurs {score} times")
    else:
        print(f"V occurs {score} time")
    score = 0

if lower_name1.count("e") >= 0 or lower_name2.count("e") >= 0:
    score += lower_name1.count("e") + lower_name2.count("e")
    total2 += score
    if score == 0 or score > 1:
        print(f"E occurs {score} times")
    else:
        print(f"E occurs {score} time")
score = 0

print(f"Total = {total2}")

combined = str(total)+str(total2)
print(f"Love Score = {combined}")

combined_to_int = int(combined)

if combined_to_int < 10 or combined_to_int > 90:
    print(f"Your score is {combined}, you go together like coke and mentos.")
elif combined_to_int >= 40 or combined_to_int <= 50:
    print(f"Your score is {combined}, you are alright together.")
else:
    print(f"Your score is {combined}.")

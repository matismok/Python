
#age = input("What is your age? ")
#year = input("How many years do u wanna live? ")
#years = int(year) - int(age)
#days = int(years) * 365
#weeks = int(years) * 52
#months = int(years) * 12

#print(f"You have {days} days, {weeks} weeks and {months} months")

# ---------splitting bill for few people-----------
#bill = float(input("What is total bill? "))
#tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
#people = int(input("How many people to split the bill? "))

#bill_with_tip = bill * (1 + (tip / 100))

#each_person_tip = round(bill_with_tip / people, 2)


#print(f"Each person should pay: ${each_person_tip}")

print("It's calculator BMI")
height = float(input("Enter your height in m: " ))
weight = float(input("Enter your weight in kg: " ))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, Underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, Normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, Overweight")
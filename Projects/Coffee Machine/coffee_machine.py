from data import resources, MENU


def report():
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee} \nMoney: {round(money, 2)}")


def check_status(input_coffee):
    global status
    ingrid_water = MENU[input_coffee]["ingredients"]["water"]
    ingrid_coffee = MENU[input_coffee]["ingredients"]["coffee"]
    if input_coffee == "latte" or input_coffee == "cappuccino":
        ingrid_milk = MENU[input_coffee]["ingredients"]["milk"]
        if milk < ingrid_milk:
            print("Sorry there is not enough milk.")
            status = False
    if water < ingrid_water:
        print("Sorry there is not enough water.")
        status = False
    if coffee < ingrid_coffee:
        status = False
        print("Sorry there is not enough coffee.")
    return status


def change_status(coffee_input):
    global water, milk, coffee
    ingrid_water = MENU[coffee_input]["ingredients"]["water"]
    ingrid_coffee = MENU[coffee_input]["ingredients"]["coffee"]
    water -= ingrid_water
    coffee -= ingrid_coffee
    if coffee_input == "latte" or coffee_input == "cappuccino":
        ingrid_milk = MENU[coffee_input]["ingredients"]["milk"]
        milk -= ingrid_milk


def add_ingrid(input_ingrid):
    global water, milk, coffee
    if input_ingrid == "add":
        choice_ingrid = input("What do you want to add? ")
        how_much = int(input("How much? "))
        if choice_ingrid == "water":
            water += how_much
        elif choice_ingrid == "milk":
            milk += how_much
        elif choice_ingrid == "coffee":
            coffee += how_much


def input_coins():
    global change
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    change += 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return change


def formula(input_formula):
    global money, change
    status_after_checking = check_status(input_formula)
    if status_after_checking:
        print("Please insert coins.")
        input_change = input_coins()
        your_change = round(change_money(input_formula), 2)
        status_after_money_check = check_money_status(input_formula, input_change)
        if not status_after_money_check:
            print(f"Here is your change: {input_change}")
        else:
            print(f"Here is your change: {your_change}")
            change_status(input_formula)
            print(f"Here is your {input_formula}. Enjoy!")
        change = 0


def check_money_status(choice_input, input_change):
    global status, change
    cost = MENU[choice_input]["cost"]
    if input_change < cost:
        print("Sorry that's not enough money. Money refunded.")
        status = False
    return status


def change_money(choice_input):
    global money, change
    cost = MENU[choice_input]["cost"]
    if not change < cost:
        money += cost
        change -= cost
    return change


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
change = 0
end = True
status = True


while end:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        formula(choice)
    elif choice == "latte":
        formula(choice)
    elif choice == "cappuccino":
        formula(choice)
    elif choice == "off":
        end = False
    elif choice == "report":
        report()
    elif choice == "add":
        add_ingrid(choice)
    else:
        print("Wrong name! Try again :)")
    status = True

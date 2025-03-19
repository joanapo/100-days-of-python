from data import MENU, resources

profit = 0

def sufficient_resources(order):
    """
    Returns True if resources sufficient, False if not.
    :param order: choice of drink
    :return: boolean
    """
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry, there is not enough {item}. Please refill the machine.")
            return False
        else:
            return True

def payment_sum():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    print(f"Inserted: {round(total, 2)}.")
    total += int(input("How many dimes?: ")) * 0.1
    print(f"Inserted: {round(total, 2)}.")
    total += int(input("How many nickles?: ")) * 0.05
    print(f"Inserted: {round(total, 2)}.")
    total += int(input("How many pennies?: ")) * 0.01
    print(f"Inserted: {round(total, 2)}.")
    return total

def is_transaction_successful(cost, received):
    global profit
    if received > cost:
        change = round(received - cost, 2)
        print(f"Here is your change: ${change}.")
        profit += cost
    elif received == cost:
        profit += cost
    else:
        print(f"Sorry, that's not enough money. Returning ${received}.")
        return False
    return True

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink_name}. Enjoy!")

def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100

def report(data):
    print(f"Water: {data['water']}ml.")
    print(f"Milk: {data['milk']}ml.")
    print(f"Coffee: {data['coffee']}g.")


is_working = True
while is_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice.lower() == "off":
        print("Turning off...")
        is_working = False

    elif choice.lower() == "report":
        report(resources)
        print(f"Money: ${profit}")

    elif choice.lower() == "refill":
        refill()
        print("Coffee Machine refilled.")
        report(resources)

    else:
        try:
            drink = MENU[choice]
            if sufficient_resources(drink["ingredients"]):
                print(f"You have selected {choice}.")
                payment = payment_sum()
                if is_transaction_successful(drink["cost"], payment):
                    make_coffee(choice, drink["ingredients"])

        except KeyError:
            print("Invalid input. Please enter espresso/latte/cappuccino.")

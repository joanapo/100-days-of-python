from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_working = True
while is_working:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice.lower() == "off":
        print("Turning off...")
        is_working = False

    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        try:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                print(f"You have selected {choice}.")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

        except AttributeError:
            print("Invalid input. Please enter espresso/latte/cappuccino.")



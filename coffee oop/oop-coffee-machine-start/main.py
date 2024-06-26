from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()
money_machine = MoneyMachine()


# print(menu.find_drink(choice).ingredients)
# print(menu.find_drink(choice).cost)

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order? {options}: ").lower()

    if choice == "off":
        print("Turning OFF!")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



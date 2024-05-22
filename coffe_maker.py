# ingridients = [water, milk, coffee]
# this is the start of the coffee machine
from re import I


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def is_enough_ingredients(choice):
    for item in choice:
     if choice[item] >= resources[item]:
         print(f"There is not enough {item}") 
         return False

    return True

def is_enough_money(choice):
    print("Please enter coins: ")
    total = int(input("Enter quater: $")) * 0.25
    total += int(input("Enter dime: $")) * 0.10
    total += int(input("Enter nickles: $")) * 0.05
    total += int(input("Enter pennies: $")) * 0.01
    return round(total, 2)


while is_on:
    choice = input("What would you like to drink? (Espresso, Latte, Cappuccino) ").lower()
    if choice == 'off':
        is_on = False
        print("Turning off!")

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")

    else:
        drink = MENU[choice]
        if is_enough_ingredients(drink['ingredients']):
            is_enough_money(drink['cost'])
        else:
            print("helloooooo") 













# def is_enough_resources(order_ingredients):
#     """Returns weather or not there is enough resources to make the drink"""
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enought {item}")
#             return False
#     return True

# def process_coins():
#     """Returns the calculated amount of coins inserted"""
#     print("Insert coins: ")
#     total = int(input("How many quaters: ")) * 0.25
#     total += int(input("How many dime: ")) * 0.1
#     total += int(input("How many nickles: ")) * 0.05
#     total += int(input("How many pennies: ")) * 0.01

#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """This fucntion return TRUE when the money received is greater than the price of the drink"""
#     if money_received >= drink_cost:
#         global profit
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is you change ${change}")
#         profit += drink_cost
    
#         return True
#     else:
#         print("Sorry that's not enough money. Money refounded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the ingredients from the resources"""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your drink {drink_name}")



# is_on = True

# while is_on:
#     choice = input("What would you like to drink? (Espresso, Latte, Cappuccino) ").lower()
#     if choice == 'off':
#         is_on = False
#     elif choice == 'report':
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"profit: ${profit}")

#     else:
#         drink = MENU[choice]
#         if is_enough_resources(drink['ingredients']):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink['cost']):
#                 make_coffee(choice, drink['ingredients'])


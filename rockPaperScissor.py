######################################### 4.4 ROCK PAPER SCISSORS ######################################
import random

selection_list = ["rock", "paper", "scissors"]

choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

comp_selection = random.randint(0, len(selection_list) - 1)
#print(f"Computer picked {selection_list[ran_selection]}")

user_selection = selection_list[choice]

if user_selection == selection_list[comp_selection]:
    print(f"It's a DRAW! You chose {user_selection} and compuer chose {selection_list[comp_selection]}")
elif user_selection == "rock" and comp_selection == "scissors":
    print(f"You WON! You chose {user_selection} and compuer chose {selection_list[comp_selection]}")
elif user_selection == "scissors" and comp_selection == "paper":
    print(f"You WON! You chose {user_selection} and compuer chose {selection_list[comp_selection]}")
elif user_selection == "paper" and comp_selection == "rock":
    print(f"You WON! You chose {user_selection} and compuer chose {selection_list[comp_selection]}")
else:
    print(f"You Loose! You chose {user_selection} and compuer chose {selection_list[comp_selection]}")

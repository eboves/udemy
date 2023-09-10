from black_jack_logo import logo


#imports
import random

#Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
dealer_hand = []
def start_game():
    init_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n' ")
    for _ in range(0, 2):
        my_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
    print(f"Your cards: {my_hand}, current score: {cal_sum(my_hand)}")
    #print(f"Computer's first card: {dealer_hand[0]}")
    print(f"Computer's first card: {dealer_hand}")
# if random.choice(cards) == 11 and cal_sum(my_hand) + 11 > 21: my_hand.append(1)

def re_start_game():
    print("This should reset the lists")
    my_hand = []
    dealer_hand = []
    should_continue = False
    print("THEY SHOULD BE EMPTY")
    print("THIS IS MY HAND: ", my_hand)
    print("THIS IS THE COMPUTER HAND: ", dealer_hand)
    start_game()
    bj_new_game()

  

def cal_sum(lst):
    """ This function will calculate the score of the hands"""
    if sum(lst) == 21 and len(lst) == 2:
        return 0:

    if 11 in lst and sum(lst) > 21:
        lst.remove(11)
        lst.append(1)
        

    return sum(lst)
    #suma = 0
    #for num in lst:
    #    suma += num
    #return suma
def text_display():
    print(f"Your Final Hand: {my_hand}, current score: {cal_sum(my_hand)}")
    print(f"Computer's Final Hand: {dealer_hand}, Final Score: {cal_sum(dealer_hand)}")

def bj_new_game():
    should_continue = True
    while should_continue:
        if (input("Type 'y' to get another card, type 'n' to pass: ")).lower() == 'y':
            my_hand.append(random.choice(cards))
            print(f"Your cards: {my_hand}, current score: {cal_sum(my_hand)}")
            print(f"Computer's first card: {dealer_hand[0]}")
            if random.choice(cards) == 11 and (cal_sum(my_hand) + 11 > 21):
                my_hand.append(1)
            if cal_sum(my_hand) > 21:
                text_display()
                print("You Lost")
                re_start_game()
            #here can handle the sum > than 21
        else:
            while cal_sum(dealer_hand) < 17:
                dealer_hand.append(random.choice(cards))
            if cal_sum(dealer_hand) == cal_sum(my_hand):
                text_display()
                print("It's a DRAW!!!")
                re_start_game()
            elif cal_sum(dealer_hand) <= 21 and (cal_sum(dealer_hand) > cal_sum(my_hand)):
                text_display()
                print("You Lost")
                re_start_game()
            else:
                text_display()
                print("Opponent went over. You WIN")
                re_start_game()

            # HERE IS WHERE ALL THE OTHER LOGIC GOES
           # my_hand = []
           # dealer_hand = []        
            re_start_game()
# CREATE A FUNCT that hold start_game() and bj_new_game() to call it from dif places.
re_start_game()


#my_full_hand = []
#house_full_hand = []
#my_sum = 0
#my_hand = []
#house_hand = []
#
#while start_game:
#    def main():
#        if_yes = input("Type 'y' to get another card, type 'n' to pass: ")
#        play_game(if_yes)
#
#    def my_random_card(card_deck):
#        rand_card = random.randint(0, len(card_deck) - 1)
#        my_full_hand.append(rand_card)
#
#    def house_random_card(card_deck):
#        rand_card = random.randint(0, len(card_deck) - 1)
#        house_full_hand.append(rand_card)
#
#    def sum_of_cards(list_of_cards):
#        """
#        This function is going to print the cards sum
#        """
#        for num in range(0, len(list_of_cards) - 1):
#            num1 = 0
#            num1 = list_of_cards[num]
#            my_sum = num1 + list_of_cards[num + 1] 
#            return my_sum
#    
#    def play_game(response):
#            #computer_final_score = sum_of_cards(my_hand)
#            #my_final_score = sum_of_cards(house_hand)       
#        if response.lower() == 'y':
#            print("This is inside the while inside play_game fnct")
#            my_random_card(cards)
#
#        else:
#            computer_final_random_card = sum_of_cards(house_random_card(cards))
#            while computer_final_random_card <= 17:
#                house_random_card(cards)
#                if computer_final_random_card < 17:
#                    continue
#                else:
#                    print(f"Your Final Hand Cards: {my_full_hand}, Final Score: {my_final_hand}")
#                    print(f"Computer's Final Hand: {house_full_hand}, Final Score: {computer_final_hand}")
#
#                    if my_final_hand > computer_final_hand:
#                        print("YOU WON!!!")
#                    elif my_final_hand < computer_final_hand:
#                        print("YOU LOST!!!")
#                    else:
#                        print("IT's a DRAW!!!")
#                        
#                    start_game = False        
#
#            
#            # here is when i do the recursion
#
#
#    def start_first_game():
#        for _ in range(0,2):
#            my_random_card(cards)
#            house_random_card(cards)
#            
#        my_current_cards = sum_of_cards(my_full_hand)
#        #computer_current_cards = sum_of_cards(house_full_hand)
#        print(logo)
#
#        print(f"Your Cards: {my_full_hand}, Current Score: {my_current_cards}")
#        print(f"Computer's First Card: {house_full_hand[0]}")
#
#    if init_game.lower() == 'y':
#        start_first_game()
#        main()
#    else:
#        break
#
#
       
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run































############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


from black_jack_logo import logo


#imports
import random

#Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

init_game = input("Do you want to play a game of Black Jack? Type 'y' or 'n'.")
start_game = True
my_full_hand = []
house_full_hand = []
my_sum = 0
my_hand = []
house_hand = []

while start_game:
    def main():

    play_game(init_game)

    def my_random_card(card_deck):
        rand_card = random.randint(0, len(card_deck) - 1)
        my_full_hand.append(rand_card)
    def house_random_card(card_deck):
        rand_card = random.randint(0, len(card_deck) - 1)
        house_full_hand.append(rand_card)
            

#        if(input("Do you want to play a game of Black Jack? Type 'y' or 'n'.")).lower() == 'y':
#            print("Hello")

    def sum_of_cards(list_of_cards):
        """
        This function is going to print the cards sum
        """
        for num in range(0, len(list_of_cards) - 1):
            num1 = 0
            num1 = list_of_cards[num]
            my_sum = num1 + list_of_cards[num + 1] 
            return my_sum
    
    def play_game(response):
            #computer_final_score = sum_of_cards(my_hand)
            #my_final_score = sum_of_cards(house_hand)       
        if init_game.lower() == 'y':
            my_random_card(cards)

        else():
            computer_final_random_card = sum_of_cards(house_random_card(cards))
            while computer_final_random_card =< 17:
                house_random_card(cards)
                if computer_final_random_card < 17:
                    continue
                else:
                    print(f"Your Final Hand Cards: {my_full_hand}, Final Score: {my_final_hand}")
                    print(f"Computer's Final Hand: {house_full_hand}, Final Score: {computer_final_hand}")

                    if my_final_hand > computer_final_hand:
                        print("YOU WON!!!")
                    elif my_final_hand < computer_final_hand:
                        print("YOU LOST!!!")
                    else:
                        print("IT's a DRAW!!!")
                    
                    start_game = False        

            
            # here is when i do the recursion


    def start_first_game(response):
        if response.lower() == 'y':
            for _ in range(0,1):
                my_random_card(cards)
                house_random_card(cards)
            
            my_current_cards = sum_of_cards(my_hand)
            computer_current_cards = sum_of_cards(house_hand)
            print(logo)
            print(f"Your Cards: {my_full_hand}, Current Score: {my_current_cards}")
            print(f"Computer's Cards: {house_full_hand}, Final Score: {computer_current_cards}")

        else:
            break



        #print(logo)
        # Variables
        #my_hand = []
        #house_hand = []
        #
        #
        #first_num = random.randint(0, len(cards) - 1)
        #second_num = random.randint(0, len(cards) - 1)
        #house_first_num = random.randint(0, len(cards) - 1)
        #house_second_num = random.randint(0, len(cards) - 1)
        #my_hand.append(first_num)
        #my_hand.append(second_num)
        #house_hand.append(house_first_num)
        #house_hand.append(house_second_num)

       
#        print("This is my hand: ", sum_of_cards(my_hand))
#        print("This is the house hands: ", sum_of_cards(house_hand))
        #start_game = False 
        
        # Shows only computer 1st card 8.
        # Type yes to get another card and no to pass. (this is an input)
    else:
        print("thanks for playing")
        start_game = False
        
        
        
        

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


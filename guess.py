import random

rand = random.randint(1, 100)
attemps = 0

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")
print(f"Pssst the correct answer is {rand}")

dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")

def guess_again(attemps):
    print("Guess again")
    print(f"You have {attemps} remaning to guess the number")

def game_on(attemps):
    is_game = True
    print(f"You have {attemps} attempts")
    while is_game:
        guess_num = int(input("Make a guess: "))
        if attemps == 0:
            print("You've run out of guesses, You lose.")
            return
        if guess_num == rand:
            print(f"You got it, the answer was {rand}")
            is_game = False
        elif guess_num < rand:
            attemps -= 1
            print("Too low.")
            guess_again(attemps)   
        else:
            attemps -= 1
            print("Too high.")
            guess_again(attemps)   


if dificulty != 'easy':
    attemps = 5
    game_on(attemps)
else:
    attemps = 10
    game_on(attemps)


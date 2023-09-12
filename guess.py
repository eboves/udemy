import random

rand = random.randint(1, 100)
attempts = 0



print(rand)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")
print(f"Pssst the correct answer is {rand}")



dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")




if dificulty != 'easy':
    global attempts = 5
    print("You have {attemps} attempts")
    guess_num = input("Make a guess: ")




"""
TODO:
0- if attempts == 0:
    you;ve run out of guesses, you loose
1- if easy attempts = 10 if hard attempts = 5
2- if input is lower than the random number :
    print(too low)
    print(guess again)
    print(you have {attempts} - 1 remaning to guess the number.)
    make a guess: 

3- if input is greater than random number :
    print(too high)
    print(guess again)
    print(you have {attempts} - 1 remaning to guess the number.)
    make a guess: 


4- else:
    print(You got it, the answer was {rand})
"""

import random

word_list = ["camel", "baboon", "food"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a letter: ").lower()

for l in chosen_word:
    if guess == l:
        print("right")
    else:
        print("wrong")
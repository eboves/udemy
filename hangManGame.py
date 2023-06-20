import random

display = []
word_list = ["camel", "baboon", "food"]

chosen_word = random.choice(word_list)

for _ in range(0, len(chosen_word)):
    display += "_"

print(display)
print(chosen_word)


guess = input("Guess a letter: ").lower()

for l in range(0, len(chosen_word)):
    if guess == chosen_word[l]:
        display[l] = chosen_word[l]
        print("right")
    else:
        print("wrong")

print(display)
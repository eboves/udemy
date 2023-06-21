import random

display = []
word_list = ["camel", "baboon", "food"]

chosen_word = random.choice(word_list)

for _ in range(0, len(chosen_word)):
    display += "_"

print(display)
print(chosen_word)

#lives = len(chosen_word)
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Already picked!")

    for l in range(0, len(chosen_word)):
        if guess == chosen_word[l]:
            display[l] = chosen_word[l]
    if guess not in chosen_word[l]:
        lives -= 1
        if lives == 0:
            print("You Lost!")
            end_of_game = True


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You WON!.")
import random
import hangman_art
import hangman_words


display = []
word_list = ["camel", "baboon", "food"]

# This section make a random selection from the list imported from hangman_words
chosen_word = random.choice(hangman_words.word_list)

for _ in range(0, len(chosen_word)):
    display += "_"

print(display)
print(chosen_word)

#lives = len(chosen_word)
lives = 6

print(hangman_art.logo)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Already picked!")
    # This is the for loop to check if a guess char is part of the hidden word
    for l in range(0, len(chosen_word)):
        if guess == chosen_word[l]:
            display[l] = chosen_word[l]
    # This section check if the char selected is not part of the word
    if guess not in chosen_word:
        print(f"{guess} is not a part of the word. You lose a life")
        lives -= 1
        if lives == 0:
            print("You Lost!")
            end_of_game = True

    print(hangman_art.stages[lives])

    # This section check if the user have guessed the hidden word
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You WON!.")
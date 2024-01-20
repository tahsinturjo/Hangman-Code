import random
import word
import art

print(art.logo)
lives = 6
word_list = word.word_list
chosen_word = random.choice(word_list)

# print(chosen_word)

display = []

for letter in chosen_word:
    display.append("_")

print(display)

game_on = True

while game_on:

    guess = input("Guess a letter: ").lower()
    index_no = 0
    if guess in display:
        print(f"You have already guessed this letter '{guess}'")

    for letter in chosen_word:
        if letter == guess:
            display[index_no] = letter
            index_no += 1
        else:
            index_no += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter '{guess}' is not in this word.")

    print(display)
    print(art.stages[lives])
    if "_" not in display:
        game_on = False
        print("YOU WIN!!!")
    elif lives == 0:
        game_on = False
        print(f"YOU LOSE!!! The word was {chosen_word}")


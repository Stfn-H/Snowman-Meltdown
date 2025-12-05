import random
from ascii_art import STAGES
from words import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")

    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Prompt user for one guess
    word_not_solved = True
    while mistakes != len(STAGES)-1 and word_not_solved:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        word_not_solved = False
        for letter in secret_word:
            if letter not in guessed_letters:
                word_not_solved = True
                break

    display_game_state(mistakes, secret_word, guessed_letters)

    if not word_not_solved:
        print("Congratulations, you saved the snowman!")
    else:
        print(f"Game Over! The word was: {secret_word}")


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
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print()


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    wrong_guessed_letters = []

    print("\n========================================")
    print("        WELCOME TO SNOWMAN MELTDOWN")
    print("========================================\n")
    print("Try to guess the secret word one letter at a time.")
    print("Every wrong guess melts part of the snowman.")
    print("Can you save him before he melts completely?\n")
    print("Let the game begin!\n")

    #print("Secret word selected: " + secret_word)  # for testing

    # Prompt user for one guess
    word_not_solved = True
    while mistakes != len(STAGES)-1 and word_not_solved:
        display_game_state(mistakes, secret_word, guessed_letters)

        #input validation
        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1:
                print("Please enter exactly ONE character.")
                continue

            if not guess.isalpha():
                print("Please enter a LETTER (a-z).")
                continue

            if guess in guessed_letters or guess in wrong_guessed_letters:
                print("You already guessed that letter!")
                continue
            break

        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
            wrong_guessed_letters.append(guess)

        word_not_solved = False
        for letter in secret_word:
            if letter not in guessed_letters:
                word_not_solved = True
                break

    display_game_state(mistakes, secret_word, guessed_letters)

    if not word_not_solved:
        print("\n" + "=" * 30)
        print(" 🎉  CONGRATULATIONS! ".center(30))
        print("=" * 30)
        print("You saved the snowman!\n")
    else:
        print("\n" + "=" * 30)
        print(" 💀  GAME OVER ".center(30))
        print("=" * 30)
        print(f"The snowman melted...\nThe word was: {secret_word}\n")


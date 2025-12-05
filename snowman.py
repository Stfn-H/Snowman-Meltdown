from game_logic import play_game


def main():
    while True:
        play_game()
        while True:
            play_again = input("Play again? (y/n): ").lower().strip()

            if play_again in ("y", "n"):
                break
            else:
                print("Please enter 'y' or 'n'.")

        if play_again == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
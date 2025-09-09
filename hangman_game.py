# HANGMAN GAME USING PYTHON
import random

# A small list of words to guess.
# (In a bigger project, you could import from a file.)
words = ("apple", "orange", "banana", "coconut", "pineapple")

# ASCII art for the hangman figure.
# Keys = number of wrong guesses, values = figure state.
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\"),
}

def display_man(wrong_guesses):
    #Print the hangman figure for the current number of wrong guesses.
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    #Show the current progress of the word (with underscores for missing letters).
    print(" ".join(hint))

def display_answer(answer):
    #Reveal the full answer word, used at game over.
    print(" ".join(answer))

def main():
    #Main game loop (includes replay option).

    # Outer loop allows the player to replay after win/lose
    while True:
        # Initialize/reset variables for a new game
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        # Inner loop: runs one round of the game
        while is_running:
            print("*************************")
            display_man(wrong_guesses)
            display_hint(hint)
            print("*************************")

            # Ask for input and clean it
            guess = input("Enter a letter: ").lower().strip()

            # Validate input: must be a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input!")
                continue

            # Prevent repeated guesses
            if guess in guessed_letters:
                print(f"{guess} was already guessed!")
                continue

            # Add guess to the set of used letters
            guessed_letters.add(guess)

            # Update hint if correct, otherwise increase mistakes
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            # Win condition: no more underscores in hint
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You win!")
                is_running = False

            # Lose condition: too many wrong guesses
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You lose!")
                is_running = False

        # Ask if the player wants to play again
        play_again = input("Play again? (Y/N): ").lower().strip()
        if play_again not in ("y", "yes"):
            print("See you later!")
            break

if __name__ == "__main__":
    main()

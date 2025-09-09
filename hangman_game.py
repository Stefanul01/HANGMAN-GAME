#HANGMAN GAME USING PYTHON:
import random

#We could create another file with a longer list and import it,
#But for keeping it simple and all-together I will leave just a short list here.
words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:() (we are using this to display our hangman)
hangman_art = {0: ("   ",
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
                   "/ \\"),}

#Here we creat a loop that would iterate trough our dictionary and print our hangman,
#according to the number of mistaks the user is currently having.
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

#We will set "hint" to be a list, for each letter in our word to guess we would print an "_"
#and we will have this strings to be joined by a space.
def displaly_hint(hint):
    print(" ".join(hint))

#Here we split the word we are guessing in letter and display it,
#we will use this after the player wins or loses.
def display_answer(answer):
    print(" ".join(answer))

def main():

    #We are setting an outer while loop so the user would be able to restart the program and play again.
    #In the outer-loop we set some enclosing variables that we would be able to use in our functions.
    while True:
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        #This is where our game is happening:
        while is_running:
            #first: we are calling in our display_man() function that would start at the key of 0
            #and our display_hint() function that will show us how manny letters there are in our word.
            print("*************************")
            display_man(wrong_guesses)
            displaly_hint(hint)
            print("*************************")

            #we ask the user for a guess which we store in a variable.
            #also making sure the input is lower-case and stripped out of any spaces using .lower() and .strip()
            guess = input("Enter a letter: ").lower().strip()

            #checking the input for posible erros that would make our program crash.
            #first, we are making sure the lenght is not longer than 1 and that everything is alphabetical.
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input!")
                continue
            
            #second, we make sure that the letter was not already guessed by our user.
            if guess in guessed_letters:
                print(f"{guess} is already guessed!")
                continue
            
            #we add the guessed letters to our set of guessed letters. 
            guessed_letters.add(guess)

            #Using a for loop we are changing every "_" in our hint to a correctly guessed letter.
            #Or increasing the number of mistakes so we can show further more of our hangman.
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            #If the our "hint" list is completely changed, the user wins!
            #(That is how the program figures it all out) 
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You win!")
                is_running = False
            #Or if the wrong guesses number exceeds our dictionary length the user looses.
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You lose!")
                is_running = False
        
        #Giving the option to play the game again and restart the loop.
        play_again = input("Want to play again?(Y/N): ").lower().strip()
        if play_again not in ("yes", "y"):
            print("See you later!")
            break
        

if __name__ == "__main__":
    main()
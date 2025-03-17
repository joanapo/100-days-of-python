from random import randint
import art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def choose_difficulty():
    """
    Choosing the difficulty of the game. Will loop if the input isn't 'easy' or 'hard'
    :return: global ints EASY_ATTEMPTS and HARD_ATTEMPTS
    """
    selection = True #loop if the selection isn't easy or hard.
    while selection:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

        if difficulty.lower() == "easy":
            selection = False
            return EASY_ATTEMPTS
        elif difficulty.lower() == "hard":
            selection = False
            return HARD_ATTEMPTS
        else:
            print("Invalid selection. Try again.")

def check_answer(user_input, computer_number, turns):
    """
    Checks whether the user input is higher, lower or the same as the randint the computer generated.
    :param user_input: int that the user guessed
    :param computer_number: int that the computer chose
    :param turns: int how many turns are left in the game
    :return: int turns - 1, how many turns are left in the game after this guess
    """
    if user_input > computer_number:
        print("Too high.")
        return turns - 1
    elif user_input < computer_number:
        print("Too low.")
        return turns - 1
    elif user_input == computer_number:
        print(f"You guessed it! The number was {computer_number}")



def play_game():
    """
    Main function of the game.
    Prints the art logo, generates the answer number and prompts the user to guess the number.
    Function breaks when user runs out of attempts to guess.
    """
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    attempts = choose_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)
        if attempts == 0:
            print(f"You ran out of attempts. The correct answer was {number}")
            break
        elif guess != number:
            print("Guess again.")


play_game()
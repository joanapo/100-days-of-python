from art import logo, vs
from game_data import data
import random

def account_information(account):
    """
    Gets relevant information from account
    :param account: random item from the game_data dictionary
    :return: string with data relevant for gameplay
    """
    account_name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{account_name}, a(n) {description}, from {country}"

def answer(followers_a, followers_b, user_guess):
    """

    :param followers_a: int follower number of choice_a
    :param followers_b: int follower number of choice_b
    :param user_guess: what the user input as their guess
    :return: boolean whether the user guess was true or false
    """
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0

choice_b = random.choice(data)
should_continue = True # Loops the game while the answer is true
while should_continue:
    choice_a = choice_b
    choice_b = random.choice(data)

    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare A: {account_information(choice_a)}.")
    print(vs)
    print(f"Against B: {account_information(choice_b)}.")

    # User guesses
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen for the next round
    print("\n" * 20)
    print(logo)

    # Get the follower count from game_data
    followers_choice_a = choice_a["follower_count"]
    followers_choice_b = choice_b["follower_count"]

    # Checks if user's guess is right
    is_right = answer(followers_choice_a,followers_choice_b, guess)

    if is_right:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False # Stops gameplay


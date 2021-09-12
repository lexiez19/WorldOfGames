import random


def generate_number(max_range):
    return random.choice(range(1, max_range + 1))


def get_guess_from_user(guess_range):
    user_input_guess = int(input(f"Please enter a number from 1 to {guess_range}\n"))
    while user_input_guess < 1 or user_input_guess > guess_range:
        user_input_guess = int(input(f"Wrong Number, Kindly choose a number from 1 to {guess_range}\n"))
    else:
        return user_input_guess


def compare_results(secret, guess_input):
    if secret == guess_input:
        print(f"{secret} and {guess_input} are equal, you Won the game !")
        return True
    else:
        print(f"{secret} and {guess_input} are not equal, you Lost the game !")
        return False


def GuessGamePlay(difficulty):
    secret_number = generate_number(difficulty)
    user_input_guess_from_user = get_guess_from_user(difficulty)
    is_equal = compare_results(secret_number, user_input_guess_from_user)
    return is_equal



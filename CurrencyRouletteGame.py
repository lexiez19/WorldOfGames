import random
from currency_converter import CurrencyConverter

c = CurrencyConverter()
ils_2_usd = c.convert(1, 'USD', 'ILS')


def get_random_choice():
    random_number = range(1, 101)
    get_random_number = random.choice(random_number)
    return get_random_number


def get_money_interval(d, random_choice):
    total_value = random_choice * ils_2_usd
    # Interval > t - (5 - d), t + (5 - d)
    interval_min = total_value - (5 - d)
    interval_max = total_value + (5 - d)
    interval = [interval_min, interval_max]
    return interval


def get_guess_from_user(guess_choice):
    user_guess = float(input(f"Guess the USD amount of {guess_choice}\n"))
    return user_guess


def CurrencyRouletteGamePlay(dfc):
    random_choice = get_random_choice()
    user_input = get_guess_from_user(random_choice)
    interval_result = get_money_interval(dfc, random_choice)
    if interval_result[0] < user_input < interval_result[1]:
        return True
    else:
        return False









def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    my_dict = {"1": "Memory Game", "2": "Guess Game", "3": "Currency Roulette Game"}
    game_number_input = input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for "
                              "1 second and you have to guess it back\n2. Guess Game - guess a number and see if you "
                              "choose like the computer\n3. Currency Roulette - try and guess the value of a random "
                              "amount of USD in ILS\n")

    while game_number_input != "1" and game_number_input != "2" and game_number_input != "3":
        game_number_input = input("Please enter a number between 1 to 3\n")
    else:
        game_difficulty_input = int(input("Please choose game difficulty from 1 to 5:\n"))
        while game_difficulty_input > 5 or game_difficulty_input <= 0:
            game_difficulty_input = int(input("Please enter a number between 1 to 5:\n"))
        else:
            print("You choose", my_dict[game_number_input], "With difficulty", game_difficulty_input)
    return {"difficulty": game_difficulty_input, "game_number": game_number_input}

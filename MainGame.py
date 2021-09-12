from Live import load_game, welcome
from GuessGame import GuessGamePlay
from MemoryGame import MemoryGameplay
from CurrencyRouletteGame import CurrencyRouletteGamePlay
from Score import add_score
from Utils import score_insert_to_file

print(welcome(input("Enter Your Name\n")))
game_settings = load_game()

is_won = ""

if game_settings["game_number"] == "1":
    is_won = MemoryGameplay(game_settings["difficulty"])

if game_settings["game_number"] == "2":
    is_won = GuessGamePlay(game_settings["difficulty"])

if game_settings["game_number"] == "3":
    is_won = CurrencyRouletteGamePlay(game_settings["difficulty"])


if is_won:
    print("Well Done, You WON ! :) ")
    game_score = add_score(game_settings["difficulty"])
    score_insert_to_file(game_score)
else:
    print("Game Over, You Lose ! :( ")
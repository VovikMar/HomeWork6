from Live import load_game, welcome
import GuessGame
print(welcome("Vladimir"))
choose_game = load_game()  # choose_game[0] which game, choose_game[1]-difficulty
if choose_game[0] == 1:
    GuessGame.play(choose_game[1])
elif choose_game[0] == 2:
    print("You choose MemoryGame ")
elif choose_game[0] == 3:
    print("You choose CurrencyRouletteGame ")




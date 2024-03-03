# Welcome (name)
def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            f"Here you can find many cool games to play.")


# Load Game()
def load_game():
    print("Please choose a game to play:\n"
          "\t1. Memory Game - a sesequence of numbers will appear for 1 second and you have to\n"
          "guess it back.\n"
          "\t2. Guess Game - guess a number and see if you chose like the computer\n"
          "\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    check = True
    while check:
        try:
            game_choice = int(input("Please choose a game: "))
            while not (1 <= game_choice <= 3):
                game_choice = int(input("Please choose 1-3 game number: "))
            if 1 <= game_choice <= 3:
                check = False
        except ValueError:
            print(f"Wrong, input is not number between 1-3")

    while not check:
        try:
            difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
            while not (1 <= difficulty_level <= 5):
                difficulty_level = int(input("Please choose game difficulty(number) from 1 to 5: "))
            if 1 <= difficulty_level <= 5:
                check = True
        except ValueError:
            print(f"Wrong, input is not integer number between 1-5")

    return game_choice, difficulty_level

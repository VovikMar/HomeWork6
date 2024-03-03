import random  # Import randomizer lab


# Generate random number fanc()
def generate_number(game_difficulty):
    secret_number = random.randint(1, game_difficulty)
    return secret_number

# Enter User choise number fanc()
def get_guess_from_user(game_difficulty):
    legal_value = False
    while not legal_value:
        try:
            user_number = int(input(f"Enter number between 1 to {game_difficulty} ==>"))
            if 1 <= user_number <= game_difficulty:
                legal_value = True
        except ValueError:
            print("Wrong value it mast be an integer number!!! ")

    return user_number

# Compare fanc() will compare secret number to user choise number
def compare_results(secret_number, user_number):
    print(f"Your number is {user_number} and the Computer number is {secret_number}")
    return secret_number == user_number


# Play func() is the call the func above and play them
def play(game_difficulty):
    print("<=====You Play th GuessGame =====>")
    generate_number(game_difficulty)
    print("\n ===>\n", )
    if compare_results(generate_number(game_difficulty), get_guess_from_user(game_difficulty)):
        print("You WON the GAME!!!! ")
    else:
        print("You lost, try next time.")



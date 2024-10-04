def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def choose_game():
    print("Choose a game:")
    print("1. NOK(Least Common Multiple)")
    print("2. Geometric Progression")
    choice = int(input("Enter your choice(1 or 2): "))
    return choice

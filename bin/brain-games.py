from src.cli import welcome_user, choose_game
from src.games.nok import play_nok
from src.games.progression import play_progression

if __name__ == "__main__":
    name = welcome_user()
    choice = choose_game()

    if choice == 1:
        play_nok(name)
    elif choice == 2:
        play_progression(name)
    else:
        print("Invalid choice. Please run the game again and choose 1 or 2.")

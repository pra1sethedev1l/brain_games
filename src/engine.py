def run_game(game_logic):
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            return False
    print("Congratulations! You've won the game!")
    return True

import random
from src.engine import run_game


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    return [start + i * step for i in range(length)]


def game_logic():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def play_progression(name):
    print("What number is missing in the progression?")
    return run_game(game_logic)

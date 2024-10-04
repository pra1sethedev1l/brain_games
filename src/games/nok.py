import math
import random
from src.engine import run_game


def nok(nums):
    return math.lcm(*nums)


def game_logic():
    nums = [random.randint(1, 20) for _ in range(3)]
    question = ' '.join(map(str, nums))
    correct_answer = nok(nums)
    return question, correct_answer


def play_nok(name):
    print("Find the least common multiple of given numbers.")
    return run_game(game_logic)

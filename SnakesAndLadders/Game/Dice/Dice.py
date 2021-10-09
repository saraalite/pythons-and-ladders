import random
from .DiceValues.DiceValues import DiceValues


class Dice:
    @staticmethod
    def roll() -> int:
        return random.choice(list(DiceValues)).value

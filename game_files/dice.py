import random, character
from character import Player


def roll_dice(rolls, dice):
    """Enter the number of rolls to be performed and the number of sides on the dice"""
    results = []
    for i in range(rolls):
        roll = random.randint(1, dice)
        results.append(roll)
    return results
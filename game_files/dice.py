import random


def roll_dice(rolls, dice):
    """Enter the number of rolls to be performed and the number of sides on the dice"""
    results = []
    for i in range(rolls):
        roll = random.randint(1, dice)
        results.append(roll)
    return results


def primary_stat_roll():
    """Rolls 4 D6, removes the lowest and adds up the total"""
    good_roll = False
    a = []
    while not good_roll:
        for i in range(6):
            x = roll_dice(4, 6)
            x.remove(min(x))
            a.append(int(sum(x)))
        if max(a) > 13:
            good_roll = True
        else:
            a.clear()
    return a



import random, character
from character import Player


def roll_dice(rolls, dice):
    """Enter the number of rolls to be performed and the number of sides on the dice"""
    results = []
    for i in range(rolls):
        roll = random.randint(1, dice)
        results.append(roll)
    return results


# TODO Let's redo the character stat generation logic

def primary_stat_roll():
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

a = primary_stat_roll()
b = {player1['strength'], player1['agility'], player1['intel'], player1['wisdom'], player1['con']}

# TODO Fix this While loop to pull the name for the stat and assign the number
'''
while len(a) > 0:
    print('You have the following stats to use:')
    index = 1
    for i in a:
        print('Roll', index, ':', i)
        index += 1
    print('Enter the roll you would like to assign to', b[0])
    choice = int(input('>>> ')) - 1
    b[0] = a.pop(choice)
'''

print(player1.__dict__)


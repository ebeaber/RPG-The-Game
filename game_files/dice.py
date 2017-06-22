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
# x = character.get_player_class()  # create a variable for the subclasses of the Player object
# player1 = Player.factory("Warrior")  # Call the Player Object Factory and create a player
# class_info = Player.info_factory(x)  # Fetch the information on the chosen character class for the player.
# print('The Player', player1.__dict__)
# Start setting statistics
# Roll four D6 and remove the lowest value. Repeat this process 5 times.

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

x = primary_stat_roll()
print('You have rolled the following stats:')
index = 1
for i in x:
    print('Roll', index, ':', i)
    index += 1

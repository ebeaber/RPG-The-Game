from random import random, randint

import dice
from character import Character


class Enemy(Character):
    def __init__(self, name, strength, agility, intelligence, wisdom, constitution):
        super().__init__(name)
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution

    # TODO Add Combat functions
    # TODO Add loot generator functions


enemies = {'Spider': 'small', 'Imp': 'small', 'Wolf': 'medium', 'Goblin': 'medium',
           'Ogre': 'large', 'Orc': 'large', 'Troll': 'large', 'Marmalade': 'boss'}

# Stat modifiers for enemy size
size_modifiers = dict()
size_modifiers['large'] = {'Strength': 3, 'Agility': -2, 'Intelligence': -2,
                           'Wisdom': -2, 'Constitution': 3}
size_modifiers['medium'] = {'Strength': 1, 'Agility': 1, 'Intelligence': 1,
                            'Wisdom': 1, 'Constitution': 1}
size_modifiers['small'] = {'Strength': -2, 'Agility': 3, 'Intelligence': 2,
                           'Wisdom': 2, 'Constitution': -1}
size_modifiers['boss'] = {'Strength': 5, 'Agility': 5, 'Intelligence': 5,
                          'Wisdom': 5, 'Constitution': 5}


def random_enemy_size():
    x = sorted(list(set(enemies.values())))  # make a sorted list of sizes
    odds = round(random(), 3)  # float value for odds
    if odds >= 0.980:  # compare float to boss chance value (currently 2%)
        return x[0]  # return boss
    else:
        return x[randint(1, len(x) - 1)]  # return random size if not boss


def random_enemy_name(size):
    # list of names based on size return input
    x = list({k for k, v in enemies.items() if v == size})
    # get a random name for the enemy from the filtered list
    name = x[randint(0, len(x) - 1)]
    # return that name
    return name


def enemy_modifier(size):
    return size_modifiers[size]  # return the modifiers for the size


def modified_enemy_stats(modifier):
    scores = dice.enemy_stat_roll()  # roll some random stats
    stat_names = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Constitution']
    enemy_stats = dict()
    for j in range(5):
        enemy_mods = modifier[stat_names[j]]
        thisscore = -99
        while thisscore not in scores:
            thisscore = scores[-1]
        enemy_stats[stat_names[j]] = thisscore + enemy_mods  # assign mods to score
        score_index = scores.index(thisscore)
        del scores[score_index]
    return enemy_stats


def create_enemy_object():
    size = random_enemy_size()  # get a random size
    name = random_enemy_name(size)  # get a random name based on size
    mods = enemy_modifier(size)  # get the size modifier
    stats = (modified_enemy_stats(mods))  #apply mod and get new random stats
    enemy = {**stats}  # create dict for stats
    # return stats as an Enemy object
    return Enemy(name, enemy['Strength'], enemy['Agility'],
                 enemy['Intelligence'], enemy['Wisdom'], enemy['Constitution'])
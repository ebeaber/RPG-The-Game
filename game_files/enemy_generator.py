import dice, random
from character import Character

# TODO Create enemies to continue combat module....

class Enemy(Character):
    def __init__(self, name, strength, agility, intelligence, wisdom, constitution):
        super().__init__(name)
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution


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


def random_enemy_stats():
    scores = sorted(dice.enemy_stat_roll())
    stat_names = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Constitution']
    enemy_stats = dict()
    for j in range(5):
        enemy_modifier = size_modifiers[stat_names[j]]
        thisscore = -99
        while thisscore not in scores:
            thisscore = scores[-1]
        enemy_stats[stat_names[j]] = thisscore + enemy_modifier  # assign mods to score
        score_index = scores.index(thisscore)
        del scores[score_index]
    return enemy_stats

stat_names = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Constitution']
print(size_modifiers['small'])
print([size_modifiers['small'][stat_names[0]]])


def ran_enemy_size():
    x = (sorted(list(set(enemies.values()))))  # get all enemy sizes
    boss_odds = .99
    if random > boss_odds:
        return x[0]
    else:
        return x[random.randint[1,3]]


# Imports
import random


def get_player_class():
    print('Choose your roll:')
    x = [name.__name__ for name in Player.__subclasses__()]
    index = 1
    for item in x:
        print(index, ':', item)
        index += 1
    choice = int(input('>>>>  ')) - 1
    return x[choice]


def player_stat_constructor():
    point_pool = 50
    print('Customize your character\'s stats. You have', point_pool, 'points to use.')


class Character(object):
    """Primary Object for all Characters in the game"""

    # Constructor
    def __init__(self, name):
        self.name = name  # all characters need name


class Player(Character):
    """Player objects and functions"""

    def factory(pclass):  # build the factory to call the subclass modifiers for the chosen class
        if pclass == 'Warrior':
            return Warrior()
        if pclass == 'Wizard':
            return Wizard()
        if pclass == 'Paladin':
            return Paladin()
        if pclass == 'Priest':
            return Priest()
        if pclass == 'Monk':
            return Monk()

    factory = staticmethod(factory)

    def __init__(self, name, strength, agility, intel, wisdom, health, max_health, mana,
                 max_mana, atkpwr, magpwr, crit):
        super().__init__(name)
        self.strength = strength
        self.agility = agility
        self.intel = intel
        self.wisdom = wisdom
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.atkpower = atkpwr
        self.magpwr = magpwr
        self.crit = crit

    def player_name(self):
        self.name = str(input('Enter your character\'s name:'))


class Warrior(Player):
    pass

class Wizard(Player):
    pass

class Paladin(Player):
    pass

class Priest(Player):
    pass

class Monk(Player):
    pass

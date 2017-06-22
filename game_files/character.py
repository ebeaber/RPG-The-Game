# Imports
from dice import roll_dice


class Character(object):
    """Primary Object for all Character objects in the game"""

    # Constructor
    def __init__(self, name):
        self.name = name  # all characters need name


class Player(Character):
    """Player objects and functions"""

    @staticmethod
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

    # Constructor
    def __init__(self, name, pclass, ctype, strength, agility, intel, wisdom, con, health, max_health,
                 mana, max_mana, energy, max_energy, defense, atkpwr, magpwr, crit):
        super().__init__(name)
        self.pclass = pclass
        self.ctype = ctype
        self.strength = strength
        self.agility = agility
        self.intel = intel
        self.wisdom = wisdom
        self.con = con
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.energy = energy
        self.max_energy = max_energy
        self.defense = defense
        self.atkpower = atkpwr
        self.magpwr = magpwr
        self.crit = crit

    # Deconstructor!
    @staticmethod
    def del_player():
        del Player

    def player_name(self):
        self.name = str(input('Enter your character\'s name:  '))


# TODO Work on Dictionaries, Tuples and Lists for Characters: Race, Class, Stats, Bonuses, Abilities, Spells, etc

player_races
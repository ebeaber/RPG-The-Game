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
    def __init__(self, name, pclass, ctype, strength, agility, intel, wisdom,
                 constitution, health, max_health, mana, max_mana, energy,
                 max_energy, defense, atkpwr, magpwr, crit):
        super().__init__(name)
        self.pclass = pclass
        self.ctype = ctype
        self.strength = strength
        self.agility = agility
        self.intel = intel
        self.wisdom = wisdom
        self.constitution = constitution
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


# TODO Work on Dictionaries, Tuples and Lists for Characters: Race, Class, Stats,
# TODO Bonuses, Abilities, Spells, etc


# Racial Modifiers
racial_modifiers = dict()
# {"Strength": , "Agility": , "Intel": ,
#  "Wisdom": , "Constitution": }
racial_modifiers["Human"] = {"Strength": 1, "Agility": 1, "Intel": 1,
                             "Wisdom": 1, "Constitution": 1}
racial_modifiers["Elf"] = {"Strength": 0, "Agility": 1, "Intel": 2,
                           "Wisdom": 1, "Constitution": 0}
racial_modifiers["Halfling"] = {"Strength": -1, "Agility": 2, "Intel": 0,
                                "Wisdom": 0, "Constitution": -1}

# Armor Types, Skill to use, and armor class
armortypes = {'Padded Cloth': ('light armor', 10),
              'Leather Armor': ('light armor', 12),
              'Chain Mail': ('medium armor', 13),
              'Half Plate Armor': ('medium armor', 15),
              'Splint Armor': ('heavy armor', 16),
              'Full Plate Armor': ('heavy armor', 18)}

# Melee Attacks
melee_attacks = dict()
# Define attack, Class to use and base dmg
melee_attacks['Punch'] = {'Warrior': 2, 'Paladin': 2, 'Monk': 5}
melee_attacks['Slash'] = {'Warrior': 5, 'Paladin': 5}
melee_attacks['Kick'] = {'Warrior': 1, 'Paladin': 1, 'Monk': 4}
melee_attacks['Flying Kick'] = {'Monk': 3}


# Spell Attacks
spell_attacks = dict()
# Define attack, classes that can use and dmg for that class
spell_attacks['Fireball'] = {'Wizard': 5}
spell_attacks['Blizzard'] = {'Wizard': 4}
spell_attacks['Plasma Shot'] = {'Wizard': 3}

# Beneficial Spells
beneficial_spells = dict()
spell_attacks['Light Heal'] = {'Priest': 2, 'Paladin': 1}
spell_attacks['Heal'] = {'Priest': 4, 'Paladin': 2}
spell_attacks['Extreme Heal'] = {'Priest': 7, 'Paladin': 4}


def choose_race():
    index = 1
    for i in racial_modifiers.keys():
        print(index, '-', i)
        index += 1
    choice = int(input('Choose the number for your race: '))
    return i

print(choose_race())
# def get_racial_modifiers(x):
#    for k, v in racial_modifiers.items(x):

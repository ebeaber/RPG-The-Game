# Imports
from dice import roll_dice
import random

class Character(object):
    """Primary Object for all Character objects in the game"""

    # Constructor
    def __init__(self, name):
        self.name = name  # all characters need name


class Player(Character):
    """Player objects and functions"""

    # Constructor
    def __init__(self, name, race, pclass, ctype, strength, agility, intelligence,
                 wisdom, constitution, health, max_health, mana, max_mana,
                 energy, max_energy, inventory):
        super().__init__(name)
        self.race = race
        self.pclass = pclass
        self.ctype = ctype
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.energy = energy
        self.max_energy = max_energy
        self.inventory = inventory
        #self.defense = defense
        #self.atkpower = atkpwr
        #self.magpwr = magpwr
        #self.crit = crit

    # Deconstructor!
    def del_player(self):
        del Player

# Racial Modifiers
racial_modifiers = dict()
# {"Strength": , "Agility": , "Intel": ,
#  "Wisdom": , "Constitution": }
racial_modifiers["Human"] = {"strength": 1, "agility": 1, "intelligence": 1,
                             "wisdom": 1, "constitution": 1}
racial_modifiers["Elf"] = {"strength": 0, "agility": 1, "intelligence": 2,
                           "wisdom": 1, "constitution": 0}
racial_modifiers["Halfling"] = {"strength": -1, "agility": 2, "intelligence": 0,
                                "wisdom": 0, "constitution": -1}

# Armor Types, Skill to use, and armor class
armortypes = {'Padded Cloth': ('light armor', 10),
              'Leather Armor': ('light armor', 12),
              'Chain Mail': ('medium armor', 13),
              'Half Plate Armor': ('medium armor', 15),
              'Splint Armor': ('heavy armor', 16),
              'Full Plate Armor': ('heavy armor', 18)}

# dictionary of Character classes (pclass) and class type (ctype)
ctypes = {'Warrior': 'Melee', 'Paladin': 'Hybrid', 'Wizard': 'Magic'}

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


def choose_race():
    # Prompt for and return Character Race
    races = set(racial_modifiers.keys())
    for i in races:
        print('>> ', i)
    while True:
        race = input('Type in the race you\'d like to play: ').title()
        if race not in races:
            print('Try again there Hawking.  You have to type a race on the list.\n')
            continue
        else:
            # Good input received, exit loop
            break
    return race


def choose_class():
    # Prompt for and return Character Class
    for i in ctypes:
        print('>> ', i)
    while True:
        pclass = input('Type in the class you\'d like to play: ').title()
        if pclass not in ctypes:
            print('English motherfucker, do you read it? Type in a Class on the list!\n')
            continue
        else:
            # Good input received
            break
    return pclass

choose_class()

def generate_stats(racial_modifiers):
    # Methods to generate stat scores
    scores = primary_stat_roll() # 4D6 - lowest * 5
    print('The dice have been rolled!')
    # End score generation method
    stat_names = ["strength", "agility", "constitution",
                  "intelligence", "wisdom"]
    player_stats = dict()
    for j in range(5):  # loop through the specific abilities
        print("Scores to choose from are:")
        print(scores)
        thismod = racial_modifiers[stat_names[j]]
        if thismod != 0:
            if thismod > 0:
                thismodtxt = "+" + str(thismod)
            else:
                thismodtxt = str(thismod)
            print('''\nA {0} racial increase will be added for {1}.
                  '''.format(thismodtxt, stat_names[j]))
        thisscore = -99
        while thisscore not in scores:
            thisscore = int(input("Choose score for " + stat_names[j] + ": "))
        player_stats[stat_names[j]] = thisscore + thismod  # assign score to ability
        thisind = scores.index(thisscore)
        del scores[thisind]  # remove score from collection
    return player_stats


def player_health(constitution, level):
    base = 10  # set a base increase in hp
    factor = 1.35  # set the factor curve 1.8 or lower
    health = int(constitution + (base * (level ** factor)))
    return health


def player_mana(wisdom, level):
    base = 10
    factor = 1.35
    mana = int(wisdom + (base * (level ** factor)))
    return mana


def player_energy(agility, level):
    base = 10
    factor = 1.35
    energy = int(agility + (base * (level ** factor)))
    return energy


# BEGIN BUILD SCRIPT #
# build the player dictionary before passing to Object
def build_player_object():
    # Gather's all the data to build a new player object.
    print('{0:=^90}'.format(' RPG The Game '))
    p = dict()
    p['level'] = 1  # New Characters start at level 1
    p['experience'] = 0  # Dream on greenhorn.  0 XP to start
    p['name'] = input('Enter your character\'s name: ')  # .... duh
    p['race'] = choose_race()  # choose a race
    p['pclass'] = choose_class()  # choose a class
    p['ctype'] = ctypes[p['pclass']]
    player_stats = generate_stats(racial_modifiers[p['race']])  # Roll for stats
    p = {**p, **player_stats}  # combine stats into player dict
    p['health'] = player_health(p['constitution'], p['level'])
    p['max_health'] = p['health']
    p['mana'] = player_mana(p['wisdom'], p['level'])
    p['max_mana'] = p['mana']
    p['energy'] =  player_energy(p['agility'], p['level'])
    p['max_energy'] = p['energy']
    p['inventory'] = {}  # No experience, no inventory, life is hard.
    # print('Current Player Dict', sorted(player.items())) printout for testing
    '''Player Object includes:
    name, race, pclass, ctype, strength, agility, intelligence,
    wisdom, constitution, health, max_health, mana, max_mana,
    energy, max_energy
    '''
    return Player(p['name'], p['race'], p['pclass'], p['ctype'], p['strength'],
                  p['agility'], p['intelligence'], p['wisdom'], p['constitution'],
                  p['health'], p['max_health'], p['mana'], p['max_mana'],
                  p['energy'], p['max_energy'], p['inventory'])


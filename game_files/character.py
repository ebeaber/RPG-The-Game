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
                 wisdom, constitution):
        super().__init__(name)
        self.race = race
        self.pclass = pclass
        self.ctype = ctype
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution
        #self.health = health
        #self.max_health = max_health
        #self.mana = mana
        #self.max_mana = max_mana
        #self.energy = energy
        #self.max_energy = max_energy
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

#dictionary of Character classes (pclass) and class type (ctype)
character_classes = {'Warrior': 'Melee', 'Paladin': 'Hybrid', 'Wizard': 'Magic'}

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
    # Prompt for and return Character Race as a global
    global race
    for i in racial_modifiers.keys():
        print('>> ', i)
    race = str(input('Type in the race you\'d like to play: '))
    return race.title()

def choose_class():
    # Prompt for and return Character Class as a global
    global pclass
    for i in character_classes:
        print('>> ', i)
    pclass = str(input('Type in the class you\'d like to play: '))
    return pclass.title()

def generate_stats(racial_modifiers):
    # Methods to generate stat scores
    scores = primary_stat_roll() # 4D6 - lowest * 5
    print('The dice have been rolled!')
    #End score generation method
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
    # TODO update base HP to dice roll??
    base = constitution  # set a base increase in hp
    factor = 1.3  # set the factor curve 1.8 or lower
    hp = int(constitution + (base * (level ** factor)))
    return hp

### BEGIN BUILD SCRIPT ###
# build the player dictionary before passing to Object


def build_new_player():
    print('{0:=^90}'.format(' RPG The Game '))
    player = dict()
    player['level'] = 1  # New Characters start at level 1
    player['experience'] = 0  # Dream on greenhorn.  0 XP to start
    player['name'] = input('Enter your character\'s name: ')  # .... duh
    player['race'] = choose_race()  # choose a race
    player['pclass'] = choose_class()  # choose a class
    player_stats = generate_stats(racial_modifiers[player['race']])  # Roll for stats
    player = {**player, **player_stats}  # combine stats into player dict
    player['health'] = player_health(player['constitution'], player['level'])
    player['max_health'] = player['health']

    print('Current Player Dict', player)


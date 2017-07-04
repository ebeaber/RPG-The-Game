"""This file contains the Character Object and the Player class required
to build a new character.  Modifications to the Character class must be
reflected in the Player Class and the Enemy module."""

# Imports
from game_files.dice import primary_stat_roll


class Character(object):
    """Primary Object for all Character objects in the game"""

    # Constructor
    def __init__(self, name):
        self.name = name  # all character objects must be named


class Player(Character):
    """Player objects and functions"""

    # Constructor
    def __init__(self, name, race, pclass, ctype, strength, agility,
                 intelligence, wisdom, constitution, health, max_health,
                 mana, max_mana, energy, max_energy, inventory):
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

    # TODO Add Combat functions
    def attack_power(self):
        pass

    def defense_value(self):
        pass

    def reduce_stat(self, stat):
        pass

    def increase_stat(self, stat):
        pass

    def incease_xp(self, enemy_xp_value):
        pass

    # TODO Add inventory functions
    def list_items(self):
        items = self.inventory
        for k in items:
            print(k)

    def add_item(self):
        pass

    def remove_item(self):
        pass

    # TODO Add player gear functions???


# # # Being Character Creations Functions # # #

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

# dictionary of Character classes (pclass) and class type (ctype)
ctypes = {'Warrior': 'melee', 'Paladin': 'hybrid', 'Wizard': 'magic'}

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


def generate_stats(racial_modifiers):
    # Methods to generate stat scores
    scores = primary_stat_roll() # 4D6 - lowest * 5
    print('\nThe dice have been rolled!')
    # End score generation method
    stat_names = ["strength", "agility", "constitution",
                  "intelligence", "wisdom"]
    player_stats = dict()
    for j in range(5):  # loop through the specific abilities
        print("\nScores to choose from are:")
        print(scores)
        thismod = racial_modifiers[stat_names[j]]
        if thismod != 0:
            if thismod > 0:
                thismodtxt = "+" + str(thismod)
            else:
                thismodtxt = str(thismod)
            print('''A {0} racial increase will be added for {1}.
                  '''.format(thismodtxt, stat_names[j]))
        thisscore = -99
        while thisscore not in scores:
            thisscore = int(input("Enter a score for " + stat_names[j] + ": "))
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

    '''
    Player Object includes:
    name, race, pclass, ctype, strength, agility, intelligence,
    wisdom, constitution, health, max_health, mana, max_mana,
    energy, max_energy
    '''

    return Player(p['name'], p['race'], p['pclass'], p['ctype'], p['strength'],
                  p['agility'], p['intelligence'], p['wisdom'], p['constitution'],
                  p['health'], p['max_health'], p['mana'], p['max_mana'],
                  p['energy'], p['max_energy'], p['inventory'])

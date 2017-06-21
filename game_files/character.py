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

def create_player():
    # Instantiate an empty player object
    player1 = Player(name="", pclass="", ctype="", strength=0, agility=0, intel=0, wisdom=0, charisma=0,
                     health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
    player1.name = str(input('Enter your character\'s name: '))

def custom_player_stats():
    """This function allows complete customization of the player stats"""
    print('Let\'s customize your character\'s stats!')
    point_pool = 50
    choices = {'strength': 0, 'agility': 0, 'intel': 0, 'wisdom': 0, 'charisma': 0}
    while point_pool > 0:
        for key, value in choices.items():
            x = int(input('\nHow many points for ' + key.title() + ': '))
            choices[key] = x
            point_pool -= x
            print(key.title() + ' has been set to', x)
            print('You have', point_pool, 'points left.')
        if point_pool > 0:
            print('\nYou didn\'t spend all your points.  Try again.')
            point_pool = 50
        else:
            print('No more points left')
            break
    return choices


def random_player_stats(ctype):
    # Create an empty dictionary for the Primary stats
    choices = {'strength': 0, 'agility': 0, 'intel': 0, 'wisdom': 0, 'charisma': 0}

    # Create the total points pool
    point_pool = 50

    # Define the random dividers
    pdiv = random.uniform(1.5, 1.9)  # random float for division of pool
    pdiv2 = random.uniform(1.5, 1.7)  # random float for division of Primary stats
    pdiv3 = random.uniform(2.6, 3)

    # Start IF statement for Melee based player classes
    if ctype == "melee":

        # Generate random stats for the primary melee stats
        primary_points = int((point_pool / pdiv))
        point_pool -= primary_points  # Remove Primary Stat Pool from total point_pool

        choices['strength'] = int(primary_points / pdiv2)  # Set random Strength value
        primary_points -= choices['strength']  # Remove Strength Value from Primary Stat Pool
        choices['agility'] = primary_points  # Set Agility to remaining value
        # Generate random stats for the secondary stats
        choices['intel'] = int(point_pool / pdiv3)
        point_pool -= choices['intel']
        choices['wisdom'] = int(point_pool / pdiv2)
        point_pool -= choices['wisdom']
        choices['charisma'] = point_pool
        point_pool -= choices['charisma']

        # Print the results!
        for item, key in sorted(choices.items(), key=lambda x: x[0]):
            print(item.title(), key)

    # Start IF statement for magic based player classes
    if ctype == "magic":
        # Generate random stats for the primary melee stats
        primary_points = int((point_pool / pdiv))
        point_pool -= primary_points  # Remove Primary Stat Pool from total point_pool

        choices['intel'] = int(primary_points / pdiv2)  # Set random Strength value
        primary_points -= choices['intel']  # Remove Strength Value from Primary Stat Pool
        choices['wisdom'] = primary_points  # Set Agility to remaining value

        # Generate random stats for the secondary stats
        choices['charisma'] = int(point_pool / pdiv3)
        point_pool -= choices['charisma']
        choices['strength'] = int(point_pool / pdiv2)
        point_pool -= choices['strength']
        choices['agility'] = point_pool
        point_pool -= choices['agility']

        # Print the results!
        for item, key in sorted(choices.items(), key=lambda x: x[0]):
            print(item.title(), key)
        return choices


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
        assert 0, "Bad Player Subclass Creation, check factory:" + type

    factory = staticmethod(factory)

    def __init__(self, name, pclass, ctype, strength, agility, intel, wisdom, charisma, health, max_health, mana,
                 max_mana, atkpwr, magpwr, crit):
        super().__init__(name)
        self.pclass = pclass
        self.ctype = ctype
        self.strength = strength
        self.agility = agility
        self.intel = intel
        self.wisdom = wisdom
        self.charisma = charisma
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

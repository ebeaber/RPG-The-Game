# Imports
import random

# Add New Branch

class Character(object):
    """Primary Object for all Characters in the game"""

    # Constructor
    def __init__(self, name):
        self.name = name  # all characters need name


class Player(Character):
    """Player objects and functions"""

    @staticmethod
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
        assert 0, "Bad Player Subclass Creation, check factory."

    @staticmethod
    def info_factory(pclass):  # build a factory to call the info about the character class for players
        if pclass == 'Warrior':
            return Warrior.class_info()
        if pclass == 'Wizard':
            return Wizard.class_info()
        if pclass == 'Paladin':
            return Paladin.class_info()
        if pclass == 'Priest':
            return Priest.class_info()
        if pclass == 'Monk':
            return Monk.class_info()
        else:
            pass

    # Constructor
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
        self.name = str(input('Enter your character\'s name:  '))


""" Start Playable Character Classes"""


class Warrior(Player):
    """Creates a Warrior Player Object"""
    def __init__(self):
        super().__init__(name="", pclass="Warrior", ctype="melee", strength=0, agility=0, intel=0, wisdom=0,
                         charisma=0, health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
        super().player_name()

    @staticmethod
    def class_info():
        info = 'You have chosen the Warrior class.\nThey are master\'s of defense and armor and excel' \
               'in front line combat defending their comrades from harm.\n' \
               'Warriors use Strength and Agility as their primary stats.'
        return info


class Wizard(Player):
    """Creates a Wizard Player Object"""
    def __init__(self):
        super().__init__(name="", pclass="Wizard", ctype="magic", strength=0, agility=0, intel=0, wisdom=0,
                         charisma=0, health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
        super().player_name()

    @staticmethod
    def class_info():
        info = 'You have chosen the Wizard class.\nWizards control the four elements of the world and can\n' \
               'conjure spells that deal massive damage to their foes.  Wizards use Intelligence and Wisdom\n' \
               'as their primary stats.'
        return info


class Paladin(Player):
    """Creates a Paladin Player Object"""
    def __init__(self):
        super().__init__(name="", pclass="Paladin", ctype="melee", strength=0, agility=0, intel=0, wisdom=0,
                         charisma=0, health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
        super().player_name()

    @staticmethod
    def class_info():
        info = 'You have chosen the Paladin class.\nDefenders of the Holy Order and keepers of the peace,\n' \
               'a Paladin mixes the raw combat power of Warriors with the holy spells of a Priest to smite\n' \
               'their enemies and maintain order in the world.  Paladins use Strength and Wisdom as their\n' \
               'stats'
        return info


class Priest(Player):
    """Creates a Priest Player Object"""
    def __init__(self):
        super().__init__(name="", pclass="Priest", ctype="magic", strength=0, agility=0, intel=0, wisdom=0,
                         charisma=0, health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
        super().player_name()

    @staticmethod
    def class_info():
        info = 'You have chosen the Priest class.\nAs faithful servants of the Gods, Priests oversee\n' \
               'the physical and spiritual health of all living creatures in the world.  Wielding divine\n' \
               'powers, a Priest can grant the gift of live, or smite the evil within any creature.\n' \
               'Priests use Wisdom and Intelligence as their primary stats.'
        return info

class Monk(Player):
    """Creates a Monk Player Object"""
    def __init__(self):
        super().__init__(name="", pclass="Monk", ctype="melee", strength=0, agility=0, intel=0, wisdom=0,
                         charisma=0, health=0, max_health=0, mana=0, max_mana=0, atkpwr=0, magpwr=0, crit=0)
        super().player_name()

    @staticmethod
    def class_info():
        info = 'You have chosen the Monk class.\nMasters of balance and order, Monks live a lifestyle of \n' \
               'of seclusion and meditation.  Granting them a supreme awareness of the natural flow of the\n' \
               'world around them.  Monks use Agility and Strength as their primary stats.'
        return info


"""Being functions for character generation and customization"""

def get_player_class():
    print('Choose your character\'s class:')
    x = [name.__name__ for name in Player.__subclasses__()]
    index = 1
    for item in x:
        print('\t', index, ':', item)
        index += 1
    choice = int(input('>>>>  ')) - 1
    return x[choice]


def custom_player_stats():
    """This function allows complete customization of the player stats"""
    print('Let\'s customize your character\'s stats!')
    point_pool = 50
    stats = {'strength': 0, 'agility': 0, 'intel': 0, 'wisdom': 0, 'charisma': 0}
    while point_pool > 0:
        for key, value in stats.items():
            x = int(input('\nHow many points for ' + key.title() + ': '))
            stats[key] = x
            point_pool -= x
            print(key.title() + ' has been set to', x)
            print('You have', point_pool, 'points left.')
        if point_pool > 0:
            print('\nYou didn\'t spend all your points.  Try again.')
            point_pool = 50
        else:
            print('No more points left')
            break
    return stats


def random_player_stats(ctype):
    # Create an empty dictionary for the Primary stats
    stats = {'strength': 0, 'agility': 0, 'intel': 0, 'wisdom': 0, 'charisma': 0}

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

        stats['strength'] = int(primary_points / pdiv2)  # Set random Strength value
        primary_points -= stats['strength']  # Remove Strength Value from Primary Stat Pool
        stats['agility'] = primary_points  # Set Agility to remaining value
        # Generate random stats for the secondary stats
        stats['intel'] = int(point_pool / pdiv3)
        point_pool -= stats['intel']
        stats['wisdom'] = int(point_pool / pdiv2)
        point_pool -= stats['wisdom']
        stats['charisma'] = point_pool
        point_pool -= stats['charisma']

        # Print the results!
        for item, key in sorted(stats.items(), key=lambda x: x[0]):
            print(item.title(), key)

    # Start IF statement for magic based player classes
    if ctype == "magic":
        # Generate random stats for the primary melee stats
        primary_points = int((point_pool / pdiv))
        point_pool -= primary_points  # Remove Primary Stat Pool from total point_pool

        stats['intel'] = int(primary_points / pdiv2)  # Set random Strength value
        primary_points -= stats['intel']  # Remove Strength Value from Primary Stat Pool
        stats['wisdom'] = primary_points  # Set Agility to remaining value

        # Generate random stats for the secondary stats
        stats['charisma'] = int(point_pool / pdiv3)
        point_pool -= stats['charisma']
        stats['strength'] = int(point_pool / pdiv2)
        point_pool -= stats['strength']
        stats['agility'] = point_pool
        point_pool -= stats['agility']

        # Print the results!
        for item, key in sorted(stats.items(), key=lambda x: x[0]):
            print(item.title(), key)
        return stats

random_player_stats("melee")
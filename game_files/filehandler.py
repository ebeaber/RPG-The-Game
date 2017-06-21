"""This module handles user data saving and loading"""
import os
import json
from character import Player

# Some text formatting strings for return messages
yellow = '\033[33m'
bold = '\033[1m'
end_color = '\033[0m'

# Some test data - uncomment to use
# player1 = Player("Moron001", "Wizard", 200, 1250, 110, 40, 2, 1490)

def absolute_path():
    # Absolute Path Variables
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)


# Create a function to just save the damn data
def save_player_data(player):
    absolute_path()  # call the path!
    filename = '../savedata/' + player.name + ' - ' + player.pclass
    data = player.__dict__
    if os.path.isfile(filename):
        os.remove(filename)
        with open(filename, "w+") as savefile:
            json.dump(data, savefile)
        print('Oh, but you can\'t expect to wield supreme executive power\n'
              'just because some watery tart threw a sword at you.\n'
              + yellow + bold + 'Player File Updated' + end_color)
    else:
        with open(filename, "w+") as savefile:
            json.dump(data, savefile)
        print('Go and boil your bottoms, you sons of silly persons!\n'
              + yellow + bold + 'Player File Created' + end_color)


def list_player_files():
    absolute_path()
    print('\nSaved Data Files\n' + '=' * 30)
    files = os.listdir('../savedata/')
    index = 1
    for item in files:
        print(index, ': ',  item)
        index += 1
    print('\nEnter the number of the player file you wish to load:')
    choice = input('>>>> ')
    return choice


def load_player_data(player):
        """Update this to load data to the player object"""
        absolute_path()

        with open( 'r+') as infile:
            player = json.load(infile)
        return player


"""
          "\"Listen. Strange women lying in ponds distributing swords is\n"
          "no basis for a system of government. Supreme executive\n"
          "power derives from a mandate from the masses, not from\n"
          "some farcical aquatic ceremony.\"\n" + end_color +
"""


'''


#  Update this function later to load data to the player class
def load_file():
    """Update this to load data to the player object"""
    with open(sdir + sfile, 'r+') as infile:
        player = json.load(infile)
    return player
'''
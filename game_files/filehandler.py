"""This module handles user data saving and loading"""
import os
import json
import character

# Some text formatting strings for return messages
yellow = '\033[33m'
bold = '\033[1m'
end_color = '\033[0m'

# Some test data - uncomment to use
player1 = character.Player('TestSave', 'Human', 'Warrior', 'melee',
                           18, 17, 16, 15, 14, 25, 25, 20, 20, 22, 22,
                           {'Padded Armor': 'armor', 'Long Sword':
                            'pri_weapon', 'rubles': 200})


# TODO Fix Directory function to work without user input
def file_directory():
    pass


def write_file(player_data):
    pass
    '''
    filename = player_data['name'] + '-' + player_data['pclass']
    thisdir = file_directory()
    with open(os.path.join(thisdir, filename), mode="w") as myfile:
        json.dump(player_data, myfile)


def read_file():
    thisdir = choose_directory(False)

write_file(player1.__dict__)


'''
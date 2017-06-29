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


def write_file(name, pclass, data):
    filename = name + '-' + pclass
    with open('../savedata/' + filename, "w") as outfile:
        json.dump(data, outfile)
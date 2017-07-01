import json
import os
from character import Player

# Some test Player data
player1 = Player("TestData", "Human", "Warrior", "melee", 20, 19, 18, 17,
                 16, 25, 25, 20, 20, 18, 18,
                 {"Padded": "armor", "Long Sword": "weapon"})

# First navigate to top level folder of the package
while True:
    if os.path.relpath('.', '..') != 'RPG-The-Game':
        os.chdir('..')
        continue
    else:
        break

# Then create or move to the directory to store the data
save_dir = './savedata/'  # name the directory to save to

if not os.path.isdir(save_dir):  # check if directory isn't there
    os.makedirs(save_dir)  # create directory
    os.chdir(save_dir)  # move to directory
else:
    os.chdir(save_dir)  # if directory exists - just move to it


# JSON Converter function
# Input object (such as Player), output dictionary of that object
def convert_to_json(x):
    return x.__dict__


# Save function. Convert to JSON then write to file.
def write_file(player_data):
    x = convert_to_json(player_data)  # serialize new data
    with open('player.json', 'w') as file:  # write new data
        json.dump(x, file, sort_keys=True, indent=4)
    print('Saved Player Data...')  # print return message
    print('Data saved:', x)

write_file(player1)  # test write functions

# Load function.  Read JSON file and load to Player object.
''' A Player object contains the following required arguments: 
name, race, pclass, ctype, strength, agility,
intelligence, wisdom, constitution, health, max_health,
mana, max_mana, energy, max_energy, inventory
'''


def read_file():
    # open the file and load the info
    with open('player.json', 'r') as f:
        data = json.load(f)
    return data

x = read_file()
print('Loading return', x)


# TODO Complete the build function to return a Player object
def build_from_load(d):
    pass

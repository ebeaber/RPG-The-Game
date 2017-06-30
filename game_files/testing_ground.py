import json
import os
from character import Player
from filehandler import player1 as player

# First navigate to top level folder
while True:
    if os.path.relpath('.', '..') != 'RPG-The-Game':
        os.chdir('..')
        continue
    else:
        break

if not os.path.isdir('./savedata'):  # check for folder
    os.makedirs('./savedata/')  # create folder
    os.chdir('./savedata/')  # move to folder
    # print('Created and moved to Save Data')  # print a test message for devs
else:
    os.chdir('./savedata')  # folder exists - just move to it
    # print('Folder exists, moving to Save Data')  # test message for devs


# JSON Converter function
def convert_to_json(x):
    return x.__dict__


# Writing JSON data
def write_file(player_data):
    x = convert_to_json(player_data)  # serialize new data
    with open('player.json', 'w') as file:  # write new data
        json.dump(x, file)
    print('Saved Player Data...')  # print return message
    print('Data saved:', x)


# TODO Finish this... Needs to load saved data into a Player object
# Reading data back
def read_file():
    with open('player.json', 'r') as f:
        data = json.load(f)
    return data
import json
import os
from filehandler import player1

data = player1.__dict__


# Get correct to the correct directory
if os.path.relpath('.', '..') == 'game_files':
    print('Game files check', os.getcwd())
    os.chdir('../savedata')
if os.path.relpath('.', '..') == 'RPG-The-Game':
    print('Root Folder Check', os.getcwd())
    os.chdir('./savedata')
if os.path.relpath('.', '..') == 'savedata':
    print('You made it to the correct folder')


# Writing JSON data
def write_file(x):
    with open('data.json', 'w') as f:
        json.dump(x, f)


# Reading data back
def read_file():
    with open('data.json', 'r') as f:
        data = json.load(f)
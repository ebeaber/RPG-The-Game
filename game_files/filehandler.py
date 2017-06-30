import json
import os

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
        json.dump(x, file)
    print('Saved Player Data...')  # print return message
    print('Data saved:', x)


# TODO Finish this... Needs to load saved data into a new Player object

# Load function.  Read JSON file and load to Player object.
def read_file():
    with open('player.json', 'r') as f:
        data = json.load(f)
    return data

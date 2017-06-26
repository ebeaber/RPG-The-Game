"""This module handles user data saving and loading"""
import os
import platform
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


def choose_directory(need_write):
    '''Select a directory for file output or import, and check that it exists
       and is writeable.  need_write is a boolean indicating whether or not
       the directory must be writeable.'''
    # writeable directory on Android devices (since scripts3 directory of
    # QPython3 is not writeable from a script)
    android_dir = '/storage/emulated/{}/Documents'
    if os.path.isdir(android_dir.format('0')):
        mydir = android_dir.format('0')
    elif os.path.isdir(android_dir.format('legacy')):
        mydir = android_dir.format('legacy')
    # for all other situations write to current directory
    else:
        mydir = '.'

    # tell the user what the default is
    if mydir == '.':
        dirprint = 'the directory where the script is saved'
    else:
        dirprint = mydir
    if need_write:
        rw = 'writing'
    else:
        rw = 'reading'
    print('\nDefault directory for {0} files is {1}'.format(rw, dirprint))

    # test if the default is writeable, ask user if directory should be changed
    mydir_writeable = os.access(mydir, os.W_OK | os.X_OK)
    if need_write and not mydir_writeable:
        print('Directory is not writeable.')
        change_dir = "2"
    else:
        change_dir = "0"
        while change_dir not in {'1', '2'}:
            change_dir = input('Press 1 to keep default directory or 2 to change.')
    if change_dir == '2':  # change the directory
        tries = 0
        if platform.system() == "Windows":
            print("Example directory for Windows: c:/Users/username/Documents/")
            while tries == 0 or not os.path.isdir(mydir) or \
                    (need_write and not mydir_writeable):
                tries += 1
                mydir = input("Enter a new directory name:")
                if not os.path.isdir(mydir):
                    print(mydir + ' is not a valid directory.')
                else:
                    mydir_writeable = os.access(mydir, os.W_OK | os.X_OK)
                    if need_write and not mydir_writeable:
                        print(mydir + ' does not have write access.')
    return mydir

def write_file(player_data):
    filename = player_data['name'] + '-' + player_data['pclass']
    thisdir = choose_directory(True)

import filehandler
import sys
from character import Player

print('\n{0:=^120}\n'.format(' RPG The Game '))

# run the file handler script and instantiate a player object
player = filehandler.game_load()
print('\nGreetings,', player.name, 'welcome to the RPG!')

# Make a main menu:
def main_menu():
    print('\nChoose an action: ')
    main_menu_options = ['Explore', 'Inventory', 'Quit Game']
    index = 1
    for i in main_menu_options:
        print(index, ':',  i)
        index += 1
    choice = int(input('>>>> ')) - 1
    if choice == 0:
        print(main_menu_options[0], 'menu goes here')
        # insert call to this menu
    if choice == 1:
        inventory_menu()
        # insert call to this menu
    if choice == 2:
        sys.exit()


def inventory_menu():
    print('\nChoose an Action: ')
    menu_options = ['List all items', 'Sell an item',
                    'Equip an item', 'Return to Main']
    index = 1
    for i in menu_options:
        print(index, ':', i)
        index += 1
    choice = int(input('>>>> ')) - 1
    if choice == 0:
        player.list_items()
        inventory_menu()
    if choice == 1:
        player.sell_item()
        inventory_menu()
    if choice == 2:
        print('''You will forever be naked!
        This feature is coming soon''')
    if choice == 3:
        main_menu()

def explore():
    # link to movement module
    pass


def inventory():
    # create inventory management functions
    Player.list_items()


# Call menu scripts and while loops down here
main_menu()



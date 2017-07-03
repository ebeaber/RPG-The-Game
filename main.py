import filehandler
import sys

print('\n{0:=^120}\n'.format(' RPG The Game '))

# run the file handler script and instantiate a player object
player = filehandler.game_load()
print('\nGreetings,', player.name, 'welcome to the RPG!')

def main_menu():
    print('\nChoose an action: ')
    menu_options = ['Explore', 'Inventory', 'Quit Game']
    index = 1
    for i in menu_options:
        print(index, i)
        index += 1
    choice = int(input('>>>> ')) - 1
    if choice == 0:
        print(menu_options[0], 'menu goes here')
        # insert call to this menu
    if choice == 1:
        print(menu_options[1], 'menu goes here')
        # insert call to this menu
    if choice == 2:
        sys.exit()


main_menu()

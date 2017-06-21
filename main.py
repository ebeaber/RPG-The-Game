# imports
import character

# initialize game
# TODO Add Load Player Logic after file handler fix

print('{0:=^90}'.format(' The RPG '))
print('{0:<90}'.format('Lets begin your adventure!'))

# Character Class Choice
x = character.get_player_class()

# Call the Player Object Factory and create a player
player1 = character.Player.factory(x)

# TODO class info message here, build an if statement to reflect the proper info on the class

# Customize stats logic here
# TODO Create the logic to have the player customize their stats and overwrite player key values
print('\nGreetings', player1.name, '. Your character has 5 primary stats. Strength, Agility, Intelligence,\n'
      'Wisdom, and Charisma.  You have 50 points to distribute between all of your stats.\n'
      'How you distribute these points will determine how strong your character\'s abilities will be.')

print('Please select from the following choices:')
print('1 : Automatic Point Distribution')
print('2 : Fully Customized Point Distribution')
prompt = int(input('Enter a number :'))


print(player1.__dict__)  # for testing purposes only
#Save the data!
# FIXME fix the file handler to correctly save the player data after creation
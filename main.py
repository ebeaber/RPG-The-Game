# imports
import character

# initialize game
# TODO Add Load Player Logic after file handler fix

print('{0:=^90}'.format(' The RPG '))  # Game Title line in text mode
print('{0:<90}'.format('Lets begin your adventure!'))  # Crappy welcome message

x = character.get_player_class()  # create a variable for the subclasses of the Player object
player1 = character.Player.factory(x)  # Call the Player Object Factory and create a player
class_info = character.Player.info_factory(x)  # Fetch the information on the chosen character class for the player.

# Customize stats logic here
# TODO Create the logic to have the player customize their stats and overwrite player key values


print(player1.__dict__)  # for testing purposes only
#Save the data!
# FIXME fix the file handler to correctly save the player data after creation
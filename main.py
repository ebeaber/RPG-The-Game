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

# Customize stats logic here
# TODO Create the logic to have the player customize their stats and overwrite player key values



print(player1.__dict__)  # for testing purposes only
#Save the data!
# FIXME fix the file handler to correctly save the player data after creation
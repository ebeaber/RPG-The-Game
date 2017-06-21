# imports
import character, filehandler

# initialize game
# ADD LOAD PLAYER DATA LOGIC HERE LATER

print('{0:=^90}'.format(' The RPG '))
print('{0:<90}'.format('Lets begin your adventure!'))

#Character Class Choice
x = character.get_player_class()

#Call the Factory and create a player
player1 = character.Player.factory(x)

#Save the data!
filehandler.save_player_data(player1)

pname = player1.name
msg1 = str('\n' + pname + ', you find yourself in a dark room lit dimly by a single candle'
             ' that is about to burn out, a small window and a door. You are'
             ' alone, cold, and mostly naked.  What shall you do now?')
print('\n'.join(wrap(msg1)))

"""
Time to work on the main menu options!!!  They should be basic for now and
include explore (followed by a direction), check inventory(this still need to
be built...), and hunt for an enemy(random roll to find and enemy or fail, and 
then random roll to pick that enemy.)

Build enemies.py classes......
"""
""" This module contains spells and abilities usable by all character
objects in the game.  Call with caution."""

# Melee Attacks
melee_attacks = dict()
# Define attack, Class to use and base dmg
melee_attacks['Punch'] = {'Warrior': 2, 'Paladin': 2, 'Monk': 5}
melee_attacks['Slash'] = {'Warrior': 5, 'Paladin': 5}
melee_attacks['Kick'] = {'Warrior': 1, 'Paladin': 1, 'Monk': 4}
melee_attacks['Flying Kick'] = {'Monk': 3}


# Spell Attacks
spell_attacks = dict()
# Define attack, classes that can use and dmg for that class
spell_attacks['Fireball'] = {'Wizard': 5}
spell_attacks['Blizzard'] = {'Wizard': 4}
spell_attacks['Plasma Shot'] = {'Wizard': 3}

# Beneficial Spells
beneficial_spells = dict()
spell_attacks['Light Heal'] = {'Priest': 2, 'Paladin': 1}
spell_attacks['Heal'] = {'Priest': 4, 'Paladin': 2}
spell_attacks['Extreme Heal'] = {'Priest': 7, 'Paladin': 4}




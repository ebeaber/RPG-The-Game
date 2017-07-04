"""
This will contain all items that are obtainable by players in the game:
Dictionaries are formated as:
name_of_dict = {'Item Name': (item type, AC/Atk Value, Sell Value)

To list all items with a specific type:
list([k for k, (val1, val2) in armortypes.items() if val1 == 'light armor'])

To call the AC or Attack of an item:
armortypes['Padded Cloth'][1]

"""


# Armor Types, Skill to use, and armor class
armortypes = {'Padded Cloth': ('light armor', 10, 10),
              'Leather Armor': ('light armor', 12, 15),
              'Chain Mail': ('medium armor', 13, 20),
              'Half Plate Armor': ('medium armor', 15, 22),
              'Splint Armor': ('heavy armor', 16, 25),
              'Full Plate Armor': ('heavy armor', 18, 30),
              'Round Shield': ('hybrid', 5, 7),
              'Tower Shield': ('hybrid', 10, 10)}

weapontypes = {'Long Sword': ('melee', 5, 10),
               'Wooden Staff': ('magic', 3, 20),
               'Gemmed Staff': ('magic', 5, 100),
               'One-Handed Sword': ('hybrid', 4, 20)}



import dice, random
from character import Character

# TODO Create enemies to continue combat module....

class Enemy(Character):
    def __init__(self, name, strength, agility, intelligence, wisdom, constitution):
        super().__init__(name)
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution


enemies = {'Spider': 'small', 'Imp': 'small', 'Wolf': 'medium', 'Goblin': 'medium',
           'Ogre': 'large', 'Orc': 'large', 'Troll': 'large', 'Marmalade': 'boss'}

# Stat modifiers for enemy size
size_modifiers = dict()
size_modifiers['large'] = {'strength': 3, 'agility': -2, 'intelligence': -2,
                           'wisdom': -2, 'constitution': 3}
size_modifiers['medium'] = {'strength': 1, 'agility': 1, 'intelligence': 1,
                           'wisdom': 1, 'constitution': 1}
size_modifiers['large'] = {'strength': -2, 'agility': 3, 'intelligence': 2,
                           'wisdom': 2, 'constitution': -1}
size_modifiers['boss'] = {'strength': 5, 'agility': 5, 'intelligence': 5,
                           'wisdom': 5, 'constitution': 5}


# TODO FINISH THE RANDOM ENEMY LOGIC
def random_enemy():
    odds = random.randint(1, 100)
    b = list(set(enemies.values()))
    if odds >= 99:
        return b[3]
    else:
        return b[random.randint(0, 2)]


count = 10000
boss_hits = 0
while count > 0:
    a = random_enemy()
    if a == "boss":
        boss_hits += 1
        print(a)
    count -= 1

print(boss_hits)
from RPG_sys import *

class HPPotion(Item):
    def __init__(self, name, description, restore):
        super().__init__(name, description)
        self.restore = restore

    def use(self, entity):
        initialHP = entity.hp
        entity.hp = entity.hp + self.restore
        if entity.hp > entity.maxhp:
            entity.hp = entity.maxhp
        print(f"{entity.name} restored {entity.hp - initialHP} HP using {self.name}.")
        return

# define items
potionA = HPPotion("Weak Potion", "A potion that restores 1 HP.", 1)
potionB = HPPotion("Moderate Potion", "A potion that restores 3 HP.", 3)
class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage


class Character:
    def __init__(self, name: str, weapon: Weapon = None):
        self.name = name
        self.weapon = weapon  

    def attack(self):
        if self.weapon:
            print(f"{self.name} attacks with {self.weapon.name} for {self.weapon.damage} damage!")
        else:
            print(f"{self.name} punches for 5 damage!")


sword = Weapon("Excalibur", 50)


hero = Character("Arthur", sword)
hero.attack()  


del hero
print(sword.name) 

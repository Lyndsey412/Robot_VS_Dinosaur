from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.active_weapon = Weapon("Giant Fist", 50)  

    def attack(self, Dinosaur):
        pass    #attack (self, dinosaur): void 
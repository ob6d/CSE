class Character(object):
    def __init__(self, name, inventory, abilities, attack, move):
        self.name = name
        self.inventory = inventory
        self.abilities = abilities
        self.attack = attack
        self.move = move

    def move(self):
        print("You move forward")

    def run(self):
        print("You run away")

class Item(object):
    def __init__(self, name, use, weight, pick_up, drop, attack, color, wear):
        self.name = name
        self.use = use
        self.weight = weight
        self.pick_up = pick_up
        self.drop = drop
        self.attack = attack
        self.color = color
        self.wear = wear

    def pick_up(self):
        print("You pick up the %s" % self.name)

    def drop(self):
        print("You drop the %s" % self.name)

class weapon(Item):
    def __init__(self, pick_up, drop):
        super(weapon, self).__init__(pick_up, drop)

    def pick_up(self):
        print("You pick up the weapon")

class sword(weapon):
    def __init__(self, use, weight):
        super(sword, self).__init__(use, weight)

    def carry(self):
        print("You carry the sword and it weighs %d" % self.weight)

class spell(weapon):
    def __init__(self, use, attack):
        super(spell, self).__init__(use, attack)

    def write(self):
        print("You write a spell on the enemy")

class crossbow(weapon):
    def __init__(self, use, pick_up):
        super(crossbow, self).__init__(use, pick_up)

    def grab(self):
        print("You grab the crossbow")

class arrow(crossbow):
    def __init__(self, use, attack):
        super(arrow, self).__init__(use, attack)

    def attack(self):
        print("Attack the enemy using the crossbow and arrow")

class clothing(Item):
    def __init__(self, name, use):
        super(clothing, self).__init__(name, use)

    def use(self):
        print("You use the clothing and the brand is %s" % self.name)

class armor(clothing):
    def __init__(self, weight, use):
        super(armor, self).__init__(weight, use)

    def use(self):
        print("You use the armor")

class helmet(armor):
    def __init__(self, wear, use):
        super(helmet, self).__init__(wear, use)

    def put(self):
        print("You put on the helmet")

class shield(armor):
    def __init__(self, weight, use):
        super(shield, self).__init__(weight, use)

    def hold(self):
        print("You hold the shield in your hand")

class bulletproof_vest(armor):
    def __init__(self, name, use):
        super(bulletproof_vest, self).__init__(name, use)

    def wear(self):
        print("You wear the bulletproof vest")

class shirt(clothing):
    def __init__(self, name, use):
        super(shirt, self).__init__(name, use)

    def wear(self):
        print("You wear the %s shirt" % self.color)

class shoes(clothing):
    def __init__(self, name, use):
        super(shoes, self).__init__(name, use)

    def put(self):
        print("You put on the %s shoes" % self.color)

class pants(clothing):
    def __init__(self, name, use):
        super(pants, self).__init__(name, use)

    def wear(self):
        print("You wear %s pants" % self.color)

class accessory(Item):
    def __init__(self, name, use):
        super(accessory, self).__init__(name, use)

    def find(self):
        print("You find an accessory")

class hat(accessory):
    def __init__(self, wear, use):
        super(hat, self).__init__(wear, use)

    def wear(self):
        print("You wear a %s hat" % self.color)

class consumable(Item):
    def __init__(self, name, use):
        super(consumable, self).__init__(name, use)

    def use(self):
        print("You use the %s" % self.name)

class healing_potion(consumable):
    def __init__(self, name, use):
        super(healing_potion, self).__init__(name, use)

    def drink(self):
        print("You drink the healing potion")

class apple(consumable):
    def __init__(self, name, use):
        super(apple, self).__init__(name, use)

    def eat(self):
        print("You eat the apple")

class med_kit(consumable):
    def __init__(self, name, use):
        super(med_kit, self).__init__(name, use)

    def use(self):
        print("You use the med kit")

class Item(object):
    def __init__(self, name, use, weight, color):
        self.name = name
        self.use = use
        self.weight = weight
        self.color = color

    def pick_up(self):
        print("You pick up the %s" % self.name)

    def drop(self):
        print("You drop the %s" % self.name)


class Weapon(Item):
    def __init__(self, name, weight, color, attack):
        super(Weapon, self).__init__(name, "Use it to attack", weight, color)
        self.attack = attack

    def pick_up(self):
        print("You pick up the weapon")


class Sword(Weapon):
    def __init__(self, name, weight, color, attack):
        super(Sword, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def carry(self):
        print("You carry the sword and it weighs %d" % self.weight)


class SpellBottle(Weapon):
    def __init__(self, name, weight, color, attack):
        super(SpellBottle, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def write(self):
        print("You write a spell on the enemy")


class Crossbow(Weapon):
    def __init__(self, name, weight, color, attack):
        super(Crossbow, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def grab(self):
        print("You grab the crossbow")


class Arrow(Crossbow):
    def __init__(self, name, weight, color, attack):
        super(Arrow, self).__init__(name, weight, color, "Use it to attack with the crossbow")
        self.attack = attack

    def attack(self):
        print("Attack the enemy using the crossbow and arrow")


class Clothing(Item):
    def __init__(self, name, weight, color, attack):
        super(Clothing, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the clothing and the brand is %s" % self.name)


class Armor(Clothing):
    def __init__(self, name, weight, color, attack):
        super(Armor, self).__init__(name, weight, color, "Use the armor for protection")
        self.attack = attack

    def use(self):
        print("You use the armor")


class Helmet(Armor):
    def __init__(self, name, weight, color, attack):
        super(Helmet, self).__init__(name, "1 pound", color, attack)
        self.weight = weight

    def put(self):
        print("You put on the helmet")


class Shield(Armor):
    def __init__(self, name, weight, color, attack):
        super(Shield, self).__init__(name, weight, color, "Use it to defend")
        self.attack = attack

    def hold(self):
        print("You hold the shield in your hand")


class BulletproofVest(Armor):
    def __init__(self, name, weight, color, attack):
        super(BulletproofVest, self).__init__(name, weight, color, "Use the bulletproof vest for protection")
        self.attack = attack

    def wear(self):
        print("You wear the bulletproof vest")


class Shirt(Clothing):
    def __init__(self, name, weight, color, attack):
        super(Shirt, self).__init__(name, weight, "blue", attack)
        self.color = color

    def wear(self):
        print("You wear the %s shirt" % self.color)


class Shoes(Clothing):
    def __init__(self, name, weight, color, attack):
        super(Shoes, self).__init__(name, weight, "black and white", attack)
        self.color = color

    def put(self):
        print("You put on the %s shoes" % self.color)


class Pants(Clothing):
    def __init__(self, name, weight, color, attack):
        super(Pants, self).__init__(name, weight, "black", attack)
        self.color = color

    def wear(self):
        print("You wear %s pants" % self.color)


class Accessory(Item):
    def __init__(self, name, weight, color, attack):
        super(Accessory, self).__init__(name, weight, color, attack)

    def find(self):
        print("You find an accessory")


class FlashLight(Item):
    def __init__(self, name, weight, color, attack):
        super(FlashLight, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the flashlight")


class Hat(Accessory):
    def __init__(self, name, weight, color, attack):
        super(Hat, self).__init__(name, weight, "white", attack)
        self.color = color

    def wear(self):
        print("You wear a %s hat" % self.color)


class Consumable(Item):
    def __init__(self, name, weight, color, attack):
        super(Consumable, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the %s" % self.name)


class HealingPotion(Consumable):
    def __init__(self, name, weight, color, attack):
        super(HealingPotion, self).__init__(name, weight, color, attack)

    def drink(self):
        print("You drink the healing potion")


class Apple(Consumable):
    def __init__(self, name, weight, color, attack):
        super(Apple, self).__init__(name, weight, color, "Eat the apple to get energy")

    def eat(self):
        print("You eat the apple")


class MedKit(Consumable):
    def __init__(self, name, weight, color, attack):
        super(MedKit, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the med kit")

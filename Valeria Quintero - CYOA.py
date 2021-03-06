# import statements
# import class definitions
# items
# characters
# rooms
# instant
# class item(object):
#   self.room


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


class Room(object):
    def __init__(self, name, north, south, east, west, southeast, southwest, northeast, northwest, description,
                 item=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.northeast = northeast
        self.northwest = northwest
        self.southwest = southwest
        self.southeast = southeast
        self.description = description
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Items
sword = Sword(Sword, "4 pounds", "silver", "Use the sword to defend yourself")
spellBottle = SpellBottle("SpellBottle", "1 pound", None, "Use the spell to heal")
crossbow = Crossbow("Crossbow", "50 pounds", "brown", "Use the crossbow and the arrow to attack")
arrow = Arrow("Arrow", None, None, "Use the arrows and the crossbow to attack")
armor = Armor("Armor", "70 pounds", "bronze", "Use the armor for protection")
helmet = Helmet("Helmet", "1 pound", "bronze", "Use the helmet for protection")
shield = Shield("Shield", "15 pounds", "silver", "Use the shield to defend")
bulletproofVest = BulletproofVest("BulletproofVest", "5 pounds", "black", "Use the bulletproof vest for protection")
shirt = Shirt("Shirt", None, "blue", None)
shoes = Shoes("Shoes", None, "black and white", None)
pants = Pants("Pants", None, "black", None)
flashLight = FlashLight("FlashLight", None, "red", "Use the flashlight if you can't see")
hat = Hat("Hat", None, "white", None)
healingPotion = HealingPotion("HealingPotion", None, None, "Drink the potion to heal yourself")
apple = Apple("Apple", None, None, "Eat the apple to get energy")
medKit = MedKit("MedKit", "2 pounds", None, "Use the medkit when you're injured or need something")

# Initialize Rooms
FRONTHOUSE = Room('Front of House', None, None, None, None, "LIVING_ROOM", "GARDEN", None, None,
                  "You are NORTHEAST of the GARDEN and NORTHWEST of the LIVING_ROOM")
LIVING_ROOM = Room('Living Room', None, 'KITCHEN', None, None, None, None, None, 'FRONTHOUSE',
                   "You are NORTH of the KITCHEN and SOUTHEAST of the FRONTHOUSE", "Sword")
KITCHEN = Room('The Kitchen', 'LIVING_ROOM', 'TUNNEL', 'RIGHTHOUSE', None, None, None, None, None,
               "You are SOUTH of the LIVING_ROOM, WEST of the RIGHTHOUSE, and NORTH of the TUNNEL", "Apple")
RIGHTHOUSE = Room('Right Side of House', None, None, None, "KITCHEN", None, None, None, None,
                  "You are EAST of the KITCHEN", "Crossbow, Arrow")
TUNNEL = Room('The Tunnel', "KITCHEN", None, None, None, None, 'CAVEROOM', None, None,
              "You are SOUTH of the KITCHEN and NORTHEAST of the CAVEROOM")
SMALLROOM = Room('The Small Room', None, None, None, None, None, 'MYSTERYROOM', "LIVING_ROOM", None,
                 "You are SOUTHWEST of the LIVING_ROOM and NORTHEAST of the MYSTERYROOM", "Shirt, Pants, Shoes")
GARDEN = Room('The Garden', None, 'CIRCLEROOM', None, None, None, None, "FRONTHOUSE", None,
              "You are SOUTHWEST of the FRONTHOUSE and NORTH of the CIRCLEROOM", "SpellBottle")
CIRCLEROOM = Room('The Circle Room', "GARDEN", 'CELLAR', None, None, None, None, None, None,
                  "You are NORTH of the CELLAR and SOUTH of the GARDEN", "Armor, Helmet, Shield")
MYSTERYROOM = Room('The Mystery Room', None, None, None, None, None, 'CELLAR', "SMALLROOM", None,
                   "You are SOUTHWEST of the SMALLROOM and NORTHEAST of the CELLAR", "HealingPotion")
CAVEROOM = Room('The Cave Room', None, 'TROLLROOM', None, 'CELLAR', None, None, "TUNNEL", None,
                "You are SOUTHWEST of the TUNNEL, EAST of the CELLAR, and NORTH of the TROLLROOM")
LEFTHOUSE = Room('Left Side of House', None, None, "CIRCLEROOM", None, None, None, None, None,
                 "You are WEST of the CIRCLEROOM", "MedKit")
CELLAR = Room('The Cellar', "CIRCLEROOM", 'TREASUREROOM', 'CAVEROOM', None, None, 'ATTIC', 'MYSTERYROOM', None,
              "You are SOUTH of the CIRCLEROOM, SOUTHWEST of the MYSTERYROOM, NORTH of the TREASUREROOM,"
              "NORTHEAST of the ATTIC, and WEST of the CAVEROOM", "Flashlight")
ATTIC = Room('The Attic', None, "BACKHOUSE", None, None, None, None, 'CELLAR', None,
             "You are NORTH of the BACKHOUSE and SOUTHWEST of the CELLAR", "BulletproofVest")
TREASUREROOM = Room('The Treasure Room', "CELLAR", None, None, None, 'CAGEROOM', None, None, None,
                    "You are SOUTH of the CELLAR and NORTHWEST of the CAGEROOM", "HealingPotion, Armor")
TROLLROOM = Room('The Troll Room', "CAVEROOM", 'CAGEROOM', None, None, None, None, None, None,
                 "You are NORTH of the CAGEROOM and SOUTH of the CAVEROOM")
BACKHOUSE = Room('Back of House', "ATTIC", None, None, None, None, None, None, None,
                 "You are SOUTH of the ATTIC", "SpellBottle, MedKit")
CAGEROOM = Room('The Cage Room', "TROLLROOM", None, None, None, None, None, None, 'TREASUREROOM',
                "You are SOUTH of the TROLLROOM and SOUTHEAST of the TREASUREROOM")


current_node = FRONTHOUSE
directions = ['north', 'south', 'east', 'west', 'southwest', 'southeast', 'northeast', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'sw', 'se', 'ne', 'nw']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')

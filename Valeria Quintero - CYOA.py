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


class sword(Weapon):
    def __init__(self, name, weight, color, attack):
        super(sword, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def carry(self):
        print("You carry the sword and it weighs %d" % self.weight)


class spell(Weapon):
    def __init__(self, name, weight, color, attack):
        super(spell, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def write(self):
        print("You write a spell on the enemy")


class crossbow(Weapon):
    def __init__(self, name, weight, color, attack):
        super(crossbow, self).__init__(name, weight, color, "Use it to attack")
        self.attack = attack

    def grab(self):
        print("You grab the crossbow")


class arrow(crossbow):
    def __init__(self, name, weight, color, attack):
        super(arrow, self).__init__(name, weight, color, "Use it to attack with the crossbow")
        self.attack = attack

    def attack(self):
        print("Attack the enemy using the crossbow and arrow")


class clothing(Item):
    def __init__(self, name, weight, color, attack):
        super(clothing, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the clothing and the brand is %s" % self.name)


class armor(clothing):
    def __init__(self, name, weight, color, attack):
        super(armor, self).__init__(name, weight, color, "Use the armor for protection")
        self.attack = attack

    def use(self):
        print("You use the armor")


class helmet(armor):
    def __init__(self, name, weight, color, attack):
        super(helmet, self).__init__(name, "1 pound", color, attack)
        self.weight = weight

    def put(self):
        print("You put on the helmet")


class shield(armor):
    def __init__(self, name, weight, color, attack):
        super(shield, self).__init__(name, weight, color, "Use it to defend")
        self.attack = attack

    def hold(self):
        print("You hold the shield in your hand")


class BulletproofVest(armor):
    def __init__(self, name, weight, color, attack):
        super(BulletproofVest, self).__init__(name, weight, color, "Use the bulletproof vest for protection")
        self.attack = attack

    def wear(self):
        print("You wear the bulletproof vest")


class shirt(clothing):
    def __init__(self, name, weight, color, attack):
        super(shirt, self).__init__(name, weight, "blue", attack)
        self.color = color

    def wear(self):
        print("You wear the %s shirt" % self.color)


class shoes(clothing):
    def __init__(self, name, weight, color, attack):
        super(shoes, self).__init__(name, weight, "black and white", attack)
        self.color = color

    def put(self):
        print("You put on the %s shoes" % self.color)


class pants(clothing):
    def __init__(self, name, weight, color, attack):
        super(pants, self).__init__(name, weight, "black", attack)
        self.color = color

    def wear(self):
        print("You wear %s pants" % self.color)


class accessory(Item):
    def __init__(self, name, weight, color, attack):
        super(accessory, self).__init__(name, weight, color, attack)

    def find(self):
        print("You find an accessory")


class hat(accessory):
    def __init__(self, name, weight, color, attack):
        super(hat, self).__init__(name, weight, "white", attack)
        self.color = color

    def wear(self):
        print("You wear a %s hat" % self.color)


class consumable(Item):
    def __init__(self, name, weight, color, attack):
        super(consumable, self).__init__(name, weight, color, attack)

    def use(self):
        print("You use the %s" % self.name)


class HealingPotion(consumable):
    def __init__(self, name, weight, color, attack):
        super(HealingPotion, self).__init__(name, weight, color, attack)

    def drink(self):
        print("You drink the healing potion")


class apple(consumable):
    def __init__(self, name, weight, color, attack):
        super(apple, self).__init__(name, weight, color, attack)

    def eat(self):
        print("You eat the apple")


class MedKit(consumable):
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
    def __init__(self, name, north, south, east, west, southeast, southwest, northeast, northwest, description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
FRONTHOUSE = Room('Front of House', None, None, None, None, "LIVING_ROOM", "GARDEN", None, None,
                  "You are NORTHEAST of the GARDEN and NORTHWEST of the LIVING_ROOM")
LIVING_ROOM = Room('Living Room', None, 'KITCHEN', None, None, None, None, None, 'FRONTHOUSE',
                   "You are NORTH of the KITCHEN and SOUTHEAST of the FRONTHOUSE")
KITCHEN = Room('The Kitchen', 'LIVING_ROOM', 'TUNNEL', 'RIGHTHOUSE', None, None, None, None, None,
               "You are SOUTH of the LIVING_ROOM, WEST of the RIGHTHOUSE, and NORTH of the TUNNEL")
RIGHTHOUSE = Room('Right Side of House', None, None, None, "KITCHEN", None, None, None, None,
                  "You are EAST of the KITCHEN")
TUNNEL = Room('The Tunnel', "KITCHEN", None, None, None, None, 'CAVEROOM', None, None,
              "You are SOUTH of the KITCHEN and NORTHEAST of the CAVEROOM")
SMALLROOM = Room('The Small Room', None, None, None, None, None, 'MYSTERYROOM', "LIVING_ROOM", None,
                 "You are SOUTHWEST of the LIVING_ROOM and NORTHEAST of the MYSTERYROOM")
GARDEN = Room('The Garden', None, 'CIRCLEROOM', None, None, None, None, "FRONTHOUSE", None,
              "You are SOUTHWEST of the FRONTHOUSE and NORTH of the CIRCLEROOM")
CIRCLEROOM = Room('The Circle Room', "GARDEN", 'CELLAR', None, None, None, None, None, None,
                  "You are NORTH of the CELLAR and SOUTH of the GARDEN")
MYSTERYROOM = Room('The Mystery Room', None, None, None, None, None, 'CELLAR', "SMALLROOM", None,
                   "You are SOUTHWEST of the SMALLROOM and NORTHEAST of the CELLAR")
CAVEROOM = Room('The Cave Room', None, 'TROLLROOM', None, 'CELLAR', None, None, "TUNNEL", None,
                "You are SOUTHWEST of the TUNNEL, EAST of the CELLAR, and NORTH of the TROLLROOM")
LEFTHOUSE = Room('Left Side of House', None, None, "CIRCLEROOM", None, None, None, None, None,
                 "You are WEST of the CIRCLEROOM")
CELLAR = Room('The Cellar', "CIRCLEROOM", 'TREASUREROOM', 'CAVEROOM', None, None, 'ATTIC', 'MYSTERYROOM', None,
              "You are SOUTH of the CIRCLEROOM, SOUTHWEST of the MYSTERYROOM, NORTH of the TREASUREROOM,"
              "NORTHEAST of the ATTIC, and WEST of the CAVEROOM")
ATTIC = Room('The Attic', None, "BACKHOUSE", None, None, None, None, 'CELLAR', None,
             "You are NORTH of the BACKHOUSE and SOUTHWEST of the CELLAR")
TREASUREROOM = Room('The Treasure Room', "CELLAR", None, None, None, 'CAGEROOM', None, None, None,
                    "You are SOUTH of the CELLAR and NORTHWEST of the CAGEROOM")
TROLLROOM = Room('The Troll Room', "CAVEROOM", 'CAGEROOM', None, None, None, None, None, None,
                 "You are NORTH of the CAGEROOM and SOUTH of the CAVEROOM")
BACKHOUSE = Room('Back of House', "ATTIC", None, None, None, None, None, None, None,
                 "You are SOUTH of the ATTIC")
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

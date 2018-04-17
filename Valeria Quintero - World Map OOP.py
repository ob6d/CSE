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

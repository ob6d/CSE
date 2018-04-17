# minimum = 15 rooms
"""world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
    }
    }
},
'NORTHHOUSE': {
    'NAME': 'North of House',
    'DESCRIPTION': "Insert Description here",
    'PATHS': {
        'NORTH': 'WESTHOUSE'
    }
}
'SOUTHHOUSE': {
    'NAME': 'South of House',
    'DESCRIPTION': "Insert Description here",
    'PATHS': {
        'NORTH': 'WESTHOUSE'
    }
}"""

world_map = {
    'FRONTHOUSE': {
        'NAME': "Front of House",
        'DESCRIPTION': "You are NORTHEAST of the GARDEN and NORTHWEST of the LIVINGROOM",
        'PATHS': {
            'SOUTHWEST': 'GARDEN',
            'SOUTHEAST': 'LIVINGROOM'
        }
    },
    'LIVINGROOM': {
        'NAME': "Living Room",
        'DESCRIPTION': "You are NORTH of the KITCHEN and SOUTHEAST of the FRONTHOUSE",
        'PATHS': {
            'SOUTH': 'KITCHEN',
            'NORTHWEST': 'FRONTHOUSE'
        }
    },
    'KITCHEN': {
        'NAME': "The Kitchen",
        'DESCRIPTION': "You are SOUTH of the LIVINGROOM, WEST of the RIGHTHOUSE, and NORTH of the TUNNEL",
        'PATHS': {
            'NORTH': 'LIVINGROOM',
            'EAST': 'RIGHTHOUSE',
            'SOUTH': 'TUNNEL'
        }
    },
    'RIGHTHOUSE': {
        'NAME': "Right Side of House",
        'DESCRIPTION': "You are EAST of the KITCHEN",
        'PATHS': {
            'WEST': 'KITCHEN'
        }
    },
   'TUNNEL': {
        'NAME': "The Tunnel",
        'DESCRIPTION': "You are SOUTH of the KITCHEN and NORTHEAST of the CAVEROOM",
        'PATHS': {
            'NORTH': 'KITCHEN',
            'SOUTHWEST': 'CAVEROOM',
        }
    },
    'SMALLROOM': {
        'NAME': "The Small Room",
        'DESCRIPTION': "You are SOUTHWEST of the LIVINGROOM and NORTHEAST of the MYSTERYROOM",
        'PATHS': {
            'NORTHEAST': 'LIVINGROOM',
            'SOUTHWEST': 'MYSTERYROOM'
        }
    },
    'GARDEN': {
        'NAME': "The Garden",
        'DESCRIPTION': "You are SOUTHWEST of the FRONTHOUSE and NORTH of the CIRCLEROOM",
        'PATHS': {
            'NORTHEAST': 'FRONTHOUSE',
            'SOUTH': 'CIRCLEROOM'
        }
    },
    'CIRCLEROOM': {
        'NAME': "The Circle Room",
        'DESCRIPTION': "You are NORTH of the CELLAR and SOUTH of the GARDEN",
        'PATHS': {
            'NORTH': 'GARDEN',
            'SOUTH': 'CELLAR'
        }
    },
    'MYSTERYROOM': {
        'NAME': "The Mystery Room",
        'DESCRIPTION': "You are SOUTHWEST of the SMALLROOM and NORTHEAST of the CELLAR",
        'PATHS': {
            'NORTHEAST': 'SMALLROOM',
            'SOUTHWEST': 'CELLAR'
        }
    },
    'CAVEROOM': {
        'NAME': "The Cave Room",
        'DESCRIPTION': "You are SOUTHWEST of the TUNNEL, EAST of the CELLAR, and NORTH of the TROLLROOM",
        'PATHS': {
            'NORTHEAST': 'TUNNEL',
            'SOUTH': 'TROLLROOM',
            'WEST': 'CELLAR'
        }
    },
    'LEFTHOUSE': {
        'NAME': "Left Side of House",
        'DESCRIPTION': "You are WEST of the CIRCLEROOM",
        'PATHS': {
            'EAST': 'CIRCLEROOM'
        }
    },
    'CELLAR': {
        'NAME': "The Cellar",
        'DESCRIPTION': "You are SOUTH of the CIRCLEROOM, SOUTHWEST of the MYSTERYROOM, NORTH of the TREASUREROOM, "
                       "NORTHEAST of the ATTIC, and WEST of the CAVEROOM",
        'PATHS': {
            'NORTH': 'CIRCEROOM',
            'EAST': 'CAVEROOM',
            'NORTHEAST': 'MYSTERYROOM',
            'SOUTH': 'TREASUREROOM',
            'SOUTHWEST': 'ATTIC'
        }
    },
    'ATTIC': {
        'NAME': "The Attic",
        'DESCRIPTION': "You are NORTH of the BACKHOUSE and SOUTHWEST of the CELLAR",
        'PATHS': {
            'SOUTH': 'BACKHOUSE',
            'NORTHEAST': 'CELLAR'
        }
    },
    'TREASUREROOM': {
        'NAME': "The Treasure Room",
        'DESCRIPTION': "You are SOUTH of the CELLAR and NORTHWEST of the CAGEROOM",
        'PATHS': {
            'NORTH': 'CELLAR',
            'SOUTHEAST': 'CAGEROOM'
        }
    },
    'TROLLROOM': {
        'NAME': "The Troll Room",
        'DESCRIPTION': "You are NORTH of the CAGEROOM and SOUTH of the CAVEROOM",
        'PATHS': {
            'NORTH': 'CAVEROOM',
            'SOUTH': 'CAGEROOM'
        }
    },
    'BACKHOUSE': {
        'NAME': "Back of House",
        'DESCRIPTION': "You are SOUTH of the ATTIC",
        'PATHS': {
            'NORTH': 'ATTIC'
        }
    },
    'CAGEROOM': {
        'NAME': "The Cage Room",
        'DESCRIPTION': "You are SOUTH of the TROLLROOM and SOUTHEAST of the TREASUREROOM",
        'PATHS': {
            'NORTH': 'TROLLROOM',
            'NORTHWEST': 'TREASUREROOM'
        }
    },

}

current_node = world_map['FRONTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'SOUTHWEST', 'SOUTHEAST', 'NORTHEAST', 'NORTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')

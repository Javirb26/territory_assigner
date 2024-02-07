import random

# This program assigns a territory to a user(s) given a number of territories

# Territory list
territories = list(range(1, 23)) # Territories 1 through 22

# example list of dictionaries holding names of brothers and their current as well as previous held territory
brothers = [
    {'name': 'brotherA',
     'current_territory': None,
     'previous_territory': None,
     },
    {'name': 'brotherB',
     'current_territory': None,
     'previous_territory': None,
     },
    {'name': 'brotherC',
     'current_territory': None,
     'previous_territory': None,
     },
]

for brother in brothers:
    brother['current_territory'] = random.choice(territories)
    print(f'Brother {brother["name"]} has been assigened territory #{brother["current_territory"]}')

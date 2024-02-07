import random
import json

# This program assigns a territory to a user(s) given a number of territories

# Territory list
territories = list(range(1, 23)) # Territories 1 through 22

# example list of dictionaries holding names of brothers and their current as well as previous held territory
initial_brothers = [
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

# assignment function
def assigner(brothers, territories):
    # Copy the list to maintain the original list 
    available_territories = territories.copy()

    for brother in brothers:
        # filters out the brother's previous territory if possible
        filtered_territories = [t for t in territories if t != brother['previous_territory']]

        # if no Terr are left that aren't the brothers previous, use the available ones
        if not filtered_territories:
            filtered_territories = available_territories

        # Randomly select a new Terr from the filtered list
        new_territory = random.choice(filtered_territories)

        # Update/Assign brother's territory information
        brother['previous_territory'] = brother['current_territory']
        brother['current_territory'] = new_territory

        # Remove the newly assign territory from the pool of available territories
        available_territories.remove(new_territory)
        
        print(f'Brother {brother["name"]} has been assigened territory #{brother["current_territory"]}')

        # Reset the available territories if all have been assigned
        if not available_territories:
            available_territories = territories.copy()

assigner(brothers, territories)

# print(brothers)
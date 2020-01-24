from room import Room
from player import Player
from item import Item
import sys 

# Declare items

item = {
    'torch':  Item("Torch",  "A torch to light the way"),
    'key':  Item("Key",  "A key to unlock a door"),
    'apple':  Item("Apple",  "An apple to sate your appetite")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [ item['torch'], item['apple'] ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['key']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player1 = Player("Mike", room['outside'])

##################################################
# Loop start
##################################################

# Print at the beginning
player1.get_current_room()

while True:

    input_text = input("#: ")
    
    # Quit
    if input_text == "q":
        break
    
    # Print items in current room
    elif input_text == "look":
        player1.current_room.get_room_items()

    # Print items in inventory
    elif input_text == "inv":
        player1.get_inventory()

    elif len(input_text.split(" ")) > 1:
        action = input_text.split(" ")[0]
        item = input_text.split(" ")[1]
        
        # Pick up item
        if action == "take":
            player1.set_inventory_item(item)
        # Drop item
        elif action == "drop":
            player1.drop_inventory_item(item)

    # Change room
    else:
        player1.set_current_room(input_text)
        



# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

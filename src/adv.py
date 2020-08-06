from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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
def what_way(player, direction):
    attribute = direction + '_to'

#we use the hasattr method to check a class has attributes
    if hasattr(player.location, attribute):
        #the getattr fetches the value associated and updates location
        player.location = getattr(player.location, attribute)
    else:
        print(" \nTry again, there is nothing in that direction ")

# Make a new player object that is currently in the 'outside' room.
#starting point is outside the game, ask player to input a name 
player_name = input('Welcome to the game! Enter your name : ')
player_first = Player(player_name, room['outside'])

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

while True:
    #to start at a new line
    print('\n')
    print(f"{player_name}, Welcome to {player_first.location}")


    first_char = input("\nWhich way do you want to go? ").strip().lower().split()
    first_one = first_char[0]
    first_char = first_one[0]

    if first_char == 'q':
        print(f"Bye! \n")
        break
    if first_char == 'n': #if the first character in the input is n, move north
        what_way(player_first, first_char)
    elif first_char == 's': #if first character in input is s, move south
        what_way(player_first, first_char)
    elif first_char == 'e': # if first character is e, move east
        what_way(player_first, first_char)
    elif first_char == 'w':# if first char is w, move west
        what_way(player_first, first_char)
    else: 
        print(" \nTry again, there is nothing in that direction ")



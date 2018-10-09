# Python Adventure v2.0

# Initialize player inventory flags
hasMainKey = False
hasHandbag = False
hasSword = False
hasLibraryKey = False

# Initialize player status flags
isAlive = True
isEntering = True
hasEscaped = False
room = "Hallway"

# Function to show the help text
def showHelp():
    print("Don't be scared. You can do a couple of things:")
    print("- 'go' in a compass direction, e.g. 'go south' ")
    print("- 'search' to 'search room', or look into an object")
    print("- 'attack' to attack a monster")
    print("- 'take' an object, e.g. 'take key' ")

# Main loop - as long as the player is alive, and has not escaped, continue
while (isAlive == True and hasEscaped == False):

    if (room == "ROOMNAME"):
        if (isEntering):
            # print the room description
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive    
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go DIRECTION"):
                # change the room, set flag that player is entering
                room = "ROOMNAME"
                isEntering = True
            if (command == "look around" or "search room"):
                # print description

            if (command == "attack"):
                # if there is something to attack, handle attack
                # otherwise provide a witty statement
            if (command == "take OBJECT"):
                # check whether the object can be taken; if so take
            if (command == "help") : showHelp()

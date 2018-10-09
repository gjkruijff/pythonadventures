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

    # Hallway
    if (room == "Hallway"):
        if (isEntering):
            # print the room description
            print("You are in a dark, spooky house, all alone out in the forest.")
            print("There is only one door to the outside, and it is locked.")
            print("You hear strange, creaky sounds.")
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                room = "Parlour"
                isEntering = True
            if (command == "go south"):
                room = "DiningRoom"
                isEntering = True
            if (command == "go east"):
                print("Sickly green water and stinking mud is flowing down the staircase.")
                print("It looks like the water in the dark puddles at the bottom is moving.")
                print("You decide it is probably safer not to set foot on those rotten steps.")
            if (command == "go west"):
                if (hasMainKey):
                    print("With shaking hands you try putting the key into the lock,")
                    print("All the while looking over your shoulder left and right,")
                    print("to see whether there isn't another monster lurking in the dark.")
                    print("With a dry click, and then a creaking sound, the door opens.")
                    print("You are greated by a gale, slashing ice-cold rain on your face,")
                    print("but at least you can leave this forsaken place.")
                    hasEscaped = true
                else:
                    print("Franticly you rattle door, but it won't budge.")
                    print("The door remains locked and closed.")
            if (command == "look around" or command == "search room"):
                print("You find yourself in the hallway.")
                print("To the east is a winding staircase, on the verge of collapse.")
                print("To the west is the door to the outside.")
                print("You can go north, and south.")
            if (command.startswith("attack")):
                print("You wildly slash the air around you,")
                print("until you see yourself in the mirror in the hallway.")
                print("This looks silly. There is nothing to attack.")
            if (command.startswith("take")):
                print("Aside from some appalling mud, dust, and brackish water,")
                print("there really isn't anything worth taking here.")
            if (command == "help") : showHelp()
        # End while block for room
    # End if block for checking which room


    if (room == "Parlour"):
        if (isEntering):
            print("You go through the door, into the Parlour.")
            print("Heavy curtains cover most of the windows. ")
            print("It smells dusty here.")
            print("There is a door to the west, which appears locked.")
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                print("You cannot go north")
            if (command == "go south"):
                room = "Hallway"
                isEntering = True
            if (command == "go east"):
                if (hasLibraryKey):
                    room = "Library"
                    isEntering = True
                else:
                    print("You try the door, which seems to go to the Library,")
                    print("but you quickly notice it is really locked.")
                    print("You do hear sighing sounds coming from behind the door,")
                    print("yet until you have the key, you won't find out what causes them.")
            if (command == "go west"):
                if (hasMainKey):
                    print("With shaking hands you try putting the key into the lock,")
                    print("All the while looking over your shoulder left and right,")
                    print("to see whether there isn't another monster lurking in the dark.")
                    print("With a dry click, and then a creaking sound, the door opens.")
                    print("You are greated by a gale, slashing ice-cold rain on your face,")
                    print("but at least you can leave this forsaken place.")
                    hasEscaped = true
                else:
                    print("Franticly you rattle door, but it won't budge.")
                    print("The door remains locked and closed.")
            if (command == "look around" or command == "search room"):
                print("You find yourself in the hallway.")
                print("To the east is a winding staircase, on the verge of collapse.")
                print("To the west is the door to the outside.")
                print("You can go north, and south.")
            if (command.startswith("attack")):
                print("You wildly slash the air around you,")
                print("until you see yourself in the mirror in the hallway.")
                print("This looks silly. There is nothing to attack.")
            if (command.startswith("take")):
                print("Aside from some appalling mud, dust, and brackish water,")
                print("there really isn't anything worth taking here.")
            if (command == "help") : showHelp()

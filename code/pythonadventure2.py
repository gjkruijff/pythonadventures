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

# Introduction
print("=============================================================")
print("The Haunted House On The Hill")
print("(v2.0 -- a stupendous Story Byte Studios production)")

# Main loop - as long as the player is alive, and has not escaped, continue
while (isAlive == True and hasEscaped == False):

    # Hallway
    if (room == "Hallway"):
        if (isEntering):
            # print the room description
            print("-------------------------------------------------------------")
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
                    print("\nYOU WIN.")
                    print("\nTHE END (in case you hadn't figured that one out yet.)")
                    hasEscaped = True
                    isEntering = True
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

    # Parlour
    if (room == "Parlour"):
        if (isEntering):
            print("-------------------------------------------------------------")
            print("You go through the door, into the Parlour.")
            print("Heavy curtains cover most of the windows. ")
            print("It smells dusty here.")
            print("There is a door to the west, which appears locked.")
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                print("You cannot go north.")
                print("The wall seems pretty solid,")
                print("you won't scratch it away with your fingernails.")
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
                print("You cannot go west.")
                print("There are windows there, and they are all shut.")
            if (command == "look around" or command == "search room"):
                print("In the faint light, you see several chairs, and a coffee table.")
                print("There is a key on the coffee table.")
            if (command.startswith("attack")):
                print("You wildly slash the air around you,")
                print("whirling up the dust, causing you to cough heavily.")
                print("This looks silly. There is nothing to attack.")
            if (command == "take key"):
                print("You take the key from the coffee table.")
                print("Looking at it, you figure this may be the key to the Library.")
                hasLibraryKey = True
            if (command == "help") : showHelp()
        # End while for Parlour
    # End if checking whether Parlour

    # Library
    if (room == "Library"):
        if (isEntering):
            print("-------------------------------------------------------------")
            print("You unlock the door, and enter the Library.")
            print("You immediately notice the free floating full torso vaporous apparition.")
            print("In other words, there is a ghost.")
            print("It is floating in front of a sword, hanging above the mantelpiece.")
            ghostPresent = True
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                print("You cannot go north.")
                print("The wall seems pretty solid.")
                if (ghostPresent): print("Moreover, there is a ghost in the room!")
            if (command == "go south"):
                print("You cannot go south.")
                print("There are rows upon rows of books")
                if (ghostPresent): print("Moreover, there is still a ghost in the room!")
            if (command == "go east"):
                print("What looks like a door to the east is just a dark mirror.")
                print("Slightly unsettled, you withdraw.")
                if (ghostPresent): print("And then there is still that ghost!")
            if (command == "go west"):
                room = "Parlour"
                isEntering = True
            if (command == "look around" or command == "search room"):
                print("The room is covered wall to wall with bookshelves.")
                print("And the bookshelves have a lot of books.")
                print("In the middle of one wall, there is a fireplace.")
                print("Your attention is drawn to the sword hanging over the mantelpiece.")
                if (ghostPresent): print("There is a ghost reading a book, and sighing.")
            if (command == ("attack ghost")):
                print("You slowly walk towards the ghost.")
                print("As you approach, she looks towards you, about to say 'Shh!'")
                print("You respond with a questionable 'Boo?!' ")
                print("The ghost disappears, whispering 'the kitchen, danger...'.")
                ghostPresent = False
            if (command == "take sword"):
                if (ghostPresent == False):
                    print("You reach up to the sword, and take it.")
                    print("Be careful not to cut your fingers, as it is sharp.")
                    hasSword = True
                else:
                    print("As you try to reach thru the ghost, to reach the sword,")
                    print("She turns into a frighteningly old lady, flies through you,")
                    print("and covers you in sticky ectoplasmic goo.")
                    print("The ghost is still floating around, muttering angrily.")
                    print("Needless to say, you do not have the sword.")
            if (command == "help") : showHelp()
        # End while for Library
    # End if checking whether Library

    # Dining room
    if (room == "DiningRoom"):
        if (isEntering):
            # print the room description
            print("-------------------------------------------------------------")
            print("Through the open double doors you enter the dining room.")
            print("You see a large dining table in the center, with the sad remains of a past dinner.")
            print("The chairs are all over the place, some fallen.")
            print("A sickening, sweet smell hangs in the air, like something rotten.")
            print("The kitchen is to the east, the hallway to the north.")
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                room = "Hallway"
                isEntering = True
            if (command == "go east"):
                room = "Kitchen"
                isEntering = True
            if (command == "go west"):
                print("You cannot go west.")
                print("The windows a closed, covered by heavy curtains.")
            if (command == "go south"):
                print("Maybe 'it' is rapidly going south from here,")
                print("But you certainly aren't.")
            if (command == "look around" or command == "search room"):
                print("You see tracks on the floor, going from a fallen chair to the kitchen.")
                print("The tracks look like something heavy was dragged.")
                print("You hear strange sounds coming from the kitchen.")
                print("You can go north, and east to the kitchen.")
            if (command.startswith("attack")):
                if (hasSword == False):
                    print("You wildly chop and kick around you,")
                    print("until you see yourself in the mirror in the hallway.")
                    print("This looks silly. There is nothing to attack.")
                else:
                    print("You swing the sword through the air,")
                    print("and although the air is rather thick in here,")
                    print("it looks like you are even thicker.")
                    print("There is nothing to attack here.")
            if (command.startswith("take")):
                print("For a moment you inspect the broken dishes,")
                print("and the unappealing morsels of rotten food,")
                print("then you wisely decide there really isn't anything worth taking here.")
            if (command == "help") : showHelp()
        # End while block for room
    # End if block for checking which room

    # Kitchen
    if (room == "Kitchen"):
        if (isEntering):
            # print the room description
            print("-------------------------------------------------------------")
            print("As you open the door to the kitchen, ")
            print("an incredible stench assails your every sense.")
            print("Amidst rotten food strewn across the kitchen floor,")
            print("there sits a foul ghoul.")
            ghoulPresent = True
            isEntering = False
        # Loop within the room, as long as player is not leaving, and alive
        while (isAlive == True and isEntering == False):
            command = input("> ")
            if (command == "go north"):
                print("There are kitchen cabinets to the north.")
                print("They are too small for you to hide in.")
                print("You cannot go north.")
                if (ghoulPresent): print("Mind you, there is a ghoul in the kitchen.")
            if (command == "go west"):
                room = "DiningRoom"
                isEntering = True
            if (command == "go east"):
                print("There is a heap of foul-smelling meat towards the end of the kitchen.")
                if (ghoulPresent): print("Some of that takes the shape of a ghoul.")
                print("No matter how much you'd like to, you cannot go west.")
            if (command == "go south"):
                print("You cannot go south either.")
            if (command == "look around" or command == "search room"):
                if (ghoulPresent):
                    print("Towards the end of the kitchen, there is a ghoul,")
                    print("Eyeing you suspiciously, while chomping on what seems to be an arm,")
                    print("and covering a handbag that is hanging around its neck.")
                if (ghoulPresent == False):
                    print("What was once a ghoul is now a pile of despicably stinking muccus.")
                    print("Somewhere amidst the gore, you see the handbag.")
            if (command == "attack ghoul"):
                if (hasSword == False):
                    print("You wildly chop and kick around you,")
                    print("but the ghoul really isn't impressed.")
                    print("It burps loudly, and shows its teeth.")
                    print("You may need clean underwear once this is over.")
                else:
                    print("You swing the sword through the air,")
                    print("and with a fearsome cry you stumble towards the ghoul.")
                    print("As you slip and slide across the bloody floor,")
                    print("You trip over some half-eaten leg,")
                    print("and while falling over, you manage to skewer the surprised ghoul.")
                    print("The ghoul dies there and then, much to your own disbelief.")
                    ghoulPresent = False
            if (command == "take handbag"):
                if (ghoulPresent == False):
                    print("You see the handbag, and although you go all 'eeeeeuuwwww',")
                    print("you use a large fork to pick it up.")
                    print("Congratulations, you now have a handbag smeared with blood.")
                    hasHandbag = True
                else:
                    print("Unsurprisingly, the ghoul is not at all bemused.")
                    print("With her sharp claws covered in scraps of arm,")
                    print("she pushes you away hard,")
                    print("so hard that you slide all the way back to the dining room.")
                    room = "DiningRoom"
                    isEntering = True
            if (command == "search handbag" or command == "look handbag"):
                if (ghoulPresent == True):
                    print("Well, the handbag is right there,")
                    print("around the neck of the proud owner,")
                    print("the ghoul.")
                elif (ghoulPresent == False and hasHandbag == True):
                    print("Overcoming your disgust and fear for more strange things,")
                    print("you rummage through the handbag, and find the key to the main door,")
                    print("and for a moment you think, 'of course, where else could it have been?'")
                    hasMainKey = True
                else:
                    # else the ghoul is gone but you don't have the handbag yet
                    print("The handbag is amidst the heap of rot that was once a ghoul.")
                    print("No, you don't have it yet.")
            if (command == "help") : showHelp()
        # End while block for room
    # End if block for checking which room

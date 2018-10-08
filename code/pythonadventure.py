# Initialize flags
hasMainKey = False
hasHandbag = False
hasSword = False
hasLibraryKey = False
# The story begins -- the Hallway
print("You are in a dark, spooky house, all alone out in the forest.")
print("There is only one door to the outside, and it is locked.")
print("You hear strange, creaky sounds.")
command = input("> ")

if (command == "help"):
    print("Don't be scared. You can do a couple of things:")
    print("- 'go' in a compass direction, e.g. 'go south' ")
    print("- 'search' to 'search room', or look into an object")
    print("- 'attack' to attack a monster")
    print("- 'take' an object, e.g. 'take key' ")
    command = input("> ")

if (command == "look around"):
    print("You find yourself in the hallway.")
    print("To the east is a winding staircase, on the verge of collapse.")
    print("To the west is the door to the outside.")
    print("You can go north, and south.")
    command = input("> ")

if (command == "go west"):
    if (hasMainKey == True) :
        print("You have escaped the house! You can breathe easy now.")
    else:
        print("The door is locked. You need a key...")
        command = input("> ")

if (command == "go north"):
    print("You go through the door, into the Parlour.")
    print("Heavy curtains cover most of the windows. ")
    print("It smells dusty here.")
    print("There is a door to the west, which appears locked.")
    command = input("> ")
    if (command == "look around" or command == "search room"):
        print("In the faint light, you see several chairs, and a coffee table.")
        print("A key is laying on the coffee table.")
        command = input("> ")
    if (command == "take key"):
        hasLibraryKey = True
        print("You found the key to the library!")
        command = input("> ")
    if (command == "go west"):
        if (hasLibraryKey == False):
            print("The door to the library is locked.")
            print("You need the key to the library to open the door.")
        else:
            print("You unlock the door, and enter the Library.")
            print("You immediately notice the free floating full torso vaporous apparition.")
            print("In other words, there is a ghost.")
            print("It is floating in front of a sword, hanging above the mantelpiece.")
            command = input("> ")
            ghostPresent = True
            if (command == "look around" or command == "search room"):
                print("What are you doing?! There is a ghost flying around!")
                command = input("> ")
            if (command == "attack" or command == "attack ghost"):
                print("You slowly walk towards the ghost.")
                print("The ghost appears to be reading a book.")
                print("As you approach, she looks towards you, about to say 'Shh!'")
                print("You respond with a questionable 'Boo?!' ")
                print("The ghost disappears, whispering 'the kitchen, danger...'.")
                ghostPresent = False
                command = input("> ")
                if (command == "take sword" and ghostPresent == False):
                    print("You reach up to the sword, and take it.")
                    print("Be careful not to cut your fingers, as it is sharp.")
                    hasSword = True
            if (command == "take sword" and ghostPresent == True):
                print("As you try to reach thru the ghost, to reach the sword,")
                print("She turns into a frighteningly old lady, flies through you,")
                print("and covers you in sticky ectoplasmic goo.")
                print("The ghost is still floating around, muttering angrily.")

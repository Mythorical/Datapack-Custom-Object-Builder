##
 # Makes creating custom entities, items, or blocks easier.
 # dev/util/dcob/main.py
 # By Mythorical
##
import time
import os

type = ""
version = 1.0
validTypes = [
    "item",
    "block",
    "entity"
]

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkPathExistance(path):
    if os.path.exists(path):
        return True
    else:
        return False

def printHeader():
    with open("logo.txt", "r", encoding="utf-8") as file:
        logo = file.read()
    print(logo + "Datapack Custom Object Builder V" + str(version) + " By Mythorical\n")

def typeSelector():
    global type
    global version
    while True:
        printHeader()
        print("|> What type of object would you like to create:")
        type = input(str("|>      Item     Block     Entity\n")).lower()
        if type in validTypes:
            break
        else:
            print("ERROR: Not a valid type!")
            time.sleep(1)
            clearTerminal()

def main():
    import item
    typeSelector()

    if type == "item":
        clearTerminal()
        item.itembuilder()

    if type == "Block":
        print("Test")

    if type == "Entity":
        print("Test")

if __name__ == "__main__":
    main()
##
 # Creates custom item.
 # dev/util/dcob/item.py
 # By Mythorical
##
import time
import os

def itembuilder():
    from main import printHeader, checkPathExistance, clearTerminal
    filetypes = [
        ".mcfunction",
        ".json"
    ]
    validItemTypes = [
        "interactive",
        "debug"
    ]
    printHeader()
    itemName = str(input("|> What would you like to name your item:\n"))
    time.sleep(0.5)

    while True:
        printHeader()
        itemPath = str(input("|> What is the file path you would like to use (Type current to use the current directory.):\n")).lower()
        if itemPath == "current": itemPath = os.getcwd()
        if checkPathExistance(itemPath) == True:
            break
        else:
            print("ERROR: File path does not exist!")
            time.sleep(0.5)
    time.sleep(0.5)

    while True:
        printHeader()
        print("|> What type of item would you like to use:")
        itemType = str(input("|>     Interactive     Debug\n")).lower()
        if itemType in validItemTypes:
            break
        else:
            print("ERROR: Invalid item type!")

    time.sleep(0.5)

    printHeader()
    itemTextureType = str(input("|> What is the name of the items texture (Type skip if you'd like to setup textures and models yourself.):\n")).lower()
    time.sleep(0.5)

    while True:
        print("Item name: " + itemName)
        print("File path: " + itemPath)
        print("Item type: " + itemType)
        if itemTextureType == "skip":
            print("Skipped item texture!")
        else:
            print("Item texture: " + itemTextureType)
        confirmation = str(input("|> Are all of these correct (y/n):\n")).lower()
        if confirmation == "y":
            break
        elif confirmation == "n":
            clearTerminal()
            itembuilder()
        else:
            ("ERROR: Invalid answer!")
    
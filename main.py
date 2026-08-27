##
 # Makes creating custom entities, items, or blocks easier.
 # dev/util/dcob/main.py
 # By Mythorical
##
import time
import os
import item

type = ""
validTypes = [
    "Item",
    "Block",
    "Entity"
]

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def typeSelector():
    global type
    while True:
        print("What type of object would you like to create:")
        type = input(str("Item, Block, or Entity?\n"))
        if type in validTypes:
            break
        else:
            print("ERROR: Not a valid type!")
            time.sleep(1)
            clearTerminal()

typeSelector()

if type == "Item":
    clearTerminal()
    item.itembuilder()

if type == "Block":
    print("Test")

if type == "Entity":
    print("Test")
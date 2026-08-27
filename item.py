##
 # Creates custom item.
 # dev/util/dcob/item.py
 # By Mythorical
##
def itembuilder():
    import main
    import time
    import os
    name = str(input("What would you like to name your " + main.type + ":\n"))
    time.sleep(0.5)
    path = str(input("What is the file path you would like to use:\n"))
    time.sleep(0.5)
    filetype = name + ".mcfunction"
    with open(os.path.join(path, filetype), 'w') as fp:
        fp.write('give @s poisonous_potato[custom_name="' + str(name) + '",!food,!consumable]')
    







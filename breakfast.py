# Running on Python 2.7
# Importing libraries and packages
# To be able to print out strings properly
from __future__ import print_function
import time
import datetime
import math

# Breakfast menu decision tree
print (
    "Your breakfast options are:\n" +
    "1. Cereal\n" +
    "2. Toast\n" +
    "3. Pancakes\n" +
    "4. Porridge\n"
    )

mainChoice = int(input("Enter your choice of breakfast: "))

print("You chose option: ", mainChoice)

if (mainChoice <= 0) or (mainChoice >= 5):
    print("Play the game son. Your choice is invalid.")
    exit(1)

if (mainChoice == 1):
    print("\nThis is Cereal")
elif (mainChoice == 2):
    print("\nThis is Toast")
elif (mainChoice == 3):
    print("\nThis is Pancakes")
elif (mainChoice == 4):
    print("\nThis is Porridge")
else:
    print("Neal, your script is broken!")

if mainChoice in (1, 4):
    print("You have chosen a breakfast product which contains milk.")
    if mainChoice == 1:
        print("We have a range of cereals available for you to choose from.")
else:
    print("You have chosen a breakfast product which contains gluten.")

if (mainChoice == 1):
    print ("Which cereal would you like:\n" +
           "1. Cornflakes\n" +
           "2. Frosties\n" +
           "3. Sugar Puffs\n" +
           "4. Coco Pops\n"
           )
else:
    exit(0)

cerealChoice = int(input("Please choose the cereal you would like. "))

if cerealChoice in (1, 2, 3, 4):
    if cerealChoice == 1:
        print("You will be served Cornflakes")
    if cerealChoice == 2:
        print("You will be served Frosties")
    if cerealChoice == 3:
        print("You will be served Sugar Puffs")
    if cerealChoice == 4:
        print("You will be served Coco Pops")
else:
    print("We do not serve that cereal option. Play the game son.")
    exit(1)

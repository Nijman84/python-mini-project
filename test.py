# Running on Python 2.7
# Importing libraries and packages
# To be able to print out strings properly
from __future__ import print_function
import time
import datetime
import math

# Print function on the same line, but written on multiple lines here:
# print("This is the first line. " +
#     "This is the 2nd line.")

# Commebt blocks:
"""
This is a comment block
For writing stuff
On multiple lines
Haiku nyet
"""

# Print out the date time in a 'YYYY-MM-DD HH:MM:SS' format
'''
print(time.strftime("%Y-%m-%d %H:%M:%S"))
'''

# Capturing string input
'''
Name = raw_input("Tell me your name: ")
print("Hello", str(Name))
'''

# Inputting numbers
'''
ANumber = int(input("Type a number: "))
print("You typed: ", ANumber)
'''

# Basic if..else
'''
Value = int(input("Enter a value between 1 and 10: "))

if (Value >= 1) and (Value <= 10):
    print ("Nice one Charlie")
    print ("You typed: ", Value)
else:
    print ("You have to type a number between 1 and 10")
    print ("You typed: ", Value)
'''

# More complex if..elif..else
'''
print ("Are you ready for the rainbow piece?" +
    " Choose your favourite colour of the rainbow:\n"
    " 1. Red\n" +
    " 2. Orange\n" +
    " 3. Yellow\n" +
    " 4. Green\n" +
    " 5. Blue\n" +
    " 6. Indigo\n" +
    " 7. Violet")

Choice = int(input("Pick your colour by its number: "))

if Choice == 1:
    print("Red equals danger.")
elif Choice == 2:
    print("Orange is also a fruit.")
elif Choice == 3:
    print("Yellow is also a colour.")
elif Choice == 4:
    print("Green is also the colour of grass.")
elif Choice == 5:
    print("Blue is also the colour of the ocean.")
elif Choice == 6:
    print("Indigo is a very soothing colour.")
elif Choice == 7:
    print("Violet is a sultry choice.")
else:
    print("Your choice is invalid, you cheeky monkey.")
'''
# Multiple, nested if..elif..else statements
'''
One = int(input("Type a number between 1 and 10: "))
Two = int(input("Type a number between 1 and 10: "))

if (One >= 1) and (One <= 10):
   if (Two >= 1) and (Two <= 10):
      print("Your secret number is: ", One * Two)
   else:
      print("Incorrect second value!")
else:
   print("Incorrect first value!")
'''
'''
dob = int(input("Input the day of the month you were born as a number: "))
mob = int(input("Input your month of birth as a number: "))

if (dob >= 1) and (dob <= 31):
    if (dob == 20) and (mob == 1):
        print("You have the same birth date as Nealio")
    else:
        print("You have a different birthday to me")
else:
    print("Your input day of the month is wrong")
'''
'''
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

'''
# Basic for loop with break
'''
Value = raw_input("Write less than 7 characters: ")
LetterNum = 1

for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
    if LetterNum > 6:
        print("Your input is too long")
        break
'''
# Length checking len command
'''
inputPhrase = raw_input("Type some characters: ")
if len(inputPhrase) > 10:
    print("You are too long")
else:
    print("You are an acceptable length")
'''
# lowercase conversion with lower()
'''
word = "Turn Th!S !nt0 a L0w3rCas3! $string"
print(word.lower())
'''
# continue and pass statements within a for loop
# replace pass with continue and vice versa in the code below
# pass will process the line, continue will skip with no output to stdout
'''
LetterNum = 1
inputWord = raw_input("Type a word, any word: ")
for Letter in inputWord:
    if Letter.lower() == "o":
        pass
        print("cba with the letter ", Letter)
    print("Letter ", LetterNum, " of ", inputWord, " is ", Letter)
    LetterNum += 1
    if LetterNum > 9:
        print("Your word is too long for my tiny brain")
        break
else:
    print("You gave me an empty string you cheeky monkey.")
'''

# Running on Python 2.7
# Importing libraries and packages
# To be able to print out strings properly
from __future__ import print_function
from argparse import ArgumentParser
import time
import datetime
import math

# Print function on the same line, but written on multiple lines here:
# print("This is the first line. " +
#     "This is the 2nd line.")

# Comment blocks:
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

# Simple function and how to call it from command line
# Linter wants a docstring, which is the thing surrounded by """

'''
Calling this function from command line, from this file (test.py):
python -c 'from test import Hello; Hello("Greeting")'
'''
'''
def Hello(Greeting):
    """I think this is a docstring."""
    print("Hello world\n" +
          "Here is a personal greeting:", Greeting
          )
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
# For breakfast menu see breakfast.py
'''
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
# Basic while looping
'''
sum = 0
while sum <= 5:
    print("The current sum is ", sum)
    sum += 1
'''
# for and while loop to create times table
# the end=' ' will end a print line on the same line rather than a new one
'''
From command line:
python -c 'from test import timesTable; timesTable()'
'''


def timesTable():
    """Timestable example."""


X = 1
Y = 1

print ('{:>4}'.format(' '), end=' ')

for X in range(1, 14):
    print('{:>4}'.format(X), end=' ')

print()

for X in range(1, 14):
    print('{:>4}'.format(X), end=' ')
    while Y <= 13:
        print('{:>4}'.format(X * Y), end=' ')
        Y += 1
    print()
    Y = 1


'''
eof
'''

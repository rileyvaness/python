#All Excercises done in Python 2.7

import time
import math
import random

#EXCERCISE 1
print "Let's add two numbers together!"
A = 5
B = 6
C = 11

print A + B
print "Is C larger than A?"
if C > A:
    print "It appears so!"


## EXCERCISE 2

answer = "Trajedy"
if answer == "Trajedy":
    print "You chose to see a Trajedy."
elif answer == "Comedy":
    print "You chose to see a Comedy."
else:
    print "Please chose a Comedy or a Trajedy."

# EXCERCISE 3

##An if, elif, and else statement 
number = 5
if number == 2:
    print "Two is a very good number!"
elif number == 3:
    print "Three is also a good number!"
else:
    print number**2
## For loop
counter = 10
for counter in range(1,11):
    print counter * 2
## While Loop
x = 2
while x < 11:
    print x * 3
    time.sleep(.25)
    x = x + 1
    time.sleep(.25)
## A dictionary

shows = {'Comedy' : 'Merry Wives of Windsor', 'Trajedy' : 'Hamlet', 'History' : 'Richard III'}
print shows
print "The first show will be: " + shows['Comedy'] + "!"

print math.sqrt(64)
print(random.randint(0,100))    

## Some Math

print math.sqrt(64)
print(random.randint(0,100))

def Subtraction(A,B):
    subtract = A-B
    return subtract
print Subtraction(20,10)
print Subtraction(10, 5)
print Subtraction(500,350)

def addition(C,D,E):
    add = C + D + E
    return add
print addition (5, 10, 20)

def multipication (F,G,H):
    multiply = F*G*H
    return multiply
print multipication (2,4,6)

def division(I,J,K):
    divide = float(I)/float(J)/float(K)
    return divide
print division (20,4,2)

## MORE EXCERCISES 

#1 Assign an integer to a variable.
A = 3
#2 Assign a string to a variable.
B = "It is snowing"
#3 Assign a float to a variable.
C = float(10)
#4 Use the print function to print out the variable you assigned.
print B
#5 Use each of these operators: +, *, /, =, %.
print A + C
print A * C
print A / C
print A == C
print A%C
#6  Use each of these logical operators: and, or, not.
print A < 5 and C > 20
print A < 5 or C > 20
print not(A > 5 and C > 20)

#7 Use each conditional statement: if, elif, else.
if B == "It is snowing":
    print "It must be winter!"
elif B == "The leaves are falling":
    print "It must be the fall season!"
else:
    print "It seems to be either spring or summer..."

#8 Use a while loop.
y = 5
while y <= 50 :
    print y 
    time.sleep(.1)
    y = y + 5
    time.sleep(.1)

#9 Use a for loop.
counter = 2.2
for counter in range (1, 11):
    print counter* 1.1

#10 Create a list and iterate through that list using a for loop to print each item out on a new line.

shows = ['Knight of the Burning Pestle', 'Hamlet', 'Henry VI', 'Antony and Cleopatra', 'As You Like It']
for show in shows:
    print (show)
    time.sleep(.5)

#11 Create a tuple and iterate through it using a for loop to print each item out on a new line.
actors = ("Bob Saget", "Jim Carrey", "Jimmy Stewart", "Daniel Day Lewis")
for a in actors:
    print (a)
    time.sleep(.5)

#12 Define a function that returns a string variable.


def act(x):
    print x + ' is playing now!'
act('As You Like It')    



## Printing a list out in alphabetical order, line by line ##

characters = ["Duke Senior", "Duke Frederick", "Adam", "Orlando", "Oliver", "Rosalind", "Celia", "Jaques", "Amiens", "Touchstone", "Phebe", "Audrey", "Silvius"]
characters.sort()
for character in characters:
    print (character)

## use the Python range() function with one parameter to display the following (parameter being 'list_len':
#0,1,2,3
"""
list = ['0', '1', '2', '3']
list_len = len(list)
for i in range(list_len):
    print(list[i])
    """

## Use the Python range() function with 3 parameters to display the following
# 3,2,1,0
"""
list = ['0', '1', '2', '3']
list_len = len(list)
for i in range(3, -1, -1):
    print(list[i])
"""

## Use the Python range() function with 3 parameters to display the following:
#8,6,4,2

x = 8
for count in (range(x, 1, -2)):
    print(count)

## How old are you? ##
Name = raw_input ('Name: ')
print "Hello " + Name + "! We are going to find out how long you have been alive!"
Age = int(raw_input('How old are you?: ')) 
print "You are " + str(Age) + " years old."
Months = Age * 12
Days = Age * 365
Minutes = Age * 525948
Seconds = Age * 31556926
print Name + " has been alive for about: " + str(Months) + " months, " + str(Days) + " days," +str(Minutes) + " minutes, and " + str(Seconds) + " seconds!"

##Passing information between functions

def start ():
    print("Hello {}!".format(get_name()))

def get_name():
    name = raw_input("What is your name? ")
    return name

def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name, l_name,age, gender)
def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}".format(f_name,l_name,age,gender))

if __name__ == "__main__":
    start()




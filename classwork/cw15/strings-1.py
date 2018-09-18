# Simple concatenation, "adding" one string to another

string1 = "Hello"
string2 = "World"
string3 = string1 + string2

print(string3)

# Making it prettier

string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2

print(string3)

# Building ABCDEFGHIJKLMNOPQRSTUVWXYZ by concatenating one character
# at a time using their ordinal (ASCII) values.

myString = ""
for i in range (ord('A'),ord('Z') + 1):
    myString += chr(i)
print(myString)

# What does this do?

import random

myString = ""
for i in range (1,27):
    myString += chr(random.randint(ord('a'),ord('z')))
print(myString)

# Using loops and concatenation, print this:
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

myString = ""
for i in range(ord('0'),ord('9') + 1):
    myString += chr(i)
for i in range(ord('a'),ord('z') + 1):
    myString += chr(i)
for i in range(ord('A'),ord('Z') + 1):
    myString += chr(i)
print(myString)

# You can get the length of a string.  Strings are indexed from 0 to len() - 1

myString = "GoNavy"
print(len(myString))

print(min(myString)) # "Min" based on ASCII value
print(max(myString)) # "Max" based on ASCII value

# You can pick out individual characters in a string using an index

myString = "This is a test of concatenation"
print(myString[2])

# How about this?

myString = "This is a test of concatenation"
for i in range(0,len(myString)):
    print(myString[i])

# Python even lets you use negative numbers as "offsets" from end of a string

myString = "This is a test of concatenation"
print(myString[-2]) # Prints "o"

# Write a program to reverse the string:
# "This is a test of concatenation"
# 
# so it reads:
# 
# "noitanetacnoc fo tset a si sihT"

myString = "This is a test of concatenation"
myReverseString = ""
index = len(myString) - 1 # Strings are indexed from 0 -> n-1
while index >= 0:
    myReverseString += myString[index]
    index -= 1

print(myString)
print(myReverseString)

# Changing case

myString = "This is a test of concatenation"
upperString = myString.upper() # Change to uppercase

print(myString)
print(upperString)

lowerString = upperString.lower() # Change to lowercase

print(myString)
print(lowerString)

# Advanced strings -- Functions

# IMPORTANT: Strings in Python are immutable.  That means when you create
# one, you can't then change the individual characters in it.  That might
# seem counter-intuitive, but once you get used to it, it makes sense.  Well
# use some techniques later, using lists, that allow us to act on a string
# like it's mutable.

# You can use the times operator (*) to get multiple copies of a string:

s = "Welcome"

print(s*3) # Prints WelcomeWelcomeWelcome

# "in" and "not in" operators

s = "Welcome"
print("Wel" in s)
print("Wel" not in s)
print("Navy" not in s)

# Comparing strings

print("green" == "glow")
print("Hello" <= "World")
print("navy" > "Navy") # Why is this true?

# Python compares the ASCII values of strings one character at a time.
# What's the result of this comparison?

print("green" > "greenfield")


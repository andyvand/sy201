# Version 2.0.  This version of the legal drinking age calculator utilizes
# exception handling and formatted output.

# This program introduces nested conditionals using if..elif.

# In python3 (and many other languages) it's often a convention among
# programmers to use all caps for variable names that are intended to be
# constants.

import sys

ADULT = 18
LEGAL_DRINKER = 21

# Get a target age from the user and cast it to an int.

try:
   age = int(input("Enter your age: "))
except:
   print("Type in a number.")
   sys.exit(1)

# Using nested conditionals, check the age against the rules for adulthood and
# legal drinking age.  Print messages as appropriate.

if age <= 0:
   print("Invalid age")
   sys.exit(2)
elif (age >= ADULT) and (age < LEGAL_DRINKER):
   status = "you're an adult but not legal to drink."
elif age < ADULT:
   status = "you're not yet a legal adult."
else:
   status = "you're an adult and legal to drink."

print("You are age {0}, therefor {1}".format(age,status))


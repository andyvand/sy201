# This program introduces nested conditionals using if..elif.

# In python3 (and many other languages) it's often a convention among
# programmers to use all caps for variable names that are intended to be
# constants.

ADULT = 18
LEGAL_DRINKER = 21

# Get a target age from the user and cast it to an int.

age = int(input("Enter your age: "))

# Using nested conditionals, check the age against the rules for adulthood and
# legal drinking age.  Print messages as appropriate.

if (age >= ADULT) and (age < LEGAL_DRINKER):
   print("You're an adult but not legal to drink.")
elif age < ADULT:
   print("You're not yet a legal adult.")
else:
   print("You're an adult and legal to drink.")

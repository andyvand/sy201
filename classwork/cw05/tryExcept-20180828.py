# Introductory example of using try..except

# Import libraries.  Your import statements should be the first executable lines
# of code in your python programs.
import sys

# Try to run a line of code, and handle the exception if it occurs.
try:
   x = int(input("Enter a integer: "))
except:
   print("Oops! Invalid integer.")
   sys.exit(1) # Exit the program with a code of 1

# If there's an exception, this line of code never executes.
print("Your integer is:",x)
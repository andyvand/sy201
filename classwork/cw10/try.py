# Demonstration of how try...except interacts with sys.exit().

# When sys.exit() is called, that itself raises an exception called
# "SystemExit".  What happens in this code below if I enter -1?  How about if I
# enter DOG?  How do we fix it?

import sys

try:
   n = int(input("Enter an integer: "))
   if (n < 0):
      print("Negative number")
      sys.exit(1)
      
except:
   print("Invalid integer")
   sys.exit(2)

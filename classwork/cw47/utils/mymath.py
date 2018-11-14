import math

# This function determines if the natural number (n) is prime -- returns True or
# False.  If n is a non-integer, or < 2, then isPrime returns False.

def isPrime(n):
   
   counter = 3
   
   if n == 2:
      nIsPrime = True
      
   else:
      nIsPrime = type(n) == int
      nIsPrime = nIsPrime and (n % 2) != 0 and (n >= 3)
      while counter <= math.sqrt(n) and nIsPrime:
         nIsPrime = (n % counter) != 0
         counter += 2
         
   return nIsPrime

# --------------------------------------------------------------------------

# A more sophisticated example.  Allowing the user to input a positive integer
# (n), and calculating sum the integers from 1 to n.

n = 1

while n != 0:

   count = 0
   validInteger = False

   try:
      n = int(input("Enter a positive integer (0 to quit): "))
      validInteger = True
   except ValueError:
      print("Sorry, you entered an illegal integer")
    
   if validInteger: # Same as: "if validInteger == True"

      if n > 0:
         for i in range(1,n+1):
            count = count + i
         print("The sum of the integers from 1 to {0:,d} is {1:,d}".format(n,count))

      elif n < 0:
         print("Please make sure your integer is non-negative")

      else:
         print("Thanks for playing")

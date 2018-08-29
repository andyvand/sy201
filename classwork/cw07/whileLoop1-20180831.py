# While loop using a control variable (n)

n = 0

while n != -1:

   try:
      n = int(input("Enter an integer (-1 to exit): "))
      if n != -1:
         print("Your number squared =",n**2)
   except:
      print("Sorry, I need a valid integer")

print("The program is ended.")

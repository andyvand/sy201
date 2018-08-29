# While loop using infinite looping with break

while True:

   try:
      n = int(input("Enter an integer (-1 to exit): "))
      if n != -1:
         print("Your number squared =",n**2)
      else:
         break # Break out of the current loop
   except ValueError:
      print("Sorry, I need a valid integer")

print("The program is ended.")

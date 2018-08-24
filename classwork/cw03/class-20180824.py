# Note: to enable or disable sections of the code below, just comment it out by
# selecting it and pressing the control key and / (cntl-/)

# Read a number for the user and cast it to an int.
number = int(input("Enter a number: "))

# This is another way to collect user data with "input", and cast it to an int
number2 = int(number2)
print(number2)

# The code below uses conditionals (if statements) and the modulo operator to
# determine if the user input is evenly divisible by 5.  If so, "High Five!" is
# printed.  If not, then the code checks to see if the number is evenly
# divisible by 2 (meaning it's an even number).  If so, then "Even Number!" is
# printed.

# Don't forget the importance of indentation when you use conditionals.  Python
# expects the code below the "if" to be indented.  In this example, we only have
# one line below the "if", but we could have multiple lines -- we'll see
# examples of that later.

# Also remember to put a colon (:) at the end of the line when you use a
# conditional statement

if number % 5 == 0:
   print("High Five!")
if number % 2 == 0:
   print("Even number!")
   
# The code below uses the "else" clause with an "if" statement to check to see
# if an entered number is even or odd.  Notice the colon (:) after "else".

if number % 2 == 0:
   print("Even number")
else:
   print("Odd number")
   
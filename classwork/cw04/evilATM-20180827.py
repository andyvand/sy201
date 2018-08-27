# This code snippet demonstrates while "eval" is "evil".  When prompted for
# userPin, what happens if I enter "print(pin)" instead of a 4-digit number?

pin = 4567

userPin = eval(input("Enter your pin: "))

if userPin == pin:
   print("Success!")
else:
   print("Failure.")
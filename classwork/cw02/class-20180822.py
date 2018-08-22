# We can hard-code a value for radius, but it's not as useful as prompting the
# user for a value at run time.

# radius = 20
radius = float(input("Enter the radius: "))
# To raise a value to a power, use **
area = radius**2 * 3.14159
print("The area for the circle of radius", radius, "is", area)

# This program will crash when the two lines below are run.  Why?
interestRate = 0.05
interest = interestrate * 45
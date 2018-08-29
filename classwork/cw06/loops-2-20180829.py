# Here's an example of a loop with user input serving as a control mechanism.

n = 1
while n != 0:
   n = int(input("Enter an n (0 to exit): "))
   n = n * 2
   print("n times 2 =",n)
   
print("done")
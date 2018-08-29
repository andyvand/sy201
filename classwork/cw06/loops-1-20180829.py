# Introduction to looping.  See if you can tell what happens if:

# line 11 is changed to: n = n + 1
# line 9 is changed to: while n > 0
# line 8 is changed to: n = 0
# How would you have the program print 1 through 10, rather than 10 down to 1?

n = 10
while n != 0:
   print(n)
   n = n - 1
   
print("Program complete")
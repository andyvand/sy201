# A for loop, using a range of values.  Remember, when using "range(x,n)", the
# values produced will cover the range from x to n - 1.

# Here are some things to try:
#
# What if I enter 0?
# What if I enter -10?
# What if I change the loop to: for i in range(1,n+1)?
# What if I change the loop to: for i in range(1,n,2)?
# What if I change the loop to: for i in range(1,n,-1)?

n = int(input("Enter n: "))
for i in range(1,n):
   print(i)
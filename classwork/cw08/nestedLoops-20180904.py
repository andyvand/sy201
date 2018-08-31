# Some interesting nested loop examples.

# These loops introduce a new element to our print() statements: the "end ="
# clause. The default for print() is to put a newline at the end of whatever is
# printed. By adding a comma and "end = " (with a desired trailing output) we
# can replace the newline with whatever we want.

# Remember our "Hello World" loop below?  It used to print all the letters in
# "Hello World", one on each line.  What does it print now?

# for c in "Hello World":
#    print(c,end = " ")
# print() # Print a newline

# --------------------------------------------------------

# Loop 1 

# for i in range (1,5):
#    j = 0
#    while j < i:
#       print(j,end = " ")
#       j = j + 1

# --------------------------------------------------------

# Loop 2

# i = 0
# while i < 5:
#    for j in range(i,1,-1):
#       print(j,end = " ")
#    print("****")
#    i = i + 1
   
# --------------------------------------------------------

# Loop 3

# i = 5
# while i >= 1:
#    num = 1
#    for j in range(1,i+1):
#       print(num, end = "xxx")
#       num = num * 2
#    print() # Prints a new line
#    i = i - 1
   
# --------------------------------------------------------

# Loop 4

# i = 1
# while i <= 5:
#    num = 1
#    for j in range(1,i+1):
#       print(num,end = "G")
#       num = num + 2
#    print()
#    i += 1

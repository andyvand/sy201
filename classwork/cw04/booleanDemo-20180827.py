# More practice using complex Boolean expressions.

a = 4
b = 5
c = 6

# True and False, meaning Boolean 1 and 0, are reserved words in python3 and can
# be assigned directly to variables.

d = True
e = False

# What gets printed as a result of each of the statements below?  Try to figure
# it out before you run the code to see the answers.

bool1 = d and (a > b)
print("bool1 =",bool1)

bool2 = (not d) or (b != c)
print("bool2 =",bool2)

bool3 = (d and (not e)) or (a > b)
print("bool3 =",bool3)

bool4 = (a % b == 2) and ((not d) or e)
print("bool4 =",bool4)

# What gets printed as a result of the statement below?

print((bool1 and bool2) or (bool3 and not bool4))

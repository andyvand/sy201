# Sets are collections of *unique* (no duplicates), unordered values.

# Create an empty set, and add the number 5 to it.  When you print a set, what
# does it look like?

#----------------------------------------------------------------------
# s1 = set()
# s1.add(5)
# print(s1)
#----------------------------------------------------------------------

# Initializing a non-empty set

#----------------------------------------------------------------------
# s1 = {1,3,5}
# print(s1)
#----------------------------------------------------------------------

# Creating a set from a string.  What's notable about this conversion?

#----------------------------------------------------------------------
# str = "Hello World!"
# s1 = set(str)
# print(s1)
#----------------------------------------------------------------------

# Iterating over a set. Observations?

#----------------------------------------------------------------------
# for item in s1:
#    print(item)
#----------------------------------------------------------------------
   
# Manipulating sets

#----------------------------------------------------------------------
# print("There are {0:d} items in the set".format(len(s1)))
#----------------------------------------------------------------------

# Run the code below a few times.  I want to add 25 items to my set (0..24).  Do
# you ever encounter a run of the program where len(s1) is less than 25?  Why?

#----------------------------------------------------------------------
# import random
# s1 = set()
# for i in range(25):
#    s1.add(random.randint(1,100))
# 
# print(s1)
# print("Max = {0:d}; Min = {1:d}; Sum = {2:d}".format(max(s1),min(s1),sum(s1)))
# print("Set size = {0:d}".format(len(s1)))
#----------------------------------------------------------------------

# Subset and Superset

#----------------------------------------------------------------------
# s1 = {1,2,4}
# s2 = {1,4,5,2,6}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))
#----------------------------------------------------------------------

# Testing for equality.  What happens when you run the code below?

#----------------------------------------------------------------------
# s1 = {1,2,4}
# s2 = {2,1,4}
# print(s1 == s2)
#----------------------------------------------------------------------

# Union of two sets - The union of two sets is a new set that contains all of
# the elements that are in at least one of the two sets.
#
# Intersection of two sets - The intersection of two sets is a new set that
# contains all of the elements that are in both sets.
#
# Difference of two sets: is an new set that consists of the elements of one set
# which are not elements of the other.
#
# What happens when you run the code below?

#----------------------------------------------------------------------
# s1 = {1,2,4}
# s2 = {1,3,5}
# 
# print("s1 = ",s1)
# print("s2 = ",s2)
# print("\ns1 union s2")
# print(s1.union(s2))
# print(s1 | s2)
# print("\ns1 intersect s2")
# print(s1.intersection(s2))
# print(s1 & s2)
# print("\ns1 difference s2")
# print(s1.difference(s2))
# print(s1 - s2)
#----------------------------------------------------------------------

# What about accessing individual items in a list?  What does this code do?

# s1 = {1,3,4}
# print(s1[0])

# What if we want to remove a specific item from a set?  Can we test for
# membership, then use "remove()"?

#----------------------------------------------------------------------
# s1 = {1,3,5,7,9}
# print("Here's your set: ",s1)
# n = int(input("Enter value to remove: "))
# if n in s1:
#    s1.remove(n)
#    print("New set: ",s1)
# else:
#    print("{0:d} Not found in set".format(n))
#----------------------------------------------------------------------


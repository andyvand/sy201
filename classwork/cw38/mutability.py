# Several examples that demonstrate the difference between mutable and immutable
# data types when using functions.
# 
# How about ints?
#
# def multiplySquares(x,y):
#    x = x**2
#    y = y**2
#    return x * y
# 
# a = 5
# b = 6
# print(a,b)
# result = multiplySquares(a,b)
# print(a,b,result)
#
# -----------------------------------------------------------------
#
# How about lists?
#
# def multiplySquares(nums):
#    nums[0] = nums[0]**2
#    nums[1] = nums[1]**2
#    return nums[0] * nums[1]
# 
# L = [5,6]
# print(L)
# result = multiplySquares(L)
# print(L,result)
#
# -----------------------------------------------------------------
#
# How about dictionaries?
#
# def multiplySquares(D):
#    D['first'] = D['first']**2
#    D['second'] = D['second']**2
#    return D['first'] * D['second']
# 
# numDictionary = {}
# numDictionary['first'] = 5
# numDictionary['second'] = 6
# print(numDictionary)
# result = multiplySquares(numDictionary)
# print(numDictionary,result)
#
# -----------------------------------------------------------------
#
# How about strings?
#
# def camelString(s1):
#    s2 = s1
#    s1 = ""
#    i = 0
# 
#    while i < len(s2):
#       if i % 2 == 0:
#          s1 += s2[i].lower()
#       else:
#          s1 += s2[i].upper()
#       i += 1
# 
#    return s1
# 
# s = "welcometocyberoperations"
# print(s)
# result = camelString(s)
# print(s,result)

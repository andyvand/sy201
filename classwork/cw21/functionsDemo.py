# # Basic function, no parameters
# 
# def my_function():
#   print("Hello from a function")
# 
# my_function()
# 
# --------------------------------------------------
# 
# # Basic function, with a parameter
# 
# def my_function(fname):
#   print(fname + " Navy")
# 
# my_function("Peter")
# my_function("Joseph")
# my_function("Linda")
# 
# --------------------------------------------------
# 
# # Basic Function, with a default parameter
# 
# def my_function(country = "Norway"):
#   print(country + " is a nation in the world.")
# 
# my_function("Qatar")
# my_function("India")
# my_function()
# my_function("Singapore")
# 
# --------------------------------------------------

# Basic Function, with two parameters, one default (note, default parameters
# need to come at the end of the parameter listing).  Can I switch number and
# color in the parameter list?
# 
# def my_function(number, color = "red"):
#   print("{0:d} {1:s} {0:d}".format(number,color))
# 
# my_function(1,"blue")
# my_function(2,"yellow")
# my_function(3)
# my_function(4,"green")
# 
# --------------------------------------------------
# 
# # Functions can return values.
# 
# def timesFive(x):
#   return 5 * x
# 
# print(timesFive(3))
# print(timesFive(5))
# print(timesFive(9))
# 
# --------------------------------------------------
# 
# # What does this program do?  What happens if I try to make n1 a default
# # parameter by setting it to 0? i.e. change the top of the function to read:
# # def sumNumbers(n1=0,n2)
# 
# def sumNumbers(n1,n2):
#     sum = 0
#     for i in range(n1,n2+1):
#         sum += i
#     return sum
# 
# def main():
# 
#    num1 = int(input("Enter num1: "))
#    num2 = int(input("Enter num2: "))
#    num3 = sumNumbers(num1,num2)
#    print("The sum from {0:,d} to {1:,d} is: {2:,d}".format(num1,num2,num3))
# 
# main()
#
# --------------------------------------------------

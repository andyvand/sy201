#!/usr/bin/env python3

# Author: Peter Nardi
# Date: 08/02/18
# 
# Purpose:  Demonstration of basic exception handling using using try-except in
# Python.
#
# Run the code multiple times.  What happens if you enter the letter "P" for
# num1?  What happens if you enter 5 for num1 and 3.14 for num2?  What happens
# if you enter 3 for num1 and 5 for num2?  Try all of these cases.

# Import the sys library to make use of "sys.exit()"
import sys

# Define our main() function
def main():

    try:
        num1 = int(input("Enter integer 1: "))
        num2 = int(input("Enter integer 2: "))
    except:
        print("One of your numbers was not a valid integer")
        sys.exit(1)

    # Note: If the exception is thrown (an error is encountered) we never get to
    # the print statement below, because the program exits with an error code of
    # 1.
    print("The sum of the two integers is: ",num1 + num2)

# Call Main
main()

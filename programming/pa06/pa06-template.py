# Description:
# 
# This is a template file for coding the ATM program.  It is not "the answer",
# but rather a commented guide that will walk you through the steps of creating
# a working ATM program.

# Imports

import hashlib
# Also import any custom tool libraries that you wrote.

# Globals

ACCTFILE = "acctfile.dat"
FROZENACCT = -1

# Functions

# ------------------------------------------------

# This is intended to be a very short function that returns a Boolean value
# (either True or False).  It takes the given pin and hashes it using md5.  It
# then looks in the hashedPINsList at the given index to see if what's there
# matches the hash you just computed.  If so, this function returns true.  If
# not, this function returns false.

def isCorrectPIN(pin,index,hashedPINsList):

   hashedPin = # Compute the md5 hash of pin
   
   # If hashedPin equals the hash stored in hashedPINsList at location index,
   # then return True, otherwise, return False.
   
   if ...:
   
# ------------------------------------------------

# This function prints your program's welcome banner and asks for the account
# number and PIN.  It will return an integer that represents the index in the
# acctNumsList where the selected account number resides.  This integer will
# then be used throughout your program as you process data in your lists.

def userLogin(acctNumsList,hashedPINsList,frozenList):
   
   print("*** Welcome Cyber Citizens National Bank ***\n")
   
   while True:
      
      # 1. Read an account number from the User
      # 2. Check to see if the account number is in acctNumsList.  If it is,
      # then break out of the loop.  If not, then print a warning that the
      # account number was not found and ask the User to try again.
      
      acctNum = input("Account number: ")
      ...
   
   # Now we're outside the loop above and have a valid account number.  We need
   # to determine the index (location) of acctNum in acctNumsList.
   
   index = # Location of acctNum in acctNumsList
   
   # Using index (from above), look in the frozenList and determine if the
   # account is frozen.  If it is, frozenList[index] will be set to "0".  If the
   # account is frozen, then print a notification to the User and return -1.
   # Note: We set a global variable called FROZENACCT to -1 at the top of our
   # program, so return FROZENACCT instead of the literal -1.
   
   if ...:
      ...

   # If we get to this point, that means the acctNum is valid and the account is
   # not frozen.  Excellent!  Now we need to give the User three tries to
   # authenticate with his / her pin.

   pinTries = 1
   while pinTries <= 3:
      
      # Ask the User for a PIN.  using your isCorrectPIN function, check to see
      # if the User entered the correct pin.  If not, print a notification
      # message to the User and ask them to try again.  Also add 1 to the number
      # of pinTries.  If they did enter a correct PIN, break out of this loop.
   
      pin = input("PIN: ")
      ...
   
   # Now we're outside the loop above, if pinTries > 3, that means we exited the
   # loop above because we failed the pin entry more than 3 times.  In this
   # case, we need to freeze the account (set the frozenList entry at position
   # index to "0"), print a warning to the User and return -1 (FROZENACCT)

   if pinTries > 3:
      ...

   # If we get to this point, it means: (1) We have a valid account number, (2)
   # The account is not frozen, and (3) The User entered a correct pin in less
   # than or equal to 3 tries.  In this case, return index.
   
   return index
      
# ------------------------------------------------

# This function takes an index and a list of hashed PINs and does not return a
# value.  It prompts the User to enter a new PIN and updates the hashedPINsList
# at position index with the md5 hash of the new PIN.

def changePIN(index,hashedPINsList):
   
   # Get a new pin from the User.
   
   newPIN = input("\nEnter new PIN: ")

   # If the length of newPIN is equal to 4 and all the characters in newPIN are
   # numeric, then it's in the correct format.
   
   if ...:
      
      newPIN2 = # Ask the User to confirm the pin they just entered
      
      # If newPIN equals newPIN2, then update hashedPINsList at position index
      # with the md5 hash of newPIN.  Also print a message to the User
      # indicating that the pin has been updated.
      
      if ...:
         ...
         
      # If newPIN does not match newPIN2, then warn the User that the pins don't
      # match.  Make no changes to hashedPINsList.
      
      else:
         ...

   # The "else" below goes with the "if" at the top of our function.  If we get
   # here, it means the new pin the User selected is not in the correct format
   # (either it's longer than 4 characters or there are non-numeric characters
   # in it.) In this case, print a warning to the User that the pin is not in
   # the correct format.  Make no changes to hashedPINsList

   else:
      ...

# ------------------------------------------------

# This function takes seven parameters and does not have a return value.  It
# takes an open file handle (f) and gets the item located at position index in
# each of the provided lists.  It then creates a string that complies with the
# file format specification given in paragraph (2) and writes that string to the
# file using f.  

def writeLineToFile(f,index,acctNumsList,hashedPINsList,
   balanceList,frozenList,nameList):
   
   # Start with an empty string.
   result = ""   
   # Concatenate what's in acctNumsList at position index to result
   result += 
   # Concatenate a colon (':') to result
   result += 
   # Concatenate what's in balanceList at position index to result.  Note, since
   # balanceList contains floats, you'll need to cast it to a string before you
   # Concatenate.
   result += 
   # Concatenate a colon (':') to result
   result += 
   # Concatenate what's in frozenList at position index to result
   result +=
   # Concatenate a colon (':') to result
   result += 
   # Concatenate what's in nameList at position index to result
   result +=
   # Concatenate a newline ('\n') to result
   result += 
   # Write the line (result) to the file.
   f.write(result)
   
   # Note: You can reduce the number of lines in this function by concatenating
   # the colons as you build each item, but it's not necessary

# ------------------------------------------------

# Here's a function I wrote to display my menu.  You don't have to use this if
# you wrote your own.

def displayMenu():
   
   print("\n1. Withdraw funds")
   print("2. Deposit funds")
   print("3. Balance inquiry")
   print("4. Change PIN")
   print("5. Quit\n")

# ------------------------------------------------

def main():
   
   # Open file; initialize data structures; close file
   
   # Open the account data file for reading.  Use the global variable we defined
   # at the top of the program.
   
   fin = ...

   # initialize our lists
   
   acctNumsList = []
   hashedPINsList = []
   balanceList = []
   frozenList = []
   nameList = []
   
   # Read the lines in the file, split each one on the colon character (:), and
   # append each field of each line to its associated list.  Note, you'll end up
   # with a newline character at the end of each line in the file, so think
   # about how you need to handle that.  Also, all the data in the file will be
   # stored as strings.  All the data in your lists should be stored as strings,
   # *except* balances, which should be stored as floats.  You should cast
   # balances to float before you put them in balanceList.
   
   # Write the code to read the lines from the file and load the lists here.
         
   # Close the file when we're done.
   
   fin.close()
   
   # Authenticate a User to our ATM
   
   selection = 0
   atmUser = userLogin(acctNumsList,hashedPINsList,balanceList,
      frozenList,nameList)  
   
   # Run the simulation
   
   while selection != 5 and atmUser != FROZENACCT:
      
      # Display the menu
      
      displayMenu()
      
      # Get a menu selection from the User.
   
      selection = # Use the getInt function you wrote
      
      # Withdraw Cash
      if selection == 1:
         
         # Ask the User for an an amount to withdraw.  I recommend using the
         # getInt function you wrote to do this.  Make sure the User cannot
         # withdraw a negative amount of cash.
         
         withdrawal = # Get amount to withdraw
         
         # If withdrawal is not evenly divisible by 10, then we cannot service
         # the withdrawal using $10 and $20 dollar bills.  Report this to the
         # User.

         if withdrawal ...:
            ...
            
         # If the withdrawal amount is okay, then determine how many $10 and $20
         # dollar bills to dispense.  Display those results to the User using
         # formatted output.  For example, if the machine is dispensing 1231 $20
         # dollar bills, display that as: "$20 bills: 1,231" (with the thousands
         # separator). Once you display the result, update the balanceList at
         # position atmUser to remove the funds from the User's account.

         else:
            ...
      
      # Deposit cash
      elif selection == 2:
         
         # Ask the User for an amount to deposit.  I recommend using a getFloat
         # function that you need to write to do this.  Make sure the User
         # cannot deposit a negative amount of cash.

         deposit = # Get amount to deposit
         
         # Once you get the deposit amount, update the balanceList at position
         # atmUser to add the funds to the User's account. The variable
         # "atmUser" is what we used to authenticate to our ATM.

         ...
         
      # Balance inquiry
      elif selection == 3:
         
         # Print the account holder's name, account number and balance by
         # accessing the data in nameList, acctNumsList and balanceList at
         # position atmUser.  Make sure to use formatted output when printing
         # the balance.
         
         ...
         
      # Change PIN
      elif selection == 4:
         
         # Call your changePIN function and pass it atmUser and hashedPINsList
         
         ...
      
   # ------------------------ Simulation end --------------------------------
   
   # At this point, the User selected "5" (Quit) or the account was frozen when
   # we tried to open it.  Now open the account file for writing, write data
   # back to file, and close the file.

   fout = ...
   for i in range(len(acctNumsList)):
      # Call your writeLineToFile function and pass it: fout, i,
      # acctNumsList,hashedPINsList, balanceList, frozenList, nameList

   fout.close()

# ------------------------------------------------
      
# Call the Main Program
   
main()

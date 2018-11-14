# Notice the format for importing our Country class from the "classes.py" file,
# located in the "utils" directory.
from utils.classes import Country

def main():
   
   # Start with an empty dictionary and open the file.
   D = {}
   fin = open("populationData.csv","r")
   
   # Write the code to read all the lines in the file.  Call your Country class
   # initializer for each line you read, and add the object returned by the
   # initializer to your dictionary.  When complete, your dictionary will
   # contain all the country data.

   # Your code goes here....
   
   # Write a loop.  Inside the loop, ask the user for a letter.  Since your
   # country search needs to be case in-sensitive, cast the letter from the user
   # to uppercase. When searching through your dictionary, compare the uppercase
   # version of the first letter of each country to the uppercase letter entered
   # by the user.  If they match, print that country's name, along with its
   # data.
   while True:
      letter = input("Enter a letter: ")
      
      # What if the user pressed enter with no input (blank line)?
      if ....
         # Do something if blank line...
      else:
         # Got a valid letter, so lookup country data.

         # Here's how iterate across a sorted list of dictionary keys
         for key in sorted(D.keys()):
            
            # Your code goes here....
               
# Call the main() function.
main()

# This program will parse the /etc/passwd file and extract the User Name and
# Full Name for every entry.  It will then display those items using formatted
# output.  Some Full Name entries may be empty (blank), and you'll see that in
# the results.
#
# There is an executable version of this program in the repo called
# "etcPasswdScanner"  To run it:
# 
# 1. Copy it from the repo to a location of your choosing.
# 2. Set up its permissions by entering: "chmod 755 etcPasswdScanner".
# 3. Run the program using the "./" prefix, like this: "./etcPasswdScanner"

# This is the file we want to work on.
FILE = "/etc/passwd"
f = open(FILE,"r")

# Read a line from the file.
# >> Your line of code here <<

# Keep looping, as long as the line is not empty (meaning you haven't reached
# the end of the file yet)
# >> Your line of code here <<

   # Initialize a variable with the left-most index that you want to examine
   # (starts at 0)
   # >> Your line of code here <<

   # Calculate the "right" index by using "find" to search the line you read for
   # the first colon (:)
   # >> Your line of code here <<

   # Extract the first entry (User Name) by using sub-string notation on the
   # line to get the characters between "left" to "right"
   # >> Your line of code here <<

   # Set "left" equal to "right" + 1
   # >> Your line of code here <<

   # Starting at the new "left", calculate a new "right" index by using "find"
   # to search the line you read for the second colon (:).
   # >> Your line of code here <<

   # Set "left" equal to "right" + 1
   # >> Your line of code here <<

   # Starting at the new "left", calculate a new "right" index by using "find"
   # to search the line you read for the third colon (:).
   # >> Your line of code here <<

   # Set "left" equal to "right" + 1
   # >> Your line of code here <<

   # Starting at the new "left", calculate a new "right" index by using "find"
   # to search the line you read for the fourth colon (:).
   # >> Your line of code here <<

   # Set "left" equal to "right" + 1
   # >> Your line of code here <<

   # Starting at the new "left", calculate a new "right" index by using "find"
   # to search the line you read for the fifth colon (:). The Full Name entry
   # sits between the fourth and fifth colons.
   # >> Your line of code here <<

   # Extract the next entry (Full Name) by using sub-string notation on the
   # line to get the characters between "left" and "right"
   # >> Your line of code here <<

   # Strip any trailing commas off the Full Name entry you extracted
   # >> Your line of code here <<

   # Using formatted printing, print the User Name, followed by the Full Name,
   # each lined up on separate columns. Run the executable version of the
   # program to see what that looks like.
   # >> Your line of code here <<

   # Read the next line
   # >> Your line of code here <<
   
f.close()

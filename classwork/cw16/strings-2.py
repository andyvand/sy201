# Revisiting iteration -- Fast iteration:

s = "Welcome"
for c in s:
    print(c)

# Misc string functions:

s = "ABC123"

print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.isspace())

# Notice the syntax for use.  We say: "isalpha()" is a method that operates
# on a member of the "string class".  Code like this is perfectly legal:

print("Welcome".isupper())

# Searching for substrings:

# Prints the index where "Navy" starts.
# Returns -1 if it can't find the substring in s.

s = "Go Navy"

print(s.endswith("Navy"))
print(s.startswith("Go"))
print(s.find("World"))

# Returns the number of non-overlapping occurrences of "Go" in s.

s = "Go Good Midshipmen, Go!"
print(s.count("Go"))

# Converting strings:

s = "hello world!"

print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())

print(s.swapcase())
print(s.replace("l","z"))

# Stripping whitespace characters from a string:

s1 = "   This is a string!   "
s2 = "This is another  "

s3 = s1.lstrip() + s2  # Strips leading spaces.
print(s3)

s3 = s1.rstrip() + s2 # Strings trailing spaces.
print(s3)

s3 = s1.strip() + s2 # Strings all leading and trailing spaces.
print(s3)

# Formatting strings

s1 = "Go Navy"
s2 = "Beat Army"

s3 = s1.center(20)
print(s3 + s2)

s3 = s1.ljust(20)
print(s3 + s2)

s3 = s1.rjust(20)
print(s3 + s2)

n = 123456789
s = "{0:,d}".format(n).rjust(30)
print(s)

#----------------------------------------------------------------------------------------------------------------
# String Manipulation
#----------------------------------------------------------------------------------------------------------------
# String manipulation refers to the process of modifying or transforming strings to produce new strings that meet specific requirements.
# Python offers a variety of built in functions to manipulate strings
# Strings are a list of characters where the first character in a string has an index of 0.

myString = "Hello World!"

# Character Index and Ranges
print(myString[0]) # -> H
print(myString[1]) # -> E
print(myString[0:5]) # -> Hello | 0 is inclusive, 5 is exclusive
print(myString[-1]) # -> ! | -1 is the last character in the string
print(myString[:5]) # -> Hello | Start at the beginning of the string and go to index 5 (exclusive)
print(myString[6:]) # -> World! | Start at index 6 (inclusive) and go to the end of the string

# In and Not In
myBool = "Hello" in "Hello World" # -> True
myBool = "hello" in "Hello World" # -> False
myBool = "Hello" not in "Hello World" # -> False

# Modification
print(myString.upper()) # -> HELLO WORLD!
print(myString.lower()) # -> hello world!

# Checking a string for condition
print(myString.isupper()) # -> False (prints True if all characters are uppercase)
print(myString.islower()) # -> False (prints True if all characters are lowercase)
print(myString.isalpha()) # -> False (prints True if string is all letters, and no blanks)
print(myString.isalnum()) # -> False (prints True if string is all letters, and or numbers, and no blanks)
print(myString.isdecimal()) # -> False (prints True if string is all numeric characters and no blanks)
print(myString.istitle()) # -> True (prints True if every word in the string has an uppercase first letter)
print(myString.startswith("Hello")) # -> True (prints True if string starts with argument)
print(myString.endswith("World!")) # -> True (prints True if string ends with argument)

# Split a string into a list of strings
print(myString.split(" ")) # -> ['Hello', 'World!']
print(len(myString.split(" "))) # -> 2

# Position a string in a specific position within the document
print(myString.rjust(10)) # -> prints the string and justifies it to the right
print(myString.ljust(10)) # -> prints the string and justifies it to the left
print(myString.center(10)) # -> prints the string and justifies it to the center

print(myString.strip()) # -> Hello World!
# strip() removes all leading and trailing whitespace characters

print(myString.find("Hello")) # -> 0
# returns the index of the argument if found, while searching the string from left to right

print(myString.find("hello")) # -> -1
# returns -1 if argument is not found

print(myString.replace("Hello", "Goodbye")) # -> Goodbye World!
# replaces a substring inside a string with a new string

print(myString.count("Hello")) # -> 1
# returns the amount of times a substring is used in a string

myList = myString.split(" ") # -> ['Hello', 'World!']
print(", ".join(myList)) # -> Hello, World!
# join joins a list into a string and concatenates the ", " between each index of the list
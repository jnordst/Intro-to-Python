#-------------------------------------------------------------------------------------------
# Strings
#-------------------------------------------------------------------------------------------
# Strings are a data type used to represent a sequence of characters. 
# Strings are a built-in data type in Python and are represented by enclosing the characters within single quotes, double quotes, or triple quotes. 
# Strings can contain letters, numbers, symbols, and whitespace characters. 
# Strings are immutable, meaning once they are created, their contents cannot be changed. 
# However, you can create a new string by concatenating or slicing parts of an existing string. 
# Python provides many built-in functions and methods for working with strings, including formatting, searching, and manipulating.

myString = "Hello!" # double quotes
myString = 'Goodbye!' # single quotes
myString = 'Jacob\'s Optical' # \ is an escape character, it can be used to "escape" certain characters like single quotes that would break a string

#----------------------------------------------------
# String Concatenation
#----------------------------------------------------
# String concatenation is the process of combining two or more strings into a single string. 
# This can be done using the + operator. 
# When you concatenate two strings, the resulting string is the original strings joined together in the order they were specified. 
# For example, the expression "Hello" + " " + "World" will result in the string "Hello World". 
# You can also concatenate strings and other data types, such as integers or floats, by first converting them to strings using the str() function. 
# String concatenation is a common operation in Python programming, especially when working with text or user input.

# String Concatenation with +
myString = "My name is " + "Jacob" + ", and my age is " + "28" # -> My name is Jacob, and my age is 28

# String Concatenation with comma
myString = "My name is ", "Jacob", ", and my age is ", "28" # -> My name is Jacob, and my age is 28

# String Concatenation with Variables
myName = "Jacob"
myAge = 28
myString = "My name is " + myName + ", and my age is " + str(myAge) # -> My name is Jacob, and my age is 28

#----------------------------------------------------
# f-Strings (String Interpolation)
#----------------------------------------------------
# f-strings (or formatted string literals) provide a convenient way to embed expressions inside string literals
# f-strings start with the letter 'f' before the opening quote and can contain expressions enclosed in curly braces {}. 
# The expressions inside the curly braces are evaluated at runtime and their values are inserted into the resulting string. 
# For example, f"Hello, my name is {name} and I am {age} years old." will replace the variables name and age with their actual values when the string is created. 
# f-strings can also contain formatting options, such as specifying the number of decimal places for a float, using the same syntax as the older string formatting methods. 
# f-strings make it easier and more concise to create formatted strings in Python, especially when combining strings with variables or expressions.

myString = f"My name is {myName}, and my age is {myAge}" # -> My name is Jacob, and my age is 28
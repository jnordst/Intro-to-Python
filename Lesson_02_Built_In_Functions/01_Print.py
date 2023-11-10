#-------------------------------------------------------------------------------------------
# The Print Function
#-------------------------------------------------------------------------------------------
# The print() function is used to display output on the screen or to a file. 
# The print() function takes one or more expressions as arguments and prints their values, separated by a space by default, to the console or to a specified file. 
# For example, print("Hello, World!") will print the string "Hello, World!" to the console. 
# The print() function can also take multiple arguments, which are printed in order, separated by a space. 
# You can also specify the separator and end characters to be used between the values, using the sep and end parameters respectively. 
# The print() function can be used to display variables, literals, and expressions of any data type, including strings, integers, floats, booleans, lists, dictionaries, and even functions. 
# The print() function is a fundamental tool for debugging and displaying information in Python programming.

print("Hello World!") # -> Hello World

# Argument is automatically cast as a String
print(42) # -> 42

#-------------------------
# end Parameter
#-------------------------
# This parameter specifies the string to append at the end of the printed values. 
# By default, it is a newline character. 
# You can specify any string value as the end character.

print("Hello", end = " ") # -> Hello 
print("World", end = "!") # -> Hello World!

#-------------------------
# sep Parameter
#-------------------------
# This parameter specifies the separator character to use between the values to be printed. 
# By default, it is a space character. 
# You can specify any string value as the separator.

print("Hello", "World", sep="-") # -> Hello-World
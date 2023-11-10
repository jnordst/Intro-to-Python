#-------------------------------------------------------------------------------------------
# Casting
#-------------------------------------------------------------------------------------------
# Cast functions are used to convert variables of one data type to another data type. 
# There are several built-in cast functions available in Python.

# Convert a string to an integer
myString = "123"
myInt = int(myString) # 123

# Convert an integer to a float
myInt = 123
myFloat = float(myInt) # 123.0

# Convert a float to a string
myFloat = 3.14
myString = str(myFloat) # "3.14"

# Convert a non-zero value to True
myInt = 123
myBool = bool(myInt) # True

# Convert a zero value to False
myInt = 0
myBool = bool(myInt) # False
#-------------------------------------------------------------------------------------------
# Conditional Operators
#-------------------------------------------------------------------------------------------
# Conditional statements are composed of conditional operators, which are used to compare values and return a boolean value (True or False).
# If an operand operator operand evaluates to True, the entire expression evaluates to True
# We use this to control the flow of execution in a program based on certain conditions

# Equal to
myBool = 5 == 5 # True
myBool = 5 is 5 # True

# Not Equal to
myBool = 5 != 5 # False
myBool = 5 is not 5 # False

# Not
# Not converts a boolean value to its opposite
myBool = True # True
myBool = not True # False

# Greater than
myBool = 5 > 5 # False

# Greater than or equal to
myBool = 5 >= 5 # True

# Less than
myBool = 5 < 5 # False

# Less than or equal to
myBool = 5 <= 5 # True

# And
# And returns True if both operands are True
myBool = True and True # True
myBool = 5 > 5 and 5 < 5 # False

# Or
# Or returns True if either operand is True
myBool = True or False # True
myBool = 5 >= 5 or 10 < 5 # True
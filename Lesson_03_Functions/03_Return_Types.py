#-------------------------------------------------------------------------------------------
# Return Types
#-------------------------------------------------------------------------------------------
# the return statement is used to specify the value that a function should return when it is called. 
# When a return statement is executed, the function is immediately terminated, and the specified value is returned to the calling code.
# The return statement can be used to return a value of any data type in Python, and even other functions.
# If no return type is specified, the function will return None.

# Because this function does not have a return statement, it will return None by default
def myFunction():
    print("Hello World!")

# If you print a function that does not have a return statement, it will execute the function and then print None
print(myFunction()) 
# -> Hello World!
# -> None

# Here's an example of a simple function that adds two numbers and returns the sum
def add_numbers(a=int, b=int) -> int: # can predefine that the function should return an integer
    """
    Adds This function calculates the sum of a and b and returns the result

    Args:
        a: int
        b: int

    Returns:
        int: the sum of a and b
    """ # this is called a function 
    sum = a + b
    return sum

# Returning in Practice
print(add_numbers(10, 9)) # add_numbers will return the value 19 which will then be printed

# Setting the Value of a Variable as a Function
funcVariable = add_numbers(10, 9) # same as writing funcVariable = 19
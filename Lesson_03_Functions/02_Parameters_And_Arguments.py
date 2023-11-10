#-------------------------------------------------------------------------------------------
# Parameters and Arguments
#-------------------------------------------------------------------------------------------
# In Python, a function can take one or more parameters, which are placeholders for values that will be passed to the function when it is called. 
# An argument, on the other hand, is a value that is passed to the function when it is called. 
# In other words, an argument is a specific value that is used to replace a parameter in a function call.

# Using a Parameter
def parametersOne(parameter):
    pass

# Using Multiple Parameters
def parametersTwo(parameterOne, parameterTwo, parameterThree):
    pass

# Predefine the Data Type of the Parameters
def parametersThree(parameter=int):
    # By predefining the data type of the parameter, we can ensure that the function only accepts arguments of that data type
    # This is also useful for documentation purposes
    # As a developer you can recognize that parameter is expected to be an integer
    pass

# Calling a Function with Arguments
parametersTwo(1, "Hello", 3.12) # objects inside the paranthesis are called Arguments, when the function is called
parametersThree(3) # since we predefined the parameters for this function it expects an integer argument
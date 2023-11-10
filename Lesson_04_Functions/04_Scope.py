#-------------------------------------------------------------------------------------------
# Global vs Local Scope
#-------------------------------------------------------------------------------------------
# Variables can have either global or local scope. 
# The scope of a variable determines where it can be accessed and modified within a program.
# A global variable is defined outside of any functions, and can be accessed from anywhere within a program. 
# It can also be modified from anywhere within the program.
# A local variable, on the other hand, is defined within a function, and can only be accessed and modified within that function.
# Even if a Local Variable shares the same name as the Global Variable, the global variable is not altered unless the "global" keyword is used.

# Creating a Global Variable
myString = "Hello"

# Creating a Local Variable
def localFunction():
    myString = "Hello World"
    print(myString)

localFunction() # -> Hello World

# Changing a Global Variable
def changeGlobalVariable():
    # The "global" keywords signifies that we want to modify the global variable "myString"
    global myString

    # Changing the Global Variable
    myString = "Hello World"

print(myString) # -> Hello
changeGlobalVariable()
print(myString) # -> Hello World
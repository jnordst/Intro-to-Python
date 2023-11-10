#-------------------------------------------------------------------------------------------
# Match Statements
#-------------------------------------------------------------------------------------------
# In other programming languages you may have learned about Switch Statements
# In Python the closest thing to a Switch Statement is a Match Statement
# The Match Statement is a new feature in Python 3.10
# It allows you to compare a value against a series of patterns and execute code based on which pattern matches
# The ``match`` keyword is followed by an expression, usually a variable name
# The expression is then compared against a series of patterns using the ``case`` keyword
# If the expression matches a pattern, the code below the pattern is executed
# An advantage of using Match Statements in python is there is no need to use the ``break`` keyword
# Match Statements also have a ``case _`` keyword which is used as a default case

# Example
# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

language = input("What's the programming language you want to learn? ")

match language:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")

    # Default case if no other case matches    
    case _:
        print("The language doesn't matter, what matters is solving problems.")
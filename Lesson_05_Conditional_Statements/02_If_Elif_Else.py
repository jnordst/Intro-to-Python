#-------------------------------------------------------------------------------------------
# Conditional Statements
#-------------------------------------------------------------------------------------------
# Conditional statements are used to control the flow of execution in a program based on certain conditions. 
# Consists of the if keyword, followed by a condition to be evaluated, and a block of code to be executed if the condition is true. 
# Optionally, the if statement can be followed by any number of elif statements (short for "else if").
# Finally, the if statement can be followed by an optional else statement, which is executed if none of the previous conditions are true.
# Similarly to functions, if statements must be tabbed over and followed by a colon.
# In python the brackets are not required, but the indentation is required.

weight = 190.4

if weight == 195:
    print("Weight is 195")
elif weight < 195:
    print("Weight is less than 195")
elif weight > 195: 
    print("Weight is greater than 195")
elif not weight > 0:
    print("Weight is not greater than 0")
else:
    print("Error")

# -> Weight is less than 195
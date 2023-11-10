#-------------------------------------------------------------------------------------------
# Loops
#-------------------------------------------------------------------------------------------
# In Python, loops are used to repeatedly execute a block of code. 
# There are two main types of loops: for loops and while loops.
# Both types of loops can be used to solve a variety of problems, 
#   such as iterating over a list to perform some calculation, or repeatedly prompting a user for input until a valid response is received. 
# Loops are an important concept in programming, as they allow you to automate repetitive tasks and process large amounts of data efficiently.

#----------------------------------------------------
# While Loops
#----------------------------------------------------
# A while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# It's important to be careful when using while loops, since it's possible for a while loop to run indefinitely if the condition is never false. 
# This is called an infinite loop and can cause your program to become unresponsive or crash. 
# To avoid this, it's a good idea to make sure that the condition in a while loop will eventually become false. 

# In this example, the loop body is executed as long as the value of i is less than 5. 
# Inside the loop body, the value of i is incremented by 1 using the += operator.
# This eventually causes the loop to terminate when the value of i becomes 5.
x = 5
while (x < 10):
    print(x)
    x += 1 # short from of adding 1 to x
# -> 5 6 7 8 9

# Let's break down the exact process of what happened in the above example:
# WHILE x is LESS THAN 10 we execute the code inside the body of the loop
# Inside the loop we first print the value of x, then increment x by 1
# This process continues until the value of x becomes 10 then the loop terminates

# Iteration 1:
# x = 5
# x < 10 ? True -> Run the code inside the loop
# print(x) -> 5
# x += 1 -> x = 6

# Iteration 2:
# x = 6
# x < 10 ? True -> Run the code inside the loop
# print(x) -> 6
# x += 1 -> x = 7

# Iteration 5:
# x = 9
# x < 10 ? True -> Run the code inside the loop
# print(x) -> 9
# x += 1 -> x = 10

# Iteration 6:
# x = 10
# x < 10 ? False -> Exit the loop
# The code inside the loop is no longer executed

# Therefore the output of the loop is:
# 5 6 7 8 9

# Notice we do not print 10, because the loop after x becomes 10 the loop is terminated.
# It is important to remember that the condition is checked before the code inside the loop is executed.


# Using Booleans to Control Loops

loop = True

while loop:
    print("Looping...")
    loop = False
# -> Looping...

# In this example, the loop variable is set to True before the loop begins.
# Inside the loop body, the value of loop is set to False, which causes the loop to terminate.
# Our example is very simple but you can create more complex conditions to toggle out of your loop.
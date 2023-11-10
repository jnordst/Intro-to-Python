#-------------------------------------------------------------------------------------------
# For Loops
#-------------------------------------------------------------------------------------------
# A for loop is used to iterate over a sequence (such as a list or a string) and execute a block of code for each item in the sequence. 

# Iterate over a list
days = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']
for day in days:
    print(day) 
# -> mon tues wed thur fri sat sun

# Iterate over a range
# range() is a built-in function that returns a sequence of numbers.
# It can be used to generate a sequence of numbers for use in a for loop.
# The range() function takes three arguments: start, stop, and step.
# The start argument specifies the starting value of the sequence.
# The stop argument specifies the stopping value of the sequence.
    # Note: The stop argument is not included in the sequence.
    # For example, range(1, 5) will return the sequence 1, 2, 3, 4.
# The step argument specifies the increment (or decrement) of the sequence.

# Iterate from 0 to 4
for i in range(5): # starts at 0, stops at 5
    # i is initialized to 0 and incremented by 1 each iteration since we did not specify a start or step value
    print(i)
# -> 0, 1, 2, 3, 4

# Iterate from 5 to 9
for i in range(5, 10): # starts at 5, stops at 10
    print(i)
# -> 5, 6, 7, 8, 9

# Iterate from 1 to 9 with an incremental step of 2
for i in range(start=1, stop=10, step=2):
    print(i)
# -> 1, 3, 5, 7, 9
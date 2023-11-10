#-------------------------------------------------------------------------------------------
# Continue and Break
#-------------------------------------------------------------------------------------------
# "continue" and "break" are keywords that can be used in loops to alter the control flow of the program.
# The continue keyword causes the current iteration of the loop to be skipped and the loop to immediately move on to the next iteration. 
# It skips the remaining statements in the loop body for the current iteration and moves to the next iteration. 
# This can be useful if you want to skip over certain values or conditions in the loop.
# The break keyword causes the loop to immediately exit, regardless of whether or not all iterations have been completed. 
# It completely stops the loop and moves on to the next statement in the program.
# This can be useful if you want to terminate a loop prematurely based on a certain condition.

# Iterate from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue # skip even numbers
    if i == 7:
        break # exit loop when i equals 7
    print(i)
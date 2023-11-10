#-------------------------------------------------------------------------------------------
# Lists
#-------------------------------------------------------------------------------------------
# Lists are a data structure used to store a collection of items. 
# Lists are a built-in data type in Python and are represented by enclosing the items within square brackets and separating them with commas. 
# Lists can contain any type of data, including integers, floats, strings, booleans, and even other lists. 
# Lists are mutable, meaning their contents can be modified after they are created. 
# You can add, remove, or modify elements in a list using various methods provided by Python. 
# Lists are ordered, meaning their elements are stored in a specific sequence and can be accessed by their index. 
# Lists are also dynamic, meaning they can grow or shrink in size as needed.
# Lists are 0 based, meaning that the first element of a list is index 0

# Creating a new list
myList = [5, 13.2, "Hello", True]

#----------------------------------------------------
# List Functions
#----------------------------------------------------
myList = [5, 13.2, "Hello", True]

# Accessing the first element of a list
print(myList[0]) # -> 5

# Accessing the last element of a list
print(myList[-1]) # -> True

# Getting the length of a list
print(len(myList)) # -> 4

# Slicing a list to create a new list
newList = myList[1:3] # gets range from 1 to 2 as a list. 3 is not inclusive
print(newList) # -> [13.2, "Hello"]
newList = myList[:3] # gets range from 0 to 2 as a list. 3 is not inclusive
print(newList) # -> [5, 13.2, "Hello"]
newList = myList[1:] # gets range from 1 to last index as a list
print(newList) # -> [13.2, "Hello", True]

# Modifying elements in a list
newList[0] = 10 # changes the first element to 10

# Adding elements to a list
newList.append(6) # adds 6 to the end of the list
newList.insert(0, 0) # inserts 0 at the beginning of the list
print(newList) # -> [0, 10, "Hello", 6]

# Removing elements from a list
newList.pop() # removes and returns the last element
newList.remove(0) # removes the first occurrence of 0 from the list
index_zero = newList.pop(0) # removes element at index 0 and returns the value of index 0 then saved it to the variable index_zero
del newList[0] # removes the element at index 0
print(newList) # -> []
print(index_zero) # -> 10

# Sorting a list
sortedList = ["b", "a", "d", "e", "c"]
sortedList.sort() # sorts the list in ascending order
print(sortedList) # -> ['a', 'b', 'c', 'd', 'e']
# Unlike some languages, when you sort the list you are directly modifying the list, and do not need to create a new list
sortedList.reverse() # reverses the order of the list
print(sortedList) # -> ['e', 'd', 'c', 'b', 'a']

# Combining lists
bigList = sortedList + myList # concatenates the two lists   
print(bigList) # -> ['e', 'd', 'c', 'b', 'a', 5, 13.2, 'Hello', True]

# Checking if an element is in a list
if 5 in bigList:
    print("5 is in the list") # -> 5 is in the list
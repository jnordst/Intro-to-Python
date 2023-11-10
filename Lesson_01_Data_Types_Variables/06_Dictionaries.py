#-------------------------------------------------------------------------------------------
# Dictionaries
#-------------------------------------------------------------------------------------------
# Dictionaries are a built-in data type used to store a collection of key-value pairs. 
# Dictionaries are represented by enclosing the key-value pairs within curly braces and separating them with commas. 
# Each key-value pair is separated by a colon. 
# Dictionaries can contain any type of data as values, including integers, floats, strings, booleans, lists, and even other dictionaries. 
# Keys must be unique and immutable, meaning they cannot be changed once they are created. 
# Dictionaries are mutable, meaning their contents can be modified after they are created. 
# You can add, remove, or modify key-value pairs in a dictionary using various methods provided by Python. 
# Dictionaries are unordered, meaning their key-value pairs are not stored in a specific sequence and cannot be accessed by their index. 
# Instead, you can access the value of a specific key by using the key as a lookup.

# Creating a new dictionary
myDict = { # dictionaries are represented by curly braces
    "one": 1, # "one" is the key and 1 is the value
    "two": 2, # each key-value pair is separated by a comma
    "three": 3, 
    "four": 4
}

# Dictionary Functions
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values in a dictionary
print(person['name']) # -> 'John'
print(person.get('age')) # -> 30

# Modifying values in a dictionary
person['age'] = 31 # changes the value of 'age' to 31
person['city'] = 'San Francisco' # changes the value of 'city' to 'San Francisco'

# Adding new key-value pairs to a dictionary
person['occupation'] = 'Software Engineer' # adds a new key-value pair to the dictionary

# Removing key-value pairs from a dictionary
del person['city'] # removes the 'city' key-value pair from the dictionary
person.pop('occupation') # removes the 'occupation' key-value pair from the dictionary

# Looping through a dictionary
for key, value in person.items():
    print(key, value) 
# -> name John 
# -> age 31

# Checking if a key exists in a dictionary
if 'age' in person:
    print("age is a key in the dictionary")

# Getting the keys or values of a dictionary
keys = person.keys() # returns a list of the keys in the dictionary
values = person.values() # returns a list of the values in the dictionary
print(keys) # -> dict_keys(['name', 'age']) 
print(values) # -> dict_values(['John', 31])   

# Creating a dictionary using a loop with keys as numbers and values as their squares
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares) # -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Why are dictionaries more efficient than lists?
# Dictionaries are more efficient than lists because they use a hash table to store their key-value pairs.
# This allows them to look up values by key in constant time, while lists have to search through the entire list to find a value.
# This makes dictionaries much faster than lists for large data sets.

# Dictionaries are not ordered, so they cannot be accessed by index like lists can
# print(person[1]) # -> KeyError: 1
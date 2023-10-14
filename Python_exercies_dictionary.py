# The following code primarily demonstrates working with dictionaries, including creation, modification, and deletion of key-value pairs. 
#It also shows how to iterate through a dictionary's keys and values, as well as how to create a dictionary of lists with random integer values.


import random  # Import the random module.

var = {}  # Creates an empty dictionary named 'var' using curly braces.
print(type(var))  # Prints the type of the 'var' variable, which is 'dict' (dictionary).

var2 = {'juice': 'cranberry', 'movie': 'Top Gun', 'fruit': 'pineapple'}  # Creates a dictionary named 'var2' with key-value pairs.
print(var2)  # Prints the content of the 'var2' dictionary.

print(var2['juice'])  # Prints the value associated with the 'juice' key in the 'var2' dictionary.

var2['drank'] = 'Patron'  # Adds a new key-value pair to the 'var2' dictionary.
print(var2)  # Prints the updated 'var2' dictionary.

var2['movie'] = 'LOTR'  # Modifies the value associated with the 'movie' key.
print(var2)  # Prints the updated 'var2' dictionary.

del var2['drank']  # Deletes the 'drank' key and its associated value from the 'var2' dictionary.
print(var2)  # Prints the updated 'var2' dictionary.

print(list(var2.keys()))  # Converts the keys of the 'var2' dictionary into a list and prints the list of keys.

# Iterates through the keys and values in the 'var2' dictionary and prints them.
for k, v in var2.items():
    print(k,v)

# Creates a dictionary named 'dict_of_lists' with keys '000', '001', and '002', where the values are lists of random integers.
dict_of_lists = {
    '000': [random.randint(0, 10) for i in range(3)],
    '001': [random.randint(0, 10) for i in range(3)],
    '002': [random.randint(0, 10) for i in range(3)]
}
print(dict_of_lists)  # Prints the 'dict_of_lists' dictionary.
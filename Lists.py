# This code covers various Python concepts such as lists, ranges, list comprehensions, and iteration through nested lists

import random  # Import the random module for generating random numbers.

var = []  # Creates an empty list named 'var'.
print  # This line doesn't do anything since 'print' is not followed by parentheses and a value to print.

var2 = [151, 251, 386, 493, 649]  # Creates a list named 'var2' with numeric values.
var = var2.append(721)  # Appends 721 to the 'var2' list but assigns the result (None) to 'var'. It's better to use 'var2.append(721)' without assignment.

print(dir(var2))  # Prints a list of attributes and methods available for the 'var2' list.

var2.reverse()  # Reverses the order of elements in the 'var2' list.
print(var2)  # Prints the reversed 'var2' list.

print(dir('This is a string'))  # Prints a list of attributes and methods available for the given string.

numbers = range(0, 10)  # Creates a range object that represents numbers from 0 to 9.
print(type(numbers))  # Prints the type of the 'numbers' variable, which is 'range'.

numbers = list(numbers)  # Converts the 'numbers' range object into a list.
print(numbers)  # Prints the list of numbers from 0 to 9.

sq_numbers = [0, 1, 4, 9, 16]  # Creates a list of squared numbers.
print(sq_numbers[2])  # Prints the value at index 2, which is 4.

print(sq_numbers.index(9))  # Prints the index of the value 9 in the 'sq_numbers' list, which is 3.

try:
    print(sq_numbers.index(10))  # Tries to print the index of the value 10, but it's not in the list, so it raises an exception.
except:
    print('not in list')  # Prints 'not in list' to indicate that the value is not in the list.

sq_numbers = [0, 1, 4, 9, 16]  # Creates another list of squared numbers.
print(len(sq_numbers))  # Prints the length of the 'sq_numbers' list, which is 5.

# Creates a list of lists with random integers using nested list comprehensions.
list_of_lists = [[random.randint(0, 10) for j in range(3)] for i in range(5)]

# Iterates through the 'list_of_lists' and prints its content.
for list_of_list in list_of_lists:
    print(list_of_list)
    for element in list_of_list:
        print(element)
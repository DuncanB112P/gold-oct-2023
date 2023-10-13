# Intro to functions
# It is best practice to keep all function definitions at the top of your code


def greet():
    print('Hello, my dear!')



input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_avg(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)



def print_letter_count(text, letter):  # these are positional arguments 
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# print_letter_count('Mississippi', 's') # bc positional argument, if text and letter are switched, the call won't work



# named arguments - switched values will still work

def letter_count(text = 'Welcome', letter = 'e'):  
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

letter_count(letter='e', text='Welcome') # order is swithced from the def line
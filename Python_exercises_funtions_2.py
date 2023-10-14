
#set one of the PARAMETER values (indicated within the parentheses) to a fixed value (a). BUT... the positional argument MUST come BEFORE the named argument.

def print_letter_count(text, letter='a'): 
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# only need to provide the text, because the letter is harcoded in the def

## print_letter_count('How many letters a are here?')



# if you set both of the parameter values to default value, then you do not to add them in the call for the function

def letter_count(text='This is the default string to search', letter='s'): 
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

## letter_count()



# variables outside of the function are still recognized in the function, unless the variable value has been changed in the function

def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
mysterious_var='Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)
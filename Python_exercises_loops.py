#Create a while loop. This one is a statement that is always True (the user_input will NEVER be anything other than the user's input).
while True:
    user_input = int(input('When was Python 1.0 released? '))
# Determine of the user_input is GREATER than the desired value, and if so, print the response
    if user_input > 1994:
        print('It was earlier than that!')
# Determine of the user_input is LESSER than the desired value, and if so, print the response    
    elif user_input < 1994:
        print('It was later than that!')
# If it is not greater or less than the desired value, then it must be the desired value. Print the response   
    else:
        print('Correct!')
        break
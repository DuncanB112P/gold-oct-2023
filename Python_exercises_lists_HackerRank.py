if __name__ == '__main__':
    # This condition checks whether the script is being run as the main program.
    # It is a common practice to put the main program logic under this condition to prevent execution when imported as a module.

    N = int(input())  # Reads an integer from the user and stores it in the variable 'N'.

answer_list = []  # Initializes an empty list called 'answer_list' to store data.

for i in range(N):
    # Iterates 'N' times, where 'N' is the integer input provided by the user.

    instruction = input()  # Reads a line of user input and stores it in the variable 'instruction'.

    tokens = instruction.split(' ')  # Splits the 'instruction' into a list of words using a space as the separator.

    if tokens[0] == 'insert':
        # Checks if the first word in 'instruction' is 'insert'.
        # If true, it inserts an integer (given by the second word) into 'answer_list' at the specified index (given by the third word).
        answer_list.insert(int(tokens[1]), int(tokens[2]))
    
    if tokens[0] == 'print':
        # Checks if the first word in 'instruction' is 'print'.
        # If true, it prints the contents of 'answer_list'.
        print(answer_list)

    elif tokens[0] == 'remove':
        # Checks if the first word in 'instruction' is 'remove'.
        # If true, it removes the first occurrence of the specified integer (given by the second word) from 'answer_list'.
        answer_list.remove(int(tokens[1]))

    if tokens[0] == 'append':
        # Checks if the first word in 'instruction' is 'append'.
        # If true, it appends the specified integer (given by the second word) to the end of 'answer_list'.
        answer_list.append(int(tokens[1])

    if tokens[0] == 'sort':
        # Checks if the first word in 'instruction' is 'sort'.
        # If true, it sorts 'answer_list' in ascending order.
        answer_list.sort()

    if tokens[0] == 'pop':
        # Checks if the first word in 'instruction' is 'pop'.
        # If true, it removes and returns the last item from 'answer_list'.
        answer_list.pop()

    if tokens[0] == 'reverse':
        # Checks if the first word in 'instruction' is 'reverse'.
        # If true, it reverses the order of elements in 'answer_list'.
        answer_list.reverse()

# Import the 'random' and 'string' modules to generate random numbers and strings.
import random
import string

# Prompt the user to input the number of EC2 instances needed and their department.
n = int(input('Number of EC2 instances needed: '))
department = input('Your department (Accounting, Marketing, or FinOps only): ').lower()

# Define a variable 'letters' containing all the uppercase and lowercase letters of the alphabet.
letters = string.ascii_letters

# Check if the department input is one of the valid options: 'marketing', 'accounting', or 'finops'.
if (department == 'marketing') or (department == 'accounting') or (department == 'finops'):
    # Loop 'n' times to generate and print instance names.
    for suffix in range(0, n):
        # Concatenate department name, a random 4-digit number, and a 3-character random string.
        print(department, random.randrange(1000, 9999, 1), (''.join(random.choice(letters) for i in range(3))), sep='')
else:
    # If the department input is not valid, print an error message.
    print('This name generator is restricted to Marketing, Accounting, or FinOps personnel.')
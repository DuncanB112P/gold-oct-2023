# Import the random module to generate random numbers.
import random

# Prompt the user for the number of EC2 instances needed and store it in 'n'.
n = int(input('Number of EC2 instances needed: '))

# Prompt the user for their department and convert it to lowercase for case insensitivity.
department = input('Your department (Accounting, Marketing, or FinOps only): ').lower()

# Check if the provided department is one of the allowed options: Marketing, Accounting, or FinOps.
if (department == 'marketing') or (department == 'accounting') or (department == 'finops'):
    # Generate 'n' unique names for EC2 instances based on the department and a random 4-digit number.
    for suffix in range(0, n):
        print(department, random.randrange(1000, 9999, 1), sep='')
else:
    # Display a message if the department is not one of the allowed options.
    print('This name generator is restricted to Marketing, Accounting, or FinOps personnel.')
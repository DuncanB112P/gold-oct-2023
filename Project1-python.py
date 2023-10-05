import random
n = int(input('Number of ec2 instances needed: '))
department = input('Your department(Accounting, Marketing, or FinOps only): ').lower()
if (department == 'marketing') or (department =='accounting') or (department == 'finops'):
    for suffix in range(0, n):
        print(department, random.randrange(1000,9999,1), sep='')
else:
    print('This name generator is restricted to Marketing, Accounting, or FinOps personnel.')
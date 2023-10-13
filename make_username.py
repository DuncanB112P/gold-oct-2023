def make_username():
    import random
    import string

    n = int(input('Number of EC2 instances needed: '))
    department = input('Your department (Accounting, Marketing, or FinOps only): ').lower()
    letters = string.ascii_letters

    if (department == 'marketing') or (department == 'accounting') or (department == 'finops'):
        print('Here are the usernames you require: ') 
        for suffix in range(0, n):
            print(department, random.randrange(1000, 9999, 1), (''.join(random.choice(letters) for i in range(3))), sep='')
    else:
        print('This name generator is restricted to Marketing, Accounting, or FinOps personnel.')


make_username()
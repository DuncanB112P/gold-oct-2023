import random

number = random.randint(0,10)
print(number)

if number > 6:
    print('Big number')
elif number < 6: 
    print('Small number')
    
    
number = number + 1
print(number)


if number > 6:
    print('Big number')
elif number < 6:
    print('Small numbers')
elif number -- 6:
    print('number is 6')
    
    
#######

purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')
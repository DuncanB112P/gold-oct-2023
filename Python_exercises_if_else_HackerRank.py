#Instrcutions:
# n is an integer in the range of 1 to 100 inclusive
# if n is an odd integer, then print "Weird"
# if n an even integer between 6 and 20 inclusive, then print "Weird"
# if n is an even integer between 1 and 5, or if n is an even integer greater than 20, print "Nor Weird"


#input number between 1 and 100
n = int(input('Enter a whole number between 1 and 100: '))
if n > 100:
    n = int(input('Your number must be between 1 and 100: '))

    
#determine if number is "Weird" or "Not Weird" 
if (n%2 > 0) or (n%2 == 0 and (6 <= n <= 20)):
    print('Weird')
else:
    if n%2 == 0 and ((1 <= n <= 5) or (n > 20)):
        print('Not Weird')
name = input('Enter your name: ')
age = int(input('Enter your age: '))
gender = input('Are you male or female? (m/f) ').lower()
if 'c' in name.lower() or 't' in name.lower():
    print('We do not recommend you to do sports.')
elif age <= 15:
    print('We recommend tennis.')
elif gender == 'm':
    print('We recommend football.')
elif gender == 'f':
    print('We recommend basketball.')
else:
    print('You entered wrong gender.')
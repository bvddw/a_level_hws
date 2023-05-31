name = input('Your name: ')
if 'a' in name:
    print('We are not going to check it.')
else:
    age = int(input('Enter your age: '))
    if age > 100:
        print('Wrong age.')
    elif age < 18:
        print('It is not fine.')
    else:
        print('It is fine.')
        print('Your age is an even number.' if age % 2 == 0 else 'Your age is an odd number.')
        print('You won the prize!' if age % 2 == 0 and 'v' in name.lower() else 'You did not win the prize.')
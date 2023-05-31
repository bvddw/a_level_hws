fizz = int(input('Enter first number (fizz): '))
buzz = int(input('Enter second number (buzz): '))
number = int(input('Enter third number: '))
for i in range(1, number + 1):
    if not i % fizz and i % buzz:
        print(f'F ', end = '')
    elif not i % buzz and i % fizz:
        print(f'B ', end = '')
    elif not i % fizz and not i % buzz:
        print(f'FB ', end = '')
    else:
        print(f'{i} ', end = '')
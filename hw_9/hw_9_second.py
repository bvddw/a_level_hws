try:
    number = int(input('Enter an odd positive number: '))
    if number < 0:
        print('Is is a negative number.')
    elif not number % 2:
        print('It is even number.')
    else:  # if number inputted correctly
        for i in range(number):  # first part - spaces, second - '*'
            # need to print number // 2 spaces in first row, after number // 2 - 1, ..., 0, ... number //2
            # formula - abs(number // 2) - i
            # need to print '*' after spaces
            # 1, 3, 5, ..., number, number - 2, ... 3, 1 - number of '*' in rows
            # formula - 2 * (number // 2 - abs(number // 2 - i)) + 1
            print(abs(number // 2 - i) * ' ' + (2 * (number // 2 - abs(number // 2 - i)) + 1) * '*')
except ValueError:
    print('It is not a number.')

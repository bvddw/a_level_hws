# https://www.codewars.com/kata/565c4e1303a0a006d7000127

def number_format(n):
    n = str(n)
    right_format = ''
    if n[0] == '-':
        right_format += '-'
        n = n[1:]
    if len(n) % 3 == 1:
        right_format += n[0] + ','
        n = n[1:]
    if len(n) % 3 == 2:
        right_format += n[0] + n[1] + ','
        n = n[2:]
    count = 0
    for i in range(len(n)):
        right_format += n[0]
        n = n[1:]
        count += 1
        if count == 3:
            count = 0
            right_format += ','
    return right_format[:-1]
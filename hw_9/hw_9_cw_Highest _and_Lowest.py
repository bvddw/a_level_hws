# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    return str(max(list(map(int, numbers.split()))))  + ' ' + str(min(list(map(int, numbers.split()))))

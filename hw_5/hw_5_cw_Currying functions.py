# https://www.codewars.com/kata/586909e4c66d18dd1800009b

# Currying functions

def multiply_all (array):
    return lambda number: [number * i for i in array]
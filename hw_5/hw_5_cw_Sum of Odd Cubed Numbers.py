# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python

# Sum of Odd Cubed Numbers

def cube_odd(arr):
    suma = 0
    for i in arr:
        if type(i) != type(1):
            return None
        elif i % 2:
            suma += i ** 3
    return suma
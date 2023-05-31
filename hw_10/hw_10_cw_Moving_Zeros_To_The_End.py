# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    without_zeros = []
    zeros = []
    for i in lst:
        if i:
            without_zeros.append(i)
        else:
            zeros.append(i)
    without_zeros.extend(zeros)
    return without_zeros

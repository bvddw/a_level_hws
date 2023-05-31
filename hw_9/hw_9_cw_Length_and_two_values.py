# https://www.codewars.com/kata/62a611067274990047f431a8

def alternate(n, first_value, second_value):
    result = []
    flag = 1
    for i in range(n):
        if flag == 1:
            result.append(first_value)
            flag = 2
        else:
            result.append(second_value)
            flag = 1
    return result

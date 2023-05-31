# https://www.codewars.com/kata/57ef016a7b45ef647a00002d

# Homogenous arrays

def filter_homogenous(arrays):
    homogenous = []
    for arr in arrays:
        mistake = 0
        if len(arr) == 0:
            mistake = 1
        for i in range(len(arr) - 1):
            if type(arr[i]) != type(arr[i + 1]):
                mistake = 1
                break
        if mistake == 0:
            homogenous.append(arr)
    return homogenous
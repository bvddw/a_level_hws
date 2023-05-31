# https://www.codewars.com/kata/5558cc216a7a231ac9000022

def duplicates(arr):
    dublicates_ = {}
    for i in range(len(arr)):
        if arr[i] not in dublicates_.keys():
            if arr[i] in arr[i + 1:]:
                dublicates_[arr[i]] = arr[i + 1:].index(arr[i]) + len(arr[:i + 1])
    result = []
    for i in dublicates_.keys():
        result.append(i)
    return sorted(result, key=lambda n: dublicates_[n])
# https://www.codewars.com/kata/52c31f8e6605bcc646000082

def two_sum(numbers, target):
    seen = {}
    for i,num in enumerate(numbers):
        if num in seen:
            return [seen[num], i]
        else:
            seen[target - num] = i
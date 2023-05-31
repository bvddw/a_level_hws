# https://www.codewars.com/kata/582746fa14b3892727000c4f

# Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe

def count_developers(lst):
    count = 0
    for person in lst:
        if person['continent'] == 'Europe' and person['language'] == 'JavaScript':
            count += 1
    return count
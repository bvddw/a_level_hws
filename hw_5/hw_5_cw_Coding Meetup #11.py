# https://www.codewars.com/kata/582ba36cc1901399a70005fc

# Coding Meetup #11 - Higher-Order Functions Series - Find the average age

def get_average(lst):
    total_age = 0
    count = 0
    for person in lst:
        total_age += person['age']
        count += 1
    if total_age == 0:
        return 0
    else:
        return round(total_age / count)
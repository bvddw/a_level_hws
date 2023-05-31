# https://www.codewars.com/kata/583952fbc23341c7180002fd

# Coding Meetup #14 - Higher-Order Functions Series - Order the food

def order_food(lst):
    person_type = {}
    for person in lst:
        if person['meal'] in person_type:
            person_type[person['meal']] += 1
        else:
            person_type[person['meal']] = 1
    return person_type
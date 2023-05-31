# https://www.codewars.com/kata/58279e13c983ca4a2a00002a

# Coding Meetup #2 - Higher-Order Functions Series - Greet developers

def greet_developers(lst):
    greet = []
    for person in lst:
        person['greeting'] = f"Hi {person['firstName']}, what do you like the most about {person['language']}?"
        greet.append(person)
    return greet
# https://www.codewars.com/kata/5827acd5f524dd029d0005a4/train/python

# Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?

def is_ruby_coming(lst):
    for person in lst:
        if person['language'] == 'Ruby':
            return True
    return False
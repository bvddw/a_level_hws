# https://www.codewars.com/kata/582dace555a1f4d859000058

# Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins

def find_admin(lst, lang):
    admins = []
    for person in lst:
        if person['language'] == lang and person['githubAdmin'] == 'yes':
            admins.append(person)
    return admins
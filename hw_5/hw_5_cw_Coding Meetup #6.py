# https://www.codewars.com/kata/58287977ef8d4451f90001a0

# Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?

def is_same_language(lst):
    languages = []
    for person in lst:
        if len(languages) > 1:
            return False
        if person['language'] not in languages:
            languages.append(person['language'])
    if len(languages) > 1:
            return False
    return True
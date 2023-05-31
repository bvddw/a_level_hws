# https://www.codewars.com/kata/5828713ed04efde70e000346

# Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages

def count_languages(lst):
    languages = {}
    for person in lst:
        if person['language'] not in languages:
            languages[person['language']] = 1
        else:
            languages[person['language']] += 1
    return languages
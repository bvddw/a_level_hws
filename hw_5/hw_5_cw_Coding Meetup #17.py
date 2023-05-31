# https://www.codewars.com/kata/583ea278c68d96a5fd000abd

# Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language

def sort_by_language(arr):
    return sorted(arr, key=lambda person: (person['language'], person['first_name']))
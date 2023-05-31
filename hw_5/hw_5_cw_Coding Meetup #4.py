# https://www.codewars.com/kata/5827bc50f524dd029d0005f2

# Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer

def get_first_python(users):
    for person in users:
        if person['language'] == 'Python':
            return person['first_name'] + ', ' + person['country']
    return 'There will be no Python developers'
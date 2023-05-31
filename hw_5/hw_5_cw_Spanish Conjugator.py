# https://www.codewars.com/kata/5a81b78d4a6b344638000183

# Spanish Conjugator

def conjugate(verb):
    suffixes = {
        'ar' : ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er' : ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir' : ['o', 'es', 'e', 'imos', 'is', 'en']
    }
    return {verb : [verb[:-2] + i for i in suffixes[verb[-2:]]]}
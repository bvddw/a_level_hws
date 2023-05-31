# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0

# Sort by Last Char

def last(s):
    words = s.split()  # створили список
    return sorted(words, key=lambda word: word[-1])  # сортуємо за останнім символом

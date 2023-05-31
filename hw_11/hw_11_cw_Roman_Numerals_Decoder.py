# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(s):
    n = 0
    i = 0
    s += '0'
    while s[i] == 'M':
        n += 1000
        i += 1

    if s[i] == 'C' and s[i + 1] == 'M':
        n += 900
        i += 2
    elif s[i] == 'C' and s[i + 1] == 'D':
        n += 400
        i += 2
    elif s[i] == 'D':
        n += 500
        i += 1
    while s[i] == 'C':
        n += 100
        i += 1

    if s[i] == 'X' and s[i + 1] == 'C':
        n += 90
        i += 2
    elif s[i] == 'X' and s[i + 1] == 'L':
        n += 40
        i += 2
    elif s[i] == 'L':
        n += 50
        i += 1
    while s[i] == 'X':
        n += 10
        i += 1

    if s[i] == 'I' and s[i + 1] == 'X':
        n += 9
        i += 1
    elif s[i] == 'I' and s[i + 1] == 'V':
        n += 4
        i += 1
    elif s[i] == 'V':
        n += 5
        i += 1
    while s[i] == 'I':
        n += 1
        i += 1
    return n

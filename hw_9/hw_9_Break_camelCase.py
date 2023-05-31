# https://www.codewars.com/kata/5208f99aee097e6552000148

def solution(s):
    answer = ''
    point = 0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            answer =answer + s[point:i] + ' '
            point = i
    answer += s[point:]
    return answer
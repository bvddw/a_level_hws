# https://www.codewars.com/kata/51b62bf6a9c58071c600001b


def solution(n):
    symbols = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman = ''
    roman += n // 1000 * symbols[1000]
    n %= 1000
    for i in [100, 10, 1]:
        if n // i == 9:
            roman += symbols[i] + symbols[i * 10]
        elif n // i in range(5, 9):
            roman += symbols[i * 5] + symbols[i] * (n // i % 5)
        elif n // i == 4:
            roman += symbols[i] + symbols[i * 5]
        else:
            roman += symbols[i] * (n // i)
        n %= i
    return roman

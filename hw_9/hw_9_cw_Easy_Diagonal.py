# https://www.codewars.com/kata/559b8e46fa060b2c6a0000bf

def diagonal(n, k):
    result = 1
    for i in range(n - k + 1, n + 2):
        result *= i
    for i in range(1, k + 2):
        result //= i
    return result
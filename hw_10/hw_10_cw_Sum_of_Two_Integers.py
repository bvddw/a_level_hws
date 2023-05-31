# https://www.codewars.com/kata/5a9c35e9ba1bb5c54a0001ac

def sum_of_sums(n):
    n = n * (n+1) * (n+2) // 6
    return n * (n+1) // 2

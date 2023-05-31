# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    return sum(num for num in range(number) if not num % 3 or not num % 5)

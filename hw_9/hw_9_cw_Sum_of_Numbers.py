# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a,b):
    return (max(a, b) + min(a, b)) * (max(a, b) - min(a, b) + 1) // 2  if a - b else a
# https://www.codewars.com/kata/54147087d5c2ebe4f1000805

# The 'if' function

def _if(bool, func1, func2):
    return func1() if bool else func2()
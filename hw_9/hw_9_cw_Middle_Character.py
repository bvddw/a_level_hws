# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    return s[len(s) // 2 - 1] + s[len(s) // 2] if not len(s) % 2 else s[len(s) // 2]
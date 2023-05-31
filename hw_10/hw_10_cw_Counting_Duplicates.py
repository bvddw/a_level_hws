# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    dublicates = []
    text = text.lower()
    for i in range(len(text)):
        if text[i] not in dublicates:
            if text[i] in text[:i] + text[i + 1:]:
                dublicates.append(text[i])
    return len(dublicates)

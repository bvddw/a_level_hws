# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    sorted_words = []
    for num in range(1, len(sentence) + 1):
        for i in sentence.split():
            if str(num) in i:
                sorted_words.append(i)
                break
    return ' '.join(sorted_words)
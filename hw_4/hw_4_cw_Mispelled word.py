#  https://www.codewars.com/kata/5892595f190ca40ad0000095

#  Mispelled word

def mispelled(word1,word2):
    if len(word1) > len(word2):
        if word1[1:] == word2 or word1[:len(word1) - 1] == word2:  # випадок, коли дописали літеру спочатку або в кінці другого слова і таким чином отримали перше
            return True
        else:
            return False
    if len(word2) > len(word1):
        if word2[1:] == word1 or word2[:len(word2) - 1] == word1:  # випадок, коли дописали літеру спочатку або в кінці першого слова і таким чином отримали друге
            return True
        else:
            return False
    count = 0
    for i in range(len(word1)):  # випадок, коли у слів однакова довжина, просто має бути максимум одна різниця у символах
        if word1[i] != word2[i]:
            count += 1
    return True if count < 2 else False